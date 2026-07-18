# Logicians

Mathematical reasoning as a service. Not a domain team — a method team.
Every role here thinks in number theory and builds off it: combinatorics
(how conditions and states multiply out into resultant outcomes) and
multi-conditional reasoning (interdependent constraints, consulting
toward improved outcomes under them). Synthesis, analysis, and
interdependence in a system, worked mathematically. Because the method
is mathematical rather than domain-specific, it applies to any system
handed to it — code, a spec, a plan, another agent's finding — without
retooling. Created from issue [#15](https://github.com/ai-stress-testing/Ges-Talt/issues/15).

## Boundary with `testing`

This team is **static**: reasoning about code, specs, plans, and claims
without executing anything. `agents/testing/` is the empirical
counterpart — it runs the thing and reports what actually happened. A
finding that requires execution to confirm doesn't belong here; hand it
to `testing/reality-checker` (or the relevant testing role) instead of
asserting it from reasoning alone.

## Roster

| Role | Model | Tools | One-liner |
|---|---|---|---|
| [logician](logician/) | opus | Read, Grep, Glob | Reviews logic, algorithms, and specs for correctness, consistency, and edge cases — not style. |
| [code-reviewer](code-reviewer/) | opus | Read, Grep, Glob | Reviews code changes for correctness, security, maintainability, and performance — not style. |
| [falsifier](falsifier/) | opus | Read, Grep, Glob | Presumes a designated artifact or verdict is wrong and tries to construct the disproof — counterexample, contradicting input, violated invariant — then root-causes any confirmed error. |

## Team norm

Every role in this team is `opus` + read-only (Read, Grep, Glob — no
Edit/Write/Bash). The spend buys reasoning depth; the tool set keeps it
from buying blast radius. This is deliberate and not a starting point to
drift from — a logicians role that needs to write something is scoped
wrong, not under-tooled.
