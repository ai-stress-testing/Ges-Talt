# Red Team — standing critique pairing (issue #47)

Every blue-team (defensive) security role gets a standing red-team
critique from `security/red-team-critic`. The pairing is the security
analog of the verdict loop's adversary grader
(`agents/logicians/falsifier` ↔ the producer it checks,
`agents/WORKFLOW.md` §1): a defensive control isn't done until its
red-team critique has been produced against it, and survived.

`red-team-critic` is read-only and reasoning-bound (opus; Read/Grep/Glob
only, per `agents/TEMPLATE`'s roster lint). It presumes a designated
control is already beaten and works backward to the attacker's concrete
bypass path — technique, input, or step sequence — in
`agents/WORKFLOW.md`'s FAIL-handback shape: expected control → actual
bypass → the attack steps → root cause of the defensive gap → the fix
that closes it. A critique with no concrete bypass path is invalid, same
bar as the falsifier; a PASS with no attempts listed is invalid too.

**`security/penetration-tester` is the ACTIVE arm** — authorized
exploitation against the org's own systems inside a signed engagement
scope, with execution tools (`Bash`, `Write`) to match. `red-team-critic`
is the standing, design-time critique: no engagement, no execution, just
the disproof. A bypass `red-team-critic` finds that needs actual running
to confirm gets routed to `penetration-tester` (in-scope engagement) or
`testing/reality-checker`, never asserted as reasoned-through.

## The pairing

One row per blue-team role currently in `agents/security/`: the
red-team question its standing critique must answer.

| Blue-team role | Red-team question its critique must answer |
|---|---|
| `security/architect` | What trust-boundary assumption does the design get away with, and what's the concrete abuse path through it? |
| `security/appsec-engineer` | What payload gets through this code-level fix — which injection, authz gap, or crypto misuse wasn't covered? |
| `security/cloud-security-architect` | What IAM or network path crosses this zero-trust boundary that the policy-as-code guardrail didn't block? |
| `security/senior-secops` | What bypasses this PR-gate control — which header, CORS, rate-limit, CSP, or secret-scan case slips through? |
| `security/threat-detection-engineer` | What evades this detection? |
| `security/threat-intelligence-analyst` | What TTP, actor attribution, or confidence call does this assessment get wrong, and what does the adversary actually do differently? |
| `security/incident-responder` | What does this containment/forensics playbook miss that lets the attacker keep a foothold, or destroys evidence first? |
| `security/secrets-crypto-engineer` | Where does key material leak? |
| `security/identity-access-engineer` | What auth/session/tenant-isolation check can be forged, replayed, or confused into granting access it shouldn't? |
| `security/rbac-abac-consultant` (new consultant) | What grant in this access-control model lets a subject reach an object none of the spec's user journeys justified? |
| `security/rls-consultant` (new consultant) | What query or session-context trick makes a supposedly deny-by-default row policy return a row it shouldn't? |

## The gate

Same shape as the OPSEC gate (`docs/opsec/README.md`): before the paired
control ships, the owning blue-team role's output goes to
`security/red-team-critic` as the security step of the verdict loop
(`agents/WORKFLOW.md` §1). FAIL hands back to the owning role with the
bypass and its fix; PASS (with attempts listed) clears the gate. A
control added to `agents/security/` after this doc ships gets a row added
here before it's considered paired.
