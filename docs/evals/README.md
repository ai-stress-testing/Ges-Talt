# Agent evals — one directory per team

Issue #49 ("Eval Agent"): a role that evaluates *other agents* against
tests designed for that agent, grounded in mathematics and abstract
algebra — group-theory-style abstraction over an agent's behavior space
(the set of inputs, the transformations its acceptance criteria promise,
the invariants its outputs must preserve across them). The role is
`agents/logicians/agent-evaluator`; this directory is where its output
lives.

## Layout

```
docs/evals/<team>/<role>-<yyyy-mm-dd>.md   (one evaluation file per run)
```

One subdirectory per team — `docs/evals/backend/`, `docs/evals/design/`,
`docs/evals/security/`, and so on, mirroring `agents/<team>/`. Each
subdirectory holds `agent-evaluator`'s results for every role on that
team it has evaluated: which SPEC acceptance criteria hold, which break,
the specific input class that breaks each one, and the closure/identity/
composition verdicts for that agent's behavior space.

## Why one role, filed per team — not fifteen evaluators

The evaluation *method* is universal: reasoning about a declared domain,
a transformation, and an invariant with group-theory abstraction doesn't
change shape between `backend/backend-dev` and `design/ui-designer` — only
the domain being abstracted over changes, and that comes from the target
agent's own `SPEC.md`, not from the evaluator's. Issue #49 states this
directly: the method "evaluates all things." Standing up a
`backend/agent-evaluator`, a `design/agent-evaluator`, a
`security/agent-evaluator`, and so on would be fifteen copies of the same
reasoning procedure pointed at different folders — exactly the
duplication the roster rules forbid (`agents/README.md`, `agents/logicians/
README.md`'s team norm). So there is one role,
`agents/logicians/agent-evaluator`, applied to whichever agent needs
evaluating, and its *output* is what gets partitioned per team — because
the results, unlike the method, are genuinely team-specific: they belong
next to the team whose agent was evaluated, for that team to act on.

This is the same shape as `docs/opsec/`: one applied discipline
(`security/` + `networking/` roles working an ATT&CK matrix), organized
into per-tactic files rather than duplicated per consumer. Here the axis
is team instead of MITRE tactic, and the discipline is
`logicians/agent-evaluator` instead of the security roster.

## Complements, doesn't duplicate, `docs/credit.md`

`docs/credit.md` and `docs/feedback-loop.md` already give every role a
selection signal from `docs/agent-ledger.jsonl` — pass rate, mean token
cost, mean retries, rolled into a relative score
(`docs/selection-weights.json`) that `pm/project-manager` reads when
picking an assignee. That signal is empirical and outcome-shaped: it
answers "has this role been cheap and reliable across its actual runs."

What lives here is structural and spec-shaped instead: it answers "does
this role's behavior actually satisfy the algebraic invariants its own
charter promises" — independent of whether recent runs happened to pass.
A role can have a healthy credit score and still carry a SPEC criterion
that's silently unenforced, or an untestable criterion nobody flagged; a
role can also have a rough credit score from an unlucky sample while its
structure is sound. The two signals are read together, not merged: credit
says whether a role has been performing; an eval filed here says whether
a role's own contract holds together, criterion by criterion, closure by
closure.

## Filing an evaluation

`agent-evaluator` writes one file per run into `docs/evals/<team>/`,
named for the role and date. A run that finds nothing wrong still gets
filed — a clean hold/break map across every acceptance criterion, plus
the closure/identity/composition checks, is itself the record; silence
is not evidence of a passing evaluation.
