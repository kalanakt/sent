"""AST helpers for documentation generation."""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Param:
    name: str
    annotation: str = ""
    default: str = ""
    kind: str = "positional"


@dataclass
class MethodInfo:
    name: str
    params: list[Param] = field(default_factory=list)
    returns: str = ""
    docstring: str = ""
    is_async: bool = False


@dataclass
class ClassInfo:
    name: str
    docstring: str = ""
    methods: list[MethodInfo] = field(default_factory=list)
    bases: list[str] = field(default_factory=list)
    slots: list[str] = field(default_factory=list)
    constructor_id: Optional[int] = None


def _annotation(node: ast.AST | None) -> str:
    if node is None:
        return ""
    return ast.unparse(node)


def _default(node: ast.AST | None) -> str:
    if node is None:
        return ""
    return ast.unparse(node)


def _extract_params(args: ast.arguments) -> list[Param]:
    params: list[Param] = []
    pos = args.args
    defaults = args.defaults
    num_no_default = len(pos) - len(defaults)
    for i, arg in enumerate(pos):
        default = ""
        if i >= num_no_default:
            default = _default(defaults[i - num_no_default])
        params.append(Param(arg.arg, _annotation(arg.annotation), default))
    if args.vararg:
        params.append(Param(f"*{args.vararg.arg}", _annotation(args.vararg.annotation), ""))
    for i, arg in enumerate(args.kwonlyargs):
        default = ""
        if i < len(args.kw_defaults) and args.kw_defaults[i] is not None:
            default = _default(args.kw_defaults[i])
        params.append(Param(arg.arg, _annotation(arg.annotation), default, "keyword_only"))
    if args.kwarg:
        params.append(Param(f"**{args.kwarg.arg}", _annotation(args.kwarg.annotation), ""))
    return params


def _method_from_node(node: ast.FunctionDef | ast.AsyncFunctionDef) -> MethodInfo:
    return MethodInfo(
        name=node.name,
        params=_extract_params(node.args),
        returns=_annotation(node.returns),
        docstring=(ast.get_docstring(node) or "").strip(),
        is_async=isinstance(node, ast.AsyncFunctionDef),
    )


def parse_module(path: Path) -> list[ClassInfo]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    classes: list[ClassInfo] = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        info = ClassInfo(
            name=node.name,
            docstring=(ast.get_docstring(node) or "").strip(),
            bases=[b.id for b in node.bases if isinstance(b, ast.Name)],
        )
        for item in node.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == "CONSTRUCTOR_ID":
                        if isinstance(item.value, ast.Constant):
                            info.constructor_id = item.value.value
            if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                if item.target.id == "CONSTRUCTOR_ID" and isinstance(item.value, ast.Constant):
                    info.constructor_id = item.value.value
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if item.name.startswith("_") and item.name not in (
                    "__init__",
                    "__aenter__",
                    "__aexit__",
                    "__call__",
                ):
                    continue
                info.methods.append(_method_from_node(item))
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == "__slots__":
                        if isinstance(item.value, (ast.Tuple, ast.List)):
                            info.slots = [
                                elt.value if isinstance(elt, ast.Constant) else ast.unparse(elt)
                                for elt in item.value.elts
                            ]
        classes.append(info)
    return classes


def format_signature(method: MethodInfo, *, prefix: str = "") -> str:
    async_kw = "async " if method.is_async else ""
    params = []
    for p in method.params:
        if p.name in ("self", "cls"):
            continue
        part = p.name
        if p.annotation:
            part += f": {p.annotation}"
        if p.default:
            part += f" = {p.default}"
        params.append(part)
    ret = f" -> {method.returns}" if method.returns else ""
    return f"{async_kw}{prefix}{method.name}({', '.join(params)}){ret}"


def params_table(method: MethodInfo) -> str:
    rows = []
    for p in method.params:
        if p.name in ("self", "cls"):
            continue
        default = p.default if p.default else "—"
        ann = p.annotation if p.annotation else "—"
        rows.append(f"| `{p.name}` | `{ann}` | `{default}` |")
    if not rows:
        return "_No parameters._"
    header = "| Parameter | Type | Default |\n|-----------|------|---------|"
    return header + "\n" + "\n".join(rows)


def mdx_method_section(method: MethodInfo, example: str = "") -> str:
    sig = format_signature(method)
    doc = method.docstring or "No description available."
    lines = [
        f"### `{method.name}`",
        "",
        "```python",
        sig,
        "```",
        "",
        doc,
        "",
        "**Parameters**",
        "",
        params_table(method),
        "",
    ]
    if method.returns:
        lines.extend([f"**Returns:** `{method.returns}`", ""])
    if example:
        lines.extend(["**Example**", "", "```python", example.strip(), "```", ""])
    return "\n".join(lines)


def slugify(name: str) -> str:
    return name.lower().replace("_", "-")
