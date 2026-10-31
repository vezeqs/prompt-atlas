# Contributing

PRs are welcome. Three rules:

1. **Use the template.** Every prompt follows the layout in
   [templates/prompt-template.md](./templates/prompt-template.md) — metadata
   header, when to use it, the prompt in a fenced block, a real example,
   notes on failure modes, and a version block.
2. **Only add prompts you've actually run.** The example output should be
   from a real session, trimmed for length if needed. No theoretical prompts,
   no scraped lists.
3. **Keep the tone.** Direct, honest about limits, no padding. If a prompt
   falls apart in a known way, say so in the notes — that's half the value.

## House style

- One prompt per file, named in lowercase kebab-case, inside the right
  `prompts/<category>/` directory.
- Add your prompt to the category index (`prompts/<category>/README.md`)
  and the full index in the root README — a prompt nobody can find is a
  prompt nobody runs.
- Placeholders in `[BRACKETS]`, documented in a variables table.
- Fenced prompt blocks use quadruple backticks when the prompt itself
  contains a triple-backtick block.
- Bump `Last updated` and add a line to `Changes` in the version block
  when you edit an existing prompt.

## Links

Every README link has to resolve — check yours before opening the PR. Run
`python3 tools/check_repo.py` locally: it checks that every relative link
resolves, that every prompt appears in both the root index and its category
index, and that every prompt has the sections this file requires. CI runs the
same check, plus an external link checker on all markdown files, so a dead link
or an unindexed prompt fails the build.
