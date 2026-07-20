# 2026-07-20 — Evolutionary architecture: MX + Data + fitness functions (#58)

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: #58 (GitHub); GT-58 (backlog).

```
run-id: 2026-07-20-evolutionary-architecture
prompt: "Start on 58 (MX and Data — fitness functions + evolutionary-software agents), clean up the repo, push to main. (56 deferred; user still interpreting data.)"
agents: main session only (role authoring, direct; no measured subagent token cost to ledger)
specs: 2 new roles (agent.md + SPEC.md) + docs/fitness-functions.md + software-architect charter note
verdicts: build_index PASS (105 agents, 15 teams), verify.py 10/10 PASS, verify_comms/credit/audit_skills exit 0
commits: (see push)
```

## Done
- **#58 — evolutionary architecture**, delivered as the triad the linked
  article's practice requires (feature-toggle literature — Rahman, Querel,
  Rigby, Adams, MSR 2016 — plus the fitness-function practice around
  evolutionary architecture):
  - `mx/feature-flag-engineer` — **the article-based agent**: feature toggles
    as the engine of incremental delivery across surfaces. Toggle taxonomy
    (release/experiment/ops/permission), staged & cohort rollout, kill
    switches, A/B experimentation, and the central **toggle-debt** discipline
    (every flag born with a type, owner, and removal plan; both states tested;
    stale flag = finding).
  - `data/evolutionary-data-engineer` — **the data controls** the article says
    toggles + fitness functions are unsafe without: expand-contract
    (parallel-change) schema evolution, backward/forward-compatible contracts
    across a rollout window, versioned reversible migrations, and experiment/
    cohort data governance (isolation, lineage, consent/retention, cleanup on
    toggle removal).
  - `docs/fitness-functions.md` — **the fitness-function pillar**, formalized
    as a convention rather than a new machine: a fitness function *is* a
    verifier with an architectural-characteristic property, so the GT-43
    registry (`scripts/verifiers/` + `verify.py`) is already the mechanism.
    Ownership: `logicians/software-architect` designs them (charter extended),
    the registry/testing implements them.
- **Cleanup pass**: refreshed INDEX (103→105) + repo-map + tools-baseline;
  fixed the stale enterprise.md agent count; swept for dissolved-team
  references (`platform/` mentions are intentional provenance notes,
  `netdevops` is an industry term, `mobile-release-engineer` is a real role —
  no stale refs); confirmed no tracked junk (`__pycache__` gitignored). All
  four roster lints + the 10-verifier gate green.
- **Pushed to `main`** (fast-forward) in addition to the dev branch, per owner
  request.

## Decisions
- **Fitness functions reuse the verifier registry — no second machine.** The
  cleanest reading of "fitness functions" here is that GT-43 already built
  them; #58 names the concept, maps it to the evolutionary-architecture triad,
  and assigns design ownership. Building a parallel fitness-function runner
  would duplicate `verify.py`.
- **The three roles interlock, one gap breaks it.** A fitness function gates
  the ramp, the toggle performs it, the data controls keep every ramp step
  readable — drift / flag-day / broken-read respectively if any is missing.
  Each role's SPEC hands off to the other two explicitly.
- **Toggle-debt is the headline risk** (the paper's core finding), so it's the
  feature-flag role's central discipline, not a footnote.
- **No ledger rows** — orchestrator-direct work, no measured token cost.

## Blocked / carried
- Issue **#56** deferred at owner's request (still interpreting data); **#53**
  also still open.
- Natural follow-up: a `reason`/`static` fitness-function verifier asserting
  data-contract compatibility across a rollout window, once a target repo
  exists to point it at. A verifier that pins enterprise.md's agent count to
  INDEX would end the recurring manual-count drift — a small future hygiene win.
