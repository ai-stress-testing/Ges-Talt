# OPSEC — 04. Execution (MITRE TA0002)

Source: issue #25 "Hardening" · Primary owner: `agents/security/senior-secops` +
`agents/devops/` · MITRE TA0002

Execution is the attacker running their own code on a system they've reached — a
scripting interpreter, a scheduled task, a container exec, a cloud admin API call.
OPSEC denies this by narrowing what's allowed to run and by whom, and by making
everything that does run visible enough that unauthorized execution stands out
immediately. Each row is one MITRE technique from #25 with both of its source
controls preserved; owner and phase are combined where a technique pairs a
prevention control with a detection control.

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1197 BITS Jobs | Monitor BITS jobs for unusual file types or suspicious target domains; restrict BITS job creation to admins | `agents/security/threat-detection-engineer` + `agents/security/senior-secops` | detect + prevent |
| T1651 Cloud Administration Command | Enforce least-privilege cloud admin roles; log all execution via SSM/RunCommand; require MFA for admin sessions | `agents/security/cloud-security-architect` + `agents/security/identity-access-engineer` | prevent + detect |
| T1059 Command and Scripting Interpreter | Application control to block unauthorized interpreters (PowerShell/Python/Lua); log and transcribe allowed shell sessions | `agents/security/senior-secops` | prevent + detect |
| T1609 Container Administration Command | Restrict container API (Docker/Kubernetes) access via RBAC; monitor audit logs for privileged exec commands | `agents/devops/kubernetes-engineer` | prevent + detect |
| T1610 Deploy Container | Scan images for vulnerabilities before deploy; block privileged/untrusted container deployment via admission controllers | `agents/devops/containerization-engineer` + `agents/devops/kubernetes-engineer` | prevent |
| T1675 ESXi Administration Command | Restrict vSphere API access; monitor guest commands via VMware Tools and disable guest-host communication channels | `agents/security/cloud-security-architect` | prevent + detect |
| T1203 Exploitation for Client Execution | Rigorous patching of client applications; exploit prevention via Application Guard/sandboxing | `agents/security/appsec-engineer` | prevent |
| T1574 Hijack Execution Flow | Secure search paths; strict ACLs on system directories, service binaries, and registry keys | `agents/security/senior-secops` | prevent |
| T1674 Input Injection | EDR detection of simulated keystroke patterns; block unauthorized HID devices | `agents/security/threat-detection-engineer` | detect + prevent |
| T1559 Inter-Process Communication | Disable unneeded COM/DDE; firewall and endpoint policy to restrict IPC | `agents/security/senior-secops` | prevent |
| T1106 Native API | EDR monitoring of suspicious syscall sequences; process creation/access auditing | `agents/security/threat-detection-engineer` | detect |
| T1053 Scheduled Task/Job | Audit tasks/cron/systemd timers; restrict task creation and alert on non-admin task creation | `agents/security/senior-secops` + `agents/security/threat-detection-engineer` | prevent + detect |
| T1648 Serverless Execution | Enforce least-privilege serverless execution roles; log and monitor all function invocations | `agents/security/cloud-security-architect` | prevent + detect |
| T1129 Shared Modules | Monitor unauthorized DLL/SO loads; application control to permit only approved modules | `agents/security/senior-secops` | detect + prevent |
| T1072 Software Deployment Tools | Secure credentials for SCCM/Intune/Ansible; monitor deployment logs for out-of-policy execution | `agents/devops/gitops-engineer` | prevent + detect |
| T1569 System Services | Enforce least-privilege service accounts; audit service creation/modification | `agents/security/senior-secops` | prevent + detect |
| T1127 Trusted Developer Utilities | Monitor MSBuild/ClickOnce invocation; application control to restrict use to developer workflows | `agents/security/appsec-engineer` | detect + prevent |
| T1204 User Execution | Email/web filtering; user awareness for untrusted attachments and pasted code | `agents/security/senior-secops` | prevent |
| T1047 Windows Management Instrumentation | Enable WMI event logs; restrict remote WMI access to admin hosts and monitor unusual WMI queries | `agents/security/threat-detection-engineer` + `agents/security/identity-access-engineer` | detect + prevent |
