"""Chat and channel methods."""

from __future__ import annotations


class ChatMethods:
    """Mixin providing chat management methods."""

    async def create_channel(
        self,
        title: str,
        about: str = "",
        *,
        megagroup: bool = False,
        broadcast: bool = False,
    ):
        from sent.tl.functions.channels import ChannelsCreateChannel

        result = await self(
            ChannelsCreateChannel(
                broadcast=broadcast and not megagroup,
                megagroup=megagroup,
                for_import=False,
                title=title,
                about=about,
            )
        )
        return result

    async def create_group(self, title: str, users=None):
        return await self.create_channel(title, megagroup=True)

    async def edit_title(self, entity, title: str):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.channels import ChannelsEditTitle

        return await self(ChannelsEditTitle(channel=entity, title=title))

    async def get_participants(
        self,
        entity,
        *,
        limit: int = 100,
        search: str = "",
        filter=None,
    ):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.channels import ChannelsGetParticipants
        from sent.tl.types.channels import (
            ChannelsChannelParticipantsRecent,
            ChannelsChannelParticipantsSearch,
        )

        part_filter = filter
        if search and not part_filter:
            part_filter = ChannelsChannelParticipantsSearch(q=search)
        part_filter = part_filter or ChannelsChannelParticipantsRecent()

        result = await self(
            ChannelsGetParticipants(
                channel=entity,
                filter=part_filter,
                offset=0,
                limit=limit,
                hash=0,
            )
        )
        return getattr(result, "users", [])

    async def iter_participants(self, entity, **kwargs):
        offset = 0
        limit = kwargs.get("limit", 100)
        while True:
            entity_input = await self.get_input_entity(entity)
            from sent.tl.functions.channels import ChannelsGetParticipants
            from sent.tl.types.channels import ChannelsChannelParticipantsRecent

            result = await self(
                ChannelsGetParticipants(
                    channel=entity_input,
                    filter=kwargs.get("filter") or ChannelsChannelParticipantsRecent(),
                    offset=offset,
                    limit=limit,
                    hash=0,
                )
            )
            users = getattr(result, "users", [])
            if not users:
                break
            for user in users:
                yield user
            offset += len(users)
            if len(users) < limit:
                break

    async def get_permissions(self, entity, user):
        entity = await self.get_input_entity(entity)
        user = await self.get_input_entity(user)
        from sent.tl.functions.channels import ChannelsGetParticipant

        result = await self(ChannelsGetParticipant(channel=entity, participant=user))
        return getattr(result, "participant", result)

    async def edit_admin(self, entity, user, **kwargs):
        entity = await self.get_input_entity(entity)
        user = await self.get_input_entity(user)
        from sent.tl.functions.channels import ChannelsEditAdmin
        from sent.tl.types.all import ChatAdminRights

        rights = ChatAdminRights(**kwargs) if kwargs else None
        return await self(
            ChannelsEditAdmin(channel=entity, user_id=user, admin_rights=rights, rank="")
        )

    async def edit_permissions(self, entity, user, **kwargs):
        entity = await self.get_input_entity(entity)
        user = await self.get_input_entity(user)
        from sent.tl.functions.channels import ChannelsEditBanned
        from sent.tl.types.all import ChatBannedRights

        rights = ChatBannedRights(until_date=0, **kwargs)
        return await self(
            ChannelsEditBanned(channel=entity, participant=user, banned_rights=rights)
        )

    async def kick_participant(self, entity, user):
        return await self.edit_permissions(
            entity, user, view_messages=True, send_messages=True
        )

    async def join_chat(self, entity):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.channels import ChannelsJoinChannel

        return await self(ChannelsJoinChannel(channel=entity))

    async def leave_chat(self, entity):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.channels import ChannelsLeaveChannel

        return await self(ChannelsLeaveChannel(channel=entity))

    async def delete_dialog(self, entity, *, revoke: bool = False):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.messages import MessagesDeleteHistory

        return await self(
            MessagesDeleteHistory(peer=entity, max_id=0, revoke=revoke, just_clear=not revoke)
        )

    async def export_invite_link(self, entity):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.messages import MessagesExportChatInvite

        result = await self(MessagesExportChatInvite(peer=entity))
        return getattr(result, "link", result)
