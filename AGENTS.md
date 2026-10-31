# AGENTS.md

## What this is

A curated set of prompts, one per markdown file, grouped into four categories.
There is no code and no build step: the artifact is the markdown, and the only
thing that can break is a claim in it. `tools/check_repo.py` is the test suite.

## Entry points

| Question | Where |
| --- | --- |
| How do I add a prompt? | `CONTRIBUTING.md`, then `templates/prompt-template.md` |
| Where is the full index? | `README.md` → "All prompts" |
| Where is the per-category index? | `prompts/<category>/README.md` |
| How do I check my change? | `python3 tools/check_repo.py` |
| How is the demo capture made? | `python3 tools/check_repo.py --capture assets/checks.txt` |

## Invariants

Each is checked by `tools/check_repo.py` and fails CI.

1. Every relative link in every markdown file resolves.
2. Every `prompts/*/*.md` (except `README.md`) is linked from the root README
   and from its category README.
3. Every prompt has `## When to use it`, `## The prompt`, `## Example`,
   `## Notes`, `## Version`.
4. The `## The prompt` body contains a fence of three or four backticks.
5. A prompt containing `[BRACKETS]` has a `## Variables to fill in` table.
6. The version block has `- Added:`, `- Last updated:`, `- Changes:`.
7. `assets/checks.txt` matches the current output of `report()`.

## Commands

```bash
python3 tools/check_repo.py                       # the checks
python3 -m unittest discover -s tests -v          # checks + capture freshness
python3 tools/check_repo.py --capture assets/checks.txt   # regenerate capture
```

The one command that proves the work: `python3 -m unittest discover -s tests -v`.

## Sharp edges

- **Adding a prompt means editing three files**: the prompt, its category
  README, and the root README index. The checker fails on the two you forget.
- **`assets/checks.txt` contains counts** (prompts, markdown files). Adding any
  `.md` file, including this one, invalidates it. Regenerate with `--capture`
  and update the copy quoted in `README.md`.
- **Links are resolved relative to the file that contains them**, so a category
  index uses `./name.md` while the root README uses `./prompts/<category>/name.md`.
  Do not "normalise" one to the other.
- **Links inside fenced blocks and inline code are ignored**, the same way
  markdown treats them. `prose()` strips both before scanning; keep that order.
- **External links are not checked locally.** Lychee does that in CI, and it
  needs the network; `check_repo.py` is deliberately offline and deterministic.
- **The workflow file is still named `link-check.yml`** even though it now runs
  the structural checks first. Renaming it would break nothing (no branch
  protection), but it was left alone to keep this change a rename-free diff.

## Definition of done

- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] If you added or removed a prompt, both indexes are updated.
- [ ] If you edited player-visible text in the README, `assets/checks.txt` was
      regenerated and the quoted copy in the README updated.
- [ ] `AUDIT.md` has an entry for any new finding, with a reproduction.

## Do not touch

- `LICENSE`.
- Existing prompt prose. Fix a broken claim, not the voice.
- `docs/lighthouse-model-compatibility.md` benchmark numbers without a source.
