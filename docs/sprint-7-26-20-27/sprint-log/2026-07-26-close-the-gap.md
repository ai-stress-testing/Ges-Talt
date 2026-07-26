# 2026-07-26 — Close the gap: implement the 13 growth children (#80–#92)

**Session/agent**: main session (orchestrator), inline — the work is 13
tightly-coupled docs/templates/verifiers/scripts changes to repo conventions;
per CLAUDE.md's own cost caveat, inline beat 13 cold subagents re-deriving
context. Non-critical (no auth/API/payments/crypto/irreversible), so gated by
lint/test per #74, not the falsifier.
**Issues touched**: #80–#92 (all 13 children of epic #79); GT-82…GT-95 flipped
done. ADR-0001 recorded.

```
run-id: 2026-07-26-close-the-gap
prompt: "Close the gap. Build skills and scripts where appropriate. Then create 1 markdown artifact detailing the changes and how it changes the implementation and interface of the ai agency."
agents: main session (inline) — non-critical convention/tooling batch
specs: docs/{traceability,blueprinting,prioritization,definition-of-done,testing-tiers,risk-register,accountability,doc-metadata,for-ai-agents}.md; docs/templates/{adr,srs,design-spec,erd,release-decision,risk-assessment,vulnerability-assessment,customer-feedback}.md; docs/adr/; scripts/new_adr.py; scripts/verifiers/{traceability,doc_freshness}.py; .claude/skills/release-readiness; scripts/models.toml (local tier); .github/workflows/gate.yml; LICENSE
verdicts: gate.py 7/7 PASS (full) + 4/4 (--check); verify.py 16/16 (15 PASS, 1 SKIP). traceability.py falsification-tested both ways (FAIL on missing Verify link, PASS when present). doc_freshness PASS on 10 governed docs. Non-critical batch → lint/verifier gate per #74; falsifier deliberately NOT spawned (no critical-path system).
commits: (see push)
```

## Done
- **All 13 growth children implemented** as templates/conventions/verifiers/
  scripts — the meta-repo bar (ADR-0001): ship the reusable machinery, not a
  filled-in artifact for this repo.
- **New verifiers (fitness functions), auto-discovered by `verify.py`:**
  `traceability` (#80 — downstream half: every AC → a Verify link; SKIP until
  an issue-spec/filled-PRD exists) and `doc_freshness` (#89 — governed docs
  carry a non-stale `owner`/`last_validated` marker; 10 docs governed). Registry
  14 → 16.
- **New script:** `scripts/new_adr.py` (#81) — stamps `docs/adr/NNNN-*.md` from
  the template and regenerates `docs/adr/README.md` index; dogfooded to record
  **ADR-0001** (the meta-repo hand-off-templates decision, `accepted`).
- **New skill:** `.claude/skills/release-readiness` (#82) — the go/no-go gate
  procedure (gate → DoD → traceability → vuln/risk → Release Decision → ship).
- **8 new templates** in `docs/templates/`: adr, srs, design-spec, erd,
  release-decision, risk-assessment, vulnerability-assessment, customer-feedback.
- **9 new/edited convention docs**: traceability, blueprinting, prioritization,
  definition-of-done, testing-tiers, risk-register, accountability, doc-metadata,
  for-ai-agents; enriched issue-spec (RACI #84) and prd (business case /
  stakeholder 2×2 / risks #85); model-tiers gains the escalation ladder (#91).
- **`local` model tier** (#91) added to `models.toml` (tier + alias) — the
  bottom rung of the escalation ladder; `build_index` accepts it (106 agents,
  no churn). A declarable abstraction that precedes local infra.
- **Repo health** (#88): `LICENSE` (MIT), `.github/workflows/gate.yml` now runs
  `gate.py --check` (was build_index only), README gains gate/license/deps
  badges + a pointer to `docs/for-ai-agents.md`.
- Wired into `CLAUDE.md` (Docs convention → the hand-off kit) and
  `WORKFLOW.md §5` (the two new verifiers + the DoD/release path).

## Decisions
- **Inline, not fanned out.** 13 tightly-coupled convention edits; CLAUDE.md's
  caveat says inline is the right call for tightly-coupled work, and the
  non-negotiable is the gate, not delegation. The gate ran and is green.
- **#92 adds ZERO roles.** The deliverable was the accountability layer (by
  *elevating* existing roles — CISO=`security/architect`, CLO=`legal/general-counsel`,
  delivery=`pm/delivery-lead`) + a keep/skip *recommendation* for the #78 role
  gaps (support/IT SKIP, research-scientist KEEP-thin, GRC as a lens, marketing
  KEEP-thin). Roster shape stays the owner's call; no `build_index` roster
  change.
- **`traceability` is honest, not decorative.** It SKIPs today (no filled
  issue-spec/PRD to gate) exactly as `verdict_recorded` does — and I
  falsification-tested that it FAILs the moment a sub-issue lacks a Verify link,
  so it's a live gate, not a permanent SKIP.
- **`doc_freshness` uses an explicit governed allow-list**, so generated files /
  sprint logs / templates are exempt by construction and can't be
  double-covered or forced into a big-bang stamping.

## Blocked / carried
- **Owner-gated, deliberately not executed**: adding any actual role from #92's
  keep-list (research-scientist, marketing/launch), and provisioning a real
  local model behind the `local` tier (#91 — the abstraction is in; infra is a
  follow-on). Both await an explicit owner go.
- The templates/conventions are the agency's hand-off kit; they're exercised
  for real when the agency is pointed at a target repo.
