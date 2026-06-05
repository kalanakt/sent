"""File download methods."""

from __future__ import annotations

import os
from typing import Callable, Optional, Union


class DownloadMethods:
    """Mixin providing file download methods."""

    async def download_media(
        self,
        message,
        file: Union[str, bytes] = None,
        *,
        progress_callback: Callable[[int, int], None] = None,
    ) -> Optional[Union[bytes, str]]:
        if isinstance(message, (str, bytes)):
            return message

        media = getattr(message, "media", None) or message
        if media is None:
            return None

        location = self._get_file_location(media)
        if location is None:
            return None

        from sent.tl.functions.upload import UploadGetFile

        part_size = 512 * 1024
        offset = 0
        chunks = []
        total = getattr(getattr(media, "document", None), "size", None) or part_size

        while True:
            result = await self(
                UploadGetFile(location=location, offset=offset, limit=part_size)
            )
            chunk = result.bytes
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if progress_callback:
                progress_callback(offset, total)
            if len(chunk) < part_size:
                break

        data = b"".join(chunks)
        if file:
            path = file if isinstance(file, str) else "download"
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "wb") as f:
                f.write(data)
            return path
        return data

    async def download_profile_photo(
        self,
        entity,
        file: str = None,
        *,
        download_big: bool = True,
    ) -> Optional[str]:
        entity = await self.get_entity(entity)
        photo = getattr(entity, "photo", None)
        if not photo:
            return None
        return await self.download_media(photo, file=file)

    def _get_file_location(self, media):
        if hasattr(media, "photo"):
            photo = media.photo
            if hasattr(photo, "sizes") and photo.sizes:
                size = photo.sizes[-1]
                from sent.tl.types.all import InputPhotoFileLocation

                return InputPhotoFileLocation(
                    id=photo.id,
                    access_hash=photo.access_hash,
                    file_reference=photo.file_reference,
                    thumb_size=getattr(size, "type", ""),
                )
        if hasattr(media, "document"):
            doc = media.document
            from sent.tl.types.all import InputDocumentFileLocation

            return InputDocumentFileLocation(
                id=doc.id,
                access_hash=doc.access_hash,
                file_reference=doc.file_reference,
                thumb_size="",
            )
        return None
