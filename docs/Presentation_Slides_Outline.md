# PRESENTATION SLIDES OUTLINE (10 SLIDES)
### Forensic Dissection of the SUNBURST Supply Chain Intrusion: Static Triage, Reverse Engineering, and Indian Statutory Admissibility under BSA 2023

**Department of Computer Engineering, KJ Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra**  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Project - 20 Marks)  
**Academic Year:** 2026–2027 | TY B.Tech COMP | Group 10  
**Interactive Simulation Model:** [`docs/sunburst_simulation.html`](sunburst_simulation.html)

---

## SLIDE 1: TITLE & INSTITUTIONAL CREDENTIALS
- **Header:** Somaiya Vidyavihar University / KJ Somaiya School of Engineering (Department of Computer Engineering)
- **Title:** Digital Forensic Investigation of the SolarWinds SUNBURST Supply Chain Intrusion
- **Subtitle:** Static Triage, Advanced Deobfuscation, Behavioral Capability Mapping, and Electronic Evidence Admissibility under Section 63 BSA 2023
- **Presenter:** Group 10
  - **Amandeep Singh** (Roll No: 16010123036) — Lead Investigator (PE Architecture & DiE Triage)
  - **Omik Acharya** (Roll No: 16010123218) — Reverse Engineer (FLOSS Deobfuscation & CAPA Attribution)
  - **Om Lanke** (Roll No: 16010123216) — Cyber Legal Auditor (IT Act, CERT-In, BSA 2023, DPDP 2023, BNSS 2023)
- **Course & Session:** Digital Forensics & Cyber Security Laboratory (DFCS) | Academic Year 2026–2027
- **Visuals:** Institutional Crest of Somaiya Vidyavihar University, DFCS Laboratory Insignia, Project Metadata Box.

---

## SLIDE 2: CASE OVERVIEW, 15-MONTH CHRONOLOGY & ATTACK VECTOR
- **Speaker:** Amandeep Singh
- **Title:** The Anatomy of a Supply Chain Attack: Threat Actor UNC2452 / APT29
- **Key Concepts & Technical Points:**
  - The SolarWinds Orion Platform: Centralized enterprise network monitoring software executing with elevated SYSTEM privileges.
  - The 15-Month Chronology:
    - *Sep 2019:* Initial network intrusion by adversaries.
    - *Oct 2019:* Harmless POC test code injected into build system.
    - *Feb 2020:* SUNBURST injected into production builds via the memory-only SUNSPOT dropper.
    - *Mar–Jun 2020:* Trojanized update (`v2020.2.1 HF 1`) distributed to 18,000 organizations.
    - *Dec 2020:* FireEye breach disclosure; CISA Emergency Directive 21-01 issued.
  - The Targeting Funnel: 18,000 organizations ingested the backdoor; ~100 high-value targets selected for stage-2 interactive operations.
  - Software Supply Chain Compromise (MITRE ATT&CK T1195.002): Source-swapping at build time allowed the trojan to receive a genuine corporate digital signature.
- **Visuals:** Timeline slider showing 15-month progression; supply chain animation flow diagram from build server to signed update to victim organizations.

---

## SLIDE 3: EVIDENCE ACQUISITION & CRYPTOGRAPHIC CHAIN OF CUSTODY
- **Speaker:** Amandeep Singh
- **Title:** ISO/IEC 27037:2012 & BNSS 2023 Evidence Preservation
- **Key Concepts & Technical Points:**
  - Forensic Item ID: `EVD-2020-SW-001` (`SolarWinds.Orion.Core.BusinessLayer.dll`)
  - Physical & Environmental Controls: Air-gapped workstation KJSSE-DFIR-WS01; Tableau T8u USB 3.0 hardware write-blocker; LUKS2 AES-256 encrypted container.
  - Cryptographic Fingerprints (NIST FIPS 180-4):
    - SHA-256 (Primary): `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
    - SHA-256 (Secondary): `32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77`
    - MD5: `b91641a45351f013325d46b7972ba5e3`
    - File Size: `572416` bytes (559.00 KiB)
  - Zero Hash Discrepancy: SHA-256 before triage (`hb`) identical to SHA-256 post-triage (`ha`) (64/64 hex characters match).
- **Visuals:** Hash matching terminal meter; chronological chain-of-custody transfer log from vault to workstation checkout.

---

## SLIDE 4: PE ARCHITECTURE & DETECT IT EASY (DiE) TRIAGE
- **Speaker:** Amandeep Singh
- **Title:** Header Inspection, Entropy Profiling & Signature Verification
- **Key Concepts & Technical Points:**
  - PE Format: PE32 console DLL compiled for Intel 80386 (Machine ID: `0x014c`).
  - .NET CLR Environment: Runtime `v4.0.30319`, flag `COMIMAGE_FLAGS_ILONLY` (Managed MSIL assembly).
  - Compiler Identity: Microsoft Roslyn C# Compiler (Visual Studio 2019 / MSVC 14.0).
  - Section-by-Section Entropy Analysis:
    - `.text`: 6.21 (Unpacked standard executable code)
    - `.rsrc`: 7.14 (High entropy due to compressed manifests and localized resources)
    - `.reloc`: 0.11 (Minimal relocation records)
  - Absence of Packers: Entropy curve remains strictly below the 7.5 packed threshold, ensuring the binary mimics benign software.
  - Authenticode Digital Signature: Valid certificate issued by DigiCert to `SolarWinds Worldwide, LLC` (Serial: `0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e`).
- **Visuals:** DiE v3.10 interface snippet alongside the file section map and entropy curve.

---

## SLIDE 5: DEOBFUSCATING PROTECTED STRINGS WITH FLOSS & RAW DEFLATE
- **Speaker:** Omik Acharya
- **Title:** Cracking Backdoor Cryptography: 2,146 Strings & Raw Deflate Decompression
- **Key Concepts & Technical Points:**
  - FLOSS Analysis: Extracted 2,146 static strings; flagged suspicious classes: `OrionImprovementBusinessLayer`, `ZipHelper`, `DeflateStream`.
  - Cryptographic Obfuscation Scheme: Raw Deflate compression followed by Base64 encoding.
  - Decompressed Core Indicators:
    - `SywrLstNzskvTdFLzs8FAA==` $\rightarrow$ **`avsvmcloud.com`** (C2 Domain Apex)
    - `C/Z3Cwl3...` $\rightarrow$ **`SOFTWARE\Microsoft\Cryptography`** (Registry Key)
    - `801MzsjMS3UvzUwBAA==` $\rightarrow$ **`MachineGuid`** (Victim Fingerprint)
    - `C07NSU0...` $\rightarrow$ **`Select * From Win32_NetworkAdapterConfiguration`** (WMI Query)
    - `SyzI1Cv...` $\rightarrow$ **`api.solarwinds.com`** (Connectivity Canary)
- **Visuals:** Two-column table mapping Base64 ciphertext payloads to decompressed plaintext configuration parameters.

---

## SLIDE 6: THE HIDDEN DEFENSE EVASION BLOCKLIST: FNV-1a 64-BIT + XOR
- **Speaker:** Omik Acharya
- **Title:** Process Hashing Evasion: Eliminating Plaintext Strings
- **Key Concepts & Technical Points:**
  - Evasion Rationale: Plaintext process strings trigger AV/EDR detection; SUNBURST embedded zero plaintext tool names.
  - The Hashing Pipeline:
    $$\text{Hash} = \text{FNV1a}_{64}(\text{lowercase}(\text{process\_name})) \oplus \text{0x5BAC903BA7D81967}$$
  - Offset Basis: `0xcbf29ce484222325` | Prime: `0x100000001b3` | XOR Key: `0x5BAC903BA7D81967` (6605813339339102567).
  - Target Examples:
    - `wireshark` $\rightarrow$ FNV: `0xa84ff6500970f54d` $\rightarrow$ XOR: `17574002783607647274`
    - `procmon` $\rightarrow$ FNV: `0x46240b85b6a1d8ed` $\rightarrow$ XOR: `2128122064571842954`
    - `x64dbg` $\rightarrow$ FNV: `0x9f5627c8d228677c` $\rightarrow$ XOR: `14193859431895170587`
  - Operational Result: Over 120 analysis and security tools matched; if found, the backdoor permanently mutes itself.
- **Visuals:** Interactive hashing pipeline box diagram showing string $\rightarrow$ lowercase $\rightarrow$ FNV-1a $\rightarrow$ XOR key $\rightarrow$ blacklist match.

---

## SLIDE 7: CAPABILITY ATTRIBUTION WITH CAPA & THE 8-STEP DECISION GATE
- **Speaker:** Omik Acharya
- **Title:** MITRE ATT&CK Mapping & Environmental Flow Simulation
- **Key Concepts & Technical Points:**
  - Flagship CAPA Capabilities:
    - T1497.003: Time-Based Sandbox Evasion (12 to 14 days `Thread.Sleep` delay).
    - T1071.004: Application Layer Protocol: DNS Tunneling via `avsvmcloud.com`.
    - T1562.001: Impair Defenses (Process enumeration and termination).
  - The 8-Step Reconstructed Decision Gate:
    1. Loaded by Orion? | 2. Wait 12–14 days | 3. Real corporate domain? | 4. Security tools running? | 5. Internet reachable? | 6. Beacon over DNS | 7. Selected by attackers? | 8. HTTP command channel.
  - Environmental Outcomes:
    - Analyst VM: Aborts at Step 4 (Wireshark detected).
    - Offline Machine: Aborts at Step 5 (No internet).
    - Victim Orion Server: Passes all 8 steps $\rightarrow$ persistent command channel.
- **Visuals:** Vertical flow diagram of the 8 decision steps with pass/fail branch icons; CAPA MITRE ATT&CK capability matrix.

---

## SLIDE 8: INDIAN CYBER LAW COMPLIANCE & CERT-In MANDATES
- **Speaker:** Om Lanke
- **Title:** Statutory Violations: IT Act 2000, CERT-In Directions 2022 & DPDP Act 2023
- **Key Concepts & Technical Points:**
  - IT Act Section 43: Introducing computer contaminants, data extraction (Civil compensation).
  - IT Act Section 66: Dishonest and fraudulent hacking (Imprisonment up to 3 years).
  - IT Act Section 66F: **Cyber Terrorism** (Targeting critical infrastructure or sovereignty; **Statutory Penalty: Imprisonment for Life**).
  - IT Act Section 70: Tampering with protected critical systems (Up to 10 years imprisonment).
  - IT Act Section 43A & 2011 Rules: Duty of corporate entities to maintain reasonable security against vendor supply chain risks.
  - CERT-In Directions 2022 (Section 70B): Mandatory reporting of supply chain compromises within **6 hours**; log retention for **180 days**.
  - DPDP Act 2023: Mandatory breach notification to the Data Protection Board of India.
- **Visuals:** Legal mapping matrix linking technical malware findings to Indian statutory sections and criminal/civil liabilities.

---

## SLIDE 9: ADMISSIBILITY OF ELECTRONIC EVIDENCE: SECTION 63 BSA 2023 & BNSS 2023
- **Speaker:** Om Lanke
- **Title:** Procedural Transition: Section 65B (IEA 1872) to Section 63 (BSA 2023)
- **Key Concepts & Technical Points:**
  - Repeal of Indian Evidence Act, 1872 by the Bharatiya Sakshya Adhiniyam, 2023 (Act No. 47 of 2023).
  - Mandatory Conditions under Section 63(2): Regular custody, normal feeding of records, proper operational status without distortion, exact reproduction.
  - Dual-Signatory Certification under Section 63(4) BSA 2023 & Section 105 BNSS 2023:
    - **Part A (Custodian Affirmation):** Executed by Amandeep Singh (Workstation hardware telemetry, MAC address, write-block verification).
    - **Part B (Forensic Expert Technical Certificate):** Executed by Omik Acharya & Om Lanke (NIST FIPS 180-4 hash matching, tool validation, non-tampering).
  - Admissibility: Deemed primary electronic evidence admissible in court without original physical server hardware.
- **Visuals:** Architectural comparison graphic of Section 65B vs. Section 63; certificate layout showing Part A and Part B seals.

---

## SLIDE 10: THREE-TIERED REMEDIATION & THE SIX INQUIRIES
- **Speaker:** Om Lanke
- **Title:** Enterprise Defense Architecture & Concluding Findings
- **Key Concepts & Technical Points:**
  - Answers to the Six Core Forensic Inquiries:
    1. *What kind of file?* Signed, unpacked .NET DLL posing as legitimate Orion component.
    2. *What is it hiding?* C2 apex `avsvmcloud.com` and registry paths in Deflate+Base64.
    3. *What can it do?* Host profiling, process enumeration, DNS/HTTP C2 tunneling.
    4. *How does it evade detection?* Code signing, 12-14d delay, FNV-1a hashed blacklist.
    5. *Was evidence preserved?* Yes. 64/64 SHA-256 characters matched identically.
    6. *Which laws apply?* IT Act Sec 43/66/66F/70; CERT-In 2022; DPDP 2023; BSA 2023 Sec 63.
  - Three-Tiered Defense Model:
    - *Tier 1:* Hermetic Build Environments (SLSA Level 4) & In-toto Attestations.
    - *Tier 2:* FIPS 140-2 Level 3 HSM Code Signing with Two-Person Quorum Verification.
    - *Tier 3:* Zero Trust Network Egress & DNS Response Policy Zones (RPZ).
  - Interactive Simulation: Accessible locally at [`docs/sunburst_simulation.html`](sunburst_simulation.html).
  - Capstone Defense Sign-off & Open for Q&A.
- **Visuals:** Three-tiered defense pyramid; Group 10 closing sign-off banner; link to interactive simulation.
