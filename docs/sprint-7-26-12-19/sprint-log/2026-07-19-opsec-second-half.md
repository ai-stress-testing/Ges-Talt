run-id: 2026-07-19-opsec-second-half
prompt: "Remainder of macro-level threats added to issues (second half of MITRE)."
agents:
  - main/orchestrator (opus)                       # README matrix + wiring
  - opsec-2h-A (sonnet, 52,934 tok)                # #34 defense-impairment, #35 cred-access
  - opsec-2h-B (sonnet, 47,083 tok)                # #36 discovery, #37 lateral-movement
  - opsec-2h-C (sonnet, 50,473 tok)                # #38 collection, #39 C2
  - opsec-2h-D (sonnet, 42,969 tok)                # #40 exfiltration, #41 impact
specs: docs/opsec/ tactics 08-15
verdicts: PASS (build_index/verify_comms green; format consistent with 01-07)
commits: this commit + 2 prior on-branch

# 2026-07-19 — OPSEC second half: full ATT&CK kill chain

**Session/agent**: orchestrator + 4 sonnet subagents (partitioned by file).

## Done
- #34-#41: tactics 08-15 (Defense Impairment, Credential Access,
  Discovery, Lateral Movement, Collection, C2, Exfiltration, Impact).
  ~139 more technique->control->owner->phase rows. README matrix now
  lists all 15; the OPSEC gate covers the whole kill chain.
- GT-42 closed. The full MITRE matrix is now in docs/opsec/.

## Decisions
- Second-half tactics numbered 08-15 continuing the sequence; #34
  titled Defense Impairment (T1562) per the owner's 15-class scheme
  (split from Defense Evasion).

## Blocked / carried
- GT-43 (hard-verifier registry) remains the efficacy layer on top of
  these presence checklists.
