#!/usr/bin/env python3
"""Check the claims this repo makes about itself.

Exit code 0 when every claim holds, 1 otherwise. Stdlib only, so CI needs no
setup beyond a Python interpreter.

Checks:
  1. every relative link in every markdown file resolves
  2. every prompt file is indexed in the root README and its category README
  3. every prompt has the sections CONTRIBUTING requires
  4. every prompt's "The prompt" section is inside a fenced block
  5. every prompt with [BRACKETS] documents them in a variables table
  6. every version block has Added / Last updated / Changes

Usage:
  python3 tools/check_repo.py                      # print the report
  python3 tools/check_repo.py --capture assets/checks.txt
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^(`{3,4}).*?^\1\s*$", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`")
REQUIRED_SECTIONS = ("## When to use it", "## The prompt", "## Example", "## Notes", "## Version")
VERSION_FIELDS = ("- Added:", "- Last updated:", "- Changes:")


def markdown_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def prose(path):
    """File text with fenced blocks and inline code removed — links there are not links."""
    text = FENCE.sub("", path.read_text(encoding="utf-8"))
    return INLINE_CODE.sub("", text)


def relative_links(path):
    targets = []
    for target in LINK.findall(prose(path)):
        target = target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        targets.append((path.parent / target).resolve())
    return targets


def prompt_files():
    return [p for p in sorted((ROOT / "prompts").glob("*/*.md")) if p.name != "README.md"]


def check_links():
    problems = []
    for path in markdown_files():
        for target in LINK.findall(prose(path)):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            if not (path.parent / target).resolve().exists():
                problems.append(f"{path.relative_to(ROOT)}: dead link -> {target}")
    return problems


def check_index():
    problems = []
    root_links = relative_links(ROOT / "README.md")
    for prompt in prompt_files():
        rel = prompt.relative_to(ROOT).as_posix()
        if prompt.resolve() not in root_links:
            problems.append(f"{rel}: missing from the root README index")
        category_index = prompt.parent / "README.md"
        if not category_index.exists():
            problems.append(f"{rel}: category has no README.md")
        elif prompt.resolve() not in relative_links(category_index):
            problems.append(f"{rel}: missing from {category_index.relative_to(ROOT)}")
    return problems


def check_sections():
    problems = []
    for prompt in prompt_files():
        text = prompt.read_text(encoding="utf-8")
        rel = prompt.relative_to(ROOT).as_posix()
        for section in REQUIRED_SECTIONS:
            if section not in text:
                problems.append(f"{rel}: missing section {section!r}")
        if "## The prompt" in text:
            body = text.split("## The prompt", 1)[1].split("\n## ", 1)[0]
            if not re.search(r"^(`{3,4})", body, re.MULTILINE):
                problems.append(f"{rel}: 'The prompt' section is not in a fenced block")
        if re.search(r"\[[A-Z][A-Z0-9 _/-]+\]", text) and "## Variables to fill in" not in text:
            problems.append(f"{rel}: has [BRACKETS] but no variables table")
        version = text.split("## Version", 1)[-1] if "## Version" in text else ""
        for field in VERSION_FIELDS:
            if field not in version:
                problems.append(f"{rel}: version block missing {field!r}")
    return problems


def report():
    """Return (problem_count, report_text). Deterministic, so it can be captured."""
    checks = (
        ("links", check_links()),
        ("index", check_index()),
        ("sections", check_sections()),
    )
    lines = []
    total = 0
    for name, problems in checks:
        if problems:
            lines.append(f"[{name}] {len(problems)} problem(s)")
            lines.extend(f"  - {problem}" for problem in problems)
            total += len(problems)
        else:
            lines.append(f"[{name}] ok")
    if total:
        lines.append(f"\n{total} problem(s).")
    else:
        lines.append(f"\nAll checks passed: {len(prompt_files())} prompts, {len(markdown_files())} markdown files.")
    return total, "\n".join(lines) + "\n"


def main(argv):
    total, text = report()
    if "--capture" in argv:
        target = Path(argv[argv.index("--capture") + 1])
        if not target.is_absolute():
            target = ROOT / target
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")
        return 0
    sys.stdout.write(text)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
