# OPERATION SUNBURST DFIR: SYNCHRONIZED PRESENTATION SCRIPT
### 10-Minute End-to-End Spoken Dialogue Synchronized with Slides & Live Demo
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)  
**Institution:** Department of Computer Engineering, K.J. Somaiya School of Engineering  
**University:** Somaiya Vidyavihar University, Mumbai, Maharashtra  
**Academic Year:** 2026–2027 | Class: TY B.Tech COMP | **Group 10**  
**Accompanying Word Document:** [`docs/Presentation_Speaking_Script.docx`](Presentation_Speaking_Script.docx)  
**Accompanying PowerPoint Presentation:** [`docs/SUNBURST_Forensic_Investigation_Group10.pptx`](SUNBURST_Forensic_Investigation_Group10.pptx)

---

## 1. INVESTIGATION ROSTER & DIVISION OF RESPONSIBILITY

| Student Name | Roll Number | Assigned Forensic Role | Presentation Focus & Slide Coverage | Speaking Time |
| :--- | :--- | :--- | :--- | :--- |
| **Amandeep Singh** | **16010123036** | **Lead Forensic Investigator** | PE Header Triage, Supply Chain Infiltration & Cryptographic Verification (**Slides 1–4**) | 0:00 – 3:00 (3.0 min) |
| **Omik Acharya** | **16010123218** | **Reverse Engineer** | Attack Timeline, String Deobfuscation (Deflate), FNV-1a Hashing & CAPA (**Slides 5–8**) | 3:00 – 6:00 (3.0 min) |
| **Om Lanke** | **16010123216** | **Technical & Cyber Legal Auditor** | Statutory Indian Cyber Law, Section 63 BSA 2023, CI/CD Pipeline & Q&A (**Slides 9–12**) | 6:00 – 10:00 (4.0 min) |

---

## 2. PART 1: AMANDEEP SINGH (0:00 – 3:00 | SLIDES 1 TO 4)
**Role:** Lead Forensic Investigator  
**Specialization:** PE Architecture, Supply Chain Compromise & Cryptographic Verification

### Slide & Screen Choreography:
1. **Slide 1 (Title Slide):** Introduce Somaiya Group 10, presentation paradigm, and investigation scope.
2. **Slide 2 (The Supply Chain Vector):** Switch side-by-side display to Browser $\rightarrow$ `docs/sunburst_simulation.html` (Stage 1: The Attack).
3. **Slide 3 (ISO/IEC 27037 Evidence Ingestion):** Switch side-by-side display to Terminal $\rightarrow$ Run `bash scripts/verify_hashes.sh`.
4. **Slide 4 (Static PE Architecture & Shannon Entropy):** In browser, click **Stage 4: Detect It Easy** to show beam scan and entropy curve.
5. **Slide 5 (Attack Execution Timeline):** Summarize 8 stages and hand over to Omik Acharya.

### Spoken Dialogue (Word-for-Word):
> “Respected professors, external evaluators, and colleagues. Good morning. We are Group 10 from the Department of Computer Engineering at K.J. Somaiya School of Engineering, Somaiya Vidyavihar University. Welcome to our Capstone Forensic Investigation on Operation SUNBURST: The SolarWinds Supply Chain Attack.
>
> *(PPT: Slide 1 — Title Slide)*  
> I am Amandeep Singh, Roll Number 16010123036, serving as the Lead Forensic Investigator. With me are my co-investigators: Omik Acharya (Roll 16010123218), who led our Reverse Engineering and Deobfuscation efforts, and Om Lanke (Roll 16010123216), who conducted our Technical Audit, Indian Statutory Compliance, and CI/CD Verification.
>
> Our presentation operates on a dual-synchronization model: our slides cover the threat architecture and case study findings, while our side-by-side screen demonstrates the actual forensic tools, terminal scripts, and interactive simulation in real time.
>
> *(PPT: Advance to Slide 2 — The Supply Chain Vector | Side-by-Side: Browser Stage 1)*  
> Operation SUNBURST represents the watershed supply chain intrusion of the modern cyber era. Attributed by CISA to APT29 (Nobelium), the attackers did not breach customer perimeter defenses directly. Instead, they compromised the internal MSBuild software development pipeline of SolarWinds. By deploying an in-memory injection tool named SUNSPOT, they dynamically modified the source code of the core monitoring component: `SolarWinds.Orion.Core.BusinessLayer.dll`.
>
> Crucially, because this tampering occurred during compilation, the resulting trojanized DLL received a legitimate Authenticode digital signature from DigiCert. SolarWinds signed the binary, packaged it into official Orion software updates v2019.4 through v2020.2.1, and distributed it downstream to over 18,000 public and private organizations worldwide, including the U.S. Treasury, Department of Homeland Security, and critical infrastructure providers.
>
> *(PPT: Advance to Slide 3 — ISO/IEC 27037 Evidence Ingestion | Side-by-Side: Terminal — bash scripts/verify_hashes.sh)*  
> In digital forensics, maintaining evidence integrity is sacred. Under ISO/IEC 27037:2012 guidelines, evidence must be verifiable, repeatable, and non-destructive. As you can see live on our terminal, we execute our verification script: `bash scripts/verify_hashes.sh`.
>
> The script verifies both our primary malware sample ending in `...7cf0d25` and our benchmark sample ending in `...17226d7e`. The terminal outputs an immediate green `[PASS]`. This proves bit-for-bit mathematical equality with the official CISA and FireEye forensic manifests, guaranteeing zero bitwise tampering before any analysis took place.
>
> *(PPT: Advance to Slide 4 — Static PE Architecture & Shannon Entropy | Side-by-Side: Browser Stage 4)*  
> Next, we conducted static PE header triage using Detect It Easy (DiE v3.10). Observe the live visualizer on screen:
> 1. Architecture: The malware is a 32-bit PE dynamic link library for Intel 80386 running under the Microsoft .NET CLR v4.0.30319, compiled with Roslyn C# in Visual Studio 2019.
> 2. Section Entropy: Notice our Shannon entropy curve across the sections: the code section (`.text`) measures 6.21, embedded resources (`.rsrc`) measure 7.14, and relocation (`.reloc`) measures 0.11. The overall entropy is 5.9.
> This is an extraordinary finding. Normal packed malware exhibits entropy exceeding 7.5. The attackers deliberately refrained from using UPX or commercial packers so that standard antivirus heuristic engines would evaluate the file as completely benign.
> 3. Authenticode Signature: DiE confirms a valid digital signature issued to SolarWinds Worldwide, LLC by DigiCert. This is classic Subversion of Trust Controls (MITRE ATT&CK T1553.002).
>
> *(PPT: Advance to Slide 5 — Attack Execution Timeline)*  
> On Slide 5, we reconstruct the complete 8-stage execution lifecycle of the backdoor. I now hand over to our Reverse Engineer, Omik Acharya, to dissect how we deobfuscated their encrypted strings and anti-analysis mechanisms.”

---

## 3. PART 2: OMIK ACHARYA (3:00 – 6:00 | SLIDES 5 TO 8)
**Role:** Reverse Engineer  
**Specialization:** String Deobfuscation (Deflate), 64-Bit FNV-1a Hashing & CAPA Attribution

### Slide & Screen Choreography:
1. **Slide 5 (8-Stage Attack Lifecycle):** Walk through the state machine from service launch to C2 command channel.
2. **Slide 6 (String Encryption & FLOSS):** Terminal `floss --version` $\rightarrow$ Browser Stage 5 $\rightarrow$ Click **"Decode all"** button live.
3. **Slide 7 (Anti-Analysis FNV-1a Hashing + XOR):** In browser Stage 6, click **"wireshark"** $\rightarrow$ **"Run the check"**. Then in Terminal: `python3 scripts/run_forensics.py --check-process wireshark`.
4. **Slide 8 (Capability Mapping & CAPA):** In Terminal, run `capa --version` and `python3 scripts/run_forensics.py --simulate --simulate-behavior victim`.

### Spoken Dialogue (Word-for-Word):
> “Thank you, Amandeep. Respected evaluators, I am Omik Acharya, Roll Number 16010123218, serving as Reverse Engineer for Group 10.
>
> *(PPT: Slide 5 — 8-Stage Lifecycle Overview)*  
> As outlined on Slide 5, SUNBURST's internal logic operates as an 8-stage state machine: initiating upon service startup, entering a 14-day dormancy timer, executing defensive process checks, hashing the victim host, generating domain names, tunneling covert DNS queries, dropping second-stage loaders, and establishing persistent interactive C2.
>
> *(PPT: Advance to Slide 6 — String Encryption | Side-by-Side: Terminal 'floss --version' -> Browser Stage 5)*  
> To investigate this logic, we applied Mandiant FLOSS (v3.1.1). As verified in our terminal, FLOSS is installed natively. Standard forensic string utilities failed completely because the malware authors encrypted every critical string using a two-stage mechanism: Base64 encoding followed by raw Deflate decompression (`wbits = -15`, which strips the standard zlib header).
>
> *(Side-by-Side: Click 'Decode all' button in Browser Stage 5)*  
> Watch our browser simulation decode these tokens live in real time:
> • The ciphertext `SywrLstNzskvTdFLzs8FAA==` immediately inflates to `avsvmcloud.com` — the primary command-and-control apex domain.  
> • The token `C/Z3Cwl3DHKN8c1ML...` inflates to `SOFTWARE\Microsoft\Cryptography`, the registry hive queried to read the victim's MachineGuid.  
> • The token `801MzsjMS3UvzUwBAA==` yields `MachineGuid`, confirming host fingerprinting.  
> • The token `SyzI1CvOz0ksKs/MSynWS87PBQA=` reveals `api.solarwinds.com` — a benign canary used to verify active internet connectivity.
>
> *(PPT: Advance to Slide 7 — Anti-Analysis & Defense Evasion | Side-by-Side: Browser Stage 6)*  
> On Slide 7, we address how SUNBURST evaded detection by security analysts. If the binary had contained plaintext strings like 'wireshark', 'procmon', or 'x64dbg', endpoint detection and response (EDR) rules would have flagged it immediately. Instead, the authors engineered a mathematical evasion routine:
> First, convert the running process name to lowercase.  
> Second, compute its 64-bit Fowler-Noll-Vo 1a (FNV-1a) hash using offset basis `0xcbf29ce484222325` and prime `0x100000001b3`.  
> Third, XOR the resulting 64-bit digest with the hardcoded magic constant: `0x5BAC903BA7D81967`.
>
> *(Side-by-Side: In Browser Stage 6, click 'wireshark' -> 'Run the check' | Switch to Terminal)*  
> In our simulation and terminal, we run: `python3 scripts/run_forensics.py --check-process wireshark`.  
> The terminal computes the hash `0xa84ff6500970f54d`, XORs it, and produces the exact decimal value `17574002783607647274`, confirming a direct hit against the malware's hardcoded blocklist of over 120 security utilities. If any of these tools are running, SUNBURST permanently self-terminates.
>
> *(PPT: Advance to Slide 8 — Capability Mapping | Side-by-Side: Terminal — capa --version && python3 scripts/run_forensics.py --simulate)*  
> Finally, we analyzed the binary using Mandiant CAPA (v9.4.0) to map capabilities directly to the MITRE ATT&CK framework:
> • **T1497.003 (Time-Based Sandbox Evasion):** A hardcoded `Thread.Sleep` interval of 288 to 336 hours (12 to 14 days) to outlast automated sandboxes.  
> • **T1071.004 (DNS C2 Tunneling):** Covert DNS query encoding transmitting host telemetry within subdomains of `avsvmcloud.com`.  
> • **T1562.001 (Impair Defenses):** Automated enumeration and suppression of security processes.  
> • **T1082 (System Information Discovery):** Querying network configurations and system GUIDs.
>
> I now pass the floor to Om Lanke, our Technical & Cyber Legal Auditor, to present our statutory compliance under Indian law and automated CI/CD pipeline.”

---

## 4. PART 3: OM LANKE (6:00 – 10:00 | SLIDES 9 TO 12)
**Role:** Technical & Cyber Legal Auditor  
**Specialization:** IT Act 2000, CERT-In Directions 2022, Section 63 BSA 2023 & Pytest CI Automation

### Slide & Screen Choreography:
1. **Slide 9 (Indian Statutory Cyber Law Framework):** In browser, show Stage 10 ('Indian law mapping') and click through statutory finding buttons.
2. **Slide 10 (Legal Admissibility & Section 63 BSA 2023):** Switch to Terminal $\rightarrow$ Run `python3 scripts/generate_bsa_cert.py --format both`. Switch to VS Code $\rightarrow$ Display `legal_compliance/Section_63_BSA_Certificate.md`.
3. **Slide 11 (CI/CD Automation & Verification):** Switch to Terminal $\rightarrow$ Run `pytest tests/ -v`. Show all 22 test assertions passing.
4. **Slide 12 (Conclusion & Findings Matrix):** In browser, click Stage 11 ('Conclusion') showing 6 green checkmarks, summarize key findings, and open floor for Q&A.

### Spoken Dialogue (Word-for-Word):
> “Thank you, Omik. Respected evaluators, I am Om Lanke, Roll Number 16010123216, serving as the Technical & Cyber Legal Auditor for Group 10.
>
> *(PPT: Slide 9 — Indian Statutory Cyber Law Framework | Side-by-Side: Browser Stage 10)*  
> A forensic investigation cannot conclude at technical disassembly; it must establish culpability and admissibility under statutory law. On Slide 9 and in our browser simulation, we map SUNBURST's technical behaviors directly to Indian cyber jurisprudence:
> 1. **Information Technology Act, 2000:**  
>    • **Section 43 & 66:** Unauthorized access, data extraction (`MachineGuid`), and introducing computer contaminants (penalties include civil damages and up to 3 years imprisonment).  
>    • **Section 66F (Cyber Terrorism):** SUNBURST targeted government ministries and critical communications infrastructure. Introducing malicious code with intent to threaten national sovereignty or critical infrastructure carries a mandatory sentence of Imprisonment for Life.  
>    • **Section 70:** Unauthorized access to declared Protected Systems (up to 10 years imprisonment).  
>    • **Section 43A:** Entities deploying unverified third-party vendor updates without adequate due diligence face uncapped civil compensation for negligence.  
> 2. **CERT-In Directions (28 April 2022):**  
>    • **Mandatory 6-Hour Reporting Window:** Under Annexure I Category 2, organizations must notify CERT-In within 6 hours of identifying a supply chain intrusion. We have drafted an official incident notification template in `legal_compliance/CERT_In_Incident_Notification_Template.md`.  
>    • **180-Day Log Retention:** Direction 20(3) mandates ICT service providers maintain system and network logs for 180 days within Indian jurisdiction.  
> 3. **Digital Personal Data Protection (DPDP) Act, 2023:** Section 8(5) & 8(6) mandate formal breach notification to the Data Protection Board of India.
>
> *(PPT: Advance to Slide 10 — Legal Admissibility & Section 63 BSA 2023 | Side-by-Side: Terminal — python3 scripts/generate_bsa_cert.py --format both)*  
> Now, how is digital evidence legally admitted before an Indian court? With the enactment of the Bharatiya Sakshya Adhiniyam, 2023, the Indian Evidence Act, 1872 was repealed. The traditional Section 65B certificate is now legally obsolete.
>
> Under Section 63 of the BSA 2023, admissibility of electronic records requires a rigorous two-part statutory certificate:
> *(Side-by-Side: Open legal_compliance/Section_63_BSA_Certificate.md in VS Code)*  
> As generated live by our script, observe the certificate structure:
> • **Part A (Custodian Affirmation):** Executed by Amandeep Singh, certifying workstation MAC address, hardware write-blocking, and lawful custody under ISO/IEC 27037.  
> • **Part B (Forensic Expert Affirmation):** Executed jointly by Omik Acharya and myself, affirming cryptographic hash equality under NIST FIPS 180-4 and the scientific validity of our toolchain.  
> Notice that our script dynamically binds the certificate to the physical hardware by embedding the machine MAC address, kernel release, and NTP timestamp. This satisfies Section 105 of the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023, rendering our forensic evidence fully admissible as substantive primary evidence.
>
> *(PPT: Advance to Slide 11 — CI/CD Automation & Verification | Side-by-Side: Terminal — pytest tests/ -v)*  
> To guarantee that our findings are mathematically reproducible across any forensic workstation, we constructed an automated CI/CD pipeline using Astral `uv` and GitHub Actions. Look at our terminal as we run: `pytest tests/ -v`.  
> In just 0.20 seconds, all 22 unit test assertions execute and pass green across 6 test suites: cryptographic integrity, raw Deflate inflation, FNV-1a 64-bit hashing math, CAPA capability parsing, telemetry extraction, and legal certificate generation.
>
> *(PPT: Advance to Slide 12 — Conclusion & Findings Matrix | Side-by-Side: Browser Stage 11)*  
> In conclusion, on Slide 12 and in Stage 11 of our simulation, Group 10 has definitively resolved all six core capstone questions:
> 1. **Authenticity:** Legitimate DLL trojanized in the build pipeline with valid DigiCert signature.  
> 2. **Strings:** 100% decrypted via Base64 and raw Deflate (`wbits=-15`).  
> 3. **Anti-Analysis:** 120+ tools checked via 64-bit FNV-1a hashing + XOR mask, maintaining benign entropy (5.9).  
> 4. **Network C2:** Covert DNS DGA tunneling via `avsvmcloud.com`.  
> 5. **Indian Law:** Fully actionable under IT Act Sec 66F, CERT-In 6-hour directive, and certified under BSA 2023 Section 63.  
> 6. **Verification:** 100% automated regression test coverage via CI/CD.
>
> We thank our professors and evaluators for their time and guidance. Group 10 is now open for your questions.”

---

## 5. EVALUATOR Q&A CHEAT-SHEET (Top 6 Questions & Answers)

1. **Q: Why did you not execute the malware in a dynamic sandbox?**  
   *A:* SUNBURST contains a hardcoded 12 to 14 day dormancy timer (MITRE ATT&CK T1497.003) and checks for sandbox hooks. A standard 5-minute dynamic detonation reveals zero network activity. Static analysis using DiE, FLOSS, and CAPA allowed us to reverse-engineer 100% of the malware's logic safely without risking host compromise or C2 leakage.

2. **Q: What is the exact difference between Section 65B of IEA 1872 and Section 63 of BSA 2023?**  
   *A:* BSA 2023 repealed IEA 1872. Section 63 BSA modernizes electronic evidence admissibility, explicitly recognizing virtualized systems and cloud infrastructure. It mandates a dual-certificate structure: Part A by the Custodian proving lawful management, and Part B by the Technical Expert certifying cryptographic hash integrity.

3. **Q: Why did the attackers XOR the FNV-1a hash with 0x5BAC903BA7D81967?**  
   *A:* Plain FNV-1a hashes of common process names can be reversed using rainbow tables. XORing the 64-bit digest with a secret hardcoded constant added a secondary obfuscation layer, preventing researchers from identifying which tools were targeted without disassembling the DLL.

4. **Q: How did the malware achieve persistence without setting normal Windows Run registry keys?**  
   *A:* SUNBURST achieved persistence via DLL component hijacking (T1574.002). Embedded inside the core SolarWinds Orion DLL, it executed automatically every time the legitimate Windows service `SolarWinds.BusinessLayerHost.exe` started, avoiding suspicious registry Run keys.

5. **Q: What are the mandatory reporting deadlines under CERT-In Directions 2022?**  
   *A:* Under Direction 5(i) of the 28 April 2022 Directions, any supply chain or critical system compromise must be reported to CERT-In within 6 hours of detection. Under Direction 20(3), all system and network logs must be maintained within Indian jurisdiction for 180 days.

6. **Q: How does the BSA 2023 Certificate bind evidence to the physical workstation?**  
   *A:* Our automated generator (`scripts/generate_bsa_cert.py`) queries the local network interface for its physical MAC address, reads the host kernel release, captures CPU architecture, and queries the system NTP clock. This physical telemetry is permanently written into the affidavit alongside the SHA-256 digests.
