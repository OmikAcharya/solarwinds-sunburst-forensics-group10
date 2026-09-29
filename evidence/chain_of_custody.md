# ISO/IEC 27037:2012 Digital Evidence Chain of Custody Log

## Institutional Header
- **Institution:** Department of Computer Engineering, KJ Somaiya School of Engineering
- **University:** Somaiya Vidyavihar University, Vidyavihar, Mumbai, Maharashtra 400077
- **Laboratory:** Digital Forensics & Cyber Security Laboratory (Room 402)
- **Academic Year:** 2026–2027 | Semester VI | Capstone Activity (20 Marks)
- **Investigation Group:** Group 10
- **Case Reference:** `KJSSE/COMP/DFCS/2026-27/GRP10`

---

## 1. Evidence Item Identification

| Field | Record Specification |
| :--- | :--- |
| **Evidence Item ID** | `EVD-2020-SW-001` |
| **Artifact Description** | Trojanized Windows Dynamic Link Library (`SolarWinds.Orion.Core.BusinessLayer.dll`) |
| **Source Entity** | Orion Network Management Platform Software Update Archive (`v2020.2.1 HF 1`) |
| **Acquisition Date / Time** | 2026-09-29 08:30:00 UTC |
| **Acquisition Location** | Forensic Isolation Lab (Air-Gapped Workstation KJSSE-DFIR-WS01) |
| **Hardware Write-Blocker** | Tableau T8u Forensic USB 3.0 Bridge (Hardware Write-Block Active) |
| **Container Format** | Expert Witness Format / Raw Read-Only Bitstream Image |
| **Calculated Size** | `572416` bytes (559 KB) |
| **Ingress MD5 Digest** | `b91641a45351f013325d46b7972ba5e3` |
| **Ingress SHA-256 Digest** | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` |

---

## 2. Chain of Custody Chronological Log

| Log ID | Date & Time (UTC) | Released By | Received By | Purpose of Custody Transfer | Location / Workstation | Integrity Hash Verified (SHA-256) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **COC-01** | 2026-09-29 08:30:00 | Lab Supervisor / Evidence Vault | **Amandeep Singh** (Roll: 16010123036) | Secure evidence checkout and initial write-blocked bitstream imaging. | Vault -> Station KJSSE-DFIR-WS01 | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (MATCH) |
| **COC-02** | 2026-09-29 09:15:00 | **Amandeep Singh** (Roll: 16010123036) | **Amandeep Singh** (Roll: 16010123036) | PE header inspection, digital signature triage, and section entropy calculation via Detect It Easy (DiE v3.10). | Forensic Station KJSSE-DFIR-WS01 | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (MATCH) |
| **COC-03** | 2026-09-29 11:00:00 | **Amandeep Singh** (Roll: 16010123036) | **Omik Acharya** (Roll: 16010123218) | Transfer of read-only forensic duplicate for static string deobfuscation (Mandiant FLOSS v3.1.1) and behavioral analysis (Mandiant CAPA v7.0.1). | Station KJSSE-DFIR-WS01 -> WS02 | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (MATCH) |
| **COC-04** | 2026-09-29 13:45:00 | **Omik Acharya** (Roll: 16010123218) | **Om Lanke** (Roll: 16010123216) | Legal audit, CERT-In advisory correlation, and Section 63 BSA 2023 evidence admissibility documentation. | Station KJSSE-DFIR-WS02 -> WS03 | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (MATCH) |
| **COC-05** | 2026-09-29 16:30:00 | **Om Lanke** (Roll: 16010123216) | Lab Vault / Master Repository | Verification of hash consistency and check-in to secure encrypted archival storage. | Station KJSSE-DFIR-WS03 -> Vault | `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (MATCH) |

---

## 3. Storage and Environmental Controls
- **Physical Security:** Air-gapped forensic workstation in card-access secured room with CCTV surveillance.
- **Logical Security:** Read-only mount flag (`ro,noexec,nosuid`). Live binary quarantined under simulated memory container.
- **Cryptographic Guard:** Cryptographic checksums generated before and after every read operation using SHA-256 and MD5.

---

## 4. Custodian Attestation & Signatures

We, the undersigned investigators from Group 10, hereby solemnly affirm under penalties of perjury and academic integrity regulations that:
1. The digital evidence designated `EVD-2020-SW-001` was maintained in strict custody without alteration, modification, or exposure to unmonitored systems.
2. The integrity hashes (SHA-256: `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`) remained constant across all forensic procedures.
3. All analytical procedures conform with ISO/IEC 27037 and Section 63 of Bharatiya Sakshya Adhiniyam, 2023.

```
Investigator 1 (Lead Investigator):
Amandeep Singh (Roll No: 16010123036)
Signature: _______________________ Date: 2026-09-29

Investigator 2 (Reverse Engineer):
Omik Acharya (Roll No: 16010123218)
Signature: _______________________ Date: 2026-09-29

Investigator 3 (Cyber Legal Auditor):
Om Lanke (Roll No: 16010123216)
Signature: _______________________ Date: 2026-09-29
```
