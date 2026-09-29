# CAPSTONE PRESENTATION SCRIPT (10 MINUTES WORD-FOR-WORD)
### Project: SUNBURST Supply Chain Malware Forensics & Statutory Compliance Audit
**Academic Session:** 2026–2027 | TY B.Tech Computer Engineering  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation - 20 Marks)  
**Institution:** KJ Somaiya School of Engineering, Somaiya Vidyavihar University, Mumbai  
**Group Number:** 10  
**Interactive Simulation Model:** [`docs/sunburst_simulation.html`](sunburst_simulation.html)

---

## PRESENTATION STRUCTURE & TIMELINE ALLOCATION

```
+---------------------------------------------------------------------------------------------------------+
| Speaker         | Roll No     | Segment Focus                                         | Allocated Time  |
+---------------------------------------------------------------------------------------------------------+
| Amandeep Singh  | 16010123036 | Part 1: Attack Vector, Evidence Custody & DiE Triage  | 00:00 – 03:20   |
| Omik Acharya    | 16010123218 | Part 2: FLOSS Deobfuscation & CAPA Behavioral Mapping | 03:20 – 06:40   |
| Om Lanke        | 16010123216 | Part 3: Indian Law, Section 63 BSA 2023 & Remediation | 06:40 – 10:00   |
+---------------------------------------------------------------------------------------------------------+
```

---

## PART 1: AMANDEEP SINGH (00:00 – 03:20)
**Role:** Lead Investigator (PE Architecture & DiE Triage)  
**Slides:** Slide 1 (Title), Slide 2 (Attack Overview & Chronology), Slide 3 (Evidence Acquisition & Hashing), Slide 4 (DiE Inspection & Entropy)

---

### [00:00 – 00:45] Introduction & Case Study Significance
*(Speaker Cue: Stand upright, clear confident tone, click to Slide 1)*

"Respected evaluators, faculty members, and fellow engineers. Good morning. 

On behalf of Group 10 from the Department of Computer Engineering, KJ Somaiya School of Engineering, Somaiya Vidyavihar University, I, Amandeep Singh, along with my colleagues Omik Acharya and Om Lanke, welcome you to our capstone digital forensics defense titled: **'Forensic Dissection of the SUNBURST Supply Chain Intrusion: Static Triage, Reverse Engineering, and Indian Statutory Admissibility under BSA 2023.'**

In cybersecurity, enterprise networks operate on a fundamental premise: *'Trust your digitally signed software updates.'* But in late 2020, state-sponsored adversary UNC2452—attributed to APT29 and Russia's SVR—subverted that very trust. Instead of breaching fortified perimeter firewalls, they compromised the automated build system of SolarWinds, injecting a backdoor directly into their core network management DLL. Over 18,000 global commercial and governmental organizations installed it voluntarily. Today, we demonstrate an end-to-end static forensic autopsy of that exact trojanized library without running a single line of it."

---

### [00:45 – 01:40] Attack Vector, 15-Month Chronology & Evidence Custody
*(Speaker Cue: Transition to Slide 2 and Slide 3)*

"Please look at Slide 2. Unlike runtime memory injection, SUNBURST was a pure **Software Supply Chain Compromise (MITRE ATT&CK T1195.002)**. 

The attackers were inside SolarWinds for over fifteen months:
- In September 2019, they gained access.
- In October 2019, they added harmless test code to an Orion build to validate the build injection concept.
- In February 2020, they injected SUNBURST into the build process using the memory-only SUNSPOT dropper.
- Between March and June 2020, signed, trojanized updates shipped to 18,000 organizations.
- Out of these 18,000, approximately 100 high-value organizations were hand-selected by the attackers for deep second-stage intrusion.

Turning to Slide 3: Following **ISO/IEC 27037 standards** and **Section 105 of the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023**, we acquired `SolarWinds.Orion.Core.BusinessLayer.dll` on an air-gapped workstation behind a Tableau hardware write-blocker. 

We independently calculated the SHA-256 cryptographic digest:  
`325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73` (with variant `32519b85c0b4...`).  
When re-hashed post-investigation, all 64 hexadecimal characters matched identically. The evidence was preserved mathematically intact."

---

### [01:40 – 03:20] PE Architecture & Detect It Easy (DiE) Triage
*(Speaker Cue: Click to Slide 4, point to the entropy curve and Authenticode block)*

"To triage the file without executing malicious code, we leveraged **Detect It Easy (DiE v3.10)**. 

DiE reveals three crucial structural realities:
1. **Target Architecture & Compiler:** The file is a PE32 dynamic link library for Intel 80386 running the `.NET Framework v4.0.30319` with `COMIMAGE_FLAGS_ILONLY`. It was compiled using the Microsoft Roslyn C# compiler.
2. **Entropy Curve & Packer Absence:** Notice the entropy curve on Slide 4. It stays around **5.9 to 6.21** across the `.text` section, **7.14** in `.rsrc`, and **0.11** in `.reloc`. 
   
   Why didn't the attackers pack the DLL with UPX or Themida? Because packers push entropy above the **7.5 packed threshold**, instantly triggering automated heuristic alerts in corporate security tools. By remaining unpacked, the file appeared completely benign.
3. **Authenticode Integrity:** The security directory at RVA `0x0008B200` confirms a valid Authenticode signature issued to `SolarWinds Worldwide, LLC` by DigiCert. This is classic **Subversion of Trust Controls (T1553.002)**.

With the structural envelope established, I now invite our Reverse Engineer, Omik Acharya, to dissect the deobfuscation algorithms and behavioral logic."

---

## PART 2: OMIK ACHARYA (03:20 – 06:40)
**Role:** Reverse Engineer (FLOSS Deobfuscation & CAPA Attribution)  
**Slides:** Slide 5 (FLOSS Deobfuscation & Deflate Decompression), Slide 6 (FNV-1a Hashed Blacklist), Slide 7 (CAPA & Behavioral Decision Flow)

---

### [03:20 – 04:30] Static String Deobfuscation (FLOSS & Raw Deflate)
*(Speaker Cue: Step forward, display Slide 5, technical authoritative tone)*

"Thank you, Amandeep. Good morning everyone. I am Omik Acharya. My focus was reverse engineering the internal evasion routines, cryptographic ciphers, and command channels of SUNBURST.

When we ran **Mandiant FLOSS (v3.1.1)**, it warned:  
`WARNING: .NET string deobfuscation is not supported; extracting static strings only.`  
Yet, FLOSS extracted **2,146 static strings**, immediately flagging suspicious classes: `OrionImprovementBusinessLayer`, `ZipHelper`, `Unzip`, and `DeflateStream`.

SUNBURST hid its core configuration strings using a two-tier scheme: **raw Deflate compression** followed by **Base64 encoding**. We built an automated decoder into our pipeline. As shown on Slide 5:
- `SywrLstNzskvTdFLzs8FAA==` decompresses to the C2 apex: **`avsvmcloud.com`**
- `C/Z3Cwl3...` decompresses to: **`SOFTWARE\Microsoft\Cryptography`**
- `801MzsjMS3UvzUwBAA==` decompresses to: **`MachineGuid`**, used to fingerprint victims
- `C07NSU0...` decompresses to the WMI query: **`Select * From Win32_NetworkAdapterConfiguration where IPEnabled=true`**
- `SyzI1Cv...` decompresses to the connectivity canary: **`api.solarwinds.com`**"

---

### [04:30 – 05:40] The Hidden Blacklist: FNV-1a 64-Bit + XOR Key
*(Speaker Cue: Click to Slide 6, walk through the interactive calculation)*

"Now look at Slide 6: How did SUNBURST avoid detection by analysis tools without giving away what it was looking for?

If malware contains strings like `wireshark.exe` or `x64dbg.exe`, standard antivirus scanners flag it immediately. SUNBURST solved this mathematically. It took running process names, converted them to lowercase, calculated their **64-bit FNV-1a hash**, and XORed the digest with the constant **`0x5BAC903BA7D81967`**.

Let us trace the exact pipeline:
1. Process name: `Wireshark`
2. Normalized lowercase: `wireshark`
3. 64-bit FNV-1a hash: `0xa84ff6500970f54d`
4. XOR with `0x5BAC903BA7D81967`: **`17574002783607647274`**

It compared this result against its hardcoded table of 120+ hashes. Recovered targets include `procmon`, `procexp`, `fiddler`, `x64dbg`, `ida64`, `dnspy`, `autoruns`, `tcpview`, and `sysmon`. If any matched, the backdoor went completely silent."

---

### [05:40 – 06:40] CAPA Behavioral Mapping & The 8-Step Decision Gate
*(Speaker Cue: Click to Slide 7, highlight decision stages)*

"On Slide 7, **Mandiant CAPA v7.0.1** mapped the backdoor's capabilities to the MITRE ATT&CK Matrix:
- **T1497.003 (Time-Based Evasion):** CAPA detected `delay execution`—a hardcoded `Thread.Sleep` delay of 288 hours, or **12 to 14 days**, designed to outlast automated dynamic sandboxes that terminate after 5 to 10 minutes.
- **T1071.004 (DNS C2 Tunneling):** CAPA detected `resolve DNS`. The malware transmitted encoded victim telemetry via subdomains of `avsvmcloud.com`.
- **T1562.001 (Impair Defenses):** Hashing processes and terminating active logging.

By correlating our findings, we reconstructed the **8-Step Environmental Decision Chain**:
- On an **Analyst VM with Wireshark**, the backdoor terminates at **Step 4** (Security tool detected).
- On an **Isolated Test Machine**, it terminates at **Step 5** (Internet check fails).
- On a **Fresh Installation**, it waits at **Step 2** (Dormancy period).
- Only on a **real, domain-joined enterprise server** does it proceed through all 8 steps to open the HTTP command channel.

I now invite Om Lanke to analyze the legal violations under Indian cyber law and present our Section 63 BSA 2023 certification."

---

## PART 3: OM LANKE (06:40 – 10:00)
**Role:** Cyber Legal Auditor & Compliance Lead (IT Act, CERT-In, BSA 2023, DPDP 2023, BNSS 2023)  
**Slides:** Slide 8 (Indian Statutory Mapping), Slide 9 (Section 63 BSA 2023 & BNSS 2023), Slide 10 (Remediation & 6 Inquiries)

---

### [06:40 – 07:50] Statutory Violations Under Indian Cyber Jurisprudence
*(Speaker Cue: Confident legal authority tone, display Slide 8)*

"Thank you, Omik. Respected evaluators, digital forensics without statutory integration cannot sustain prosecution or enterprise governance. As the Cyber Legal Auditor, I mapped the SUNBURST intrusion across the Indian legal corpus.

Please direct your attention to Slide 8. The intrusion triggers four core provisions under the **Information Technology Act, 2000**:
1. **Section 43(a), (b), and (c):** Unauthorized access, extraction of system identifiers, and introduction of malicious contaminants establish civil liability for damages.
2. **Section 66:** Dishonest and fraudulent hacking attracts criminal prosecution punishable by up to 3 years imprisonment.
3. **Section 66F (Cyber Terrorism):** SUNBURST compromised government infrastructure, defense suppliers, and energy backbones. Under Section 66F(1)(B), introducing malicious code with intent to threaten the sovereignty or integrity of India carries a mandatory sentence of **Imprisonment for Life**.
4. **Section 70 & NCIIPC:** Unauthorized tampering with designated Critical Information Infrastructure triggers up to 10 years imprisonment.

Furthermore, corporate entities that deployed unverified vendor updates violated **Section 43A and the 2011 Reasonable Security Practices Rules**, creating liability for corporate negligence.

Under the **CERT-In Cyber Security Directions of 28 April 2022**, mandated by Section 70B:
- Organizations must formally notify CERT-In **within 6 hours** of detecting supply chain compromises.
- Organizations must retain system and traffic logs within Indian jurisdiction for **180 days** (Direction 5(v)).
- And under the **Digital Personal Data Protection (DPDP) Act, 2023**, mandatory breach notices must be issued to the Data Protection Board of India."

---

### [07:50 – 09:00] Admissibility of Electronic Records: Section 63 BSA 2023
*(Speaker Cue: Click to Slide 9, emphasize the transition from 65B to Section 63)*

"Moving to Slide 9: In Indian evidentiary law, the Indian Evidence Act, 1872 has been repealed by the **Bharatiya Sakshya Adhiniyam (BSA), 2023**. The old Section 65B is replaced by **Section 63 of the BSA, 2023**.

Under Section 63(2), four statutory conditions must be established:
1. Lawful, regular operational custody of the computing device.
2. Regular, ordinary feeding of electronic records.
3. Proper operational state without memory corruption or unauthorized alteration.
4. Exact, unadulterated reproduction of the stored data.

To satisfy Section 63(4) of the BSA 2023 and Section 105 of the **Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023**, our team developed `generate_bsa_cert.py`, producing a dual-signatory certificate:
- **Part A (Custodian Affirmation):** Executed by Amandeep Singh, affirming physical control, workstation telemetry, and write-block integrity.
- **Part B (Forensic Expert Technical Certificate):** Executed jointly by Omik Acharya and myself, verifying cryptographic hash matching (NIST FIPS 180-4), deterministic tool outputs, and complete absence of data distortion.

This certificate renders our findings admissible as primary evidence in an Indian court of law."

---

### [09:00 – 10:00] Enterprise Defense Architecture & Concluding Takeaways
*(Speaker Cue: Click to Slide 10, energetic closing delivery)*

"Finally, on Slide 10, we answer the **Six Core Forensic Inquiries** and propose our **Three-Tiered Supply Chain Defense Architecture**:
1. **Tier 1 (SLSA Level 4 Build Security):** Mandate hermetic build environments and In-toto cryptographic attestations to ensure that compiled binaries match committed source code.
2. **Tier 2 (Hardware Security Modules):** Code signing keys must reside in FIPS 140-2 Level 3 HSMs with two-person quorum verification before signing release builds.
3. **Tier 3 (Zero Trust Protective DNS):** Network Management Systems must never have open outbound internet access. Implement DNS Response Policy Zones to block newly observed domains and terminate DNS tunneling.

To conclude: Group 10 has demonstrated that while SUNBURST weaponized trust, rigorous static forensics combined with Section 63 of the BSA 2023 provides the investigative foundation to detect, attribute, and legally prosecute advanced cyber adversaries.

Thank you. We also invite you to explore our interactive simulation model in [`docs/sunburst_simulation.html`](sunburst_simulation.html). We are now open for your questions."
