"""Parser for Telegram TL schema (.tl) files."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class TLParameter:
    name: str
    type: str
    is_flag: bool = False
    flag_index: Optional[int] = None
    flag_name: Optional[str] = None
    flags_field: str = "flags"  # "flags" or "flags2"


@dataclass
class TLDefinition:
    name: str
    hash: int
    args: List[TLParameter] = field(default_factory=list)
    result: str = ""
    is_function: bool = False
    has_flags: bool = False
    flag_fields: List[str] = field(default_factory=list)


CORE_TYPES = {"int", "long", "double", "string", "bytes", "Bool", "true", "Null", "int128", "int256"}


def _parse_type(type_str: str) -> Tuple[str, bool, Optional[int], Optional[str], str]:
    """Parse a parameter type, handling flags and flags2."""
    if type_str == "true":
        return "true", True, None, None, "flags"

    m = re.match(r"flags(\d*)\.(\d+)\?(.+)", type_str)
    if m:
        suffix = m.group(1)
        flags_field = f"flags{suffix}" if suffix else "flags"
        flag_index = int(m.group(2))
        inner = m.group(3)
        if inner == "true":
            return "true", True, flag_index, None, flags_field
        return inner, True, flag_index, None, flags_field

    return type_str, False, None, None, "flags"


def parse_tl_file(content: str) -> Tuple[List[TLDefinition], List[TLDefinition]]:
    """Parse a .tl file into type and function definitions."""
    types: List[TLDefinition] = []
    functions: List[TLDefinition] = []
    is_function_section = False

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("---functions---"):
            is_function_section = True
            continue
        if line.startswith("---types---"):
            is_function_section = False
            continue

        # Skip core type declarations, vector template, and composite message type
        if line.startswith(("int ", "long ", "double ", "string ", "vector ", "vector#")):
            continue
        if line.startswith("message ") and "#" not in line.split()[0]:
            continue

        # Parse: name#hash args = Result;
        m = re.match(
            r"([a-zA-Z0-9_.]+)#([0-9a-fA-F]+)\s*(.*?)\s*=\s*(.+?);?\s*$",
            line,
        )
        if not m:
            continue

        name = m.group(1)
        hash_val = int(m.group(2), 16)
        args_str = m.group(3).strip()
        result = m.group(4).strip()

        args: List[TLParameter] = []
        flag_fields: List[str] = []

        if args_str:
            tokens = _tokenize_args(args_str)
            i = 0
            while i < len(tokens):
                token = tokens[i]
                i += 1
                if ":" not in token:
                    continue
                if token.startswith("{") and token.endswith("}"):
                    continue
                pname, ptype = token.split(":", 1)
                # Handle "name:Vector long" split across tokens
                if ptype == "Vector" and i < len(tokens) and ":" not in tokens[i]:
                    ptype = f"Vector {tokens[i]}"
                    i += 1
                if ptype.startswith("!"):
                    ptype = "X"
                ptype, is_flag, flag_idx, flag_name, flags_field = _parse_type(ptype)
                # Skip flag bitmask fields: flags:#, flags2:#
                if pname.startswith("flags") and ptype == "#":
                    if pname not in flag_fields:
                        flag_fields.append(pname)
                    continue
                if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", pname):
                    continue
                args.append(
                    TLParameter(
                        name=pname,
                        type=ptype,
                        is_flag=is_flag,
                        flag_index=flag_idx,
                        flag_name=flag_name,
                        flags_field=flags_field,
                    )
                )

        defn = TLDefinition(
            name=name,
            hash=hash_val,
            args=args,
            result=result,
            is_function=is_function_section,
            has_flags=bool(flag_fields),
            flag_fields=flag_fields,
        )

        if is_function_section:
            functions.append(defn)
        else:
            types.append(defn)

    return types, functions


def _tokenize_args(args_str: str) -> List[str]:
    """Split argument string into individual arg tokens."""
    tokens = []
    current = []
    depth = 0
    for ch in args_str:
        if ch == "<":
            depth += 1
            current.append(ch)
        elif ch == ">":
            depth -= 1
            current.append(ch)
        elif ch == " " and depth == 0:
            if current:
                tokens.append("".join(current))
                current = []
        else:
            current.append(ch)
    if current:
        tokens.append("".join(current))
    return tokens


def parse_all_schemas(*paths: str) -> Tuple[List[TLDefinition], List[TLDefinition]]:
    """Parse multiple .tl files and merge definitions."""
    all_types: Dict[str, TLDefinition] = {}
    all_functions: Dict[str, TLDefinition] = {}

    for path in paths:
        with open(path, encoding="utf-8") as f:
            types, functions = parse_tl_file(f.read())
        for t in types:
            all_types[t.name] = t
        for fn in functions:
            all_functions[fn.name] = fn

    return list(all_types.values()), list(all_functions.values())
