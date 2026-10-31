# AI Prompts

A collection of prompts I actually use.

Not a scraped dump. Not 500 prompts I've never run. Just the ones that have earned a spot in my workflow — the ones I keep coming back to.

*Made with AI: the prompts in this repo are drafted and maintained with AI assistance, with a human deciding what earns a spot.*

## Why this exists

I got tired of digging through my notes app every time I needed a prompt I knew I'd written down somewhere. So I cleaned them up and put them here.

If you find something useful, take it. That's the whole point.

## What's in here

- **[Coding](./prompts/coding/)** — code review, refactoring, debugging, tests
- **[Writing](./prompts/writing/)** — drafting, editing, tightening
- **[Learning](./prompts/learning/)** — breaking down hard concepts, study plans
- **[Productivity](./prompts/productivity/)** — summaries, emails, planning

## How to use a prompt

1. Open the file for the prompt you want
2. Copy the block under **The prompt**
3. Replace anything in `[BRACKETS]` with your own stuff
4. Paste it into whatever AI you use

That's it. No installation, no setup.

## All prompts

### [Coding](./prompts/coding/)

| Prompt | What it does |
|---|---|
| [Senior Code Reviewer](./prompts/coding/code-review.md) | Reviews your code like a senior engineer would — honest, not padded with praise |
| [Explain This Diff](./prompts/coding/explain-this-diff.md) | Plain-English walkthrough of a git diff, plus what could break |
| [Regex Explainer + Builder](./prompts/coding/regex-explainer-builder.md) | Builds or explains a regex, with a list of what it won't match |
| [Rubber Duck Debugger](./prompts/coding/rubber-duck-debugger.md) | Asks pointed questions one at a time until you find the bug yourself |
| [Test Case Generator](./prompts/coding/test-case-generator.md) | Lists the test cases worth writing, grouped by intent |

### [Writing](./prompts/writing/)

| Prompt | What it does |
|---|---|
| [Cut 20%](./prompts/writing/cut-20-percent.md) | Shortens a draft by deleting, not rewriting — with a list of every cut |
| [The Fool Reads Your Draft](./prompts/writing/the-fool-reads-your-draft.md) | A court jester mocks your writing — every joke lands on a real flaw |
| [The Lighthouse Keeper's Last Letter](./prompts/writing/lighthouse-keepers-last-letter.md) | A constrained epistolary prompt — a keeper writes to the lighthouse on its final night |
| [Unsent Letter Editor](./prompts/writing/unsent-letter-editor.md) | Turns the heated version into the one you can actually send |

### [Learning](./prompts/learning/)

| Prompt | What it does |
|---|---|
| [Explain Like I'm Five](./prompts/learning/explain-like-im-five.md) | Breaks down hard concepts without dumbing them down |
| [Feynman Loop](./prompts/learning/feynman-loop.md) | You explain it back; the weakest point gets probed one question at a time |
| [Interview Me](./prompts/learning/interview-me.md) | A skeptical interviewer probes a topic, then maps your gaps |

### [Productivity](./prompts/productivity/)

| Prompt | What it does |
|---|---|
| [Decision Log](./prompts/productivity/decision-log.md) | Turns rambling pros/cons into options, regret analysis, and a call with confidence |
| [Email to Action Items](./prompts/productivity/email-to-action-items.md) | Tells you who owes whom by when — and which messages to skip |
| [Meeting Summarizer](./prompts/productivity/meeting-summary.md) | Turns a transcript into decisions, action items, and open questions |

## The format

Every prompt lives in its own file and follows the same layout: what it does, when to use it, the prompt itself, an example, and notes on when it falls apart. [Here's the template](./templates/prompt-template.md) if you want to add one.

## Adding your own

PRs are welcome. Use the template, keep the format, and don't add anything you haven't tried yourself. [More details here](./CONTRIBUTING.md).

## License

MIT. Use them, change them, share them, whatever. See [LICENSE](./LICENSE).

## Checks

`python3 tools/check_repo.py` verifies the claims this README makes: every
relative link resolves, every prompt is listed in both the root index and its
category index, and every prompt has the sections CONTRIBUTING requires. CI runs
it on every push and pull request, alongside an external link checker.

```text
[links] ok
[index] ok
[sections] ok

All checks passed: 15 prompts, 25 markdown files.
```

That block is real output from the run that added it. `assets/checks.txt` holds
the same capture, and a test fails when it drifts.

## Me

**codefactory** — [github.com/vezeqs](https://github.com/vezeqs)

I build small tools and write things down. More soon.
