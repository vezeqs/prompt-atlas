# Audit — 2026-10-31

Scope: README, CONTRIBUTING, prompt layout, CI.
Baseline: no test or check command existed locally. CI ran lychee only; last run
2026-10-14 passed with 56 links, 31 unique, 0 errors.

| # | Finding | Severity | Status |
| --- | --- | --- | --- |
| F1 | CONTRIBUTING's rules were not checked by anything | Medium | fixed, `test_checks_pass` |
| F2 | No AGENTS.md | Medium | fixed |
| F3 | README credited the previous account login | Low | fixed |
| F4 | CONTRIBUTING said "check yours before opening the PR" but gave no command | Low | fixed |

## F1 — The repo's own rules were unenforced (Medium)

**Claim:** CONTRIBUTING rule 1 ("every prompt follows the layout"), house style
("add your prompt to the category index and the full index — a prompt nobody can
find is a prompt nobody runs"), and the variables-table rule.
**Evidence:** the only CI check was `lychee`, which validates links. A prompt
added without an index entry has no links to break, so it passes. Reproduced by
creating `prompts/coding/zz-orphan.md` with no sections and no index entry:
`lychee` would report 0 errors; `tools/check_repo.py` reports 11 problems
(1 dead link, 2 missing index entries, 5 missing sections, 3 missing version
fields). Removing the file returns the checker to 0 problems.
**Cause:** the rules live in prose only.
**Fix:** `tools/check_repo.py` checks links, index coverage, required sections,
the fenced prompt block, the variables table, and the version block.
`tests/test_repo.py` fails if any check fails or if `assets/checks.txt` drifts.
CI runs the tests before lychee.
**Status:** fixed, `test_checks_pass`, `test_capture_is_current`.

## F2 — No AGENTS.md (Medium)

Nothing told the next contributor (or agent) that a new prompt must be added to
two indexes, that the prompt block has to be fenced, or that the version block
has three required fields. **Status:** fixed.

## F3 — Stale account credit (Low)

**Evidence:** `README.md` said `**slopmanufacturer** — github.com/slopmanufacturer`.
The account's current login is `vezeqs` (display name `codefactory`); the old URL
still redirects but the name shown is not the account's name.
**Status:** fixed.

## F4 — No local check command (Low)

**Evidence:** CONTRIBUTING told contributors to check their links before opening
a PR, but the only way to do that was to install and run lychee, which the file
never mentioned.
**Status:** fixed. CONTRIBUTING now names `python3 tools/check_repo.py`.

## Verified, no finding

- All 56 links in the last CI run resolved; the glob does cover nested files
  (checked in the run log, not assumed).
- 15 prompts, each linked from the root README and from its category index.
- Each prompt has `When to use it`, `The prompt`, `Example`, `Notes`, `Version`.
- No prompt nests a triple-backtick fence inside a triple-backtick block.
- `docs/lighthouse-model-compatibility.md` is linked from the writing index and
  from the prompt that cites it, so it is not orphaned.
