# OPERATION SUNBURST DFIR: PRESENTATION SLIDES OUTLINE
### 12-Slide Somaiya Template Deck Architecture & Side-by-Side Demo Synchronization
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)  
**Institution:** Department of Computer Engineering, K.J. Somaiya School of Engineering  
**University:** Somaiya Vidyavihar University, Mumbai, Maharashtra  
**Academic Year:** 2026–2027 | Class: TY B.Tech COMP | **Group 10**  
**Accompanying PPTX Presentation:** [`docs/SUNBURST_Forensic_Investigation_Group10.pptx`](SUNBURST_Forensic_Investigation_Group10.pptx)  
**Accompanying Word Script:** [`docs/Presentation_Speaking_Script.docx`](Presentation_Speaking_Script.docx)

---

## 1. INVESTIGATORS & FORENSIC ROLES

1. **Amandeep Singh** (Roll No: **16010123036**) — **Lead Forensic Investigator** (PE Header Triage, Supply Chain Infiltration & Cryptographic Verification)
2. **Omik Acharya** (Roll No: **16010123218**) — **Reverse Engineer** (Attack Timeline, String Deobfuscation, FNV-1a Hashing & CAPA Attribution)
3. **Om Lanke** (Roll No: **16010123216**) — **Technical & Cyber Legal Auditor** (Statutory Indian Cyber Law, Section 63 BSA 2023, CI/CD Verification & Q&A)

---

## 2. SLIDE-BY-SLIDE TECHNICAL SPECIFICATION (10-MINUTE SYNCHRONIZATION)

### SLIDE 1: SOMAIYA TITLE SLIDE
- **Header:** Somaiya Vidyavihar University / K.J. Somaiya School of Engineering Logo & Crest
- **Title:** Operation SUNBURST: Digital Forensic Investigation & Incident Response
- **Subtitle:** Supply Chain Infiltration, Static Deobfuscation, Memory Forensics & Indian Statutory Admissibility (BSA 2023 / CERT-In)
- **Roster Table:** Roll Number | Student Name | Forensic Role | Investigation Focus
- **Presentation Model Banner:** Dual Presentation Model (Case Study & Theory on PPT; Live Tools, Terminal Scripts & Interactive Simulation on Side-by-Side Screen).

---

### SLIDE 2: THE SUPPLY CHAIN VECTOR (AMANDEEP SINGH | 0:00 – 1:15)
- **Section:** Incident Background & Threat Context
- **Title:** The Supply Chain Vector: SolarWinds Orion Compromise
- **Case Study Analysis:**
  - Threat Actor: APT29 / Nobelium (Russian SVR).
  - Compromise Point: Injected at MSBuild compilation via in-memory tool `SUNSPOT`.
  - Trojanized Artifact: `SolarWinds.Orion.Core.BusinessLayer.dll` (v2019.4 through v2020.2.1).
  - Reach: 18,000 public and private sector networks worldwide.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Interactive Forensic Simulation (Stage 1)
  - Screen: Web Browser (`open docs/sunburst_simulation.html`)
  - Action: Display "The Attack" animated architecture diagram illustrating build-pipeline compromise.

---

### SLIDE 3: ISO/IEC 27037 EVIDENCE INGESTION (AMANDEEP SINGH | 1:15 – 2:00)
- **Section:** Forensic Methodology & Evidence Integrity
- **Title:** Evidence Ingestion & Dual SHA-256 Hash Verification
- **Forensic Standards:**
  - Adherence to ISO/IEC 27037:2012 principles of digital evidence handling.
  - Primary Sample SHA-256: `325c9b6ac0f441e66183579b2e00b181fc083423b009ac4800f4f05247cf0d25`
  - Benchmark Sample SHA-256: `32519b85c0b422187d7d490004e3ab63314439cda2d0fb812999645017226d7e`
  - Automated hash verification preventing evidence tampering.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Cryptographic Verification Engine
  - Screen: Terminal
  - Action: `bash scripts/verify_hashes.sh`
  - Visual: Green `[PASS]` indicator confirming bitwise integrity against `evidence/sample_hashes.sha256`.

---

### SLIDE 4: STATIC PE ARCHITECTURE & SHANNON ENTROPY (AMANDEEP SINGH | 2:00 – 3:00)
- **Section:** Static PE Triage & Architecture
- **Title:** PE32 Header Inspection & Shannon Entropy Profiling
- **Detect It Easy (DiE v3.10) Metrics:**
  - Format: PE32 DLL for Intel 80386 running .NET CLR v4.0.30319.
  - Compiler: Microsoft Roslyn C# (Visual Studio 2019).
  - Authenticode: Valid digital signature issued by DigiCert Inc to SolarWinds Worldwide, LLC.
  - Section Entropy: `.text` = 6.21, `.rsrc` = 7.14, `.reloc` = 0.11. Overall entropy ~5.9.
  - Stealth Rationale: Stayed strictly below 7.5 packed threshold; evaded heuristic antivirus flags.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Detect It Easy (DiE) Visualizer
  - Screen: Web Browser (Stage 4)
  - Action: Observe live beam scan across PE sections and examine entropy curve staying below 7.5.

---

### SLIDE 5: ATTACK EXECUTION TIMELINE (AMANDEEP SINGH $\rightarrow$ OMIK ACHARYA | 3:00 – 3:45)
- **Section:** Attack Reconstruction & Timeline
- **Title:** Chronological Attack Execution: The 8-Stage Lifecycle
- **8-Stage State Machine Breakdown:**
  1. Process Startup (`SolarWinds.BusinessLayerHost.exe`)
  2. 12 to 14 Day Dormancy (`Thread.Sleep`)
  3. Defense Checks (120+ tools via FNV-1a)
  4. Host Fingerprinting (`MachineGuid`)
  5. DGA Domain Generation
  6. Covert DNS C2 Tunneling (`avsvmcloud.com`)
  7. Payload Drop (TEARDROP / Cobalt Strike)
  8. Interactive C2 Operations & Lateral Movement
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: End-to-End Behavioral Simulation
  - Screen: Terminal & Browser
  - Action: `python3 scripts/run_forensics.py --simulate --simulate-behavior victim`

---

### SLIDE 6: STRING ENCRYPTION & DEOBFUSCATION (OMIK ACHARYA | 3:45 – 4:45)
- **Section:** Static Deobfuscation & Reverse Engineering
- **Title:** String Encryption: Base64 & Raw Deflate Decompression
- **Technical Deobfuscation:**
  - Two-stage scheme: Base64 encoding + raw Deflate decompression (`wbits = -15`, raw stream).
  - `SywrLstNzskvTdFLzs8FAA==` $\rightarrow$ `avsvmcloud.com` (C2 Domain Apex)
  - `C/Z3Cwl3DHKN8c1ML...` $\rightarrow$ `SOFTWARE\Microsoft\Cryptography` (Registry Path)
  - `801MzsjMS3UvzUwBAA==` $\rightarrow$ `MachineGuid` (Victim Identifier)
  - `SyzI1CvOz0ksKs/MSynWS87PBQA=` $\rightarrow$ `api.solarwinds.com` (Connectivity Canary)
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Mandiant FLOSS & String Decompressor
  - Screen: Terminal & Web Browser (Stage 5)
  - Action: Terminal `floss --version` $\rightarrow$ Browser Stage 5: Click live "Decode all" button to unmask C2 tokens.

---

### SLIDE 7: ANTI-ANALYSIS MECHANICS (OMIK ACHARYA | 4:45 – 5:45)
- **Section:** Defense Evasion & Anti-Analysis
- **Title:** Process Blacklist Hashing: 64-Bit FNV-1a & XOR Masking
- **Mathematical Formula:**
  - $\text{Hash} = \text{FNV1a}_{64}(\text{lowercase}(\text{process\_name})) \oplus \text{0x5BAC903BA7D81967}$
  - Offset Basis: `0xcbf29ce484222325` | Prime: `0x100000001b3` | XOR Mask: `6605813339339102567`
  - `wireshark` $\rightarrow$ `0xa84ff6500970f54d` $\rightarrow$ `17574002783607647274` (MATCH)
  - `procmon` $\rightarrow$ `0x46240b85b6a1d8ed` $\rightarrow$ `2128122064571842954` (MATCH)
  - `x64dbg` $\rightarrow$ `0x9f5627c8d228677c` $\rightarrow$ `14193859431895170587` (MATCH)
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Interactive Process Checker
  - Screen: Terminal & Web Browser (Stage 6)
  - Action: Terminal: `python3 scripts/run_forensics.py --check-process wireshark`. Browser: Click "wireshark" $\rightarrow$ "Run the check".

---

### SLIDE 8: CAPABILITY MAPPING & ATTRIBUTION (OMIK ACHARYA | 5:45 – 6:45)
- **Section:** ATT&CK Mapping & Capability Attribution
- **Title:** Behavioral Identification via Mandiant CAPA (v9.4.0)
- **MITRE ATT&CK Matrix Correlation:**
  - `T1497.003`: Time-Based Sandbox Evasion (12 to 14 day delay)
  - `T1071.004`: Application Layer Protocol: DNS C2 Tunneling
  - `T1562.001`: Impair Defenses: Process Blacklist Hashing
  - `T1082`: System Information Discovery (`MachineGuid`)
  - `T1027.002`: Software Packing / Obfuscated Strings
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Mandiant CAPA Execution Engine
  - Screen: Terminal
  - Action: `capa --version && python3 scripts/run_forensics.py --simulate`

---

### SLIDE 9: INDIAN CYBER LEGAL FRAMEWORK (OM LANKE | 6:45 – 7:45)
- **Section:** Statutory Compliance & Cyber Law
- **Title:** Indian Statutory Framework: IT Act 2000 & CERT-In Directives
- **Statutory Mandates:**
  - IT Act, 2000: Sections 43 & 66 (Contaminants & Hacking); Section 66F (Cyber Terrorism — life imprisonment); Section 70 (Protected Systems).
  - CERT-In Directions 2022: Mandatory 6-hour incident reporting window + 180-day ICT log retention.
  - DPDP Act, 2023: Section 8(5)/(6) mandatory breach disclosure.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Indian Law Mapping & CERT-In Generator
  - Screen: Web Browser (Stage 10) & VS Code
  - Action: Browser Stage 10: Click finding buttons $\rightarrow$ VS Code: Open `legal_compliance/CERT_In_Incident_Notification_Template.md`.

---

### SLIDE 10: DIGITAL EVIDENCE ADMISSIBILITY (OM LANKE | 7:45 – 8:45)
- **Section:** Legal Admissibility & Certification
- **Title:** Bharatiya Sakshya Adhiniyam (BSA), 2023: Section 63 Admissibility
- **Section 63 BSA Architecture:**
  - Repeal of IEA 1872 Section 65B; modernization under BSA 2023 Section 63.
  - Sub-section 63(4)(c) Certificate: Dual affirmation structure.
    - Part A: Custodian Affirmation (Signed by Amandeep Singh).
    - Part B: Expert Forensic Affirmation (Signed by Om Lanke & Omik Acharya).
  - Hardware Telemetry: Automatically embeds MAC address, OS kernel, and NTP timestamp.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Automated BSA Section 63 Certificate Generator
  - Screen: Terminal & VS Code
  - Action: `python3 scripts/generate_bsa_cert.py --format both` $\rightarrow$ Display `legal_compliance/Section_63_BSA_Certificate.md`.

---

### SLIDE 11: CI/CD PIPELINE & AUTOMATED VERIFICATION (OM LANKE | 8:45 – 9:15)
- **Section:** CI/CD Automation & Verification
- **Title:** Automated Forensic Pipeline & Regression Test Suite
- **CI/CD Quality Architecture:**
  - GitHub Actions CI (`.github/workflows/classroom-ci.yml`) powered by Astral `uv`.
  - 22 unit test assertions passing in 0.20s across 6 test classes (`tests/test_forensic_pipeline.py`).
  - Verifies cryptographic manifests, Deflate inflation, FNV-1a math, CAPA rules, and BSA certificates.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Automated Test Execution Suite
  - Screen: Terminal
  - Action: `pytest tests/ -v` (Watch 22 tests pass green).

---

### SLIDE 12: FORENSIC VERDICT MATRIX & Q&A (ALL TEAM MEMBERS | 9:15 – 10:00)
- **Section:** Conclusion & Evaluation Matrix
- **Title:** Forensic Findings Resolution & Evaluator Q&A
- **6 Core Capstone Resolutions:**
  1. Authenticity: Legitimate DLL trojanized in build pipeline with valid DigiCert signature.
  2. Strings: 100% decrypted via Base64 + raw Deflate (`wbits=-15`).
  3. Anti-Analysis: 120+ tools checked via FNV-1a + XOR mask, maintaining benign entropy (5.9).
  4. Network C2: Covert DNS DGA tunneling via `avsvmcloud.com`.
  5. Indian Law: Actionable under IT Act Sec 66F, CERT-In 6h rule, and certified under BSA 2023 Sec 63.
  6. Verification: 100% automated regression test coverage via CI/CD.
- **🖥️ Side-by-Side Live Demo Sync:**
  - Target: Final Conclusion & Interactive Q&A
  - Screen: Web Browser (Stage 11: Conclusion)
  - Action: Present 6 green checklist items, thank evaluators, and open floor for Q&A.
