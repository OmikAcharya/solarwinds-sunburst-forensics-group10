# SUNBURST DFIR CAPSTONE: TOOL EXECUTION & DEMO MANUAL
### Step-by-Step Technical Runbook, Command Reference, and Screen Choreography
**Department of Computer Engineering, KJ Somaiya School of Engineering**  
**Somaiya Vidyavihar University, Mumbai, Maharashtra**  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)  
**Academic Year:** 2026–2027 | Class: TY B.Tech COMP | **Group 10**  
**Accompanying Word Document:** [`docs/Tool_Execution_and_Demo_Manual.docx`](Tool_Execution_and_Demo_Manual.docx)

---

## 1. PRE-DEMO ENVIRONMENT CHECKLIST (2 MINUTES BEFORE RECORDING)

Before hitting record on your screen, ensure your workspace is prepared with the following three windows arranged side-by-side or on dedicated desktop spaces:

### Window 1: Web Browser (Google Chrome / Safari)
- Navigate to the local interactive forensic simulation:
  ```
  file:///Users/mac/Developer/csfcl/docs/sunburst_simulation.html
  ```
  *(Or launch directly from terminal using: `open docs/sunburst_simulation.html`)*
- Ensure **Stage 1 (The attack)** is loaded and ready.
- Check that the audio/speaker output and fullscreen button work.

### Window 2: Terminal
- Open Terminal in the root of your local repository directory:
  ```bash
  cd /Users/mac/Developer/csfcl
  ```
- Activate the Python 3.11 virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Ensure prompt shows `(.venv)` and run a quick version check:
  ```bash
  floss --version
  capa --version
  ```
  *(Output should display `floss 3.1.1` and `capa 9.4.0`)*

### Window 3: VS Code / Text Editor
- Open the workspace `/Users/mac/Developer/csfcl`.
- Have [`legal_compliance/Section_63_BSA_Certificate.md`](../legal_compliance/Section_63_BSA_Certificate.md) ready to display during Part 3.

---

## 2. CHRONOLOGICAL DEMO CHOREOGRAPHY (SECOND-BY-SECOND RUNBOOK)

```
+-------+------------+-------------------+-------------------------------------------------------------+-------------------------------------------------------------+
| Time  | Speaker    | Screen / Window   | Action / Exact Command Line                                 | Expected Visual Result                                      |
+-------+------------+-------------------+-------------------------------------------------------------+-------------------------------------------------------------+
| 0:00  | Avantdeep  | Browser (Stage 1) | Display "The attack" animated diagram                       | Shows APT29 supply chain vector and 18,000 victim reach.    |
| 1:15  | Avantdeep  | Terminal          | bash scripts/verify_hashes.sh                               | Green PASS output; SHA-256 baseline verified (ISO 27037).   |
| 1:50  | Avantdeep  | Browser (Stage 4) | Click "Stage 4: Detect It Easy"                             | PE section scan beam, Roslyn C#, entropy staying at 6.21.   |
| 2:45  | Omik       | Terminal          | floss --version                                             | Prints "floss 3.1.1"; proves native Mandiant tool is live.  |
| 3:00  | Omik       | Browser (Stage 5) | Click "Decode all" button live                              | Real-time raw Deflate decompression to "avsvmcloud.com".   |
| 3:45  | Omik       | Browser (Stage 6) | Click "wireshark" -> "Run the check"                        | Animated 5-box pipeline showing FNV-1a 64-bit + XOR match.  |
| 4:20  | Omik       | Terminal          | python3 scripts/run_forensics.py --check-process wireshark  | Terminal calculates 0xa84ff6500970f54d and confirms match.  |
| 4:50  | Omik       | Terminal          | python3 scripts/run_forensics.py --simulate --simulate-behavior victim | Terminal prints rich table with 14 MITRE ATT&CK techniques. |
| 5:45  | Om         | Browser (Stage 10)| Click finding buttons in "Indian law mapping"               | Interactive buttons light up IT Act, CERT-In, and BSA 2023. |
| 6:45  | Om         | Terminal          | python3 scripts/generate_bsa_cert.py --format both          | Generates Markdown and Plaintext Section 63 certificates.   |
| 7:15  | Om         | VS Code           | Display legal_compliance/Section_63_BSA_Certificate.md      | Shows Part A Custodian & Part B Expert dual affirmations.   |
| 7:50  | Om         | Terminal          | pytest tests/ -v                                            | All 22 automated test checks pass in under 0.3 seconds.     |
| 8:30  | Om         | Browser (Stage 11)| Display "Conclusion" & 6 core findings                      | Green checkmarks on 6 forensic questions; opens for Q&A.    |
+-------+------------+-------------------+-------------------------------------------------------------+-------------------------------------------------------------+
```

---

## 3. DETAILED TOOL-BY-TOOL REFERENCE & EXECUTION MANUAL

### TOOL 1: Detect It Easy (DiE v3.10)
- **Primary Presenter:** Avantdeep
- **Technical Functionality:** Static parsing of Portable Executable 32-bit (PE32) binary headers, .NET metadata streams, compiler toolchain detection, Authenticode digital signature validation, and Shannon section entropy profiling.
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
- **Primary Presenter:** Omik Acharya
- **Technical Functionality:** Static automated string extraction across ASCII, UTF-16LE, stack strings, tight strings, and custom XOR/subtraction/Deflate decoding.
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
     - `801MzsjMS3UvzUwBAA==` $\rightarrow$ **`MachineGuid`** (Victim Hardware Identifier)
     - `C07NSU0uUdBScCvKz1UIz8wzNor3Sy0pzy/KdkxJL...` $\rightarrow$ **`Select * From Win32_NetworkAdapterConfiguration where IPEnabled=true`** (WMI Query)
     - `C0otyC8qCU8sSc5ILQpKLSmqBAA=` $\rightarrow$ **`ReportWatcherRetry`** (Backdoor Config Flag)
     - `SyzI1CvOz0ksKs/MSynWS87PBQA=` $\rightarrow$ **`api.solarwinds.com`** (Connectivity Canary)
     - `C44MDnH1jXEuLSpKzStxzs8rKcrPCU4tiSlOLSrLTE4tBgA=` $\rightarrow$ **`SYSTEM\CurrentControlSet\services`** (Services Evasion Path)
  4. Raw Output Reference: View [`outputs/floss_decoded_strings.txt`](../outputs/floss_decoded_strings.txt).

---

### TOOL 3: FNV-1a 64-Bit + XOR Defense Evasion Engine
- **Primary Presenter:** Omik Acharya
- **Technical Functionality:** Reversing the mathematical algorithm used by SUNBURST to identify and terminate over 120 defensive security processes without embedding plaintext strings.
- **Mathematical Formula:**
  $$\text{Hash} = \text{FNV1a}_{64}(\text{lowercase}(\text{process\_name})) \oplus \text{0x5BAC903BA7D81967}$$
  - FNV Offset Basis: `0xcbf29ce484222325`
  - FNV Prime: `0x100000001b3`
  - XOR Constant: `0x5BAC903BA7D81967` (Decimal: `6605813339339102567`)
- **Terminal Execution Command:**
  ```bash
  python3 scripts/run_forensics.py --check-process wireshark
  ```
  Expected Output:
  ```
  [+] Process Name:      wireshark
  [+] Lowercase:         wireshark
  [+] FNV-1a 64-bit Hex: 0xa84ff6500970f54d
  [+] XOR 64-bit Dec:    17574002783607647274
  [+] In Blacklist?      YES (Matched: wireshark)
  ```
- **Interactive UI Demonstration:**
  1. In [`docs/sunburst_simulation.html`](sunburst_simulation.html), go to **Stage 6 (Hidden blocklist)**.
  2. Click the `wireshark` chip or type it into the input box $\rightarrow$ click **"Run the check"**.
  3. Point out the animated 5-stage transformation box lighting up in red to signal a blacklist match.
  4. Raw Output Reference: View [`outputs/fnv_blocklist_hashes.txt`](../outputs/fnv_blocklist_hashes.txt).

---

### TOOL 4: Mandiant CAPA (v9.4.0) & Behavioral Simulation
- **Primary Presenter:** Omik Acharya / Om Lanke
- **Technical Functionality:** Rule-based capability attribution parsing disassembled MSIL instructions and mapping findings to the MITRE ATT&CK Matrix and Malware Behavior Catalog (MBC).
- **Terminal Execution Commands:**
  ```bash
  capa --version
  python3 scripts/run_forensics.py --simulate --simulate-behavior victim
  ```
- **Key ATT&CK Indicators to Point Out in Terminal:**
  - **T1497.003 (Time-Based Evasion):** Hardcoded `Thread.Sleep` delay of 288 hours (**12 to 14 days**) designed to outlast automated dynamic analysis sandboxes.
  - **T1071.004 (DNS C2 Tunneling):** DGA query generation exfiltrating encoded machine GUIDs via subdomains of `avsvmcloud.com`.
  - **T1562.001 (Impair Defenses):** Hashing running processes and terminating logging agents.
  - **T1082 (System Information Discovery):** Querying `MachineGuid` and domain properties.
- **Interactive UI Demonstration:**
  1. Go to **Stage 7 (CAPA capabilities)** in [`docs/sunburst_simulation.html`](sunburst_simulation.html).
  2. Point out the MITRE ATT&CK grid lighting up in solid red.
  3. Go to **Stage 8 (Behaviour simulation)** $\rightarrow$ toggle between **"Victim Orion server"** (all 8 gates pass) and **"Analyst VM with Wireshark"** (stops at Step 4).
  4. Raw Output Reference: View [`outputs/capa_capabilities_report.txt`](../outputs/capa_capabilities_report.txt) and [`outputs/behavior_flow_reconstruction.txt`](../outputs/behavior_flow_reconstruction.txt).

---

### TOOL 5: Section 63 BSA 2023 Statutory Certificate Generator
- **Primary Presenter:** Om Lanke
- **Technical Functionality:** Automation utility that gathers hardware MAC addresses, workstation telemetry, and NIST FIPS 180-4 cryptographic hashes to generate a legally admissible court certificate under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023 (repealing Section 65B of the Indian Evidence Act, 1872).
- **Terminal Execution Command:**
  ```bash
  python3 scripts/generate_bsa_cert.py --format both
  ```
- **What to Show in VS Code / Editor:**
  1. Open [`legal_compliance/Section_63_BSA_Certificate.md`](../legal_compliance/Section_63_BSA_Certificate.md).
  2. Show **Part A (Custodian Affirmation)**: Signed by Avantdeep, establishing continuous lawful custody, hardware write-blocking, and system integrity.
  3. Show **Part B (Forensic Expert Certificate)**: Signed jointly by Omik and Om, certifying cryptographic hash equality (`325c9b6a...`), deterministic tool outputs, and zero evidence tampering.

---

### TOOL 6: Pytest CI/CD Pipeline Suite
- **Primary Presenter:** Om Lanke
- **Technical Functionality:** Automated test verification validating hash matching, Deflate decompression, FNV-1a XOR math, parser outputs, statutory forms, and deliverable integrity.
- **Terminal Execution Command:**
  ```bash
  pytest tests/ -v
  ```
  Expected Output:
  ```
  ============================== 22 passed in 0.22s ==============================
  ```

---

## 4. EMERGENCY TROUBLESHOOTING & BACKUP PLANS

| Symptom / Error | Root Cause | Immediate One-Line Fix |
| :--- | :--- | :--- |
| `pytest: command not found` | Virtual environment not active in current terminal tab | Run: `source .venv/bin/activate` |
| `SyntaxError: invalid syntax on match typeid:` | Default macOS Python 3.9 was invoked instead of Python 3.11 | Run: `./setup.sh` (Auto-selects Python 3.11) |
| Browser does not open simulation file | Default browser handler not registered | Run: `open docs/sunburst_simulation.html` or drag the file into Chrome |
| Hash mismatch error in script | Sample hash manifest was modified | Run: `git checkout evidence/sample_hash.sha256` |
