# 2026-07-17 — Legal team from issue #1 (first spec-driven run)

**Session/agent**: main session, running the spec-driven PM flow end to end.
**Issues touched**: #1 (parent), #2–#6 (sub-issues).

## Done
- Issue spec posted on #1; five granular sub-issues created with
  assignees, acceptance criteria, and negative prompts.
- agents/legal/ team: privacy-engineer ("true to code" GDPR
  verification), data-protection-officer (privacy program + 72h breach
  clock), product-counsel (ToS/policies/OSS licensing), general-counsel
  (opus read-only issue-spotting + risk register).
- Boundaries recorded in team README: WCAG stays with
  section-508-specialist/accessibility-auditor; certifications with
  security/compliance-auditor; residency topology with
  academic/geographer.
- AUDIT.md gap #7 (data governance) marked closed.

## Decisions
- Legal team-wide rule: no Edit/Bash ever; general-counsel is fully
  read-only (opus, no Write) — no new lint exception needed.
- WCAG "coverage" = tracked exposure citing existing owners, not a
  third accessibility auditor.

## Blocked / carried
- Issue #1 left open pending owner's merge of the sprint branch;
  sub-issues closed as implemented.
