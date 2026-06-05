"""User-related methods."""

from __future__ import annotations

from sent.client.entity import get_peer_id


class UserMethods:
    """Mixin providing user methods."""

    async def get_me(self, input_peer: bool = False):
        from sent.tl.functions.users import UsersGetUsers
        from sent.tl.types.all import InputPeerUser, InputUserSelf

        result = await self(UsersGetUsers(id=[InputUserSelf()]))
        user = result[0] if result else None
        if user:
            self._entity_cache.add(user)
        if input_peer and user:
            return InputPeerUser(user_id=user.id, access_hash=user.access_hash)
        return user

    async def get_entity(self, entity):
        return await self.get_input_entity(entity, raw=True)

    async def get_entities(self, entities):
        return [await self.get_input_entity(e, raw=True) for e in entities]

    async def get_input_entity(self, entity, raw: bool = False):
        if entity is None:
            raise ValueError("Entity cannot be None")
        if entity == "me":
            return await self.get_me(input_peer=not raw)

        if isinstance(entity, int):
            cached = self._entity_cache.get(entity)
            if cached:
                return cached if raw else self._as_input_peer(cached)

        if isinstance(entity, str):
            username = entity.lstrip("@")
            cached = self._entity_cache.get_by_username(username)
            if cached:
                return cached if raw else self._as_input_peer(cached)
            from sent.tl.functions.contacts import ContactsResolveUsername

            result = await self(ContactsResolveUsername(username=username))
            if result.users:
                self._entity_cache.add(result.users[0])
                return result.users[0] if raw else self._as_input_peer(result.users[0])
            if result.chats:
                self._entity_cache.add(result.chats[0])
                return result.chats[0] if raw else self._as_input_peer(result.chats[0])

        if hasattr(entity, "user_id") or hasattr(entity, "channel_id"):
            return entity
        if hasattr(entity, "SUBCLASS_OF_ID"):
            return entity

        raise ValueError(f"Cannot resolve entity: {entity!r}")

    def get_peer_id(self, peer):
        return get_peer_id(peer)

    def _as_input_peer(self, entity):
        from sent.tl.types.all import InputPeerChannel, InputPeerChat, InputPeerUser

        if hasattr(entity, "access_hash"):
            if getattr(entity, "broadcast", None) or getattr(entity, "megagroup", None):
                return InputPeerChannel(
                    channel_id=entity.id, access_hash=entity.access_hash
                )
            return InputPeerUser(user_id=entity.id, access_hash=entity.access_hash)
        return InputPeerChat(chat_id=entity.id)

    async def get_profile_photos(self, entity, *, limit: int = 100):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.photos import PhotosGetUserPhotos

        result = await self(
            PhotosGetUserPhotos(user_id=entity, offset=0, max_id=0, limit=limit)
        )
        return getattr(result, "photos", [])

    async def get_full_user(self, entity):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.users import UsersGetFullUser

        return await self(UsersGetFullUser(id=entity))
