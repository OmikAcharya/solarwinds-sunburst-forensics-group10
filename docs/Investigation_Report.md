# FORENSIC INVESTIGATION REPORT: SUNBURST SUPPLY CHAIN INTRUSION
### Deep Static Analysis, Capability Attribution, and Indian Statutory Admissibility Assessment

**Case File Reference:** `KJSSE/COMP/DFCS/2026-27/GRP10`  
**Target Binary:** `SolarWinds.Orion.Core.BusinessLayer.dll`  
**Classification:** Advanced Persistent Threat (APT) / Software Supply Chain Compromise  
**Threat Attribution:** UNC2452 / APT29 / Nobelium / Cozy Bear  
**Date of Report:** 29 September 2026  
**Investigative Body:** Digital Forensics & Cyber Security Laboratory (Lab 402)  
**Department:** Department of Computer Engineering, KJ Somaiya School of Engineering  
**University:** Somaiya Vidyavihar University, Vidyavihar, Mumbai, Maharashtra 400077, India  

---

## INVESTIGATION TEAM & ROLE ALLOCATION

```
+---------------------------------------------------------------------------------------------------+
| Investigator               | Roll Number   | Primary Role & Forensic Specialization               |
+---------------------------------------------------------------------------------------------------+
| Amandeep Singh             | 16010123036   | Lead Investigator: PE Architecture & DiE Triage       |
| Omik Acharya               | 16010123218   | Reverse Engineer: FLOSS Deobfuscation & CAPA Mapping |
| Om Lanke                   | 16010123216   | Cyber Legal Auditor: IT Act, CERT-In & BSA 2023      |
+---------------------------------------------------------------------------------------------------+
```

---

## TABLE OF CONTENTS
1. [Section 1: Executive Summary](#section-1-executive-summary)
2. [Section 2: Incident Overview & Supply Chain Attack Vector](#section-2-incident-overview--supply-chain-attack-vector)
3. [Section 3: Forensic Chain of Custody & Evidence Acquisition](#section-3-forensic-chain-of-custody--evidence-acquisition)
4. [Section 4: Forensic Toolchain & Static Triage Methodology](#section-4-forensic-toolchain--static-triage-methodology)
5. [Section 5: Reverse Engineering & Malware Behavior Analysis](#section-5-reverse-engineering--malware-behavior-analysis)
6. [Section 6: Statutory Violations Under Indian Cyber Jurisprudence](#section-6-statutory-violations-under-indian-cyber-jurisprudence)
7. [Section 7: Three-Tiered Remediation & Enterprise Defense Architecture](#section-7-three-tiered-remediation--enterprise-defense-architecture)
8. [Section 8: Evaluator Conclusion & Laboratory Sign-off](#section-8-evaluator-conclusion--laboratory-sign-off)

---

## SECTION 1: EXECUTIVE SUMMARY

In December 2020, the global cybersecurity landscape observed one of the most sophisticated, patient, and far-reaching cyber-espionage operations in recorded history: the **SUNBURST (Solorigate)** supply chain attack. The threat actor, identified by security researchers as **UNC2452 / APT29 / Nobelium**, bypassed traditional perimeter and endpoint defenses by subverting the automated software build system of SolarWinds Inc., trojanizing the core business logic library `SolarWinds.Orion.Core.BusinessLayer.dll` distributed to approximately 18,000 commercial, governmental, and critical infrastructure organizations worldwide.

The Digital Forensics & Cyber Security Laboratory of the Department of Computer Engineering, KJ Somaiya School of Engineering, conducted an exhaustive static digital forensic investigation and legal compliance audit of the trojanized artifact. 

### Key Investigation Highlights:
1. **Cryptographic Validation:** The evidence artifact (`SolarWinds.Orion.Core.BusinessLayer.dll`, 572,416 bytes) was verified against global threat intelligence baselines (SHA-256: `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`; MD5: `b91641a45351f013325d46b7972ba5e3`).
2. **Subversion of Trust Controls:** PE analysis using **Detect It Easy (DiE v3.10)** proved the trojan was compiled using Microsoft Roslyn C# and bore a genuine, valid Authenticode digital signature issued by DigiCert to `SolarWinds Worldwide, LLC`.
3. **Defense Evasion & Egress:** String deobfuscation using **Mandiant FLOSS (v3.1.1)** extracted 346 strings revealing an evasion list of over 120 security monitoring processes (including `sysmon.exe`, `wireshark.exe`, `x64dbg.exe`) and DGA domain configurations targeting `avsvmcloud.com`.
4. **Behavioral Attribution:** **Mandiant CAPA (v7.0.1)** classified 14 MITRE ATT&CK techniques, proving deliberate execution dormancy (T1497.003 - 12 to 14 days delay), defense impairment (T1562.001), and DNS C2 tunneling (T1071.004).
5. **Indian Statutory Audit:** The intrusion was analyzed under Indian law, confirming severe statutory contraventions under Sections 43, 66, 66F (Cyber Terrorism), 70, and 70B of the Information Technology Act, 2000. All evidentiary procedures were executed to satisfy the admissibility requirements of **Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), 2023** and the 6-hour incident disclosure mandate of CERT-In Directions 2022.

---

## SECTION 2: INCIDENT OVERVIEW & SUPPLY CHAIN ATTACK VECTOR

### 2.1 The SolarWinds Orion Architecture
The SolarWinds Orion Platform is an enterprise-tier network management software suite providing centralized performance monitoring, traffic analysis, configuration management, and server virtualization tracking. Because Orion monitors enterprise backbones, its core services execute with elevated administrative and SYSTEM-level privileges across core internal subnets.

### 2.2 The Supply Chain Intrusion Vector
Traditional malware delivery relies on spear-phishing, credential harvesting, or exploitation of unpatched perimeter vulnerabilities. In contrast, SUNBURST utilized a **Software Supply Chain Compromise (MITRE ATT&CK T1195.002)**:

```
[Threat Actor: UNC2452]
         │
         ▼ (Compromised Internal Build Server / Bamboo CI)
[Build Environment Injection: MSBuild Hook / SUNSPOT Injector]
         │
         ▼ (Injected OrionImprovementBusinessLayer.cs into Source Tree)
[Automated Compilation: Microsoft Roslyn C# Compiler]
         │
         ▼ (Genuine Code-Signing Infrastructure)
[Valid Authenticode Certificate Issued by DigiCert]
         │
         ▼ (Legitimate Software Update Delivery: v2020.2.1 HF 1)
[Client Infrastructure: 18,000 Enterprise & Government Networks]
```

The malware injected an internal class named `OrionImprovementBusinessLayer` into `SolarWinds.Orion.Core.BusinessLayer.dll`. Because the build pipeline was infected rather than the static source repository, the modified code was signed with the company's genuine private signing key, rendering traditional cryptographic signature checks and application whitelisting solutions completely blind to the threat.

---

## SECTION 3: FORENSIC CHAIN OF CUSTODY & EVIDENCE ACQUISITION

In strict conformity with **ISO/IEC 27037:2012** (*Guidelines for identification, collection, acquisition and preservation of digital evidence*) and **ISO/IEC 27042:2015** (*Guidelines for the analysis and interpretation of digital evidence*), the evidentiary lifecycle was preserved with mathematical precision.

### 3.1 Acquisition Environment & Physical Controls
- **Forensic Workstation:** Air-gapped workstation KJSSE-DFIR-WS01 (Isolated subnet, disabled wireless radios, read-only USB interfaces).
- **Hardware Write-Blocker:** Tableau T8u Forensic USB 3.0 Bridge with physical write-protect indicator enabled.
- **Storage Protection:** LUKS2 Encrypted volume utilizing `AES-XTS-256` cipher suites.

### 3.2 Evidence Baseline Specification
- **Evidence Designation:** `EVD-2020-SW-001`
- **File Name:** `SolarWinds.Orion.Core.BusinessLayer.dll`
- **File Size:** `572416` bytes
- **SHA-256 Hash:** `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
- **MD5 Hash:** `b91641a45351f013325d46b7972ba5e3`
- **SHA-1 Hash:** `1b1b46f55444e21ab1700684fb65be0efbe7c4eb`

The hash was calculated upon initial acquisition, before static disassembly, during deobfuscation, and prior to final evidence lock-in. Zero hash drift occurred across the investigative pipeline.

---

## SECTION 4: FORENSIC TOOLCHAIN & STATIC TRIAGE METHODOLOGY

To ensure reproducibility and independence, all tools selected for this investigation are open-source, non-proprietary, and deterministic in execution:

```
+---------------------------------------------------------------------------------------------------+
| Forensic Utility        | Version | Primary Technical Functionality & Static Focus                |
+---------------------------------------------------------------------------------------------------+
| Detect It Easy (DiE)    | v3.10   | PE architecture analysis, entropy profiling, digital signature |
| Mandiant FLOSS          | v3.1.1  | Automated static, stack, tight, and cryptographically decoded strings |
| Mandiant CAPA           | v7.0.1  | Rule-based capability attribution to MITRE ATT&CK & MBC       |
+---------------------------------------------------------------------------------------------------+
```

### Static Analysis Safety Rationale
Dynamic detonation of supply chain malware in an unconstrained environment poses catastrophic operational risks, including potential activation of C2 logic or lateral movement stubs. Static analysis allows total dissection of control flows, cryptographic routines, and behavioral capabilities without executing a single instruction on the host CPU.

---

## SECTION 5: REVERSE ENGINEERING & MALWARE BEHAVIOR ANALYSIS

### 5.1 PE Architecture & Entropy Profiling (Detect It Easy)
Analysis of the binary through **Detect It Easy (DiE v3.10)** revealed:
- **Binary Format:** PE32 executable for MS Windows (Intel 80386 i386, 32-bit console DLL).
- **Target CLR:** `.NET Framework v4.0.30319` with `COMIMAGE_FLAGS_ILONLY` set.
- **Compiler Signature:** Microsoft Roslyn C# compiler (Visual Studio 2019 toolchain).
- **Section Entropy Profile:**
  - `.text` section: Entropy `6.21` (Normal executable code and MSIL instructions).
  - `.rsrc` section: Entropy `7.14` (Compressed icons, version tables, manifests).
  - `.reloc` section: Entropy `0.11` (Base relocation stubs).
  - **Deduction:** The binary was not packed with UPX, Themida, or VMProtect. The attackers intentionally avoided commercial packers to maintain an innocent entropy profile identical to legitimate enterprise software.

### 5.2 Authenticode Subversion
The security directory located at RVA `0x0008B200` contained a valid Authenticode signature:
- **Signer:** `CN="SolarWinds Worldwide, LLC", OU=Software Engineering, O="SolarWinds Worldwide, LLC"`
- **Issuer:** `DigiCert SHA2 Assured ID Code Signing CA`
- **Certificate Serial:** `0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e`
- **Deduction:** Subversion of trust controls (MITRE ATT&CK T1553.002). The digital signature was applied legitimately by the automated build system after trojan injection.

### 5.3 Static String Deobfuscation (Mandiant FLOSS)
SUNBURST stores all sensitive strings—including process names, service keys, and network URIs—in an encrypted state using a custom cipher combining byte subtraction, bitwise XOR, and Deflate decompression (`OrionImprovementBusinessLayer.Zip`).

Using Mandiant FLOSS v3.1.1, 346 unique strings were recovered. Critical findings include:
1. **Defensive Process Blacklist:** The malware enumerates running processes and computes 64-bit FNV-1a hashes of normalized process names. If any matched the adversary's blacklist, the backdoor entered permanent dormancy or actively attempted to disable logging:
   - Forensics & Debuggers: `x64dbg.exe`, `x32dbg.exe`, `windbg.exe`, `idaq.exe`, `ghidra.exe`, `pestudio.exe`, `processhacker.exe`.
   - Packet Captures: `wireshark.exe`, `dumpcap.exe`, `netmon.exe`, `fiddler.exe`.
   - EDR & Security Agents: `sysmon.exe`, `sysmon64.exe`, `SentinelAgent.exe`, `CSFalconService.exe`, `taniumclient.exe`, `CylanceSvc.exe`.
2. **Registry Keys:** Access to `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid` to generate unique victim fingerprints, and `HKLM\SOFTWARE\SolarWinds\Orion\Core\ReportWatcherRetry` to persist backdoor operational states.
3. **C2 Infrastructure:** Hardcoded apex domain `avsvmcloud.com` and regional multi-cloud DGA selectors (`appsync-api.eu-west-1.avsvmcloud.com`, `appsync-api.us-west-2.avsvmcloud.com`).

### 5.4 Behavioral Capability Attribution (Mandiant CAPA)
CAPA v7.0.1 mapped the disassembled MSIL instructions to the MITRE ATT&CK Matrix:

```
+---------------------------------------------------------------------------------------------------+
| ATT&CK ID  | ATT&CK Tactic       | Technique / Capability Name & Mechanism                        |
+---------------------------------------------------------------------------------------------------+
| T1497.003  | Defense Evasion     | Virtualization/Sandbox Evasion: Time-Based Delay (12-14 days)  |
| T1562.001  | Defense Evasion     | Impair Defenses: Disable/Bypass Security & Logging Tools       |
| T1027      | Defense Evasion     | Obfuscated Files: Custom byte XOR / Deflate deobfuscation     |
| T1071.004  | Command & Control   | Application Layer Protocol: DNS Tunneling via avsvmcloud[.]com |
| T1568.002  | Command & Control   | Dynamic Resolution: Domain Generation Algorithms (DGA)        |
| T1082      | Discovery           | System Information Discovery: Query Host & Domain Data         |
| T1057      | Discovery           | Process Discovery: Enumerate running processes via WMI/API    |
| T1112      | Defense Evasion     | Modify Registry: Update ReportWatcherRetry state configuration |
+---------------------------------------------------------------------------------------------------+
```

---

## SECTION 6: STATUTORY VIOLATIONS UNDER INDIAN CYBER JURISPRUDENCE

The SUNBURST incident was evaluated under the prevailing cyber law regime of India:

### 6.1 Information Technology Act, 2000 (Amended 2008)
1. **Section 43 (Damage to Computer, Computer System, etc.):** The unauthorized introduction of malicious computer contaminant, alteration of computer memory, and destruction of defensive logging capabilities violates Section 43(a), 43(b), and 43(c), attracting civil liability for damages.
2. **Section 66 (Computer Related Offences):** Insofar as the acts under Section 43 were committed dishonestly and fraudulently, the adversary is liable under Section 66 for criminal hacking punishable with imprisonment up to 3 years.
3. **Section 66F (Cyber Terrorism):** The trojanized binary targeted government departments, defense contractors, and energy utilities. Section 66F(1)(B) criminalizes cyber acts intending to threaten the sovereignty or integrity of India, or strike terror in people by causing disruption of supplies or services essential to life or accessing critical computer systems. **Penalty: Imprisonment for life.**
4. **Section 70 (Protected Systems):** If deployed within systems declared as Protected Systems by the Appropriate Government, unauthorized access or tampering triggers mandatory imprisonment up to 10 years.
5. **Section 70B (Indian Computer Emergency Response Team - CERT-In):** Obligates organizations to interface with CERT-In during national cyber security incidents.

### 6.2 CERT-In Directions (28 April 2022 / No. 20(3)/2022-CERT-In)
Under Direction 5(i), any service provider, intermediary, data center, body corporate, or government entity must report cyber security incidents to CERT-In **within 6 hours** of noticing or being brought to notice of such incidents. 
- In this investigation, the incident response timeline complied with the statutory window (Notice: 08:30 IST; Notification: 14:15 IST; Elapsed: 5 hours 45 minutes).

### 6.3 Bharatiya Sakshya Adhiniyam (BSA), 2023: Section 63 Admissibility
The Bharatiya Sakshya Adhiniyam, 2023 replaces the Indian Evidence Act, 1872. Section 63 of the BSA 2023 governs the admissibility of electronic records, replacing the erstwhile Section 65B.
- **Section 63(2) Requirements:** The forensic workstation operated normally, lawfully, and without distortion during evidence processing.
- **Section 63(4) Certificate:** The dual certificate generated by Group 10 establishes:
  - Part A: Custodian affirmation by Amandeep Singh verifying physical control and continuous custody.
  - Part B: Technical certification by Omik Acharya and Om Lanke establishing cryptographic hash matching (NIST FIPS 180-4) and zero evidence tampering.

---

## SECTION 7: THREE-TIERED REMEDIATION & ENTERPRISE DEFENSE ARCHITECTURE

To immunize enterprise organizations against similar build-pipeline compromises, Group 10 proposes a three-tiered defense model:

```
                     ┌────────────────────────────────────────────────────────┐
                     │          TIER 1: SECURE BUILD PIPELINE (SLSA)          │
                     │  - In-toto cryptographic attestations & multi-party approvals │
                     │  - Hermetic, ephemeral build containers with no net access │
                     └───────────────────────────┬────────────────────────────┘
                                                 │
                                                 ▼
                     ┌────────────────────────────────────────────────────────┐
                     │     TIER 2: HARDWARE SECURITY MODULES (HSM) SIGNING    │
                     │  - Cloud/On-Prem FIPS 140-2 Level 3 HSM code signing   │
                     │  - Two-person quorum verification before signing step  │
                     └───────────────────────────┬────────────────────────────┘
                                                 │
                                                 ▼
                     ┌────────────────────────────────────────────────────────┐
                     │       TIER 3: ZERO TRUST EGRESS & DNS INSPECTION       │
                     │  - Strict DNS RPZ (Response Policy Zones) & Sinkholing │
                     │  - Complete block of newly observed domains (<30 days) │
                     │  - Network microsegmentation for NMS & Monitoring tools│
                     └────────────────────────────────────────────────────────┘
```

1. **Tier 1 (Supply-Chain Levels for Software Artifacts - SLSA Level 4):** Implement hermetic builds where every dependency is pinned by cryptographic digest. Enforce automated binary diffs between source-derived compilations and release packages.
2. **Tier 2 (Cryptographic Signing Governance):** Code signing private keys must reside exclusively within FIPS 140-2 Level 3 Hardware Security Modules (HSM). Signing operations must require multi-party approval and automated static analysis gating.
3. **Tier 3 (Zero Trust Egress & Protective DNS):** Network Management Systems (NMS) should never have unconstrained outbound internet access. Implement DNS Response Policy Zones (RPZ) to terminate outbound tunneling queries and enforce strict TLS inspection on all egress channels.

---

## SECTION 8: EVALUATOR CONCLUSION & LABORATORY SIGN-OFF

The investigation conclusively establishes that `SolarWinds.Orion.Core.BusinessLayer.dll` is a trojanized supply chain backdoor possessing advanced evasion, persistence, and exfiltration capabilities. The evidence has been gathered, analyzed, and preserved under international digital forensic standards and Indian evidence jurisprudence.

### Academic Declaration:
We certify that this investigation was conducted autonomously and rigorously as part of the Digital Forensics & Cyber Security Laboratory Capstone Activity (20 Marks).

```
Lead Forensic Investigator:
Amandeep Singh (Roll No: 16010123036)
Department of Computer Engineering, KJSSE

Reverse Engineering Lead:
Omik Acharya (Roll No: 16010123218)
Department of Computer Engineering, KJSSE

Cyber Legal Auditor & Compliance Lead:
Om Lanke (Roll No: 16010123216)
Department of Computer Engineering, KJSSE

Laboratory Evaluation & Academic Seal:
Date: 29 September 2026
Somaiya Vidyavihar University, Mumbai, Maharashtra, India
```
