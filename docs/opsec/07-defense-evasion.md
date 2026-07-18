# OPSEC — 07. Defense Evasion (MITRE TA0005)

Source: issue #33 "ID". Primary owner: `agents/security/threat-detection-engineer`.
Phase legend: prevent / detect / respond.

An adversary already inside wants to operate unseen — hiding processes and files, stripping
indicators from logs, proxying execution through trusted binaries, and defeating the sandboxes
and debuggers meant to catch them. OPSEC here denies invisibility: harden the living-off-the-land
paths attackers proxy through, and instrument the telemetry (process, memory, registry, and
network) that a hiding adversary can't avoid touching.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Access Token Manipulation (T1134) | Monitor 4688/4672 via Sysmon; restrict SeDebugPrivilege/SeImpersonatePrivilege | `agents/security/threat-detection-engineer` | detect |
| BITS Jobs (T1197) | BITS audit logging, Event ID 3; egress filtering | `agents/security/threat-detection-engineer` | detect |
| Build Image on Host (T1612) | Restrict Docker API; monitor docker build; image scanning rejects untrusted Dockerfiles | `agents/devops/containerization-engineer` | prevent |
| Debugger Evasion (T1622) | Anti-debugging in EDR; monitor IsDebuggerPresent/NtQueryInformationProcess; sandbox | `agents/security/threat-detection-engineer` | detect |
| Delay Execution (T1497.003) | Monitor long sleeps/time APIs; dynamic analysis accelerating sleep timers | `agents/security/threat-detection-engineer` | detect |
| Deobfuscate/Decode Files or Information (T1140) | Content disarm & reconstruction; EDR script analysis for base64/XOR | `agents/security/threat-detection-engineer` | detect |
| Direct Volume Access (T1006) | Restrict direct disk access via GPO; monitor \\.\PhysicalDrive handles (Sysmon 10) | `agents/security/senior-secops` | prevent |
| Execution Guardrails (T1480) | Behavior-based detection over environmental keying; sandbox for mutex/fingerprint checks | `agents/security/threat-detection-engineer` | detect |
| Exploitation for Defense Evasion (T1211) | Patch high-sev CVEs; exploit protection (Exploit Guard); monitor unusual child processes from privileged | `agents/security/cloud-security-architect` | prevent |
| Hide Artifacts (T1564) | Show hidden files via GPO; monitor hidden-attribute files; audit registry/account creation | `agents/security/threat-detection-engineer` | detect |
| Hijack Execution Flow (T1574) | App whitelisting (AppLocker/WDAC); monitor file/registry perm changes on hijackable paths | `agents/security/senior-secops` | prevent |
| Indicator Removal (T1070) | Centralize logs (4663/4660/4688) to SIEM; command-line auditing; FIM for timestomping/deletions | `agents/security/threat-detection-engineer` | detect |
| Indirect Command Execution (T1202) | Monitor child processes from forfiles/pcalua/ssh ProxyCommand; app control | `agents/security/threat-detection-engineer` | detect |
| Masquerading (T1036) | Validate signatures/hash reputation; flag renamed system binaries; train users on spoofed extensions/RTLO | `agents/security/threat-detection-engineer` | detect |
| Obfuscated Files or Information (T1027) | YARA + TI feeds for packers; dynamic unpacking sandbox | `agents/security/threat-detection-engineer` | detect |
| Pre-OS Boot (T1542) | Secure Boot + UEFI write-protection; TPM measured boot; monitor unsigned boot components | `agents/security/cloud-security-architect` | prevent |
| Process Injection (T1055) | Process Mitigation Policies; EDR memory scanning (APC/DLL injection/hollowing); monitor cross-process memory ops | `agents/security/threat-detection-engineer` | detect |
| Reflective Code Loading (T1620) | Monitor VirtualAlloc PAGE_EXECUTE_READWRITE + thread creation; AMSI | `agents/security/threat-detection-engineer` | detect |
| Rootkit (T1014) | Kernel-mode scanners + boot-time scan; Driver Signature Enforcement; monitor kernel driver loads/hooks | `agents/security/senior-secops` | prevent |
| Selective Exclusion (T1679) | Inspect file-filtering in memory; look for args excluding .dll/.exe during encryption (ransomware) | `agents/security/threat-detection-engineer` | detect |
| Social Engineering (T1684) | Awareness training; DMARC/SPF/DKIM; MFA | `agents/security/identity-access-engineer` | prevent |
| System Binary Proxy Execution (T1218) | Monitor rundll32/mshta/regsvr32 launching suspicious scripts; restrict signed binaries to expected dirs | `agents/security/threat-detection-engineer` | detect |
| System Script Proxy Execution (T1216) | Disable signed VB scripts (PubPrn/SyncAppvPublishingServer) via GPO; monitor cscript/wscript | `agents/security/senior-secops` | prevent |
| Template Injection (T1221) | Scan Office docs for remote template refs/external OLE; block untrusted external domains | `agents/networking/network-engineer` | prevent |
| Traffic Signaling (T1205) | NIDS for port knocking; monitor socket filter installs via kernel audit | `agents/networking/network-engineer` | detect |
| Trusted Developer Utilities Proxy Execution (T1127) | Restrict MSBuild/ClickOnce to build servers; monitor command-line args | `agents/devops/gitops-engineer` | prevent |
| Unused/Unsupported Cloud Regions (T1535) | Restrict resource creation to authorized regions; monitor CloudTrail/Azure for CreateInstance in unused regions | `agents/security/cloud-security-architect` | prevent |
| Valid Accounts (T1078) | MFA + conditional access; monitor anomalous logins; least privilege | `agents/security/identity-access-engineer` | prevent |
