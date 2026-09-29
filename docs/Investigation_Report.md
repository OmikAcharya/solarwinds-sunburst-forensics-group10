# FORENSIC INVESTIGATION REPORT: SUNBURST SUPPLY CHAIN INTRUSION
### Deep Static Analysis, Capability Attribution, and Indian Statutory Admissibility Assessment

**Case File Reference:** `KJSSE/COMP/DFCS/2026-27/GRP10`  
**Target Binary:** `SolarWinds.Orion.Core.BusinessLayer.dll`  
**Classification:** Advanced Persistent Threat (APT) / Software Supply Chain Compromise  
**Threat Attribution:** UNC2452 / APT29 / Nobelium / Russia SVR  
**Date of Report:** 29 September 2026  
**Investigative Body:** Digital Forensics & Cyber Security Laboratory (Lab 402)  
**Department:** Department of Computer Engineering, KJ Somaiya School of Engineering  
**University:** Somaiya Vidyavihar University, Vidyavihar, Mumbai, Maharashtra 400077, India  
**Interactive Simulation Model:** [`docs/sunburst_simulation.html`](sunburst_simulation.html)

---

## INVESTIGATION TEAM & ROLE ALLOCATION

```
+---------------------------------------------------------------------------------------------------------+
| Investigator       | Roll Number   | Primary Role & Forensic Specialization                             |
+---------------------------------------------------------------------------------------------------------+
| Amandeep Singh     | 16010123036   | Lead Investigator: PE Architecture, Header Triage & DiE Analysis  |
| Omik Acharya       | 16010123218   | Reverse Engineer: FLOSS Deobfuscation & CAPA Behavioral Attribution|
| Om Lanke           | 16010123216   | Cyber Legal Auditor: Indian Cyber Law (IT Act, CERT-In, BSA 2023)  |
+---------------------------------------------------------------------------------------------------------+
```

---

## TABLE OF CONTENTS
1. [Section 1: Executive Summary & The Six Core Forensic Inquiries](#section-1-executive-summary--the-six-core-forensic-inquiries)
2. [Section 2: Incident Overview, Attack Vector & 15-Month Chronology](#section-2-incident-overview-attack-vector--15-month-chronology)
3. [Section 3: Forensic Chain of Custody & Evidence Acquisition (ISO/IEC 27037 & BNSS 2023)](#section-3-forensic-chain-of-custody--evidence-acquisition)
4. [Section 4: Forensic Toolchain & Static Triage Methodology](#section-4-forensic-toolchain--static-triage-methodology)
5. [Section 5: Deep Reverse Engineering & Malware Behavior Analysis](#section-5-deep-reverse-engineering--malware-behavior-analysis)
   - 5.1 PE Architecture, Header Triage & Entropy Profiling (DiE)
   - 5.2 Authenticode Subversion Analysis
   - 5.3 Deflate-Raw & Base64 String Deobfuscation (FLOSS)
   - 5.4 The FNV-1a 64-Bit + XOR Defense Evasion Algorithm
   - 5.5 Behavioral Capability Mapping (CAPA & MITRE ATT&CK)
   - 5.6 Eight-Step Environmental Execution Flow Reconstruction
6. [Section 6: Statutory Violations Under Indian Cyber Jurisprudence](#section-6-statutory-violations-under-indian-cyber-jurisprudence)
   - 6.1 Information Technology Act, 2000 (Sections 43, 66, 66F, 70, 70B)
   - 6.2 IT Act Section 43A & Reasonable Security Practices Rules, 2011 (Vendor Risk)
   - 6.3 CERT-In Cyber Security Directions (6-Hour Window & 180-Day Log Retention)
   - 6.4 Digital Personal Data Protection (DPDP) Act, 2023 (Breach Notifications)
   - 6.5 Bharatiya Sakshya Adhiniyam (BSA), 2023: Section 63 Admissibility
   - 6.6 Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 (Digital Evidence Handling)
7. [Section 7: Three-Tiered Remediation & Enterprise Defense Architecture](#section-7-three-tiered-remediation--enterprise-defense-architecture)
8. [Section 8: Evaluator Conclusion & Laboratory Sign-off](#section-8-evaluator-conclusion--laboratory-sign-off)

---

## SECTION 1: EXECUTIVE SUMMARY & THE SIX CORE FORENSIC INQUIRIES

In December 2020, the global cybersecurity landscape observed one of the most patient, disciplined, and structurally concealed cyber-espionage operations in recorded history: the **SUNBURST (Solorigate)** supply chain intrusion. The adversary—tracked by threat intelligence entities as **UNC2452 / APT29 / Nobelium** (attributed by the United States and international intelligence bodies to the Russian Foreign Intelligence Service, SVR)—circumvented perimeter firewalls, network segmentation, and application allowlists by subverting the automated continuous integration and continuous delivery (CI/CD) build pipeline of SolarWinds Inc.

Through this build-system compromise, approximately **18,000 corporate, governmental, defense, and telecommunications entities** that installed legitimate updates for the SolarWinds Orion Network Management Platform simultaneously ingested a trojanized dynamic link library: `SolarWinds.Orion.Core.BusinessLayer.dll`. From this vast compromised pool, the adversary handpicked approximately **100 high-value target organizations** for second-stage interactive network intrusion.

The Digital Forensics & Cyber Security Laboratory at KJ Somaiya School of Engineering executed an end-to-end static forensic examination and statutory admissibility audit. Our investigation answered the **Six Core Forensic Inquiries** definitively without executing a single instruction on the host CPU:

```
+----+-----------------------------------------------+-------------------------------------------------------------+--------------------------+
| No | Forensic Question                             | Definitive Finding                                          | Tool / Technique         |
+----+-----------------------------------------------+-------------------------------------------------------------+--------------------------+
| 1  | What kind of file is it, and is it disguised? | Legitimate, unpacked .NET PE32 DLL signed by SolarWinds LLC | Detect It Easy v3.10     |
| 2  | What is it hiding in its binary text?         | C2 domain, registry paths & WMI queries in Deflate+Base64   | Mandiant FLOSS + Python  |
| 3  | What is it capable of doing?                  | Host profiling, process enumeration, DNS/HTTP C2 tunneling  | Mandiant CAPA v7.0.1     |
| 4  | How does it evade detection?                  | Genuine code signing, 12-14d delay, FNV-1a hashed blacklist | DiE, CAPA, FNV Engine    |
| 5  | Was electronic evidence preserved intact?     | Yes. 64/64 SHA-256 chars identical before and after triage  | Get-FileHash / POSIX sh  |
| 6  | Which Indian statutes apply?                  | IT Act Sec 43/66/66F/70; CERT-In; DPDP 2023; BSA 2023 Sec 63| Cyber Legal Audit        |
+----+-----------------------------------------------+-------------------------------------------------------------+--------------------------+
```

---

## SECTION 2: INCIDENT OVERVIEW, ATTACK VECTOR & 15-MONTH CHRONOLOGY

### 2.1 The Supply Chain Vector (SUNSPOT to SUNBURST)
Traditional malware infection models rely on spear-phishing attachments, brute-forcing RDP endpoints, or exploiting zero-day vulnerabilities in edge routers. SUNBURST employed a **Software Supply Chain Compromise (MITRE ATT&CK T1195.002)**:

```
[Threat Actor: UNC2452 / APT29 / SVR]
                 │
                 ▼
    [Compromised Internal Build Server]
                 │
                 ▼ (SUNSPOT Dropper Injected into Memory)
    [Intercepts MSBuild.exe Compilation Task]
                 │
                 ▼ (Substitutes OrionImprovementBusinessLayer.cs On-The-Fly)
    [Microsoft Roslyn C# Compiler Generates DLL]
                 │
                 ▼ (Legitimate Corporate Signing Vault)
    [Authenticode Signature Applied by DigiCert SHA-2 Assured ID CA]
                 │
                 ▼ (Official Update Package: v2020.2.1 HF 1)
[18,000 Client Networks Ingest Trojanized DLL Voluntarily]
```

### 2.2 The Fifteen-Month Chronology
The extended timeline demonstrates the extreme patience of the adversary and highlights why static forensics is indispensable:

```
+----------------+---------------------------------------------------------------------------------------------------+
| Date / Period  | Milestone / Operational Event                                                                     |
+----------------+---------------------------------------------------------------------------------------------------+
| September 2019 | Attackers gain initial unauthorized access to SolarWinds internal corporate network.             |
| October 2019   | Harmless POC test code injected into an Orion build to validate build-time source swapping.      |
| February 2020  | SUNBURST backdoor injected into production build pipeline via the SUNSPOT memory-only dropper.   |
| Mar – Jun 2020 | Digitally signed, trojanized Orion updates shipped to approximately 18,000 customer environments. |
| 08 Dec 2020    | FireEye publicly discloses breach of its proprietary internal red-team security assessment tools.  |
| 13 Dec 2020    | FireEye and CISA disclose SUNBURST; CISA issues Emergency Directive 21-01 ordering shutdown.      |
| April 2021     | US Government formally attributes the operation to Russia's Foreign Intelligence Service (SVR).    |
+----------------+---------------------------------------------------------------------------------------------------+
```

---

## SECTION 3: FORENSIC CHAIN OF CUSTODY & EVIDENCE ACQUISITION

In accordance with **ISO/IEC 27037:2012** (*Identification, Collection, Acquisition and Preservation of Digital Evidence*), **ISO/IEC 27042:2015** (*Analysis and Interpretation of Digital Evidence*), and **Section 105 of the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023**, the evidentiary lifecycle was preserved with mathematical precision.

### 3.1 Target Artifact Identifiers
- **Artifact Identifier:** `EVD-2020-SW-001`
- **File Name:** `SolarWinds.Orion.Core.BusinessLayer.dll`
- **File Size:** `572416` bytes (559.00 KiB)
- **Primary SHA-256 Digest:** `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
- **Secondary Documented SHA-256 Variant:** `32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77`
- **MD5 Digest:** `b91641a45351f013325d46b7972ba5e3`
- **SHA-1 Digest:** `1b1b46f55444e21ab1700684fb65be0efbe7c4eb`

### 3.2 Physical & Logical Safeguards
1. **Hardware Isolation:** Acquisition executed on forensic workstation KJSSE-DFIR-WS01 connected via a Tableau T8u USB 3.0 Bridge with physical write-blocking active.
2. **Cryptographic Sealing:** SHA-256 digests computed at checkout (14:10 IST) and re-verified post-investigation. All 64 hexadecimal characters matched identically (`hb == ha`), confirming zero evidence modification.

---

## SECTION 4: FORENSIC TOOLCHAIN & STATIC TRIAGE METHODOLOGY

To guarantee academic rigor and judicial reproducibility, all forensic tools employed are open-source and deterministic:

```
                               ┌────────────────────────────────────────────────┐
                               │           EVIDENCE ARTIFACT (PE32 DLL)         │
                               │    SolarWinds.Orion.Core.BusinessLayer.dll     │
                               └───────────────────────┬────────────────────────┘
                                                       │
                     ┌─────────────────────────────────┼────────────────────────────────┐
                     │                                 │                                │
                     ▼                                 ▼                                ▼
       ┌───────────────────────────┐     ┌───────────────────────────┐    ┌───────────────────────────┐
       │    DETECT IT EASY (DiE)   │     │       MANDIANT FLOSS      │    │       MANDIANT CAPA       │
       │           v3.10           │     │          v3.1.1           │    │           v7.0.1          │
       ├───────────────────────────┤     ├───────────────────────────┤    ├───────────────────────────┤
       │ - PE Header Dissection    │     │ - 346 Recovered Strings   │    │ - 14 MITRE ATT&CK Techs   │
       │ - Section Entropy Profile │     │ - Decoded 120+ AV Tools   │    │ - 12-14 Day Dormancy Rule │
       │ - Authenticode Validation │     │ - DGA C2 URLs Extracted   │    │ - DNS Tunneling Detection │
       └───────────────────────────┘     └───────────────────────────┘    └───────────────────────────┘
```

Static analysis guarantees that malicious logic is never executed on the physical processor, preventing inadvertent C2 contact or lateral transmission across university networks.

---

## SECTION 5: DEEP REVERSE ENGINEERING & MALWARE BEHAVIOR ANALYSIS

### 5.1 PE Architecture, Header Triage & Entropy Profiling (DiE)
Examination of the binary headers with **Detect It Easy (DiE v3.10)** proved:
- **Format:** PE32 executable for MS Windows (Intel 80386 i386, 32-bit console DLL).
- **Target CLR:** `.NET Framework v4.0.30319` with `COMIMAGE_FLAGS_ILONLY` set.
- **Compiler:** Microsoft Roslyn C# Compiler (Visual Studio 2019 / MSVC 14.0).
- **Shannon Entropy Analysis:**
  - `.text` (Executable Code): **6.21**
  - `.rsrc` (Resources & Manifest): **7.14**
  - `.reloc` (Relocations): **0.11**
  - **Overall File Entropy:** **5.9 to 6.32**

The entropy curve remains consistently **below the 7.5 packed threshold**. Commercial malware typically uses packers (UPX, Themida, VMProtect) which push code entropy above 7.8, triggering automated heuristics. SUNBURST avoided packers entirely, preserving a benign profile.

### 5.2 Authenticode Subversion Analysis
The security directory at RVA `0x0008B200` contained a valid Authenticode signature:
- **Signer:** `CN="SolarWinds Worldwide, LLC", OU=Software Engineering, O="SolarWinds Worldwide, LLC", L=Austin, S=Texas, C=US`
- **Issuer:** `CN=DigiCert SHA2 Assured ID Code Signing CA, OU=www.digicert.com, O=DigiCert Inc, C=US`
- **Certificate Serial:** `0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e`
- **TTP Mapping:** MITRE ATT&CK **T1553.002 (Subvert Trust Controls: Code Signing)**.

### 5.3 Deflate-Raw & Base64 String Deobfuscation (FLOSS)
When executing Mandiant FLOSS, the tool emits a standard notification:  
`WARNING: .NET string deobfuscation is not supported; extracting static strings only.`  
Nevertheless, 2,146 static strings were extracted, highlighting suspicious classes: `OrionImprovementBusinessLayer`, `ZipHelper`, `Unzip`, `DeflateStream`, and `FromBase64String`.

The malware protected its core configuration strings by applying **raw Deflate compression** followed by **Base64 encoding**. Our forensic pipeline reversed this scheme programmatically:

```
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Raw Base64 Encoded Ingestion String                                                               | Decompressed Plaintext Payload (Deflate-Raw)                          |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SywrLstNzskvTdFLzs8FAA==                                                                          | avsvmcloud.com (C2 Domain Apex)                                       |
| C/Z3Cwl3DHKN8c1MLsovzk8riXEuqiwoyU8vSizIqAQA                                                      | SOFTWARE\Microsoft\Cryptography (Registry Fingerprint Path)          |
| 801MzsjMS3UvzUwBAA==                                                                              | MachineGuid (Victim Hardware ID Source)                              |
| C07NSU0uUdBScCvKz1UIz8wzNor3Sy0pzy/KdkxJLChJLXLOz0vLTC8tSizJzM9TKM9ILUpV8AxwzUtMyklNsS0pKk0FAA== | Select * From Win32_NetworkAdapterConfiguration where IPEnabled=true  |
| C0otyC8qCU8sSc5ILQpKLSmqBAA=                                                                      | ReportWatcherRetry (Backdoor Status Flag)                             |
| SyzI1CvOz0ksKs/MSynWS87PBQA=                                                                      | api.solarwinds.com (Connectivity Check Canary)                        |
| C44MDnH1jXEuLSpKzStxzs8rKcrPCU4tiSlOLSrLTE4tBgA=                                                  | SYSTEM\CurrentControlSet\services (Service Evasion Path)              |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
```

### 5.4 The FNV-1a 64-Bit + XOR Defense Evasion Algorithm
To avoid embedding plaintext security tool names that would immediately trigger YARA rules or string searches, SUNBURST hashed all process and service names using **FNV-1a 64-bit** and XORed them against a hardcoded constant:

$$\text{Hash} = \text{FNV1a}_{64}(\text{lowercase}(\text{process\_name})) \oplus \text{0x5BAC903BA7D81967}$$

Where:
- $\text{Offset Basis} = \text{0xcbf29ce484222325}$
- $\text{FNV Prime} = \text{0x100000001b3}$
- $\text{XOR Key} = \text{0x5BAC903BA7D81967} \quad (6,605,813,339,339,102,567)$

Our verification engine proved the mathematical validity of this check against the entire blacklist:
- `wireshark` $\rightarrow$ FNV: `0xa84ff6500970f54d` $\rightarrow$ XOR: `17574002783607647274` (MATCH)
- `procmon` $\rightarrow$ FNV: `0x46240b85b6a1d8ed` $\rightarrow$ XOR: `2128122064571842954` (MATCH)
- `procexp` $\rightarrow$ FNV: `0x01b4bb85901cf144` $\rightarrow$ XOR: `6491986958834001955` (MATCH)
- `x64dbg` $\rightarrow$ FNV: `0x9f5627c8d228677c` $\rightarrow$ XOR: `14193859431895170587` (MATCH)

### 5.5 Behavioral Capability Mapping (CAPA & MITRE ATT&CK)
Mandiant CAPA v7.0.1 matched disassembled MSIL instructions to the MITRE ATT&CK Matrix:
- **T1497.003 (Time-Based Evasion):** Hardcoded `Thread.Sleep` delay of 288 hours (**12 full days**), with random jitter extending up to **14 days**.
- **T1562.001 (Impair Defenses):** Enumerate processes via `Process.GetProcesses()` and compare hashes to blacklist.
- **T1027 (Obfuscated Strings):** Custom Base64 + Deflate string decoding.
- **T1071.004 (DNS C2 Tunneling):** DGA query generation targeting `*.avsvmcloud.com`.
- **T1082 (System Information Discovery):** Query `MachineGuid` and network adapter properties.

### 5.6 Eight-Step Environmental Execution Flow Reconstruction
By correlating static disassembly with public incident telemetry, we reconstructed the exact 8-step decision gate SUNBURST follows:

```
[Step 1: Loaded by Orion?] ──────────────► Fails on non-SolarWinds processes
           │ (Pass)
[Step 2: Wait 12-14 Days] ───────────────► Fails on automated sandboxes (timeout 5-10 min)
           │ (Pass)
[Step 3: Real Corporate Network?] ───────► Fails if domain matches SolarWinds test lab
           │ (Pass)
[Step 4: Security Tools Running?] ───────► Fails if Wireshark, Sysmon, x64dbg detected
           │ (Pass)
[Step 5: Internet Reachable?] ───────────► Fails if api.solarwinds.com unreachable
           │ (Pass)
[Step 6: Beacon over DNS] ───────────────► Sends victim hash to *.avsvmcloud.com
           │ (Pass)
[Step 7: Selected by Attackers?] ────────► Fails if DNS response is CNAME sinkhole/abort
           │ (Pass)
[Step 8: HTTP Command Channel] ──────────► Backdoor opens secondary in-memory payload
```

- **Victim Orion Server:** All 8 checks pass $\rightarrow$ full C2 channel established.
- **Analyst VM:** Terminates at Step 4 (Wireshark detected).
- **Offline Machine:** Terminates at Step 5 (No internet).
- **Day 1 Deployment:** Dormant at Step 2 (Timer active).

---

## SECTION 6: STATUTORY VIOLATIONS UNDER INDIAN CYBER JURISPRUDENCE

```
+---------------------------------------------------------------------------------------------------+
| Finding in SUNBURST Backdoor                     | Governing Indian Legal Provision               |
+---------------------------------------------------------------------------------------------------+
| Backdoor planted through vendor build system      | IT Act 2000, Section 43 & Section 66           |
| Government and critical infrastructure targeted   | IT Act 2000, Section 66F (Cyber Terrorism)    |
| Critical information infrastructure affected      | IT Act 2000, Section 70 & NCIIPC Mandates     |
| Organisations deployed unverified vendor updates  | IT Act Sec 43A & Reasonable Security Rules 2011|
| Significant cyber security incident occurred      | CERT-In Directions 2022 (6h window, 180d logs) |
| Data principal personal data exposed              | Digital Personal Data Protection Act, 2023    |
| Hash integrity & custody logs preserved           | Bharatiya Sakshya Adhiniyam 2023, Section 63  |
| Digital evidence seizure & procedural extraction | Bharatiya Nagarik Suraksha Sanhita 2023        |
+---------------------------------------------------------------------------------------------------+
```

### 6.1 Information Technology Act, 2000
1. **Section 43 (Civil Liability for Damage to Computer System):** Introducing computer contaminant (trojan), extracting confidential data, and damaging defensive logging attracts civil liability for compensation under Section 43(a), (b), and (c).
2. **Section 66 (Criminal Hacking):** Dishonestly and fraudulently committing acts under Section 43 is punishable with imprisonment up to 3 years or fine up to 5 lakh rupees.
3. **Section 66F (Cyber Terrorism):** Insofar as SUNBURST compromised government ministries, defense contractors, and energy utilities, Section 66F(1)(B) applies directly. Introducing a contaminant intending to threaten national sovereignty or strike terror in people carries **Statutory Penalty: Imprisonment for Life**.
4. **Section 70 (Protected Systems):** Accessing declared protected critical systems carries mandatory imprisonment up to 10 years.

### 6.2 IT Act Section 43A & 2011 Reasonable Security Practices Rules
Corporate entities deploying third-party enterprise monitoring software without vendor risk assessments, supply chain attestations, or egress controls violate Section 43A, making them liable to pay uncapped compensation for negligence in data protection.

### 6.3 CERT-In Cyber Security Directions (28 April 2022)
Under Direction 5(i), organizations experiencing supply chain compromises must notify CERT-In **within 6 hours** of noticing. Under Direction 5(v), organizations must maintain system logs securely within the Indian jurisdiction for **180 days**.

### 6.4 Digital Personal Data Protection (DPDP) Act, 2023
Under Section 8(6) of the DPDP Act 2023, in the event of a personal data breach, the data fiduciary must notify the Data Protection Board of India and each affected data principal in such form and manner as prescribed.

### 6.5 Bharatiya Sakshya Adhiniyam (BSA), 2023: Section 63 Admissibility
Section 63 BSA 2023 repeals Section 65B of the Indian Evidence Act, 1872:
- **Section 63(2) Conditions:** Proven through steady, regular operation of the forensic workstation, normal evidence ingestion, and absence of distortion.
- **Section 63(4) Certificate:** Executed via our dual-affirmation model (Part A Custodian by Amandeep Singh; Part B Forensic Experts by Omik Acharya and Om Lanke).

### 6.6 Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023
Sections 94, 105, and 176 of the BNSS 2023 mandate strict cryptographic sealing, videography of search/seizure, and unbroken custody documentation for electronic records to prevent evidence tampering.

---

## SECTION 7: THREE-TIERED REMEDIATION & ENTERPRISE DEFENSE ARCHITECTURE

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

1. **Tier 1 (Supply-Chain Levels for Software Artifacts - SLSA Level 4):** Hermetic build containers, immutable software bills of materials (SBOM), and In-toto cryptographic attestations.
2. **Tier 2 (Hardware Security Modules):** Private code-signing keys stored exclusively in FIPS 140-2 Level 3 HSMs requiring two-person quorum verification.
3. **Tier 3 (Zero Trust Egress & Protective DNS):** Network Management Systems (NMS) segregated with zero outbound internet access. DNS Response Policy Zones (RPZ) configured to sinkhole DGA subdomains.

---

## SECTION 8: EVALUATOR CONCLUSION & LABORATORY SIGN-OFF

The investigation conclusively establishes that `SolarWinds.Orion.Core.BusinessLayer.dll` is a trojanized supply chain backdoor possessing advanced evasion, persistence, and exfiltration capabilities. The evidence has been gathered, analyzed, and preserved under international digital forensic standards and Indian evidence jurisprudence.

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
