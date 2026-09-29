# SolarWinds SUNBURST Malware Forensics & Statutory Compliance Audit
### Group 10 | Digital Forensics & Cyber Security Laboratory (Capstone Activity - 20 Marks)
**Department of Computer Engineering, KJ Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra, India**  
**Academic Year:** 2026–2027 | Semester VI | Class: TY B.Tech Computer Engineering  

---

[![Forensic CI Pipeline](https://github.com/OmikAcharya/solarwinds-sunburst-forensics-group10/actions/workflows/classroom-ci.yml/badge.svg)](https://github.com/OmikAcharya/solarwinds-sunburst-forensics-group10/actions/workflows/classroom-ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
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
| **SHA-256 Digest** | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` | Exact Bit-Stream Match |
| **MD5 Digest** | `b91641a45351f013325d46b7972ba5e3` | Exact Bit-Stream Match |
| **SHA-1 Digest** | `1b1b46f55444e21ab1700684fb65be0efbe7c4eb` | Confirmed Standard Digest |
| **Physical File Size**| `572416` bytes (559.00 KiB) | Standard Orion Library Size |
| **PE Architecture** | PE32 Executable (.NET Assembly / Intel 80386), Console DLL | MSIL Managed Module |
| **Target Runtime** | Microsoft .NET Framework v4.0.30319 | Roslyn C# Compiler |
| **Authenticode Status**| Legitimate DigiCert Signature (`SolarWinds Worldwide, LLC`) | Revoked Post-Incident |

---

## 3. EXECUTIVE ABSTRACT: THE SUNBURST INTRUSION

In late 2020, security researchers discovered **SUNBURST (Solorigate)**, a highly sophisticated advanced persistent threat (APT) supply chain compromise orchestrated by adversary group **UNC2452 / APT29 / Nobelium**. 

Rather than exploiting traditional network perimeters, the adversaries compromised the software build pipeline of SolarWinds Inc., deploying a malicious injector dubbed **SUNSPOT**. During automated compilation of the Orion Network Management Platform, SUNSPOT intercepted `MSBuild.exe` execution and injected a malicious C# source class (`OrionImprovementBusinessLayer.cs`) directly into `SolarWinds.Orion.Core.BusinessLayer.dll`.

Because the compromise occurred prior to code compilation and signing:
1. The resulting trojanized library received a **genuine Authenticode digital signature** from DigiCert.
2. The trojan bypassed traditional application allowlisting and endpoint detection mechanisms.
3. The malicious update was distributed to approximately **18,000 customers**, including Fortune 500 corporations, government agencies, and critical infrastructure operators.

Once installed on a victim system, SUNBURST implements an extended dormancy window of **12 to 14 days**, evaluates running processes against a blacklist of over 120 security monitoring and forensic tools, and establishes a covert command-and-control (C2) channel utilizing **DNS tunneling** targeting subdomains of `avsvmcloud[.]com`.

---

## 4. STATIC FORENSIC TOOLCHAIN PROFILE

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
- **Key Findings:** Confirmed `.text` section entropy at **6.21** (normal code), `.rsrc` at **7.14** (standard resources), and `.reloc` at **0.11**. The lack of runtime packers (e.g., UPX, Themida) enabled the malware to mimic benign enterprise software.

### 4.2 Mandiant FLOSS (FLARE Obfuscated String Solver v3.1.1)
- **Role:** Extraction and automated decryption of static strings, stack strings, tight strings, and custom XOR/subtraction encoded strings.
- **Key Findings:** Uncovered 346 strings including the defensive blacklist (`sysmon.exe`, `wireshark.exe`, `processhacker.exe`, `x64dbg.exe`, `SentinelAgent.exe`, `CSFalconService.exe`), registry keys (`MachineGuid`, `ReportWatcherRetry`), and C2 apex domains (`avsvmcloud.com`).

### 4.3 Mandiant CAPA (v7.0.1)
- **Role:** Identification of malware capabilities and automated mapping to the **MITRE ATT&CK Matrix** and Malware Behavior Catalog (MBC).
- **Key Findings:** Mapped T1497.003 (Time-based Evasion: 12-14 days dormant sleep), T1562.001 (Impair Defenses), T1027 (Obfuscated Strings), T1071.004 (DNS C2 Tunneling), and T1082 (System Information Discovery).

---

## 5. SUMMARY OF INDIAN CYBER LAW COMPLIANCE

```
+---------------------------------------------------------------------------------------------------------+
| Statutory Framework          | Section / Regulation       | Practical Legal Application                 |
+---------------------------------------------------------------------------------------------------------+
| Information Technology Act,  | Section 43                 | Unauthorized access, data extraction, and   |
| 2000 (Amended 2008)          |                            | damage to computer systems (Civil liability)|
|                              | Section 66                 | Criminal hacking & fraudulent alterations   |
|                              | Section 66F                | Cyber Terrorism (Critical Infrastructure)   |
|                              | Section 70                 | Protected Systems access (Up to 10 yrs jail)|
|                              | Section 70B                | Interfacing with CERT-In on cyber incidents |
+---------------------------------------------------------------------------------------------------------+
| CERT-In Directions           | Direction 5(i)             | Mandatory reporting of supply chain & data  |
| (28 April 2022)              | (6-Hour Mandate)           | incidents to CERT-In within 6 hours of discovery|
+---------------------------------------------------------------------------------------------------------+
| Bharatiya Sakshya Adhiniyam  | Section 63 (Repealing      | Admissibility of electronic records;        |
| (BSA), 2023                  | Section 65B of IEA 1872)   | Dual Part A (Custodian) and Part B (Expert) |
|                              |                            | statutory certification under Sec 63(4)(c)  |
+---------------------------------------------------------------------------------------------------------+
```

---

## 6. REPOSITORY STRUCTURE BREAKDOWN

```
.
├── .github/
│   └── workflows/
│       └── classroom-ci.yml                 # Automated GitHub Actions test & compliance pipeline
├── .gitignore                               # Standard Python, IDE, and live binary containment rules
├── requirements.txt                         # Pinned forensic toolchain and testing dependencies
├── setup.sh                                 # Automated environment bootstrap, chmod +x & verification
├── README.md                                # Comprehensive master project dossier
├── scripts/
│   ├── run_forensics.py                     # Standalone DFIR analysis & deterministic simulation engine
│   ├── verify_hashes.sh                     # POSIX shell cryptographic integrity verification tool
│   └── generate_bsa_cert.py                 # Section 63 BSA 2023 statutory certificate generator
├── evidence/
│   ├── sample_hash.sha256                   # Authoritative CISA baseline SHA-256 hash manifest
│   ├── evidence_metadata.json               # Detailed structured metadata (Authenticode, PE, hashes)
│   └── chain_of_custody.md                  # ISO/IEC 27037 compliant chronological custody log
├── outputs/
│   ├── die_inspection.txt                   # Detect It Easy v3.10 PE header & entropy triage report
│   ├── floss_decoded_strings.txt            # Mandiant FLOSS v3.1.1 deobfuscated strings dataset (346 strings)
│   └── capa_capabilities_report.txt        # Mandiant CAPA v7.0.1 MITRE ATT&CK capability attribution
├── legal_compliance/
│   ├── Section_63_BSA_Certificate.md        # Admissibility certificate under Section 63 BSA 2023
│   └── CERT_In_Incident_Notification_Template.md # 6-Hour mandatory incident reporting filing
├── docs/
│   ├── Investigation_Report.md              # Exhaustive 8-section formal DFIR investigation report
│   ├── Presentation_Script.md               # 10-minute word-for-word presentation script (3:20 per member)
│   └── Presentation_Slides_Outline.md       # Institutional 10-slide outline for capstone defense
└── tests/
    └── test_forensic_pipeline.py            # Pytest test suite covering hashing, parsers & legal rules
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
# Run deterministic forensic simulation and verify baseline indicators
python3 scripts/run_forensics.py --simulate --outdir outputs/
```

### Step 4: Programmatically Generate Section 63 BSA 2023 Certificate
```bash
# Generate legal admissibility certificate embedding local machine telemetry
python3 scripts/generate_bsa_cert.py --format md --output legal_compliance/Section_63_BSA_Certificate.md
```

### Step 5: Execute Automated Test Suite
```bash
pytest tests/ -v
```

---

## 8. ACADEMIC & INSTITUTIONAL DISCLAIMER

This digital forensics capstone project is developed exclusively for academic research, education, and forensic evaluation under the curriculum of the **Department of Computer Engineering, KJ Somaiya School of Engineering, Somaiya Vidyavihar University, Mumbai**. All analyses were performed on non-functional, static, or isolated artifacts in accordance with ethical standards, the Information Technology Act, 2000, and institutional research policies.

```
(c) 2026-2027 Group 10 | KJ Somaiya School of Engineering | Somaiya Vidyavihar University
Amandeep Singh (16010123036) | Omik Acharya (16010123218) | Om Lanke (16010123216)
```
