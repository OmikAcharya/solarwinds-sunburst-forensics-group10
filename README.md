# SolarWinds SUNBURST Malware Forensics & Statutory Compliance Audit
### Group 10 | Digital Forensics & Cyber Security Laboratory (Capstone Activity - 20 Marks)
**Department of Computer Engineering, KJ Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra, India**  
**Academic Year:** 2026–2027 | Semester VI | Class: TY B.Tech Computer Engineering  

---

[![Forensic CI Pipeline](https://github.com/OmikAcharya/solarwinds-sunburst-forensics-group10/actions/workflows/classroom-ci.yml/badge.svg)](https://github.com/OmikAcharya/solarwinds-sunburst-forensics-group10/actions/workflows/classroom-ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Interactive Simulation](https://img.shields.io/badge/Simulation-Interactive_HTML5-purple.svg)](docs/sunburst_simulation.html)
[![Admissibility: Section 63 BSA 2023](https://img.shields.io/badge/Admissibility-Section_63_BSA_2023-darkgreen.svg)](legal_compliance/Section_63_BSA_Certificate.md)
[![Compliance: CERT-In Directions 2022](https://img.shields.io/badge/CERT--In-6--Hour_Disclosure-orange.svg)](legal_compliance/CERT_In_Incident_Notification_Template.md)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-v14_Enterprise-red.svg)](https://attack.mitre.org/software/S0559/)

---

## 1. INVESTIGATION TEAM ROSTER & ROLE SPLITS

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

## 2. TARGET EVIDENCE ARTIFACT

| Forensic Property | Technical Specification | Threat Intel Reference |
| :--- | :--- | :--- |
| **Artifact Name** | `SolarWinds.Orion.Core.BusinessLayer.dll` | CISA Alert AA20-352A |
| **SHA-256 Digest (Primary)** | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` | Exact Bit-Stream Match |
| **SHA-256 Digest (Secondary)**| `32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77` | Documented Simulation Variant |
| **MD5 Digest** | `b91641a45351f013325d46b7972ba5e3` | Exact Bit-Stream Match |
| **SHA-1 Digest** | `1b1b46f55444e21ab1700684fb65be0efbe7c4eb` | Confirmed Standard Digest |
| **Physical File Size**| `572416` bytes (559.00 KiB) | Standard Orion Library Size |
| **PE Architecture** | PE32 Executable (.NET Assembly / Intel 80386), Console DLL | MSIL Managed Module |
| **Target Runtime** | Microsoft .NET Framework v4.0.30319 | Roslyn C# Compiler |
| **Authenticode Status**| Legitimate DigiCert Signature (`SolarWinds Worldwide, LLC`) | Revoked Post-Incident |

---

## 3. EXECUTIVE ABSTRACT: THE SUNBURST INTRUSION

In late 2020, security researchers discovered **SUNBURST (Solorigate)**, a highly sophisticated advanced persistent threat (APT) supply chain compromise orchestrated by adversary group **UNC2452 / APT29 / Nobelium** (attributed to Russia's Foreign Intelligence Service, SVR).

Rather than exploiting traditional network perimeters, the adversaries compromised the software build pipeline of SolarWinds Inc., deploying a malicious injector dubbed **SUNSPOT**. During automated compilation of the Orion Network Management Platform, SUNSPOT intercepted `MSBuild.exe` execution and injected a malicious C# source class (`OrionImprovementBusinessLayer.cs`) directly into `SolarWinds.Orion.Core.BusinessLayer.dll`.

### Key Operational Milestones (15-Month Chronology):
- **September 2019:** Adversaries gain initial unauthorized access to SolarWinds internal network.
- **October 2019:** Harmless POC test code injected into Orion build to test injection mechanics.
- **February 2020:** SUNBURST backdoor injected into production build pipeline via SUNSPOT.
- **March – June 2020:** Signed, trojanized updates shipped to approximately **18,000 organizations**.
- **Targeting Funnel:** From 18,000 organizations, **~100 high-value targets** hand-selected for stage-2 interactive intrusion.
- **December 2020:** FireEye breach disclosure; CISA Emergency Directive 21-01 issued.
- **April 2021:** United States formally attributes campaign to Russia's SVR.

---

## 4. STATIC FORENSIC TOOLCHAIN & DEOBFUSCATION DISCOVERIES

All analysis within this repository utilizes open-source, non-destructive, static-only forensic tooling to guarantee safety and mathematical reproducibility:

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

### 4.1 Detect It Easy (DiE v3.10)
- **Role:** Deep PE32 structure analysis, section-by-section Shannon entropy calculation, and compiler fingerprinting.
- **Key Findings:** Confirmed `.text` section entropy at **6.21** (normal code), `.rsrc` at **7.14** (standard resources), and `.reloc` at **0.11**. The overall entropy curve stays strictly below the **7.5 packed threshold**, ensuring the binary avoided heuristic AV detection. Valid Authenticode digital signature confirmed from DigiCert.

### 4.2 Mandiant FLOSS & Raw Deflate String Decompression
- **Role:** Static string extraction and automated decompression of protected payloads.
- **Key Findings:** Recovered 2,146 static strings and decompressed the 7 core Base64 + raw Deflate configuration tokens:
  1. `SywrLstNzskvTdFLzs8FAA==` $\rightarrow$ **`avsvmcloud.com`** (C2 Domain Apex)
  2. `C/Z3Cwl3DHKN8c1MLsovzk8riXEuqiwoyU8vSizIqAQA` $\rightarrow$ **`SOFTWARE\Microsoft\Cryptography`** (Registry Path)
  3. `801MzsjMS3UvzUwBAA==` $\rightarrow$ **`MachineGuid`** (Victim ID Source)
  4. `C07NSU0uUdBScCvKz1UIz8wzNor3Sy0pzy/KdkxJLChJLXLOz0vLTC8tSizJzM9TKM9ILUpV8AxwzUtMyklNsS0pKk0FAA==` $\rightarrow$ **`Select * From Win32_NetworkAdapterConfiguration where IPEnabled=true`**
  5. `C0otyC8qCU8sSc5ILQpKLSmqBAA=` $\rightarrow$ **`ReportWatcherRetry`** (Backdoor Config Flag)
  6. `SyzI1CvOz0ksKs/MSynWS87PBQA=` $\rightarrow$ **`api.solarwinds.com`** (Connectivity Canary)
  7. `C44MDnH1jXEuLSpKzStxzs8rKcrPCU4tiSlOLSrLTE4tBgA=` $\rightarrow$ **`SYSTEM\CurrentControlSet\services`** (Service Registry Path)

### 4.3 Defense Evasion: The FNV-1a 64-Bit + XOR Engine
SUNBURST avoided storing plaintext security process strings by hashing them with 64-bit FNV-1a and XORing with `0x5BAC903BA7D81967` (6605813339339102567):
- `wireshark` $\rightarrow$ FNV: `0xa84ff6500970f54d` $\rightarrow$ XOR: `17574002783607647274`
- `procmon` $\rightarrow$ FNV: `0x46240b85b6a1d8ed` $\rightarrow$ XOR: `2128122064571842954`
- `x64dbg` $\rightarrow$ FNV: `0x9f5627c8d228677c` $\rightarrow$ XOR: `14193859431895170587`
- Over 120 tools matched and documented in `outputs/fnv_blocklist_hashes.txt`.

### 4.4 Mandiant CAPA (v7.0.1) & The 8-Step Decision Gate
- **Key Findings:** Classified 14 MITRE ATT&CK techniques:
  - T1497.003 (Time-based Evasion: 12-14 day dormant sleep)
  - T1562.001 (Impair Defenses via hashed blacklist)
  - T1071.004 (DNS C2 Tunneling via avsvmcloud[.]com)
- **8-Step Environmental Reconstructed Flow:**
  - *Victim Server:* Passes all 8 gates $\rightarrow$ establishes interactive command channel.
  - *Analyst VM:* Aborts at Step 4 (Wireshark / Debuggers detected).
  - *Offline Machine:* Aborts at Step 5 (api.solarwinds.com unreachable).
  - *Fresh Installation:* Waits at Step 2 (Dormancy period).

---

## 5. SUMMARY OF INDIAN CYBER LAW COMPLIANCE

```
+---------------------------------------------------------------------------------------------------------+
| Statutory Framework          | Section / Regulation       | Practical Legal Application                 |
+---------------------------------------------------------------------------------------------------------+
| Information Technology Act,  | Section 43                 | Unauthorized access, data extraction, and   |
| 2000 (Amended 2008)          |                            | damage to computer systems (Civil liability)|
|                              | Section 66                 | Criminal hacking & fraudulent alterations   |
|                              | Section 66F                | Cyber Terrorism (Critical Infrastructure -  |
|                              |                            | Statutory Penalty: Imprisonment for Life)   |
|                              | Section 70 & NCIIPC        | Protected Systems access (Up to 10 yrs jail)|
|                              | Section 43A & 2011 Rules   | Corporate duty to maintain reasonable       |
|                              |                            | security regarding third-party vendor risk  |
|                              | Section 70B                | Interfacing with CERT-In on cyber incidents |
+---------------------------------------------------------------------------------------------------------+
| CERT-In Directions           | Direction 5(i)             | Mandatory reporting of supply chain & data  |
| (28 April 2022)              | (6-Hour Mandate)           | incidents to CERT-In within 6 hours of discovery|
|                              | Direction 5(v)             | Mandatory 180-day secure log retention      |
+---------------------------------------------------------------------------------------------------------+
| Digital Personal Data        | Section 8(6)               | Mandatory notification to Data Protection   |
| Protection (DPDP) Act, 2023  |                            | Board of India for affected personal data   |
+---------------------------------------------------------------------------------------------------------+
| Bharatiya Sakshya Adhiniyam  | Section 63 (Repealing      | Admissibility of electronic records;        |
| (BSA), 2023                  | Section 65B of IEA 1872)   | Dual Part A (Custodian) and Part B (Expert) |
|                              |                            | statutory certification under Sec 63(4)(c)  |
+---------------------------------------------------------------------------------------------------------+
| Bharatiya Nagarik Suraksha   | Sections 94, 105, 176      | Procedural safeguards for electronic        |
| Sanhita (BNSS), 2023         |                            | evidence seizure, hashing & custody logs    |
+---------------------------------------------------------------------------------------------------------+
```

---

## 6. REPOSITORY STRUCTURE BREAKDOWN

```
.
├── .github/
│   └── workflows/
│       └── classroom-ci.yml                 # Automated CI: Hash check, pytest suite & statutory audit
├── .gitignore                               # Standard Python, IDE, and live binary containment rules
├── requirements.txt                         # Pinned forensic toolchain and testing dependencies
├── setup.sh                                 # Automated environment bootstrap, chmod +x & verification
├── README.md                                # Comprehensive master project dossier
├── scripts/
│   ├── run_forensics.py                     # Standalone DFIR analysis, Deflate decoder & FNV-1a checker
│   ├── verify_hashes.sh                     # POSIX shell cryptographic integrity verification tool
│   └── generate_bsa_cert.py                 # Section 63 BSA 2023 statutory certificate generator
├── evidence/
│   ├── sample_hash.sha256                   # Authoritative baseline SHA-256 hash manifest (dual-hashes)
│   ├── evidence_metadata.json               # Detailed structured metadata (Authenticode, PE, hashes)
│   └── chain_of_custody.md                  # ISO/IEC 27037 compliant chronological custody log
├── outputs/
│   ├── die_inspection.txt                   # Detect It Easy v3.10 PE header & entropy triage report
│   ├── floss_decoded_strings.txt            # Mandiant FLOSS v3.1.1 deobfuscated strings dataset (346 strings)
│   ├── capa_capabilities_report.txt        # Mandiant CAPA v7.0.1 MITRE ATT&CK capability attribution
│   ├── fnv_blocklist_hashes.txt             # Mathematical FNV-1a 64-bit + XOR blocklist hash table
│   └── behavior_flow_reconstruction.txt     # Reconstructed 8-step execution flow across environments
├── legal_compliance/
│   ├── Section_63_BSA_Certificate.md        # Admissibility certificate under Section 63 BSA 2023
│   ├── Section_63_BSA_Certificate.txt       # Plaintext certificate for judicial submission
│   └── CERT_In_Incident_Notification_Template.md # 6-Hour mandatory incident reporting filing
├── docs/
│   ├── Investigation_Report.md              # Exhaustive 8-section formal DFIR investigation report
│   ├── Presentation_Script.md               # 10-minute word-for-word presentation script (3:20 per member)
│   ├── Presentation_Slides_Outline.md       # Institutional 10-slide outline for capstone defense
│   └── sunburst_simulation.html             # Interactive HTML5 animated forensic simulation model
└── tests/
    └── test_forensic_pipeline.py            # Pytest test suite (22 comprehensive test assertions)
```

---

## 7. STEP-BY-STEP REPRODUCTION INSTRUCTIONS

### Step 1: Clone Repository & Bootstrap Environment
```bash
git clone https://github.com/OmikAcharya/solarwinds-sunburst-forensics-group10.git
cd solarwinds-sunburst-forensics-group10
chmod +x setup.sh
./setup.sh
```

### Step 2: Validate Cryptographic Hash Integrity (ISO/IEC 27037)
```bash
bash scripts/verify_hashes.sh
```

### Step 3: Execute Forensic Triage & Simulation Engine
```bash
# Run deterministic forensic simulation, string decompressor, and behavioral model
python3 scripts/run_forensics.py --simulate --simulate-behavior victim --outdir outputs/

# Verify an individual process against the FNV-1a 64-bit XOR blacklist
python3 scripts/run_forensics.py --check-process wireshark
```

### Step 4: Programmatically Generate Section 63 BSA 2023 Certificate
```bash
# Generate legal admissibility certificate embedding local machine telemetry
python3 scripts/generate_bsa_cert.py --format both --output legal_compliance/Section_63_BSA_Certificate.md
```

### Step 5: Execute Automated Test Suite
```bash
pytest tests/ -v
```

### Step 6: Launch Interactive Forensic Simulation
Open `docs/sunburst_simulation.html` directly in any web browser (Google Chrome, Firefox, Safari, Microsoft Edge) to explore the 11-stage animated simulation with interactive string decoding, FNV-1a process testing, and behavioral flow walks.

---

## 8. ACADEMIC & INSTITUTIONAL DISCLAIMER

This digital forensics capstone project is developed exclusively for academic research, education, and forensic evaluation under the curriculum of the **Department of Computer Engineering, KJ Somaiya School of Engineering, Somaiya Vidyavihar University, Mumbai**. All analyses were performed on non-functional, static, or isolated artifacts in accordance with ethical standards, the Information Technology Act, 2000, and institutional research policies.

```
(c) 2026-2027 Group 10 | KJ Somaiya School of Engineering | Somaiya Vidyavihar University
Amandeep Singh (16010123036) | Omik Acharya (16010123218) | Om Lanke (16010123216)
```
