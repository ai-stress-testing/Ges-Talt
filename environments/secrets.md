# Secrets

THREAT-MODEL C4. **Secrets never live in the repo, docs, container images,
the ledger, or a run manifest.** They are injected at runtime from the
environment's secret store into the process that needs them, and nowhere
else.

Owner: `security/secrets-crypto-engineer` (the injection path + key
lifecycle), `networking/network-engineer` (the store's reachability). Ties
to the encryption hard-verifiers (`docs/opsec/hard-verifiers.md`) and OPSEC
09 (Unsecured Credentials, T1552).

## Rules

- No secret in git — not in code, config, `docs/`, `docs/agent-ledger.jsonl`,
  a sprint-log run manifest, or a test fixture. Runtime injection only.
- Injected as ephemeral env/mounted material, scoped to the one process,
  never written back to disk in the repo tree.
- A secret that touches the repo is rotated immediately (assume disclosed) —
  `security/secrets-crypto-engineer` owns the rotation.
- Child processes don't inherit secrets they don't need (the env-var-leak
  gap in hard-verifiers).

## Verifier

A secret-scan runs as a hard verifier (`docs/opsec/hard-verifiers.md`,
"in-use" encryption): scan the repo tree — including `docs/`, fixtures, and
the ledger — plus any would-be commit and CI logs for secret patterns
(high-entropy strings, known key formats). A hit is a FAIL that blocks the
commit and triggers rotation. This is the mechanical backstop for the rule
above; `security/senior-secops` already scans submissions for secrets at the
PR gate, and this extends it repo-wide and to CI output.

## Not in scope here

Key *material* lifecycle (generation, rotation, envelope wrapping, KMS/HSM)
is `security/secrets-crypto-engineer`'s charter, not this file — this file
governs only that secrets stay out of the repo and reach a process only at
runtime.
