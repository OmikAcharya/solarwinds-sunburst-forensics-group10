# CAPSTONE PRESENTATION SCRIPT (10 MINUTES WORD-FOR-WORD)
### Project: SUNBURST Supply Chain Malware Forensics & Statutory Compliance Audit
**Academic Session:** 2026–2027 | TY B.Tech Computer Engineering  
**Course:** Digital Forensics & Cyber Security Laboratory (Capstone Evaluation - 20 Marks)  
**Institution:** KJ Somaiya School of Engineering, Somaiya Vidyavihar University, Mumbai  
**Group Number:** 10  

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
**Slides:** Slide 1 (Title), Slide 2 (Attack Overview), Slide 3 (Evidence Acquisition), Slide 4 (DiE Inspection)

---

### [00:00 – 00:45] Introduction & Case Study Significance
*(Speaker Cue: Stand upright, clear confident tone, click to Slide 1)*

"Respected evaluators, faculty members, and fellow engineers. Good morning. 

On behalf of Group 10 from the Department of Computer Engineering, KJ Somaiya School of Engineering, Somaiya Vidyavihar University, I, Amandeep Singh, along with my colleagues Omik Acharya and Om Lanke, welcome you to our capstone digital forensics defense titled: **'Forensic Dissection of the SUNBURST Supply Chain Intrusion: Static Triage, Reverse Engineering, and Indian Statutory Admissibility under BSA 2023.'**

In cybersecurity, the golden rule has always been: *'Trust your digitally signed software updates.'* But in late 2020, state-sponsored adversary UNC2452—widely attributed to APT29 or Nobelium—weaponized that very trust. Instead of attacking fortified perimeter firewalls, they compromised the automated build pipeline of SolarWinds, injecting a backdoor directly into their core network management DLL. Over 18,000 global enterprises, defense ministries, and critical infrastructure providers deployed this software voluntarily. Today, we present an end-to-end static forensic autopsy of that exact trojanized library."

---

### [00:45 – 01:40] Attack Vector & Evidence Chain of Custody
*(Speaker Cue: Transition to Slide 2 and Slide 3)*

"Please look at Slide 2. Unlike runtime memory injection or credential stuffing, SUNBURST was a pure **Software Supply Chain Compromise (MITRE ATT&CK T1195.002)**. The attackers deployed an internal dropper named SUNSPOT into the vendor's build environment. When an MSBuild compilation task triggered, SUNSPOT substituted a legitimate source file with `OrionImprovementBusinessLayer.cs` on the fly, compiled it, and restored the original file. The resulting DLL was legitimately signed with SolarWinds' valid DigiCert private certificate.

Moving to Slide 3: To ensure academic rigor and legal admissibility, we acquired the official compromised artifact, `SolarWinds.Orion.Core.BusinessLayer.dll`, measuring precisely 572,416 bytes. Following **ISO/IEC 27037 standards**, acquisition was conducted on an air-gapped workstation behind a Tableau hardware write-blocker. 

We independently calculated the cryptographic digests:
- SHA-256: `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
- MD5: `b91641a45351f013325d46b7972ba5e3`

These values match the CISA AA20-352A advisory bit-for-bit. Throughout our analysis, zero hash drift occurred."

---

### [01:40 – 03:20] PE Architecture & Detect It Easy (DiE) Triage
*(Speaker Cue: Click to Slide 4, point to the entropy table and Authenticode block)*

"To triage the binary without executing malicious code, we leveraged **Detect It Easy (DiE v3.10)**. 

The DiE scan reveals three crucial insights:
1. **Target Architecture & Runtime:** The file is a PE32 dynamic link library compiled for Intel 80386 systems running the `.NET Framework v4.0.30319` with the `COMIMAGE_FLAGS_ILONLY` flag asserted. The compiler identified is Microsoft Roslyn C# version 3.x.
2. **Entropy & Packer Absence:** Notice the entropy scores across the three PE sections:
   - `.text` code section: 6.21
   - `.rsrc` resource section: 7.14
   - `.reloc` relocation section: 0.11
   
   Many students ask: *'Why didn't the attackers pack the DLL with UPX or Themida?'* The answer is tradecraft. An packed binary produces an abnormal entropy above 7.8, triggering automated heuristic flags in corporate EDR systems. By keeping entropy at a natural 6.21, the backdoor blended seamlessly into benign software catalogs.
3. **Authenticode Integrity:** The security directory at RVA `0x0008B200` proves the digital signature was valid at distribution, issued to `SolarWinds Worldwide, LLC` by DigiCert. This is classic **Subversion of Trust Controls (T1553.002)**.

With the structural envelope established, I now invite our Reverse Engineering Specialist, Omik Acharya, to dissect the deobfuscated strings and behavioral mechanics."

---

## PART 2: OMIK ACHARYA (03:20 – 06:40)
**Role:** Reverse Engineer (FLOSS Deobfuscation & CAPA Attribution)  
**Slides:** Slide 5 (FLOSS Deobfuscation), Slide 6 (CAPA Attribution), Slide 7 (MITRE ATT&CK Matrix)

---

### [03:20 – 04:30] Static String Deobfuscation with Mandiant FLOSS
*(Speaker Cue: Step forward, display Slide 5, technical authoritative tone)*

"Thank you, Amandeep. Good morning everyone. I am Omik Acharya, and my focus was reverse engineering the internal evasion routines and network beacons of the backdoor.

When you open this binary in a standard disassembler, you see virtually zero plaintext indicators. The attackers implemented a custom cryptographic routine inside `OrionImprovementBusinessLayer.Zip` using a combination of byte subtraction, bitwise XOR, and Deflate decompression. 

To break this without dynamic instrumentation, we utilized **Mandiant FLOSS (FLARE Obfuscated String Solver v3.1.1)**. 

As shown on Slide 5, FLOSS extracted **346 unique strings**, uncovering the entire operational brain of SUNBURST:
1. **The Defensive Process Blacklist:** The malware actively hunts for 120+ analysis and monitoring utilities. But it doesn't store process names in plaintext. It calculates **64-bit FNV-1a hashes** of running processes and compares them against its hardcoded table. Recovered strings include: `sysmon.exe`, `wireshark.exe`, `processhacker.exe`, `x64dbg.exe`, `taniumclient.exe`, and `SentinelAgent.exe`.
2. **Evasion Drivers & Services:** It checks for the presence of `SysmonDrv`, `CylanceSvc`, and `CSFalconService`. If an endpoint detection agent is running, the backdoor terminates its own execution thread or suppresses C2 beacons.
3. **Internal Configuration Keys:** It queries `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid` to establish a persistent victim hardware identifier."

---

### [04:30 – 05:40] Behavioral Attribution & Mandiant CAPA
*(Speaker Cue: Click to Slide 6, highlight rule matches)*

"Now turning to Slide 6: How do we prove the malware's capabilities without running it? We executed **Mandiant CAPA v7.0.1**, an automated, rule-based capability detection engine.

CAPA identified three flagship capabilities that define the SUNBURST intrusion:
1. **Dormancy / Time-Based Evasion (T1497.003):** Inside function token `0x060012a4`, CAPA identified a hardcoded `Thread.Sleep` call set to 288 hours—which is **12 full days**, with a pseudo-random jitter extending up to **14 days**. By sleeping for two weeks after installation, SUNBURST outlasted automated sandbox analysis pipelines and virtual machine timeouts, which typically terminate execution after 5 to 10 minutes.
2. **DNS Tunneling Command & Control (T1071.004):** CAPA flagged the Domain Generation Algorithm (DGA) pointing to `avsvmcloud.com`. SUNBURST encoded the victim's domain name, MachineGuid, and status into base32/base64 subdomain labels. It sent iterative DNS queries, such as `appsync-api.eu-west-1.avsvmcloud.com`.
3. **Selective C2 Activation:** The C2 response arrived in the returned DNS CNAME or IPv4 A record. If the resolved IP fell into specific private or test blocks, the backdoor aborted. Only when a designated external C2 IP was returned did the malware download secondary in-memory stubs like TEARDROP."

---

### [05:40 – 06:40] MITRE ATT&CK Matrix Mapping
*(Speaker Cue: Click to Slide 7, walk through the tactical lifecycle)*

"Slide 7 consolidates our findings into the industry-standard **MITRE ATT&CK Enterprise Matrix**:
- **Initial Access:** T1195.002 — Supply Chain Compromise.
- **Execution:** T1059 / T1129 — Execution via legitimate host process `SolarWinds.BusinessLayerHost.exe`.
- **Defense Evasion:** T1497.003 (Time-based Evasion), T1562.001 (Impair Defenses via process termination), T1027 (Custom String Obfuscation), and T1553.002 (Authenticode Subversion).
- **Discovery:** T1082 (System Information Discovery) and T1057 (Process Discovery).
- **Command & Control:** T1071.004 (DNS Data Exfiltration) and T1568.002 (Domain Generation Algorithms).

In summary, our reverse engineering proved that SUNBURST was engineered from day one for extreme operational stealth. 

I now hand over to Om Lanke to analyze the legal ramifications under Indian law and explain the Section 63 BSA 2023 certification."

---

## PART 3: OM LANKE (06:40 – 10:00)
**Role:** Cyber Legal Auditor & Compliance Lead (IT Act, CERT-In, BSA 2023)  
**Slides:** Slide 8 (IT Act & CERT-In), Slide 9 (Section 63 BSA 2023), Slide 10 (Remediation & Defense)

---

### [06:40 – 07:50] Statutory Violations under Indian Cyber Jurisprudence
*(Speaker Cue: Confident legal authority tone, display Slide 8)*

"Thank you, Omik. Respected evaluators, technological analysis without legal context cannot support prosecution or enterprise compliance. As the Cyber Legal Auditor for Group 10, I mapped the SUNBURST incident across the legal architecture of India.

Please direct your attention to Slide 8. The intrusion triggers four distinct statutory violations under the **Information Technology Act, 2000**:
1. **Section 43(a), (b), and (c):** The unauthorized extraction of computer data, introduction of computer contaminants, and disruption of network processes create civil liability with uncapped compensation under Section 43A for failure to protect data.
2. **Section 66 (Computer Related Offences):** The intentional, fraudulent injection of malicious logic constitutes criminal hacking, punishable by up to 3 years imprisonment.
3. **Section 66F (Cyber Terrorism):** This is the most critical provision. SUNBURST targeted government ministries, atomic energy contractors, and critical information infrastructure. Under Section 66F(1)(B), introducing malicious code with intent to threaten the sovereignty or integrity of India or disrupt essential public services carries a statutory sentence of **Imprisonment for Life**.
4. **Section 70 (Protected Systems):** Unauthorized access to designated national infrastructure carries up to 10 years imprisonment.

Furthermore, under the **CERT-In Cyber Security Directions of 28 April 2022**, mandated by Section 70B(6), organizations experiencing supply chain compromises must formally notify CERT-In **within 6 hours**. Our team generated an official notification adhering strictly to this window."

---

### [07:50 – 09:00] Admissibility of Electronic Records: Section 63 BSA 2023
*(Speaker Cue: Click to Slide 9, highlight the dual Part A / Part B structure)*

"Moving to Slide 9: A historic transition occurred in Indian evidentiary law with the enactment of the **Bharatiya Sakshya Adhiniyam, 2023**, which repealed the Indian Evidence Act, 1872. 

Many practitioners still cite Section 65B of the old Act. However, today, electronic evidence must satisfy **Section 63 of the Bharatiya Sakshya Adhiniyam, 2023**.

Under Section 63(2), four strict conditions must be proven:
1. The computer system was regularly used to store or process electronic records.
2. Data was supplied in the ordinary course of regular activities.
3. The computer was operating properly throughout the period without operational distortion.
4. The output is an accurate, unadulterated reproduction of the stored data.

To satisfy Section 63(4), Group 10 developed an automated Python utility (`generate_bsa_cert.py`) that produces an admissible certificate with a dual-signatory structure:
- **Part A:** Executed by Amandeep Singh as the **Lawful Custodian**, confirming physical and logical custody, workstation telemetry, and write-blocked preservation.
- **Part B:** Executed jointly by Omik Acharya and myself as **Cyber Forensic Experts**, certifying cryptographic hash equality (SHA-256 / MD5 under NIST FIPS 180-4), deterministic tool outputs, and complete absence of tampering.

This certificate establishes the artifact as substantive primary evidence in any Indian court."

---

### [09:00 – 10:00] Enterprise Remediation & Concluding Assessment
*(Speaker Cue: Click to Slide 10, wrap up with punchy delivery)*

"Finally, on Slide 10, we present our **Three-Tiered Defense Architecture** to eliminate supply chain blindness:
1. **Tier 1 (SLSA Level 4 Build Security):** Mandate hermetic build environments and In-toto cryptographic attestations to prove that compiled binaries match committed source code.
2. **Tier 2 (Hardware Security Modules):** Code signing keys must be locked in FIPS 140-2 Level 3 HSMs, requiring multi-party authorization before any release package is signed.
3. **Tier 3 (Zero Trust Protective DNS):** Network Management Systems must never have open outbound internet access. Implement DNS Response Policy Zones to block newly observed domains and terminate DNS tunneling.

To conclude: Group 10 has demonstrated that while SUNBURST weaponized trust, rigorous digital forensics combined with precise statutory compliance under Section 63 of the BSA 2023 provides the investigative foundation to detect, attribute, and legally prosecute advanced cyber adversaries.

Thank you. We are now open for your questions."
