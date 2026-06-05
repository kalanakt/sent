"""Generate Python TL types and functions from parsed schema."""

from __future__ import annotations

import os
import re
from typing import Dict, List, Set

from sent._codegen.parser import CORE_TYPES, TLDefinition, TLParameter

PYTHON_KEYWORDS = {
    "True", "False", "None", "class", "def", "return", "import", "from",
    "if", "else", "elif", "for", "while", "try", "except", "finally",
    "with", "as", "pass", "break", "continue", "raise", "yield", "lambda",
    "and", "or", "not", "in", "is", "global", "nonlocal", "assert", "del",
    "async", "await", "type",
}


def _safe_class_name(name: str) -> str:
    """Convert TL name to valid Python class name."""
    parts = name.replace(".", "_").split("_")
    cls = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if cls in PYTHON_KEYWORDS:
        return f"TL{cls}"
    return cls


def _safe_module_name(name: str) -> str:
    return name.replace(".", "_").lower()


def _safe_param_name(name: str) -> str:
    """Sanitize TL parameter names that are Python keywords."""
    if name in PYTHON_KEYWORDS or name == "self" or not name.isidentifier():
        return f"{name}_"
    return name


def _build_init(args: List[TLParameter]) -> tuple:
    """Build __init__ params with required args before optional ones."""
    required = []
    optional = []
    body = []
    for arg in args:
        pname = _safe_param_name(arg.name)
        hint = _type_hint(arg)
        line = f"        self.{pname} = {pname}"
        if arg.is_flag:
            optional.append(f"{pname}: {hint} = None")
            body.append(line)
        else:
            required.append(f"{pname}: {hint}")
            body.append(line)
    params = ["self"] + required + optional
    return params, body


def _pname(arg: TLParameter) -> str:
    return _safe_param_name(arg.name)


def _flags_var(flags_field: str) -> str:
    """Variable name for a flags bitmask field."""
    return flags_field.replace("flags", "flags").replace("flags2", "flags2")


def _append_flags_bytes(lines: List[str], defn: TLDefinition) -> None:
    for ff in defn.flag_fields or (["flags"] if defn.has_flags else []):
        var = _flags_var(ff)
        lines.append(f"        {var} = 0")
        for arg in defn.args:
            if not arg.is_flag or arg.flag_index is None:
                continue
            if arg.flags_field != ff:
                continue
            pn = _pname(arg)
            if arg.type == "true":
                lines.append(f"        if self.{pn}: {var} |= 1 << {arg.flag_index}")
            else:
                lines.append(
                    f"        if self.{pn} is not None: {var} |= 1 << {arg.flag_index}"
                )
        lines.append(f"        writer.write_int({var}, signed=False)")


def _append_flags_read(lines: List[str], defn: TLDefinition) -> None:
    for ff in defn.flag_fields or (["flags"] if defn.has_flags else []):
        var = _flags_var(ff)
        lines.append(f"        {var} = reader.read_int(signed=False)")


def _type_hint(param: TLParameter) -> str:
    t = param.type
    if t in CORE_TYPES:
        mapping = {
            "int": "int",
            "long": "int",
            "double": "float",
            "string": "str",
            "bytes": "bytes",
            "Bool": "bool",
            "true": "bool",
            "int128": "bytes",
            "int256": "bytes",
        }
        return mapping.get(t, "Any")
    if t == "X":
        return "TLObject"
    if t.startswith("Vector"):
        inner = re.match(r"Vector<(.+)>", t)
        if inner:
            inner_type = inner.group(1)
            if inner_type in CORE_TYPES:
                return "List[" + _type_hint(TLParameter("", inner_type)) + "]"
            return f"List['{_safe_class_name(inner_type)}']"
        if t.startswith("Vector "):
            inner_type = t.split(" ", 1)[1]
            if inner_type in CORE_TYPES:
                return "List[" + _type_hint(TLParameter("", inner_type)) + "]"
            return f"List['{_safe_class_name(inner_type)}']"
    return f"'{_safe_class_name(t)}'"


def _vector_inner(t: str) -> str | None:
    if not t.startswith("Vector"):
        return None
    if t.startswith("Vector "):
        return t.split(" ", 1)[1]
    m = re.match(r"Vector<(.+)>", t)
    return m.group(1) if m else None


def _read_expr(param: TLParameter) -> str:
    t = param.type
    if t == "int":
        return "reader.read_int()"
    if t == "long":
        return "reader.read_long()"
    if t == "double":
        return "reader.read_double()"
    if t == "string":
        return "reader.read_string()"
    if t == "bytes":
        return "reader.read_bytes()"
    if t == "Bool":
        return "reader.tgread_bool()"
    if t == "true":
        return "True"
    if t == "int128":
        return "reader.read(16)"
    if t == "int256":
        return "reader.read(32)"
    if t in ("X", "Object"):
        return "reader.tgread_object()"
    inner = _vector_inner(t)
    if inner:
        if inner in CORE_TYPES:
            return f"reader.tgread_vector_{inner}()"
        return "reader.tgread_vector()"
    return "reader.tgread_object()"


def _write_expr(param: TLParameter, attr: str) -> str:
    t = param.type
    if t in ("int", "long"):
        signed = t == "int"
        return f"writer.write_{'int' if t == 'int' else 'long'}(self.{attr}, signed={signed})"
    if t == "double":
        return f"writer.write_double(self.{attr})"
    if t == "string":
        return f"writer.write_string(self.{attr})"
    if t == "bytes":
        return f"writer.write_bytes(self.{attr})"
    if t == "Bool":
        return f"writer.write(serialize_bool(self.{attr}))"
    if t == "true":
        return "pass  # true flag"
    if t == "int128" or t == "int256":
        return f"writer.write_raw(self.{attr})"
    if t in ("X", "Object"):
        return f"writer.write(bytes(self.{attr}))"
    inner = _vector_inner(t)
    if inner:
        if inner in CORE_TYPES:
            return f"writer.write(BinaryWriter.serialize_vector(self.{attr}, item_type='{inner}'))"
        return f"writer.write(BinaryWriter.serialize_vector(self.{attr}))"
    return f"writer.write(bytes(self.{attr}))"


def generate_type_class(defn: TLDefinition, type_ids: Dict[str, int]) -> str:
    cls_name = _safe_class_name(defn.name)
    lines = [
        f"@register",
        f"class {cls_name}(TLObject):",
        f"    CONSTRUCTOR_ID = {defn.hash}",
    ]

    if defn.result and defn.result not in CORE_TYPES:
        result_id = type_ids.get(defn.result, 0)
        if result_id:
            lines.append(f"    SUBCLASS_OF_ID = {result_id}")

    _append_slots(lines, defn)
    init_params, init_body = _build_init(defn.args)
    _append_init(lines, init_params, init_body)

    # to_dict
    lines.append("    def to_dict(self):")
    if defn.args:
        items = ", ".join(f'"{a.name}": self.{_pname(a)}' for a in defn.args)
        lines.append(f"        return {{{items}}}")
    else:
        lines.append("        return {}")

    # _bytes
    lines.append("    def _bytes(self):")
    lines.append(f"        writer = BinaryWriter()")
    lines.append(f"        writer.write_int({defn.hash}, signed=False)")
    _append_flags_bytes(lines, defn)
    for arg in defn.args:
        pn = _pname(arg)
        if arg.is_flag:
            if arg.type == "true":
                continue
            ff = _flags_var(arg.flags_field)
            lines.append(f"        if {ff} & (1 << {arg.flag_index}):")
            lines.append(f"            {_write_expr(arg, pn)}")
        else:
            lines.append(f"        {_write_expr(arg, pn)}")
    lines.append("        return writer.get_bytes()")

    # from_reader
    lines.append("    @classmethod")
    lines.append("    def from_reader(cls, reader):")
    _append_flags_read(lines, defn)
    init_args = []
    for arg in defn.args:
        pn = _pname(arg)
        ff = _flags_var(arg.flags_field)
        if arg.is_flag:
            if arg.type == "true":
                lines.append(
                    f"        {pn} = bool({ff} & (1 << {arg.flag_index}))"
                )
                init_args.append(pn)
            else:
                lines.append(f"        if {ff} & (1 << {arg.flag_index}):")
                lines.append(f"            {pn} = {_read_expr(arg)}")
                lines.append(f"        else:")
                lines.append(f"            {pn} = None")
                init_args.append(pn)
        else:
            lines.append(f"        {pn} = {_read_expr(arg)}")
            init_args.append(pn)
    if init_args:
        lines.append(f"        return cls({', '.join(init_args)})")
    else:
        lines.append("        return cls()")

    lines.append("")
    return "\n".join(lines)


def generate_function_class(defn: TLDefinition, type_ids: Dict[str, int]) -> str:
    cls_name = _safe_class_name(defn.name)
    lines = [
        f"@register",
        f"class {cls_name}(TLObject):",
        f"    CONSTRUCTOR_ID = {defn.hash}",
    ]
    if defn.result:
        result_id = type_ids.get(defn.result.split("<")[0], 0)
        if result_id:
            lines.append(f"    SUBCLASS_OF_ID = {result_id}")

    _append_slots(lines, defn)
    init_params, init_body = _build_init(defn.args)
    _append_init(lines, init_params, init_body)

    lines.append("    def to_dict(self):")
    if defn.args:
        items = ", ".join(f'"{a.name}": self.{_pname(a)}' for a in defn.args)
        lines.append(f"        return {{{items}}}")
    else:
        lines.append("        return {}")

    lines.append("    def _bytes(self):")
    lines.append("        writer = BinaryWriter()")
    lines.append(f"        writer.write_int({defn.hash}, signed=False)")
    _append_flags_bytes(lines, defn)
    for arg in defn.args:
        pn = _pname(arg)
        if arg.is_flag:
            if arg.type == "true":
                continue
            ff = _flags_var(arg.flags_field)
            lines.append(f"        if {ff} & (1 << {arg.flag_index}):")
            lines.append(f"            {_write_expr(arg, pn)}")
        else:
            lines.append(f"        {_write_expr(arg, pn)}")
    lines.append("        return writer.get_bytes()")

    lines.append("    @classmethod")
    lines.append("    def from_reader(cls, reader):")
    _append_flags_read(lines, defn)
    init_args = []
    for arg in defn.args:
        pn = _pname(arg)
        ff = _flags_var(arg.flags_field)
        if arg.is_flag:
            if arg.type == "true":
                lines.append(
                    f"        {pn} = bool({ff} & (1 << {arg.flag_index}))"
                )
            else:
                lines.append(f"        if {ff} & (1 << {arg.flag_index}):")
                lines.append(f"            {pn} = {_read_expr(arg)}")
                lines.append(f"        else:")
                lines.append(f"            {pn} = None")
        else:
            lines.append(f"        {pn} = {_read_expr(arg)}")
        init_args.append(pn)
    if init_args:
        lines.append(f"        return cls({', '.join(init_args)})")
    else:
        lines.append("        return cls()")

    lines.append("")
    return "\n".join(lines)


def generate_all(
    types: List[TLDefinition],
    functions: List[TLDefinition],
    types_dir: str,
    functions_dir: str,
) -> None:
    """Generate all type and function modules."""
    type_ids = {t.name: t.hash for t in types}

    os.makedirs(types_dir, exist_ok=True)
    os.makedirs(functions_dir, exist_ok=True)

    # Group types by namespace prefix
    type_groups: Dict[str, List[TLDefinition]] = {}
    for t in types:
        key = t.name.split(".")[0] if "." in t.name else "all"
        type_groups.setdefault(key, []).append(t)

    func_groups: Dict[str, List[TLDefinition]] = {}
    for f in functions:
        key = f.name.split(".")[0] if "." in f.name else "all"
        func_groups.setdefault(key, []).append(f)

    header = '''"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

'''

    func_header = '''"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

'''

    all_type_names = []
    all_func_names = []

    for group, defs in type_groups.items():
        mod_name = _safe_module_name(group)
        path = os.path.join(types_dir, f"{mod_name}.py")
        content = header
        for defn in defs:
            content += generate_type_class(defn, type_ids) + "\n"
            all_type_names.append(_safe_class_name(defn.name))
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    for group, defs in func_groups.items():
        mod_name = _safe_module_name(group)
        path = os.path.join(functions_dir, f"{mod_name}.py")
        content = func_header
        for defn in defs:
            content += generate_function_class(defn, type_ids) + "\n"
            all_func_names.append(_safe_class_name(defn.name))
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    # Generate __init__ files and alltlobjects
    _write_types_init(types_dir, type_groups)
    _write_functions_init(functions_dir, func_groups)
    _write_alltlobjects(types_dir, functions_dir, types, functions)


def _import_line(module: str, defn: TLDefinition) -> str | None:
    cls = _safe_class_name(defn.name)
    original = "".join(
        p[:1].upper() + p[1:] for p in defn.name.replace(".", "_").split("_") if p
    )
    # Cannot alias to Python keywords (True, False, None, ...)
    if original in PYTHON_KEYWORDS:
        return None
    if cls != original:
        return f"from {module} import {cls} as {original}"
    return f"from {module} import {cls}"


def _append_slots(lines: List[str], defn: TLDefinition) -> None:
    """Emit __slots__ for generated TL classes to avoid per-instance __dict__."""
    if defn.args:
        seen = set()
        slot_names = []
        for arg in defn.args:
            pname = _pname(arg)
            if pname not in seen:
                seen.add(pname)
                slot_names.append(pname)
        slots_repr = ", ".join(repr(name) for name in slot_names)
        lines.append(f"    __slots__ = ({slots_repr})")
    else:
        lines.append("    __slots__ = ()")


def _append_init(lines: List[str], init_params: List[str], init_body: List[str]) -> None:
    if len(init_params) > 1:
        lines.append(f"    def __init__({', '.join(init_params)}):")
        lines.extend(init_body or ["        pass"])
    else:
        lines.append("    def __init__(self):")
        lines.append("        pass")


def _write_package_init(target_dir: str, package: str, groups: Dict[str, List[TLDefinition]]) -> None:
    """Import submodules to register all TL constructors without 1600+ import lines."""
    lines = [
        f'"""TL {package.split(".")[-1]} package — auto-generated."""\n',
        "import importlib",
        "",
        "_MODULES = [",
    ]
    for group in sorted(groups):
        mod = _safe_module_name(group)
        lines.append(f'    "{mod}",')
    lines.append("]")
    lines.append("")
    lines.append("for _mod in _MODULES:")
    lines.append(f'    importlib.import_module("{package}." + _mod)')
    with open(os.path.join(target_dir, "__init__.py"), "w") as f:
        f.write("\n".join(lines))


def _write_types_init(types_dir: str, groups: Dict[str, List[TLDefinition]]) -> None:
    _write_package_init(types_dir, "sent.tl.types", groups)


def _write_functions_init(functions_dir: str, groups: Dict[str, List[TLDefinition]]) -> None:
    """Lazy-load function submodules on first attribute access."""
    lines = [
        '"""TL functions package — auto-generated."""\n',
        "from __future__ import annotations",
        "",
        "import importlib",
        "",
        "_MODULES = [",
    ]
    for group in sorted(groups):
        mod = _safe_module_name(group)
        lines.append(f'    "{mod}",')
    lines.append("]")
    lines.append("")
    lines.append("_LOOKUP = {")
    for group, defs in sorted(groups.items()):
        mod = _safe_module_name(group)
        for defn in defs:
            cls = _safe_class_name(defn.name)
            lines.append(f'    "{cls}": "{mod}",')
    lines.append("}")
    lines.append("")
    lines.append("_loaded: set[str] = set()")
    lines.append("")
    lines.append("")
    lines.append("def _ensure_loaded(mod: str) -> None:")
    lines.append('    if mod not in _loaded:')
    lines.append(f'        importlib.import_module("sent.tl.functions." + mod)')
    lines.append("        _loaded.add(mod)")
    lines.append("")
    lines.append("")
    lines.append("def __getattr__(name: str):")
    lines.append("    mod = _LOOKUP.get(name)")
    lines.append("    if mod is None:")
    lines.append('        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")')
    lines.append("    _ensure_loaded(mod)")
    lines.append('    module = importlib.import_module("sent.tl.functions." + mod)')
    lines.append("    obj = getattr(module, name)")
    lines.append("    globals()[name] = obj")
    lines.append("    return obj")
    lines.append("")
    lines.append("")
    lines.append("def __dir__():")
    lines.append("    return sorted(set(globals()) | set(_LOOKUP))")
    with open(os.path.join(functions_dir, "__init__.py"), "w") as f:
        f.write("\n".join(lines))


def _write_alltlobjects(
    types_dir: str,
    functions_dir: str,
    types: List[TLDefinition],
    functions: List[TLDefinition],
) -> None:
    lines = [
        '"""Registry of all TL constructor IDs."""\n',
        "LAYER = 225\n",
        "CONSTRUCTOR_IDS = {\n",
    ]
    for t in types:
        lines.append(f"    {t.hash}: '{t.name}',\n")
    for f in functions:
        lines.append(f"    {f.hash}: '{f.name}',\n")
    lines.append("}\n")
    path = os.path.join(os.path.dirname(types_dir), "alltlobjects.py")
    with open(path, "w") as f:
        f.write("".join(lines))
