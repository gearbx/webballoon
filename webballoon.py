#!/usr/bin/python3

import argparse
import sys

_BAD_INPUT_ERROR_CODE = 1

def _check_larger_than_zero(value) -> int:
    try:
        v = int(value)
        if v <= 0:
            print(f"Invalid parameter value {value}", file=sys.stderr)
            sys.exit(_BAD_INPUT_ERROR_CODE)
        return v
    except Exception:
        print(f"Invalid parameter value {value}", file=sys.stderr)
        sys.exit(_BAD_INPUT_ERROR_CODE)

def _get_indent_size() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--indent", type=_check_larger_than_zero, default=2, help="the indent size in spaces.(default 2)")
    args = parser.parse_args()
    return args.indent

def _get_indent_spaces(indent: int) -> str:
    return " " * indent

def _print_to_stream(text: str):
    print(text, end="", file=sys.stdout)

def main():
    indent_increase = _get_indent_size()
    indent = 0
    for line in sys.stdin:
        for character in line:
            if character == "{":
                indent += indent_increase
                _print_to_stream(" {\n" + _get_indent_spaces(indent))
            elif character == "}":
                indent = max(0, indent - indent_increase)
                _print_to_stream("\n" + _get_indent_spaces(indent) + "}\n" + _get_indent_spaces(indent))
            elif character == ";":
                _print_to_stream(";\n" + _get_indent_spaces(indent))
            elif character == ",":
                _print_to_stream(", ")
            else:
                _print_to_stream(character)

if __name__ == "__main__":
    main()
