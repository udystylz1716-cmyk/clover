#!/usr/bin/env python3
"""Clover quality gate (PreToolUse hook for Write and Edit).

Blocks a save to output/ if the resulting file would contain an em dash
or the word "guarantee" in any capitalisation (house rules 1 and 2).

Exit 0 = allow. Exit 2 = block (stderr is shown to Claude so it can fix the text).
"""
import json
import os
import re
import sys

EM_DASH = "—"
GUARANTEE = re.compile(r"guarantee", re.IGNORECASE)  # also catches guaranteed, guarantees, guaranteeing


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def resulting_content(tool_name, tool_input, path):
    """Return the full file text as it would be after this Write or Edit, or None to let it through."""
    if tool_name == "Write":
        return tool_input["content"]

    # Edit: apply the change to the current file to get the whole resulting text.
    with open(path, encoding="utf-8") as f:
        current = f.read()
    old, new = tool_input["old_string"], tool_input["new_string"]
    if old not in current:
        return None  # the Edit tool will fail on its own
    if tool_input.get("replace_all"):
        return current.replace(old, new)
    return current.replace(old, new, 1)


def find_problems(text):
    problems = []
    for number, line in enumerate(text.splitlines(), start=1):
        if EM_DASH in line:
            problems.append(f"line {number}: em dash (house rule 1, use a comma, full stop or brackets)")
        for match in GUARANTEE.finditer(line):
            problems.append(f'line {number}: "{match.group(0)}" (house rule 2, never use "guarantee" in any form)')
    return problems


def main():
    project = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
    output_dir = os.path.join(project, "output") + os.sep

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Cannot tell which file this is, so fail closed.
        block("Clover hook: could not read the hook input, so the save was blocked to be safe.")

    tool_name = data.get("tool_name")
    tool_input = data.get("tool_input") or {}
    if tool_name not in ("Write", "Edit"):
        sys.exit(0)

    path = os.path.realpath(tool_input.get("file_path", ""))
    if not path.startswith(output_dir):
        sys.exit(0)  # only files in output/ are checked

    try:
        text = resulting_content(tool_name, tool_input, path)
    except (OSError, KeyError, UnicodeDecodeError) as error:
        block(f"Clover hook: could not check {path} ({error}), so the save was blocked to be safe.")

    if text is None:
        sys.exit(0)

    problems = find_problems(text)
    if problems:
        relative = os.path.relpath(path, project)
        block(
            f"Clover hook blocked the save to {relative}. The file would break the house rules:\n- "
            + "\n- ".join(problems)
            + "\nFix every line listed, then save again."
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
