"""Authentication methods."""

from __future__ import annotations

import os

from sent.errors.common import (
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    RPCError,
    SessionPasswordNeededError,
)


class AuthMethods:
    """Mixin providing authentication methods."""

    async def send_code_request(
        self,
        phone: str,
        *,
        force_sms: bool = False,
        _retry_count: int = 0,
    ):
        from sent.tl.functions.auth import AuthSendCode
        from sent.tl.types.all import CodeSettings

        settings = CodeSettings(
            allow_flashcall=not force_sms,
            current_number=True,
            allow_app_hash=True,
            allow_missed_call=True,
            allow_firebase=True,
        )
        result = await self(
            AuthSendCode(
                phone_number=phone,
                api_id=self.api_id,
                api_hash=self.api_hash,
                settings=settings,
            )
        )
        self._phone = phone
        self._phone_code_hash = result.phone_code_hash
        return result

    async def sign_in(
        self,
        phone: str = None,
        code=None,
        password: str = None,
        bot_token: str = None,
        phone_code_hash: str = None,
    ):
        if bot_token:
            return await self._sign_in_bot(bot_token)

        phone = phone or self._phone
        phone_code_hash = phone_code_hash or self._phone_code_hash

        if password:
            return await self._sign_in_2fa(password)

        from sent.tl.functions.auth import AuthSignIn

        try:
            result = await self(
                AuthSignIn(
                    phone_number=phone,
                    phone_code_hash=phone_code_hash,
                    phone_code=str(code),
                )
            )
        except SessionPasswordNeededError:
            raise
        except RPCError as e:
            if e.message == "SESSION_PASSWORD_NEEDED":
                raise SessionPasswordNeededError() from e
            raise

        self._authorized = True
        return result

    async def _sign_in_bot(self, token: str):
        from sent.tl.functions.auth import AuthImportBotAuthorization

        result = await self(
            AuthImportBotAuthorization(
                flags=0,
                api_id=self.api_id,
                api_hash=self.api_hash,
                bot_auth_token=token,
            )
        )
        self._authorized = True
        return result

    async def _sign_in_2fa(self, password: str):
        from sent.crypto.srp import compute_check
        from sent.tl.functions.account import AccountGetPassword
        from sent.tl.functions.auth import AuthCheckPassword
        from sent.tl.types.all import InputCheckPasswordSRP

        pwd = await self(AccountGetPassword())
        srp_id, A, M1 = compute_check(
            password=password,
            srp_id=pwd.srp_id,
            srp_B=pwd.srp_B,
            secure_random=os.urandom(256),
            algo=pwd.current_algo,
        )
        srp = InputCheckPasswordSRP(srp_id=srp_id, A=A, M1=M1)
        result = await self(AuthCheckPassword(password=srp))
        self._authorized = True
        return result

    async def edit_2fa(
        self,
        current_password: str = None,
        new_password: str = None,
        *,
        hint: str = "",
        email: str = None,
    ):
        from sent.crypto.srp import compute_check
        from sent.tl.functions.account import (
            AccountGetPassword,
            AccountUpdatePasswordSettings,
        )
        from sent.tl.types.account import AccountPasswordInputSettings
        from sent.tl.types.all import InputCheckPasswordSRP

        pwd = await self(AccountGetPassword())
        new_settings = AccountPasswordInputSettings(
            new_algo=pwd.new_algo,
            new_password_hash=pwd.new_secure_algo,
            hint=hint,
            email=email,
            new_secure_settings=None,
        )
        current = None
        if current_password:
            srp_id, A, M1 = compute_check(
                password=current_password,
                srp_id=pwd.srp_id,
                srp_B=pwd.srp_B,
                secure_random=os.urandom(256),
                algo=pwd.current_algo,
            )
            current = InputCheckPasswordSRP(srp_id=srp_id, A=A, M1=M1)
        return await self(
            AccountUpdatePasswordSettings(
                password=current,
                new_settings=new_settings,
            )
        )

    async def qr_login(self, *, timeout: float = 30.0):
        from sent.tl.functions.auth import AuthExportLoginToken

        return await self(
            AuthExportLoginToken(
                api_id=self.api_id,
                api_hash=self.api_hash,
                except_ids=[],
            )
        )

    async def takeout(self, *, contacts: bool = True, message_users: bool = True):
        from sent.tl.functions.account import AccountInitTakeoutSession

        return await self(
            AccountInitTakeoutSession(
                contacts=contacts,
                message_users=message_users,
                message_chats=True,
                message_megagroups=True,
                message_channels=True,
                files=True,
                file_max_size=0,
            )
        )

    async def sign_up(self, phone: str, code, first_name: str, last_name: str = ""):
        from sent.tl.functions.auth import AuthSignUp

        result = await self(
            AuthSignUp(
                phone_number=phone,
                phone_code_hash=self._phone_code_hash,
                first_name=first_name,
                last_name=last_name,
            )
        )
        self._authorized = True
        return result

    async def log_out(self):
        from sent.tl.functions.auth import AuthLogOut

        result = await self(AuthLogOut())
        self._authorized = False
        return result

    async def start(
        self,
        phone=None,
        password=None,
        *,
        bot_token: str = None,
        code_callback=None,
        first_name: str = "User",
        last_name: str = "",
        max_attempts: int = 3,
    ):
        """Interactive or programmatic start."""
        if bot_token:
            await self._sign_in_bot(bot_token)
            return self

        if not await self.is_user_authorized():
            if phone is None:
                phone = input("Please enter your phone: ")
            elif callable(phone):
                phone = phone()

            await self.send_code_request(phone)

            for attempt in range(max_attempts):
                if code_callback:
                    code = code_callback()
                else:
                    code = input("Enter the code you received: ")

                try:
                    await self.sign_in(phone=phone, code=code)
                    break
                except SessionPasswordNeededError:
                    if password is None:
                        password = input("Two-step verification password: ")
                    elif callable(password):
                        password = password()
                    await self._sign_in_2fa(password)
                    break
                except (PhoneCodeInvalidError, PhoneCodeExpiredError):
                    if attempt + 1 >= max_attempts:
                        raise
            else:
                raise RuntimeError("Too many failed sign in attempts")

        return self

    async def is_user_authorized(self) -> bool:
        if self._authorized:
            return True
        try:
            from sent.tl.functions.users import UsersGetUsers
            from sent.tl.types.all import InputUserSelf

            await self(UsersGetUsers(id=[InputUserSelf()]))
            self._authorized = True
            return True
        except Exception:
            return False
