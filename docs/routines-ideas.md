# Routines — brainstorm

Parking lot for recurring autonomous work (issue: routines). A routine is
recurring work with a **cadence**, an **owning agent**, and a **mechanism**.
Not a convention yet — the owner is still deciding which of these earn their
keep. When one graduates, it becomes a `docs/enterprise.md` Taxonomy entry
and (if it governs artifacts) falls under `devops/lifecycle-manager`.

Two mechanisms:
- **GitHub Actions `schedule:`** — stateless repo-hygiene checks, no
  session needed.
- **Scheduled trigger** (wakes a session) — judgment work that needs an
  agent to reason, not just a pass/fail gate.

## Candidate routines

| Routine | Cadence | Owner agent | Mechanism | What it does |
|---|---|---|---|---|
| Roster lint + audit re-run | nightly | devops/devops-automator | Actions schedule | Re-run `build_index.py` + `verify_comms.py`; open an issue on any new violation. |
| Charter-drift audit | weekly | logicians/logician | scheduled trigger | Read the roster for overlap/contradiction the fast conversions may have introduced. |
| Sprint rollover | on window turn | pm/team-operations | scheduled trigger | Scaffold the next `sprint-*` folder before the current window closes. |
| Stale-session reaping | daily | networking/network-engineer | scheduled trigger | Proactive session deletion (the original GT-6 ask). |
| Credit rollup | weekly | (observer) | scheduled trigger | Aggregate `docs/agent-ledger.jsonl` into a per-role cost/outcome scorecard; flag drift. |
| Dependency/EOL sweep | monthly | devops/lifecycle-manager | scheduled trigger | Flag artifacts past their sunset date or nearing dependency EOL. |
| Threat re-model | per env change | security/architect | manual trigger | Re-run `environments/THREAT-MODEL.md` when environments/ config changes. |
| Grader red-team | weekly | ai/model-evaluator | scheduled trigger | Plant known-bad/known-good artifacts, measure the falsifier's false-negative rate (GT-35 / #30 finding 5). |

## Open questions for the brainstorm

- Which of these are worth the token cost of a woken session vs. a cheap
  Actions check?
- Does a routine need its own registry file, or is a Taxonomy section in
  `docs/enterprise.md` enough?
- Who owns a routine that fails — the owning agent, or a new observer role?
