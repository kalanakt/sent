"""File upload methods."""

from __future__ import annotations

import hashlib
import io
import os
from typing import BinaryIO, Union


class UploadMethods:
    """Mixin providing file upload methods."""

    async def upload_file(
        self,
        file: Union[str, bytes, BinaryIO],
        *,
        part_size_kb: float = 512,
        file_name: str = None,
        use_cache: bool = True,
    ):
        if isinstance(file, str):
            file_name = file_name or os.path.basename(file)
            with open(file, "rb") as f:
                return await self._upload_file_obj(f, file_name, part_size_kb)
        if isinstance(file, bytes):
            return await self._upload_file_obj(io.BytesIO(file), file_name or "file", part_size_kb)
        return await self._upload_file_obj(file, file_name or "file", part_size_kb)

    async def _upload_file_obj(self, file_obj, file_name: str, part_size_kb: float):
        from sent.tl.functions.upload import UploadSaveBigFilePart, UploadSaveFilePart

        file_obj.seek(0, 2)
        file_size = file_obj.tell()
        file_obj.seek(0)

        part_size = int(part_size_kb * 1024)
        is_big = file_size > 10 * 1024 * 1024
        file_id = self._random_id()
        part_count = (file_size + part_size - 1) // part_size
        hash_md5 = hashlib.md5() if not is_big else None

        for part_index in range(part_count):
            data = file_obj.read(part_size)
            if hash_md5:
                hash_md5.update(data)
            if is_big:
                await self(
                    UploadSaveBigFilePart(
                        file_id=file_id,
                        file_part=part_index,
                        file_total_parts=part_count,
                        bytes=data,
                    )
                )
            else:
                await self(
                    UploadSaveFilePart(
                        file_id=file_id,
                        file_part=part_index,
                        bytes=data,
                    )
                )

        from sent.tl.types.all import InputFile, InputFileBig

        if is_big:
            return InputFileBig(id=file_id, parts=part_count, name=file_name)
        return InputFile(
            id=file_id,
            parts=part_count,
            name=file_name,
            md5_checksum=hash_md5.hexdigest(),
        )

    async def send_file(
        self,
        entity,
        file,
        *,
        caption: str = None,
        reply_to: int = None,
        buttons=None,
        silent: bool = None,
        force_document: bool = False,
        progress_callback=None,
    ):
        entity = await self.get_input_entity(entity)
        uploaded = await self.upload_file(file)

        from sent.tl.functions.messages import MessagesSendMedia
        from sent.tl.types.all import (
            InputMediaUploadedDocument,
            InputMediaUploadedPhoto,
        )

        if force_document:
            media = InputMediaUploadedDocument(
                file=uploaded,
                mime_type="application/octet-stream",
                attributes=[],
            )
        else:
            media = InputMediaUploadedPhoto(file=uploaded)

        result = await self(
            MessagesSendMedia(
                peer=entity,
                media=media,
                message=caption or "",
                random_id=self._random_id(),
                reply_to=self._build_reply_to(reply_to) if reply_to else None,
                silent=silent,
                reply_markup=self._build_reply_markup(buttons),
            )
        )
        return self._get_message_from_updates(result)
