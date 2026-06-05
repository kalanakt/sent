#!/usr/bin/env python3
"""Run TL code generation from schema files."""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from sent._codegen.parser import parse_all_schemas
from sent._codegen.generator import generate_all


def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    mtproto_tl = os.path.join(data_dir, "mtproto.tl")
    api_tl = os.path.join(data_dir, "api.tl")

    types, functions = parse_all_schemas(mtproto_tl, api_tl)
    print(f"Parsed {len(types)} types and {len(functions)} functions")

    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tl")
    types_dir = os.path.join(base, "types")
    functions_dir = os.path.join(base, "functions")

    generate_all(types, functions, types_dir, functions_dir)
    print(f"Generated code in {types_dir} and {functions_dir}")


if __name__ == "__main__":
    main()
