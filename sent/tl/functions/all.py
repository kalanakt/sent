"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ReqPq(TLObject):
    CONSTRUCTOR_ID = 1615239032
    __slots__ = ('nonce')
    def __init__(self, nonce: bytes):
        self.nonce = nonce
    def to_dict(self):
        return {"nonce": self.nonce}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1615239032, signed=False)
        writer.write_raw(self.nonce)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read(16)
        return cls(nonce)

@register
class ReqPqMulti(TLObject):
    CONSTRUCTOR_ID = 3195965169
    __slots__ = ('nonce')
    def __init__(self, nonce: bytes):
        self.nonce = nonce
    def to_dict(self):
        return {"nonce": self.nonce}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3195965169, signed=False)
        writer.write_raw(self.nonce)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read(16)
        return cls(nonce)

@register
class ReqDHParams(TLObject):
    CONSTRUCTOR_ID = 3608339646
    __slots__ = ('nonce', 'server_nonce', 'p', 'q', 'public_key_fingerprint', 'encrypted_data')
    def __init__(self, nonce: bytes, server_nonce: bytes, p: str, q: str, public_key_fingerprint: int, encrypted_data: str):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data
    def to_dict(self):
        return {"nonce": self.nonce, "server_nonce": self.server_nonce, "p": self.p, "q": self.q, "public_key_fingerprint": self.public_key_fingerprint, "encrypted_data": self.encrypted_data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3608339646, signed=False)
        writer.write_raw(self.nonce)
        writer.write_raw(self.server_nonce)
        writer.write_string(self.p)
        writer.write_string(self.q)
        writer.write_long(self.public_key_fingerprint, signed=False)
        writer.write_string(self.encrypted_data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read(16)
        server_nonce = reader.read(16)
        p = reader.read_string()
        q = reader.read_string()
        public_key_fingerprint = reader.read_long()
        encrypted_data = reader.read_string()
        return cls(nonce, server_nonce, p, q, public_key_fingerprint, encrypted_data)

@register
class SetClientDHParams(TLObject):
    CONSTRUCTOR_ID = 4110704415
    __slots__ = ('nonce', 'server_nonce', 'encrypted_data')
    def __init__(self, nonce: bytes, server_nonce: bytes, encrypted_data: str):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data
    def to_dict(self):
        return {"nonce": self.nonce, "server_nonce": self.server_nonce, "encrypted_data": self.encrypted_data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4110704415, signed=False)
        writer.write_raw(self.nonce)
        writer.write_raw(self.server_nonce)
        writer.write_string(self.encrypted_data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read(16)
        server_nonce = reader.read(16)
        encrypted_data = reader.read_string()
        return cls(nonce, server_nonce, encrypted_data)

@register
class DestroyAuthKey(TLObject):
    CONSTRUCTOR_ID = 3510849888
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3510849888, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class RpcDropAnswer(TLObject):
    CONSTRUCTOR_ID = 1491380032
    __slots__ = ('req_msg_id')
    def __init__(self, req_msg_id: int):
        self.req_msg_id = req_msg_id
    def to_dict(self):
        return {"req_msg_id": self.req_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1491380032, signed=False)
        writer.write_long(self.req_msg_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        req_msg_id = reader.read_long()
        return cls(req_msg_id)

@register
class GetFutureSalts(TLObject):
    CONSTRUCTOR_ID = 3105996036
    __slots__ = ('num')
    def __init__(self, num: int):
        self.num = num
    def to_dict(self):
        return {"num": self.num}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3105996036, signed=False)
        writer.write_int(self.num, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        num = reader.read_int()
        return cls(num)

@register
class Ping(TLObject):
    CONSTRUCTOR_ID = 2059302892
    __slots__ = ('ping_id')
    def __init__(self, ping_id: int):
        self.ping_id = ping_id
    def to_dict(self):
        return {"ping_id": self.ping_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2059302892, signed=False)
        writer.write_long(self.ping_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        ping_id = reader.read_long()
        return cls(ping_id)

@register
class PingDelayDisconnect(TLObject):
    CONSTRUCTOR_ID = 4081220492
    __slots__ = ('ping_id', 'disconnect_delay')
    def __init__(self, ping_id: int, disconnect_delay: int):
        self.ping_id = ping_id
        self.disconnect_delay = disconnect_delay
    def to_dict(self):
        return {"ping_id": self.ping_id, "disconnect_delay": self.disconnect_delay}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4081220492, signed=False)
        writer.write_long(self.ping_id, signed=False)
        writer.write_int(self.disconnect_delay, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        ping_id = reader.read_long()
        disconnect_delay = reader.read_int()
        return cls(ping_id, disconnect_delay)

@register
class DestroySession(TLObject):
    CONSTRUCTOR_ID = 3880853798
    __slots__ = ('session_id')
    def __init__(self, session_id: int):
        self.session_id = session_id
    def to_dict(self):
        return {"session_id": self.session_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3880853798, signed=False)
        writer.write_long(self.session_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        session_id = reader.read_long()
        return cls(session_id)

@register
class InvokeAfterMsg(TLObject):
    CONSTRUCTOR_ID = 3416209197
    __slots__ = ('msg_id', 'query')
    def __init__(self, msg_id: int, query: TLObject):
        self.msg_id = msg_id
        self.query = query
    def to_dict(self):
        return {"msg_id": self.msg_id, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3416209197, signed=False)
        writer.write_long(self.msg_id, signed=False)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        msg_id = reader.read_long()
        query = reader.tgread_object()
        return cls(msg_id, query)

@register
class InvokeAfterMsgs(TLObject):
    CONSTRUCTOR_ID = 1036301552
    __slots__ = ('msg_ids', 'query')
    def __init__(self, msg_ids: 'Vector', query: TLObject):
        self.msg_ids = msg_ids
        self.query = query
    def to_dict(self):
        return {"msg_ids": self.msg_ids, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1036301552, signed=False)
        writer.write(bytes(self.msg_ids))
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        msg_ids = reader.tgread_object()
        query = reader.tgread_object()
        return cls(msg_ids, query)

@register
class InitConnection(TLObject):
    CONSTRUCTOR_ID = 3251461801
    __slots__ = ('api_id', 'device_model', 'system_version', 'app_version', 'system_lang_code', 'lang_pack', 'lang_code', 'proxy', 'params', 'query')
    def __init__(self, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: TLObject, proxy: 'InputClientProxy' = None, params: 'JSONValue' = None):
        self.api_id = api_id
        self.device_model = device_model
        self.system_version = system_version
        self.app_version = app_version
        self.system_lang_code = system_lang_code
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.proxy = proxy
        self.params = params
        self.query = query
    def to_dict(self):
        return {"api_id": self.api_id, "device_model": self.device_model, "system_version": self.system_version, "app_version": self.app_version, "system_lang_code": self.system_lang_code, "lang_pack": self.lang_pack, "lang_code": self.lang_code, "proxy": self.proxy, "params": self.params, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3251461801, signed=False)
        flags = 0
        if self.proxy is not None: flags |= 1 << 0
        if self.params is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.device_model)
        writer.write_string(self.system_version)
        writer.write_string(self.app_version)
        writer.write_string(self.system_lang_code)
        writer.write_string(self.lang_pack)
        writer.write_string(self.lang_code)
        if flags & (1 << 0):
            writer.write(bytes(self.proxy))
        if flags & (1 << 1):
            writer.write(bytes(self.params))
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        api_id = reader.read_int()
        device_model = reader.read_string()
        system_version = reader.read_string()
        app_version = reader.read_string()
        system_lang_code = reader.read_string()
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        if flags & (1 << 0):
            proxy = reader.tgread_object()
        else:
            proxy = None
        if flags & (1 << 1):
            params = reader.tgread_object()
        else:
            params = None
        query = reader.tgread_object()
        return cls(api_id, device_model, system_version, app_version, system_lang_code, lang_pack, lang_code, proxy, params, query)

@register
class InvokeWithLayer(TLObject):
    CONSTRUCTOR_ID = 3667594509
    __slots__ = ('layer', 'query')
    def __init__(self, layer: int, query: TLObject):
        self.layer = layer
        self.query = query
    def to_dict(self):
        return {"layer": self.layer, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3667594509, signed=False)
        writer.write_int(self.layer, signed=True)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        layer = reader.read_int()
        query = reader.tgread_object()
        return cls(layer, query)

@register
class InvokeWithoutUpdates(TLObject):
    CONSTRUCTOR_ID = 3214170551
    __slots__ = ('query')
    def __init__(self, query: TLObject):
        self.query = query
    def to_dict(self):
        return {"query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3214170551, signed=False)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        query = reader.tgread_object()
        return cls(query)

@register
class InvokeWithMessagesRange(TLObject):
    CONSTRUCTOR_ID = 911373810
    __slots__ = ('range', 'query')
    def __init__(self, range: 'MessageRange', query: TLObject):
        self.range = range
        self.query = query
    def to_dict(self):
        return {"range": self.range, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(911373810, signed=False)
        writer.write(bytes(self.range))
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        range = reader.tgread_object()
        query = reader.tgread_object()
        return cls(range, query)

@register
class InvokeWithTakeout(TLObject):
    CONSTRUCTOR_ID = 2896821550
    __slots__ = ('takeout_id', 'query')
    def __init__(self, takeout_id: int, query: TLObject):
        self.takeout_id = takeout_id
        self.query = query
    def to_dict(self):
        return {"takeout_id": self.takeout_id, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2896821550, signed=False)
        writer.write_long(self.takeout_id, signed=False)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        takeout_id = reader.read_long()
        query = reader.tgread_object()
        return cls(takeout_id, query)

@register
class InvokeWithBusinessConnection(TLObject):
    CONSTRUCTOR_ID = 3710427022
    __slots__ = ('connection_id', 'query')
    def __init__(self, connection_id: str, query: TLObject):
        self.connection_id = connection_id
        self.query = query
    def to_dict(self):
        return {"connection_id": self.connection_id, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3710427022, signed=False)
        writer.write_string(self.connection_id)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        connection_id = reader.read_string()
        query = reader.tgread_object()
        return cls(connection_id, query)

@register
class InvokeWithGooglePlayIntegrity(TLObject):
    CONSTRUCTOR_ID = 502868356
    __slots__ = ('nonce', 'token', 'query')
    def __init__(self, nonce: str, token: str, query: TLObject):
        self.nonce = nonce
        self.token = token
        self.query = query
    def to_dict(self):
        return {"nonce": self.nonce, "token": self.token, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(502868356, signed=False)
        writer.write_string(self.nonce)
        writer.write_string(self.token)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read_string()
        token = reader.read_string()
        query = reader.tgread_object()
        return cls(nonce, token, query)

@register
class InvokeWithApnsSecret(TLObject):
    CONSTRUCTOR_ID = 229528824
    __slots__ = ('nonce', 'secret', 'query')
    def __init__(self, nonce: str, secret: str, query: TLObject):
        self.nonce = nonce
        self.secret = secret
        self.query = query
    def to_dict(self):
        return {"nonce": self.nonce, "secret": self.secret, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(229528824, signed=False)
        writer.write_string(self.nonce)
        writer.write_string(self.secret)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        nonce = reader.read_string()
        secret = reader.read_string()
        query = reader.tgread_object()
        return cls(nonce, secret, query)

@register
class InvokeWithReCaptcha(TLObject):
    CONSTRUCTOR_ID = 2914717588
    __slots__ = ('token', 'query')
    def __init__(self, token: str, query: TLObject):
        self.token = token
        self.query = query
    def to_dict(self):
        return {"token": self.token, "query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2914717588, signed=False)
        writer.write_string(self.token)
        writer.write(bytes(self.query))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token = reader.read_string()
        query = reader.tgread_object()
        return cls(token, query)

