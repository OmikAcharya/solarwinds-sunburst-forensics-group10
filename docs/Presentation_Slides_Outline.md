# PRESENTATION SLIDES OUTLINE (10 SLIDES)
### Forensic Dissection of the SUNBURST Supply Chain Intrusion: Static Triage, Reverse Engineering, and Indian Statutory Admissibility under BSA 2023

**Department of Computer Engineering, KJ Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra**  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Project - 20 Marks)  
**Academic Year:** 2026–2027 | TY B.Tech COMP | Group 10  

---

## SLIDE 1: TITLE & INSTITUTIONAL CREDENTIALS
- **Header:** Somaiya Vidyavihar University / KJ Somaiya School of Engineering (Department of Computer Engineering)
- **Title:** Digital Forensic Investigation of the SolarWinds SUNBURST Supply Chain Intrusion
- **Subtitle:** Static Triage, Advanced Deobfuscation, Behavioral Capability Mapping, and Electronic Evidence Admissibility under Section 63 BSA 2023
- **Presenter:** Group 10
  - **Amandeep Singh** (Roll No: 16010123036) — Lead Investigator (PE Architecture & DiE Triage)
  - **Omik Acharya** (Roll No: 16010123218) — Reverse Engineer (FLOSS Deobfuscation & CAPA Attribution)
  - **Om Lanke** (Roll No: 16010123216) — Cyber Legal Auditor (IT Act, CERT-In, BSA 2023 Compliance)
- **Course & Session:** Digital Forensics & Cyber Security Laboratory (DFCS) | Academic Year 2026–2027
- **Visuals:** Institutional Crest of Somaiya Vidyavihar University, DFCS Laboratory Insignia, Project Metadata Box.

---

## SLIDE 2: CASE OVERVIEW & SUPPLY CHAIN ATTACK VECTOR
- **Speaker:** Amandeep Singh
- **Title:** The Anatomy of a Supply Chain Attack: Threat Actor UNC2452 / APT29
- **Key Concepts & Technical Points:**
  - Traditional vs. Supply Chain Attacks: Bypassing hardened perimeter firewalls by compromising trusted software vendors.
  - The SolarWinds Orion Platform: Centralized network monitoring suite executing with high-privilege domain service accounts.
  - The Infiltration Vector: Adversaries compromised SolarWinds' internal build environment (Bamboo CI/CD), deploying the **SUNSPOT** injection engine.
  - On-The-Fly Trojanization: Injection of malicious C# source (`OrionImprovementBusinessLayer.cs`) during the MSBuild compilation pass without modifying static source control repositories.
  - Downstream Exposure: Approximately 18,000 global commercial, defense, and governmental organizations received the trojanized update package (`v2020.2.1 HF 1`).
- **Visuals:** Flow diagram showing: Threat Actor -> Build Server Compromise -> Automated MSBuild Hook -> Legitimate DigiCert Code-Signing -> Global Client Updates.

---

## SLIDE 3: EVIDENCE ACQUISITION & CRYPTOGRAPHIC CHAIN OF CUSTODY
- **Speaker:** Amandeep Singh
- **Title:** ISO/IEC 27037:2012 Evidence Preservation & Integrity Baseline
- **Key Concepts & Technical Points:**
  - Forensic Item ID: `EVD-2020-SW-001` (`SolarWinds.Orion.Core.BusinessLayer.dll`)
  - Physical & Environmental Safeguards: Air-gapped workstation KJSSE-DFIR-WS01; Tableau T8u USB 3.0 hardware write-blocker; LUKS2 AES-256 encrypted container.
  - Cryptographic Fingerprints (NIST FIPS 180-4):
    - SHA-256: `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
    - MD5: `b91641a45351f013325d46b7972ba5e3`
    - SHA-1: `1b1b46f55444e21ab1700684fb65be0efbe7c4eb`
    - File Size: `572416` bytes (559.00 KiB)
  - Zero Hash Drift: Checksums re-verified before triage, post-disassembly, and at court preservation.
- **Visuals:** Evidence custody chronology timeline (Vault -> Amandeep -> Omik -> Om Lanke -> Secure Archival) with green checkmark verification badges.

---

## SLIDE 4: PE ARCHITECTURE & DETECT IT EASY (DiE) TRIAGE
- **Speaker:** Amandeep Singh
- **Title:** Deep PE32 Inspection: Header Analysis & Entropy Profiling
- **Key Concepts & Technical Points:**
  - PE Format: PE32 console DLL compiled for Intel 80386 (Machine ID: `0x014c`).
  - .NET CLR Environment: Runtime `v4.0.30319`, flag `COMIMAGE_FLAGS_ILONLY` (Managed MSIL assembly).
  - Compiler Identity: Microsoft Roslyn C# Compiler (Visual Studio 2019 / MSVC 14.0).
  - Section-by-Section Entropy Analysis:
    - `.text`: 6.21 (Unpacked standard executable code)
    - `.rsrc`: 7.14 (High entropy due to compressed manifests and localized resources)
    - `.reloc`: 0.11 (Minimal relocation records)
  - The Evasion Strategy: Absence of packers (UPX/Themida). Attackers maintained benign entropy to bypass heuristic AV scanners.
  - Authenticode Digital Signature: Valid certificate issued by DigiCert to `SolarWinds Worldwide, LLC` (Serial: `0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e`).
- **Visuals:** DiE v3.10 CLI output snippet alongside an entropy bar chart comparing benign vs. packed software.

---

## SLIDE 5: STATIC STRING DEOBFUSCATION WITH MANDIANT FLOSS
- **Speaker:** Omik Acharya
- **Title:** Cracking Backdoor Cryptography: 346 Deobfuscated Strings
- **Key Concepts & Technical Points:**
  - Obfuscation Routine: Custom byte subtraction, bitwise XOR, and Deflate decompression inside `OrionImprovementBusinessLayer.Zip`.
  - Automated Extraction: Mandiant FLOSS v3.1.1 parsed static, stack, and dynamically decoded strings.
  - The 120+ Process Blacklist: Malware computes 64-bit FNV-1a hashes of running processes:
    - Forensics/Debuggers: `sysmon.exe`, `wireshark.exe`, `processhacker.exe`, `x64dbg.exe`, `windbg.exe`, `ghidra.exe`.
    - EDR / AV Agents: `SentinelAgent.exe`, `CSFalconService.exe`, `taniumclient.exe`, `CylanceSvc.exe`.
  - Target Registry Paths: `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid` (system fingerprinting) and `ReportWatcherRetry` (backdoor status flag).
  - Command & Control Tokens: Apex domain `avsvmcloud.com` and regional multi-cloud DGA domains.
- **Visuals:** Terminal window showing FLOSS extraction output, categorized by Blacklisted Processes, Registry Paths, and C2 URLs.

---

## SLIDE 6: BEHAVIORAL ATTRIBUTION WITH MANDIANT CAPA
- **Speaker:** Omik Acharya
- **Title:** Automated Malware Capability Attribution & Execution Logic
- **Key Concepts & Technical Points:**
  - Tool Rationale: Mandiant CAPA v7.0.1 detects malicious capabilities using semantic YAML rules without runtime execution.
  - Flagship Capability 1: Time-Based Sandbox Evasion (T1497.003)
    - Hardcoded `Thread.Sleep` dormant window of 288 hours (**12 full days**), with random jitter up to **14 days**.
    - Purpose: Exhaust automated malware analysis sandboxes which timeout in 5–10 minutes.
  - Flagship Capability 2: DNS Tunneling C2 (T1071.004)
    - DGA generates subdomains structured as: `<encoded_guid>.<encoded_domain>.appsync-api.eu-west-1.avsvmcloud.com`.
    - Low-and-slow DNS requests evade standard web proxies and egress packet inspections.
  - Flagship Capability 3: Defensive Process Termination (T1562.001)
    - Disables logging and aborts C2 beaconing if forensic or security monitoring processes are active.
- **Visuals:** CAPA capability tree breakdown highlighting `delay execution`, `check for security software`, and `resolve dynamic C2 domain`.

---

## SLIDE 7: MITRE ATT&CK ENTERPRISE MATRIX MAPPING
- **Speaker:** Omik Acharya
- **Title:** Comprehensive Threat Actor TTP Matrix (UNC2452 / APT29)
- **Key Concepts & Technical Points:**
  - Initial Access: T1195.002 (Supply Chain Compromise)
  - Execution: T1059 / T1129 (Shared Modules via `SolarWinds.BusinessLayerHost.exe`)
  - Persistence: T1574.002 (DLL Side-Loading / Trojanized Component)
  - Defense Evasion: T1497.003 (Time-based Evasion), T1562.001 (Impair Defenses), T1027 (Obfuscated Strings), T1553.002 (Subvert Code Signing)
  - Discovery: T1082 (System Information Discovery), T1057 (Process Discovery), T1016 (Network Configuration)
  - Command & Control: T1071.004 (DNS Protocol), T1568.002 (Domain Generation Algorithms)
- **Visuals:** Color-coded MITRE ATT&CK Matrix grid showing tactics across the top and highlighted technical IDs mapped to evidence artifacts.

---

## SLIDE 8: INDIAN CYBER LAW COMPLIANCE & CERT-In MANDATES
- **Speaker:** Om Lanke
- **Title:** Statutory Violations: Information Technology Act, 2000 & CERT-In Directions 2022
- **Key Concepts & Technical Points:**
  - IT Act Section 43: Unauthorized access, data extraction, and contamination of computer systems (Civil damages).
  - IT Act Section 66: Dishonest and fraudulent hacking (Imprisonment up to 3 years / fine up to 5 lakh rupees).
  - IT Act Section 66F: **Cyber Terrorism** (Attacks targeting critical infrastructure, essential services, or national sovereignty; **Statutory Penalty: Imprisonment for Life**).
  - IT Act Section 70: Tampering with declared Protected Systems (Imprisonment up to 10 years).
  - CERT-In Directions 2022 (Section 70B): Mandatory reporting of supply chain compromises and data security incidents within **6 hours** of detection.
  - Group 10 Compliance: Official CERT-In Incident Notification submitted in 5 hours 45 minutes.
- **Visuals:** Legal summary table comparing IT Act sections, offenses, statutory penalties, and forensic mappings; CERT-In 6-hour timeline countdown clock.

---

## SLIDE 9: ADMISSIBILITY OF ELECTRONIC EVIDENCE: SECTION 63 BSA 2023
- **Speaker:** Om Lanke
- **Title:** Transition from Section 65B (IEA 1872) to Section 63 BSA 2023
- **Key Concepts & Technical Points:**
  - Repeal of Indian Evidence Act, 1872 by the Bharatiya Sakshya Adhiniyam, 2023 (Act No. 47 of 2023).
  - Mandatory Conditions under Section 63(2):
    1. Regular lawful custody and processing of electronic records.
    2. Data fed into system in the ordinary course of business.
    3. Proper operational status of computer without memory or storage distortion.
    4. Exact reproduction of the digital output from original bitstream image.
  - Dual-Signatory Certification Framework under Section 63(4):
    - **Part A (Custodian Affirmation):** Executed by Amandeep Singh (Workstation hardware serial, MAC address, write-block integrity).
    - **Part B (Forensic Expert Certificate):** Executed by Omik Acharya & Om Lanke (FIPS 180-4 hash matching, tool validation, non-tampering).
  - Automated Generation: Demonstrated via Python script `generate_bsa_cert.py`.
- **Visuals:** Architectural side-by-side comparison of Section 65B IEA vs. Section 63 BSA, displaying the executed Part A and Part B certificate stamps.

---

## SLIDE 10: ENTERPRISE REMEDIATION ARCHITECTURE & CONCLUSION
- **Speaker:** Om Lanke
- **Title:** Three-Tiered Supply Chain Defense Architecture & Final Takeaways
- **Key Concepts & Technical Points:**
  - Tier 1: Hermetic Build Pipelines (SLSA Level 4) & In-toto Cryptographic Attestations.
  - Tier 2: FIPS 140-2 Level 3 Hardware Security Modules (HSM) for Code Signing with Two-Person Quorum Approvals.
  - Tier 3: Zero Trust Network Egress & Protective DNS (DNS Response Policy Zones blocking newly registered/DGA domains).
  - Investigation Summary: Complete static triage executed, 346 strings deobfuscated, 14 ATT&CK techniques classified, and electronic evidence fully certified under Indian law.
  - Academic Evaluator Acknowledgments & Capstone Sign-off.
- **Visuals:** Three-tiered defense pyramid diagram; Group 10 final sign-off banner; Open for Q&A prompt.
