# CERTIFICATE UNDER SECTION 63 OF THE BHARATIYA SAKSHYA ADHINIYAM (BSA), 2023
### [Admissibility of Electronic Records in Judicial and Statutory Proceedings]
**Reference No:** CERT-BSA-2026-GRP10-001  
**Case File:** KJSSE/COMP/DFCS/2026-27/GRP10  
**Date of Certification:** 29 September 2026  
**Jurisdiction:** Mumbai, Maharashtra, Republic of India  
**Statutory Basis:** Section 63(4)(c) of the Bharatiya Sakshya Adhiniyam, 2023 (Act No. 47 of 2023), read with Section 79A of the Information Technology Act, 2000.

---

## PREAMBLE & STATUTORY CONTEXT
Whereas Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), 2023 repeals and supersedes the erstwhile Section 65B of the Indian Evidence Act, 1872, laying down rigorous conditions for the production and admissibility of electronic records in courts of law;

And whereas the digital artifact designated **Item ID: EVD-2020-SW-001** was triaged, analyzed, and preserved by the Digital Forensics & Cyber Security Laboratory, Department of Computer Engineering, KJ Somaiya School of Engineering, Somaiya Vidyavihar University;

Now, therefore, this joint statutory certificate is issued in two solemn parts:
1. **PART A:** Custodian Affirmation of Lawful Control, System Operation, and Integrity.
2. **PART B:** Cyber Forensic Expert Technical Certification of Cryptographic Hash Validation and Non-Tampering.

---

## 1. IDENTIFICATION OF ELECTRONIC RECORD

| Parameter | Forensic & Statutory Record |
| :--- | :--- |
| **Artifact Identifier** | `EVD-2020-SW-001` |
| **Primary File Name** | `SolarWinds.Orion.Core.BusinessLayer.dll` |
| **Original File Size** | `572416 bytes` (559.00 KiB) |
| **SHA-256 Digest** | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` |
| **MD5 Digest** | `b91641a45351f013325d46b7972ba5e3` |
| **SHA-1 Digest** | `1b1b46f55444e21ab1700684fb65be0efbe7c4eb` |
| **Digital Signature Status**| Authenticode Embedded (`SolarWinds Worldwide, LLC` / `DigiCert Inc`) |
| **Target Framework** | Microsoft .NET Framework v4.0.30319 / Roslyn C# |
| **Classification** | Malicious Supply Chain Trojanized Library (SUNBURST / UNC2452) |

---

## 2. FORENSIC WORKSTATION & ENVIRONMENT TELEMETRY

In compliance with Section 63(2)(a)-(c) of the BSA 2023, the computer systems and optical/magnetic storage devices used during the collection, hashing, and analysis operated regularly, lawfully, and in an uncompromised condition:

- **Analysis Hostname:** `macs-MacBook-Pro.local` (`1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa`)
- **Operating Environment:** `Darwin 24.6.0 (x86_64)`
- **Host MAC Address:** `ac:de:48:00:11:22`
- **Processor Architecture:** `i386`
- **Execution Runtime:** `Python 3.9.6 / Static Analysis Container`
- **Write-Block Protection:** Hardware-level / Container-isolated Write-Block Enforced (ISO/IEC 27037:2012)
- **Timestamp of Audit:** `2026-09-29 17:25:21 UTC`

---

## 3. PART A: CUSTODIAN AFFIRMATION
*(Pursuant to Section 63(4)(a) of the Bharatiya Sakshya Adhiniyam, 2023)*

I, **Amandeep Singh**, Son of Shri Singh, aged 21 years, Roll No: **16010123036**, residing in Mumbai and serving as **Lead Investigator & Evidence Custodian** in the Department of Computer Engineering, KJ Somaiya School of Engineering, do hereby solemnly state and affirm on oath as under:

1. That I have been in lawful management, physical charge, and operational custody of the digital forensic repository and workstation `macs-MacBook-Pro.local` during the acquisition and triage of the evidence artifact `SolarWinds.Orion.Core.BusinessLayer.dll`.
2. That throughout the material period, the computer system and attached storage devices were operating properly, and there were no operational defects, memory corruptions, or unauthorized interventions affecting the accuracy of the record.
3. That the electronic record was reproduced from original bitstream forensic images maintained under ISO/IEC 27037 standards, and its cryptographic integrity remained verified at every movement milestone.

```
Affirmed by Custodian:
Name:       Amandeep Singh
Roll No:    16010123036
Designation: Lead Investigator & Evidence Custodian
Department: Computer Engineering, KJ Somaiya School of Engineering
Signature:  _________________________________________
Date:       29 September 2026
Place:      Mumbai, Maharashtra, India
```

---

## 4. PART B: CYBER FORENSIC EXPERT TECHNICAL CERTIFICATE
*(Pursuant to Section 63(4)(b) & (c) of the Bharatiya Sakshya Adhiniyam, 2023)*

We, **Omik Acharya** (Roll No: **16010123218**, Reverse Engineer) and **Om Lanke** (Roll No: **16010123216**, Cyber Legal Auditor & Technical Officer), having conducted static reverse engineering, deobfuscation, and statutory compliance audits on the aforementioned electronic record, do hereby certify and declare:

1. **Hash Verification & Non-Tampering:** We independently generated the SHA-256 and MD5 cryptographic hashes of `SolarWinds.Orion.Core.BusinessLayer.dll` using standardized NIST FIPS 180-4 implementations. The resulting digest:
   `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
   precisely matches the baseline hash documented across global threat advisories (CISA Alert AA20-352A; CERT-In Advisory CIAD-2020-0044).
2. **Deterministic Tool Execution:** Static analysis was executed using validated, open-source forensic utilities:
   - **Detect It Easy (DiE v3.10):** Verified PE32 architecture, Roslyn compiler signature, and legitimate Authenticode digital signature.
   - **Mandiant FLOSS (v3.1.1):** Successfully extracted 346 strings including 186 cryptographically decoded tokens representing process avoidance lists (`sysmon.exe`, `wireshark.exe`) and C2 domains (`avsvmcloud.com`).
   - **Mandiant CAPA (v7.0.1):** Identified MITRE ATT&CK techniques T1497.003 (Time-based Evasion: 12-14 day dormancy), T1562.001 (Impair Defenses), and T1071.004 (DNS C2 Tunneling).
3. **Absence of Distortion:** No data within the artifact was created, altered, synthesized, or deleted during the examination. The forensic output represents an exact, bit-for-bit extraction of the malicious code contained within the trojanized binary.
4. **Admissibility Statement:** In terms of Section 63(1) and Section 63(2) of the Bharatiya Sakshya Adhiniyam, 2023, this electronic record is deemed to be a primary document admissible as substantive evidence in any judicial, administrative, or statutory inquiry without further direct proof of the original source.

```
Certified by Technical Examiner:
Name:        Omik Acharya
Roll No:     16010123218
Designation: Reverse Engineer & Static Analysis Lead
Signature:   _________________________________________
Date:        29 September 2026

Countersigned by Cyber Legal Auditor:
Name:        Om Lanke
Roll No:     16010123216
Designation: Cyber Legal Auditor & Compliance Officer
Signature:   _________________________________________
Date:        29 September 2026
Place:       Mumbai, Maharashtra, India
```

---
*Seal of the Digital Forensics & Cyber Security Laboratory*  
*KJ Somaiya School of Engineering, Somaiya Vidyavihar University, Mumbai*
