# SUNBURST DFIR CAPSTONE: TOOL EXECUTION & DEMO MANUAL
### Step-by-Step Technical Runbook, Command Reference, and Screen Choreography
**Department of Computer Engineering, K.J. Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra**  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)  
**Academic Year:** 2026–2027 | Class: TY B.Tech COMP | **Group 10**  
**Accompanying Word Document:** [`docs/Tool_Execution_and_Demo_Manual.docx`](Tool_Execution_and_Demo_Manual.docx)  
**Accompanying PowerPoint Deck:** [`docs/SUNBURST_Forensic_Investigation_Group10.pptx`](SUNBURST_Forensic_Investigation_Group10.pptx)

---

## 1. PRE-DEMO ENVIRONMENT CHECKLIST (2 MINUTES BEFORE RECORDING)

Before hitting record on your screen or presenting live to evaluators, arrange these 4 application windows across your desktop spaces:

### Window 1: PowerPoint Presentation
- Open [`docs/SUNBURST_Forensic_Investigation_Group10.pptx`](SUNBURST_Forensic_Investigation_Group10.pptx) in Slide Show mode (Slide 1 ready).
- Ensure 16:9 widescreen display fills the screen.

### Window 2: Web Browser (Google Chrome / Safari)
- Navigate to the local interactive forensic simulation:
  ```
  file:///Users/mac/Developer/csfcl/docs/sunburst_simulation.html
  ```
  *(Or launch directly from terminal using: `open docs/sunburst_simulation.html`)*
- Ensure **Stage 1 (The attack)** is loaded and ready.

### Window 3: Terminal
- Open Terminal in the root of your local repository directory:
  ```bash
  cd /Users/mac/Developer/csfcl
  ```
- Activate the Python 3.11 virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Ensure prompt shows `(.venv)` and run a quick sanity check:
  ```bash
  floss --version
  capa --version
  ```
  *(Output should display `floss 3.1.1` and `capa 9.4.0`)*

### Window 4: VS Code / Text Editor
- Open the workspace `/Users/mac/Developer/csfcl`.
- Have [`legal_compliance/Section_63_BSA_Certificate.md`](../legal_compliance/Section_63_BSA_Certificate.md) ready to display during Part 3.

---

## 2. CHRONOLOGICAL DEMO CHOREOGRAPHY (SECOND-BY-SECOND RUNBOOK)

| Time | Speaker | PPT Slide | Screen / Window | Action / Exact Command Line | Expected Visual Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0:00** | **Amandeep** | **Slide 1 (Title)** | PPT Window | Introduce Group 10 and Capstone Topic | Somaiya title slide with student roster & dual-screen paradigm. |
| **0:45** | **Amandeep** | **Slide 2 (Vector)** | Browser (Stage 1) | Display "The attack" animated diagram | Shows APT29 supply chain compromise of 18,000 victims. |
| **1:30** | **Amandeep** | **Slide 3 (Evidence)**| Terminal | `bash scripts/verify_hashes.sh` | Green PASS output; SHA-256 baseline verified under ISO 27037. |
| **2:15** | **Amandeep** | **Slide 4 (DiE Triage)**| Browser (Stage 4) | Click "Stage 4: Detect It Easy" | PE section map scan beam, Roslyn C#, entropy staying at 6.21 (< 7.5). |
| **3:00** | **Omik** | **Slide 5 (Lifecycle)**| PPT Window | Explain 8-stage state machine | Multi-box architectural diagram of 8-stage attack lifecycle. |
| **3:30** | **Omik** | **Slide 6 (Strings)** | Terminal & Browser | `floss --version` $\rightarrow$ Click "Decode all" live | Mandiant FLOSS verified; `avsvmcloud.com` and `MachineGuid` decompressed. |
| **4:15** | **Omik** | **Slide 7 (FNV Evasion)**| Browser (Stage 6) | Click "wireshark" $\rightarrow$ "Run the check" | Animated 5-box pipeline showing FNV-1a 64-bit + XOR match. |
| **4:45** | **Omik** | **Slide 7 (FNV Evasion)**| Terminal | `python3 scripts/run_forensics.py --check-process wireshark` | Terminal calculates `0xa84ff6500970f54d` and confirms blacklist match. |
| **5:15** | **Omik** | **Slide 8 (CAPA Rules)**| Terminal | `python3 scripts/run_forensics.py --simulate --simulate-behavior victim` | Terminal prints rich table with 14 MITRE ATT&CK techniques. |
| **6:00** | **Om** | **Slide 9 (Cyber Law)**| Browser (Stage 10)| Click finding buttons in "Indian law mapping" | Interactive buttons light up IT Act Sec 66F, CERT-In 6h, and DPDP. |
| **7:00** | **Om** | **Slide 10 (BSA 2023)**| Terminal & VS Code| `python3 scripts/generate_bsa_cert.py --format both` | Generates Section 63 BSA certificate embedding MAC & telemetry. |
| **7:45** | **Om** | **Slide 10 (BSA 2023)**| VS Code | Display `legal_compliance/Section_63_BSA_Certificate.md` | Shows Part A Custodian & Part B Expert dual statutory affirmations. |
| **8:30** | **Om** | **Slide 11 (CI/CD)** | Terminal | `pytest tests/ -v` | All 22 automated test checks pass green in under 0.25 seconds. |
| **9:15** | **All Team** | **Slide 12 (Conclusion)**| Browser (Stage 11)| Display "Conclusion" & 6 core findings | Green checkmarks on 6 forensic questions; opens floor for Q&A. |

---

## 3. DETAILED TOOL-BY-TOOL REFERENCE & EXECUTION MANUAL

### TOOL 1: Detect It Easy (DiE v3.10)
- **Primary Presenter:** Amandeep Singh (Lead Investigator)
- **Technical Functionality:** Static parsing of PE32 binary headers, .NET metadata streams, compiler toolchain detection, Authenticode digital signature validation, and Shannon section entropy profiling.
- **Where to Show It:**
  1. Open [`docs/sunburst_simulation.html`](sunburst_simulation.html) $\rightarrow$ Navigate to **Stage 4 (Detect It Easy)**.
  2. Point out the **PE map beam scan** traversing `.text` (58%), `.rsrc` (17%), and `.reloc` (4%).
  3. Point out the **Shannon Entropy Curve**:
     - `.text` section: **6.21**
     - `.rsrc` section: **7.14**
     - `.reloc` section: **0.11**
     - *Key Takeaway for Professor:* The curve remains strictly below the **7.5 packed threshold**. The attackers did NOT use UPX or Themida, ensuring the malware looked completely benign to antivirus scanners.
  4. Raw Output Reference: View [`outputs/die_inspection.txt`](../outputs/die_inspection.txt).

---

### TOOL 2: Mandiant FLOSS & Raw Deflate String Decompressor
- **Primary Presenter:** Omik Acharya (Reverse Engineer)
- **Technical Functionality:** Static automated string extraction across ASCII, UTF-16LE, stack strings, tight strings, and custom raw Deflate stream decoding (`wbits = -15`).
- **Terminal Execution:**
  ```bash
  floss --version
  ```
  *(Confirms `floss 3.1.1`)*
- **Interactive UI Demonstration:**
  1. In [`docs/sunburst_simulation.html`](sunburst_simulation.html), go to **Stage 5 (FLOSS strings)**.
  2. Click the **"Decode all"** button live on screen.
  3. The strings will unscramble from Base64 ciphertext into plaintext configuration parameters:
     - `SywrLstNzskvTdFLzs8FAA==` $\rightarrow$ **`avsvmcloud.com`** (C2 Domain Apex)
     - `C/Z3Cwl3DHKN8c1MLsovzk8riXEuqiwoyU8vSizIqAQA` $\rightarrow$ **`SOFTWARE\Microsoft\Cryptography`** (Registry Path)
     - `801MzsjMS3UvzUwBAA==` $\rightarrow$ **`MachineGuid`** (Victim Host Fingerprint)
     - `SyzI1CvOz0ksKs/MSynWS87PBQA=` $\rightarrow$ **`api.solarwinds.com`** (Connectivity Canary)
  4. Raw Output Reference: View [`outputs/floss_decoded_strings.txt`](../outputs/floss_decoded_strings.txt).

---

### TOOL 3: FNV-1a 64-Bit + XOR Defense Evasion Engine
- **Primary Presenter:** Omik Acharya (Reverse Engineer)
- **Technical Functionality:** Mathematical verification of how SUNBURST evaluated 120+ analysis and security monitoring tools without plaintext strings.
- **Mathematical Formula:**
  $$\text{Hash} = \text{FNV1a}_{64}(\text{lowercase}(\text{process\_name})) \oplus \text{0x5BAC903BA7D81967}$$
  - Offset Basis: `0xcbf29ce484222325` | Prime: `0x100000001b3` | XOR Key: `6605813339339102567`
- **Interactive Terminal Execution:**
  ```bash
  python3 scripts/run_forensics.py --check-process wireshark
  ```
- **Expected Terminal Output:**
  ```
  [+] Process Name:       wireshark
  [+] Lowercase:          wireshark
  [+] 64-Bit FNV-1a Hash: 0xa84ff6500970f54d
  [+] XOR Mask Applied:   0x5bac903ba7d81967
  [+] Final Decimal Hash: 17574002783607647274
  [!] STATUS:             MATCH FOUND IN SUNBURST BLOCKLIST!
  [!] ACTION:             SUNBURST would immediately abort execution.
  ```
- **Interactive UI Demonstration:**
  In [`docs/sunburst_simulation.html`](sunburst_simulation.html) Stage 6, click **"wireshark"** $\rightarrow$ **"Run the check"** to show the 5-box animated calculation.

---

### TOOL 4: Mandiant CAPA (v9.4.0) & Behavioral Simulation
- **Primary Presenter:** Omik Acharya (Reverse Engineer)
- **Technical Functionality:** Semantic rule matching of disassembled MSIL instructions against the MITRE ATT&CK Matrix.
- **Terminal Execution:**
  ```bash
  capa --version
  python3 scripts/run_forensics.py --simulate --simulate-behavior victim
  ```
- **Flagship ATT&CK Techniques Identified:**
  - `T1497.003`: Time-Based Sandbox Evasion (12 to 14 day `Thread.Sleep` dormancy).
  - `T1071.004`: Application Layer Protocol: DNS C2 Tunneling via `avsvmcloud.com`.
  - `T1562.001`: Impair Defenses (Process blacklist hashing & termination).
  - `T1082`: System Information Discovery (`MachineGuid` & Domain queries).
  - `T1027.002`: Software Packing / Obfuscated Strings.
- **Raw Output Reference:** View [`outputs/capa_capabilities_report.txt`](../outputs/capa_capabilities_report.txt) and [`outputs/behavior_flow_reconstruction.txt`](../outputs/behavior_flow_reconstruction.txt).

---

### TOOL 5: Section 63 BSA 2023 Certificate & Legal Audit
- **Primary Presenter:** Om Lanke (Technical Auditor)
- **Technical Functionality:** Admissibility certification under Section 63(4)(c) of the Bharatiya Sakshya Adhiniyam, 2023 and Section 105 of the BNSS 2023.
- **Terminal Execution:**
  ```bash
  python3 scripts/generate_bsa_cert.py --format both
  ```
  *(Generates both Markdown and Plaintext certificates embedding live hardware MAC and system telemetry)*
- **Dual Affirmation Verification:**
  1. Open [`legal_compliance/Section_63_BSA_Certificate.md`](../legal_compliance/Section_63_BSA_Certificate.md) in VS Code.
  2. Show **Part A (Custodian Affirmation)**: Signed by Amandeep Singh, establishing continuous lawful custody, hardware write-blocking, and system integrity.
  3. Show **Part B (Forensic Expert Affirmation)**: Signed by Om Lanke and Omik Acharya, confirming cryptographic hash equality under NIST FIPS 180-4 and zero evidence tampering.

---

### TOOL 6: Automated CI/CD Regression Test Suite
- **Primary Presenter:** Om Lanke (Technical Auditor)
- **Technical Functionality:** Continuous Integration test suite validating hash manifests, Deflate decompression, FNV math, CAPA parsers, and legal deliverables.
- **Terminal Execution:**
  ```bash
  pytest tests/ -v
  ```
- **Expected Terminal Output:**
  ```
  tests/test_forensic_pipeline.py::TestCryptographicIntegrity PASSED
  tests/test_forensic_pipeline.py::TestDeobfuscationAndEvasionMechanics PASSED
  tests/test_forensic_pipeline.py::TestForensicArtifactParsers PASSED
  tests/test_forensic_pipeline.py::TestStatutoryAndLegalCompliance PASSED
  tests/test_forensic_pipeline.py::TestPipelineExecution PASSED
  tests/test_forensic_pipeline.py::TestDocumentationDeliverables PASSED
  ============================== 22 passed in 0.20s ==============================
  ```

---

## 4. EMERGENCY TROUBLESHOOTING & BACKUP PLANS

- **Issue 1: Terminal prints `pytest: command not found`**  
  *Fix:* Activate virtual environment first: `source .venv/bin/activate`

- **Issue 2: Terminal prints Python 3.9 SyntaxError on `match typeid:`**  
  *Fix:* Ensure you are using the Python 3.11 virtual environment. Re-run: `./setup.sh`

- **Issue 3: Browser does not open simulation**  
  *Fix:* Run in terminal: `open docs/sunburst_simulation.html`, or drag the HTML file directly into Chrome.
