#!/usr/bin/env python3
"""
build_demo_docs.py
Generates two comprehensive, professionally formatted Microsoft Word (.docx) documents:
1. docs/Presentation_Speaking_Script.docx (10-minute presentation speaking script)
2. docs/Tool_Execution_and_Demo_Manual.docx (tool runbook, commands, choreography)

Synchronized with:
- docs/SUNBURST_Forensic_Investigation_Group10.pptx (12-slide Somaiya template deck)
- docs/sunburst_simulation.html (interactive 11-stage standalone simulation)
- scripts/run_forensics.py & scripts/generate_bsa_cert.py

Team Roster:
- Amandeep Singh (Roll: 16010123036) — Lead Forensic Investigator
- Omik Acharya (Roll: 16010123218) — Reverse Engineer
- Om Lanke (Roll: 16010123216) — Technical & Cyber Legal Auditor

Department of Computer Engineering, K.J. Somaiya School of Engineering
Somaiya Vidyavihar University, Mumbai.
"""

import os
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal cell padding."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_callout_box(doc, title, text, bg_hex="F0F4F8", border_hex="A71930"):
    """Adds a stylish callout box with a colored border and background."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    cell = table.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"📌 {title}\n")
    run_t.bold = True
    run_t.font.name = "Arial"
    run_t.font.size = Pt(11)
    run_t.font.color.rgb = RGBColor(167, 25, 48)  # Somaiya Red

    run_body = p.add_run(text)
    run_body.font.name = "Arial"
    run_body.font.size = Pt(9.5)
    run_body.font.color.rgb = RGBColor(50, 50, 50)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)


def format_table_headers(table, col_widths, bg_hex="A71930"):
    """Styles the header row of a table with Somaiya Red."""
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(hdr_cells):
        set_cell_background(title, bg_hex)
        set_cell_margins(title, top=120, bottom=120, left=120, right=120)
        p = title.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.bold = True
            run.font.name = "Arial"
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(255, 255, 255)

    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = Inches(w)


def build_script_document(output_path):
    """Builds Document 1: End-to-End Presentation Speaking Script."""
    doc = Document()

    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Title Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    t_run = title_p.add_run("K.J. SOMAIYA SCHOOL OF ENGINEERING\nDEPARTMENT OF COMPUTER ENGINEERING")
    t_run.bold = True
    t_run.font.name = "Arial"
    t_run.font.size = Pt(12)
    t_run.font.color.rgb = RGBColor(100, 100, 100)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    sub_run = sub_p.add_run(
        "Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)\n"
        "Operation SUNBURST Investigation: End-to-End 10-Minute Speaking Script | Group 10"
    )
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(10)
    sub_run.font.color.rgb = RGBColor(120, 120, 120)

    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_after = Pt(14)
    h1_run = h1.add_run("OPERATION SUNBURST DFIR: SYNCHRONIZED PRESENTATION SCRIPT")
    h1_run.bold = True
    h1_run.font.name = "Arial"
    h1_run.font.size = Pt(18)
    h1_run.font.color.rgb = RGBColor(167, 25, 48)

    add_callout_box(
        doc,
        "DUAL PRESENTATION & TIMING STRATEGY",
        "Total Target Duration: Exactly 10 Minutes (~3 to 3.5 minutes per speaker).\n"
        "• Part 1: Amandeep Singh (0:00 – 3:00) — Slides 1-4: Intro, Attack Vector, Evidence Hash Check, DiE PE Triage.\n"
        "• Part 2: Omik Acharya (3:00 – 6:00) — Slides 5-8: Attack Timeline, String Deobfuscation (Deflate), FNV-1a Hashed Blacklist, CAPA.\n"
        "• Part 3: Om Lanke (6:00 – 10:00) — Slides 9-12: Indian Cyber Law, Section 63 BSA 2023 Certificate, Pytest CI Run, Findings & Q&A.\n\n"
        "🖥️ SIDE-BY-SIDE SYNCHRONIZATION: The PowerPoint presentation covers the Case Study and Threat Theory. "
        "The side-by-side display runs the interactive simulation (sunburst_simulation.html), terminal tools, and forensic code."
    )

    # Roster Table
    doc.add_heading("Team Member Roster & Responsibilities", level=2)
    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [1.4, 1.2, 2.4, 1.8]

    headers = ["Speaker Name", "Roll Number", "Forensic Specialization", "Assigned Speaking Time & Slides"]
    for i, h in enumerate(headers):
        table.rows[0].cells[i].paragraphs[0].text = h

    roster_data = [
        ("Amandeep Singh", "16010123036", "Lead Investigator: PE Triage & Hash Baseline", "0:00 – 3:00 (Slides 1 to 4)"),
        ("Omik Acharya", "16010123218", "Reverse Engineer: FLOSS & CAPA Attribution", "3:00 – 6:00 (Slides 5 to 8)"),
        ("Om Lanke", "16010123216", "Technical & Cyber Legal Auditor: BSA & CI/CD", "6:00 – 10:00 (Slides 9 to 12)")
    ]
    for row_idx, data in enumerate(roster_data, start=1):
        for col_idx, val in enumerate(data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Arial"
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

    format_table_headers(table, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==================== PART 1 ====================
    doc.add_heading("PART 1: AMANDEEP SINGH (0:00 – 3:00 | SLIDES 1 TO 4)", level=2)
    doc.add_paragraph("Role: Lead Forensic Investigator | Specialization: PE Header Triage, Supply Chain Infiltration & Cryptographic Verification").runs[0].bold = True

    p1_cues = doc.add_paragraph()
    p1_cues.add_run("🎬 SCREEN ACTIONS & CUES FOR AMANDEEP SINGH:\n").bold = True
    p1_cues.add_run(
        "1. Start with Slide 1 (Title Slide) on PPT. In side window, have Chrome ready on 'docs/sunburst_simulation.html'.\n"
        "2. Advance PPT to Slide 2 (Supply Chain Vector) -> In browser, show Stage 1 (The Attack diagram).\n"
        "3. Advance PPT to Slide 3 (Evidence Ingestion) -> Switch to Terminal and run: 'bash scripts/verify_hashes.sh'.\n"
        "4. Advance PPT to Slide 4 (Detect It Easy) -> In browser, click 'Stage 4: Detect It Easy' and show the beam scan and entropy curve.\n"
        "5. Advance PPT to Slide 5 (Attack Lifecycle) -> Introduce the 8 stages and hand over to Omik Acharya."
    )
    p1_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Word-for-Word Spoken Dialogue:", level=3)
    p1_script = doc.add_paragraph()
    p1_script.paragraph_format.line_spacing = 1.25
    p1_script.add_run(
        "“Respected professors, external evaluators, and colleagues. Good morning. We are Group 10 from the Department of "
        "Computer Engineering at K.J. Somaiya School of Engineering, Somaiya Vidyavihar University. Welcome to our Capstone "
        "Forensic Investigation on Operation SUNBURST: The SolarWinds Supply Chain Attack.\n\n"
        "[PPT: Slide 1 — Title Slide]\n"
        "I am Amandeep Singh, Roll Number 16010123036, serving as the Lead Forensic Investigator. With me are my co-investigators: "
        "Omik Acharya (Roll 16010123218), who led our Reverse Engineering and Deobfuscation efforts, and Om Lanke (Roll 16010123216), "
        "who conducted our Technical Audit, Indian Statutory Compliance, and CI/CD Verification.\n\n"
        "Our presentation operates on a dual-synchronization model: our slides cover the threat architecture and case study findings, "
        "while our side-by-side screen demonstrates the actual forensic tools, terminal scripts, and interactive simulation in real time.\n\n"
        "[PPT: Advance to Slide 2 — The Supply Chain Vector | Side-by-Side: Browser Stage 1 (The Attack)]\n"
        "Operation SUNBURST represents the watershed supply chain intrusion of the modern cyber era. Attributed by CISA to APT29 "
        "(Nobelium), the attackers did not breach customer perimeter defenses directly. Instead, they compromised the internal MSBuild "
        "software development pipeline of SolarWinds. By deploying an in-memory injection tool named SUNSPOT, they dynamically modified "
        "the source code of the core monitoring component: SolarWinds.Orion.Core.BusinessLayer.dll.\n\n"
        "Crucially, because this tampering occurred during compilation, the resulting trojanized DLL received a legitimate Authenticode "
        "digital signature from DigiCert. SolarWinds signed the binary, packaged it into official Orion software updates v2019.4 through "
        "v2020.2.1, and distributed it downstream to over 18,000 public and private organizations worldwide, including the U.S. Treasury, "
        "Department of Homeland Security, and critical infrastructure providers.\n\n"
        "[PPT: Advance to Slide 3 — ISO/IEC 27037 Evidence Ingestion | Side-by-Side: Terminal — bash scripts/verify_hashes.sh]\n"
        "In digital forensics, maintaining evidence integrity is sacred. Under ISO/IEC 27037:2012 guidelines, evidence must be verifiable, "
        "repeatable, and non-destructive. As you can see live on our terminal, we execute our verification script: 'bash scripts/verify_hashes.sh'.\n"
        "The script verifies both our primary malware sample ending in '...7cf0d25' and our benchmark sample ending in '...17226d7e'. "
        "The terminal outputs an immediate green [PASS]. This proves bit-for-bit mathematical equality with the official CISA and FireEye "
        "forensic manifests, guaranteeing zero bitwise tampering before any analysis took place.\n\n"
        "[PPT: Advance to Slide 4 — Static PE Architecture & Shannon Entropy | Side-by-Side: Browser Stage 4 (Detect It Easy)]\n"
        "Next, we conducted static PE header triage using Detect It Easy (DiE v3.10). Observe the live visualizer on screen:\n"
        "1. Architecture: The malware is a 32-bit PE dynamic link library for Intel 80386 running under the Microsoft .NET CLR v4.0.30319, "
        "compiled with Roslyn C# in Visual Studio 2019.\n"
        "2. Section Entropy: Notice our Shannon entropy curve across the sections: the code section (.text) measures 6.21, embedded resources "
        "(.rsrc) measure 7.14, and relocation (.reloc) measures 0.11. The overall entropy is 5.9.\n"
        "This is an extraordinary finding. Normal packed malware exhibits entropy exceeding 7.5. The attackers deliberately refrained from using "
        "UPX or commercial packers so that standard antivirus heuristic engines would evaluate the file as completely benign.\n"
        "3. Authenticode Signature: DiE confirms a valid digital signature issued to SolarWinds Worldwide, LLC by DigiCert. This is classic "
        "Subversion of Trust Controls (MITRE ATT&CK T1553.002).\n\n"
        "[PPT: Advance to Slide 5 — Attack Execution Timeline]\n"
        "On Slide 5, we reconstruct the complete 8-stage execution lifecycle of the backdoor. I now hand over to our Reverse Engineer, "
        "Omik Acharya, to dissect how we deobfuscated their encrypted strings and anti-analysis mechanisms.”"
    )
    doc.add_page_break()

    # ==================== PART 2 ====================
    doc.add_heading("PART 2: OMIK ACHARYA (3:00 – 6:00 | SLIDES 5 TO 8)", level=2)
    doc.add_paragraph("Role: Reverse Engineer | Specialization: String Deobfuscation (Deflate), 64-Bit FNV-1a Hashing & CAPA Attribution").runs[0].bold = True

    p2_cues = doc.add_paragraph()
    p2_cues.add_run("🎬 SCREEN ACTIONS & CUES FOR OMIK ACHARYA:\n").bold = True
    p2_cues.add_run(
        "1. Keep PPT on Slide 5 (8-Stage Lifecycle) for 30s to summarize the state machine.\n"
        "2. Advance PPT to Slide 6 (String Deobfuscation) -> Switch to Terminal: 'floss --version' -> In browser, click 'Decode all' live in Stage 5.\n"
        "3. Advance PPT to Slide 7 (Anti-Analysis FNV-1a) -> In browser Stage 6, click 'wireshark' -> 'Run the check'. "
        "Then switch to Terminal and run: 'python3 scripts/run_forensics.py --check-process wireshark'.\n"
        "4. Advance PPT to Slide 8 (CAPA Capabilities) -> In Terminal, run: 'capa --version' and "
        "'python3 scripts/run_forensics.py --simulate --simulate-behavior victim'."
    )
    p2_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Word-for-Word Spoken Dialogue:", level=3)
    p2_script = doc.add_paragraph()
    p2_script.paragraph_format.line_spacing = 1.25
    p2_script.add_run(
        "“Thank you, Amandeep. Respected evaluators, I am Omik Acharya, Roll Number 16010123218, serving as Reverse Engineer for Group 10.\n\n"
        "[PPT: Slide 5 — 8-Stage Lifecycle Overview]\n"
        "As outlined on Slide 5, SUNBURST's internal logic operates as an 8-stage state machine: initiating upon service startup, "
        "entering a 14-day dormancy timer, executing defensive process checks, hashing the victim host, generating domain names, "
        "tunneling covert DNS queries, dropping second-stage loaders, and establishing persistent interactive C2.\n\n"
        "[PPT: Advance to Slide 6 — String Encryption | Side-by-Side: Terminal 'floss --version' -> Browser Stage 5 (FLOSS strings)]\n"
        "To investigate this logic, we applied Mandiant FLOSS (v3.1.1). As verified in our terminal, FLOSS is installed natively. "
        "Standard forensic string utilities failed completely because the malware authors encrypted every critical string using a two-stage mechanism: "
        "Base64 encoding followed by raw Deflate decompression (wbits = -15, which strips the standard zlib header).\n\n"
        "[Side-by-Side: Click 'Decode all' button in Browser Stage 5]\n"
        "Watch our browser simulation decode these tokens live in real time:\n"
        "• The ciphertext 'SywrLstNzskvTdFLzs8FAA==' immediately inflates to 'avsvmcloud.com' — the primary command-and-control apex domain.\n"
        "• The token 'C/Z3Cwl3DHKN8c1ML...' inflates to 'SOFTWARE\\Microsoft\\Cryptography', the registry hive queried to read the victim's MachineGuid.\n"
        "• The token '801MzsjMS3UvzUwBAA==' yields 'MachineGuid', confirming host fingerprinting.\n"
        "• The token 'SyzI1CvOz0ksKs/MSynWS87PBQA=' reveals 'api.solarwinds.com' — a benign canary used to verify active internet connectivity.\n\n"
        "[PPT: Advance to Slide 7 — Anti-Analysis & Defense Evasion | Side-by-Side: Browser Stage 6 (Hidden blocklist)]\n"
        "On Slide 7, we address how SUNBURST evaded detection by security analysts. If the binary had contained plaintext strings like "
        "'wireshark', 'procmon', or 'x64dbg', endpoint detection and response (EDR) rules would have flagged it immediately. "
        "Instead, the authors engineered a mathematical evasion routine:\n"
        "First, convert the running process name to lowercase.\n"
        "Second, compute its 64-bit Fowler-Noll-Vo 1a (FNV-1a) hash using offset basis 0xcbf29ce484222325 and prime 0x100000001b3.\n"
        "Third, XOR the resulting 64-bit digest with the hardcoded magic constant: 0x5BAC903BA7D81967.\n\n"
        "[Side-by-Side: In Browser Stage 6, click 'wireshark' -> 'Run the check' | Switch to Terminal]\n"
        "In our simulation and terminal, we run: 'python3 scripts/run_forensics.py --check-process wireshark'.\n"
        "The terminal computes the hash '0xa84ff6500970f54d', XORs it, and produces the exact decimal value 17574002783607647274, confirming a direct hit "
        "against the malware's hardcoded blocklist of over 120 security utilities. If any of these tools are running, SUNBURST permanently self-terminates.\n\n"
        "[PPT: Advance to Slide 8 — Capability Mapping | Side-by-Side: Terminal — capa --version && python3 scripts/run_forensics.py --simulate]\n"
        "Finally, we analyzed the binary using Mandiant CAPA (v9.4.0) to map capabilities directly to the MITRE ATT&CK framework:\n"
        "• T1497.003 (Time-Based Sandbox Evasion): A hardcoded Thread.Sleep interval of 288 to 336 hours (12 to 14 days) to outlast automated sandboxes.\n"
        "• T1071.004 (DNS C2 Tunneling): Covert DNS query encoding transmitting host telemetry within subdomains of avsvmcloud.com.\n"
        "• T1562.001 (Impair Defenses): Automated enumeration and suppression of security processes.\n"
        "• T1082 (System Information Discovery): Querying network configurations and system GUIDs.\n\n"
        "I now pass the floor to Om Lanke, our Technical & Cyber Legal Auditor, to present our statutory compliance under Indian law and automated CI/CD pipeline.”"
    )
    doc.add_page_break()

    # ==================== PART 3 ====================
    doc.add_heading("PART 3: OM LANKE (6:00 – 10:00 | SLIDES 9 TO 12)", level=2)
    doc.add_paragraph("Role: Technical & Cyber Legal Auditor | Specialization: IT Act 2000, CERT-In Directions 2022, Section 63 BSA 2023 & Pytest CI").runs[0].bold = True

    p3_cues = doc.add_paragraph()
    p3_cues.add_run("🎬 SCREEN ACTIONS & CUES FOR OM LANKE:\n").bold = True
    p3_cues.add_run(
        "1. Advance PPT to Slide 9 (Indian Cyber Legal Framework) -> In browser, show Stage 10 ('Indian law mapping') and click finding buttons.\n"
        "2. Advance PPT to Slide 10 (BSA 2023 Section 63) -> Switch to Terminal and run: 'python3 scripts/generate_bsa_cert.py --format both'. "
        "Show 'legal_compliance/Section_63_BSA_Certificate.md' in VS Code highlighting Part A & Part B.\n"
        "3. Advance PPT to Slide 11 (CI/CD Pipeline) -> Switch to Terminal and run: 'pytest tests/ -v'. Show all 22 tests passing.\n"
        "4. Advance PPT to Slide 12 (Conclusion & Q&A) -> In browser, click Stage 11 ('Conclusion') showing 6 green checkmarks, conclude, and open for Q&A."
    )
    p3_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Word-for-Word Spoken Dialogue:", level=3)
    p3_script = doc.add_paragraph()
    p3_script.paragraph_format.line_spacing = 1.25
    p3_script.add_run(
        "“Thank you, Omik. Respected evaluators, I am Om Lanke, Roll Number 16010123216, serving as the Technical & Cyber Legal Auditor for Group 10.\n\n"
        "[PPT: Slide 9 — Indian Statutory Cyber Law Framework | Side-by-Side: Browser Stage 10 (Indian law mapping)]\n"
        "A forensic investigation cannot conclude at technical disassembly; it must establish culpability and admissibility under statutory law. "
        "On Slide 9 and in our browser simulation, we map SUNBURST's technical behaviors directly to Indian cyber jurisprudence:\n"
        "1. Information Technology Act, 2000:\n"
        "   • Section 43 & 66: Unauthorized access, data extraction (MachineGuid), and introducing computer contaminants (penalties include damages and up to 3 years imprisonment).\n"
        "   • Section 66F (Cyber Terrorism): SUNBURST targeted government ministries and critical communications infrastructure. Introducing malicious code "
        "with intent to threaten national sovereignty or critical infrastructure carries a mandatory sentence of Imprisonment for Life.\n"
        "   • Section 70: Unauthorized access to declared Protected Systems (up to 10 years imprisonment).\n"
        "   • Section 43A: Entities deploying unverified third-party vendor updates without adequate due diligence face uncapped civil compensation for negligence.\n"
        "2. CERT-In Directions (28 April 2022):\n"
        "   • Mandatory 6-Hour Reporting Window: Under Annexure I Category 2, organizations must notify CERT-In within 6 hours of identifying a supply chain intrusion. "
        "We have drafted an official incident notification template in legal_compliance/CERT_In_Incident_Notification_Template.md.\n"
        "   • 180-Day Log Retention: Direction 20(3) mandates ICT service providers maintain system and network logs for 180 days within Indian jurisdiction.\n"
        "3. Digital Personal Data Protection (DPDP) Act, 2023: Section 8(5) & 8(6) mandate formal breach notification to the Data Protection Board of India.\n\n"
        "[PPT: Advance to Slide 10 — Legal Admissibility & Section 63 BSA 2023 | Side-by-Side: Terminal — python3 scripts/generate_bsa_cert.py --format both]\n"
        "Now, how is digital evidence legally admitted before an Indian court? With the enactment of the Bharatiya Sakshya Adhiniyam, 2023, "
        "the Indian Evidence Act, 1872 was repealed. The traditional Section 65B certificate is now legally obsolete.\n\n"
        "Under Section 63 of the BSA 2023, admissibility of electronic records requires a rigorous two-part statutory certificate:\n"
        "[Side-by-Side: Open legal_compliance/Section_63_BSA_Certificate.md in VS Code]\n"
        "As generated live by our script, observe the certificate structure:\n"
        "• Part A (Custodian Affirmation): Executed by Amandeep Singh, certifying workstation MAC address, hardware write-blocking, and lawful custody under ISO/IEC 27037.\n"
        "• Part B (Forensic Expert Affirmation): Executed jointly by Omik Acharya and myself, affirming cryptographic hash equality under NIST FIPS 180-4 and the scientific validity of our toolchain.\n"
        "Notice that our script dynamically binds the certificate to the physical hardware by embedding the machine MAC address, kernel release, and NTP timestamp. "
        "This satisfies Section 105 of the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023, rendering our forensic evidence fully admissible as substantive primary evidence.\n\n"
        "[PPT: Advance to Slide 11 — CI/CD Automation & Verification | Side-by-Side: Terminal — pytest tests/ -v]\n"
        "To guarantee that our findings are mathematically reproducible across any forensic workstation, we constructed an automated CI/CD pipeline "
        "using Astral uv and GitHub Actions. Look at our terminal as we run: 'pytest tests/ -v'.\n"
        "In just 0.20 seconds, all 22 unit test assertions execute and pass green across 6 test suites: cryptographic integrity, raw Deflate inflation, "
        "FNV-1a 64-bit hashing math, CAPA capability parsing, telemetry extraction, and legal certificate generation.\n\n"
        "[PPT: Advance to Slide 12 — Conclusion & Findings Matrix | Side-by-Side: Browser Stage 11 (Conclusion)]\n"
        "In conclusion, on Slide 12 and in Stage 11 of our simulation, Group 10 has definitively resolved all six core capstone questions:\n"
        "1. Authenticity: Legitimate DLL trojanized in the build pipeline with valid DigiCert signature.\n"
        "2. Strings: 100% decrypted via Base64 and raw Deflate (wbits=-15).\n"
        "3. Anti-Analysis: 120+ tools checked via 64-bit FNV-1a hashing + XOR mask, maintaining benign entropy (5.9).\n"
        "4. Network C2: Covert DNS DGA tunneling via avsvmcloud.com.\n"
        "5. Indian Law: Fully actionable under IT Act Sec 66F, CERT-In 6-hour directive, and certified under BSA 2023 Section 63.\n"
        "6. Verification: 100% automated regression test coverage via CI/CD.\n\n"
        "We thank our professors and evaluators for their time and guidance. Group 10 is now open for your questions.”"
    )
    doc.add_page_break()

    # ==================== Q&A SECTION ====================
    doc.add_heading("EVALUATOR Q&A CHEAT-SHEET (Top 6 Questions & Bulletproof Answers)", level=2)

    qa_list = [
        ("Q1: Why did you not execute the malware in a dynamic sandbox?",
         "Answer: SUNBURST contains a hardcoded 12 to 14 day dormancy timer (MITRE ATT&CK T1497.003) and checks for sandbox hooks. A standard 5-minute dynamic "
         "detonation reveals zero network activity or execution. Static analysis using DiE, FLOSS, and CAPA allowed us to reverse-engineer 100% of the malware's "
         "logic safely without risking host compromise, C2 telemetry leakage, or sandbox evasion triggers."),

        ("Q2: What is the exact difference between Section 65B of IEA 1872 and Section 63 of BSA 2023?",
         "Answer: The Bharatiya Sakshya Adhiniyam, 2023 repealed the Indian Evidence Act, 1872. Section 63 BSA modernizes electronic evidence admissibility. "
         "It introduces explicit statutory recognition for distributed storage, virtual environments, and cloud computing, and establishes a mandatory "
         "dual-certification structure: Part A by the Custodian proving lawful management and operational integrity, and Part B by the Technical Expert "
         "certifying cryptographic hash equality and the absence of tampering."),

        ("Q3: Why did the attackers XOR the FNV-1a hash with 0x5BAC903BA7D81967?",
         "Answer: Plain FNV-1a hashes of common process names can be reversed using precomputed rainbow tables. XORing the 64-bit digest with a secret hardcoded "
         "constant added a secondary obfuscation layer, preventing security researchers from identifying which forensic tools were targeted without decompiling "
         "the specific MSIL comparison routine."),

        ("Q4: How did the malware achieve persistence without setting normal Windows Run registry keys?",
         "Answer: SUNBURST achieved persistence via DLL component hijacking (T1574.002). Because it was embedded inside the core SolarWinds Orion Business "
         "Layer DLL, it executed automatically every time the legitimate Windows service 'SolarWinds.BusinessLayerHost.exe' started, avoiding suspicious registry Run keys."),

        ("Q5: What are the mandatory reporting deadlines under CERT-In Directions 2022?",
         "Answer: Under Direction 5(i) of the 28 April 2022 Directions, any supply chain or critical system compromise must be reported to CERT-In within "
         "6 hours of detection. Under Direction 20(3), all system and network logs must be maintained within Indian jurisdiction for 180 days."),

        ("Q6: How does the BSA 2023 Certificate bind evidence to the physical workstation?",
         "Answer: Our automated generator (scripts/generate_bsa_cert.py) queries the local network interface for its physical MAC address, reads the host kernel release, "
         "captures CPU architecture, and queries the system NTP clock. This physical telemetry is permanently written into the affidavit alongside the SHA-256 digests.")
    ]

    for q, a in qa_list:
        p_q = doc.add_paragraph()
        p_q.add_run(q + "\n").bold = True
        p_q.runs[0].font.color.rgb = RGBColor(167, 25, 48)
        p_a = p_q.add_run(a)
        p_a.font.size = Pt(9.5)
        p_q.paragraph_format.space_after = Pt(8)

    doc.save(output_path)
    print(f"[+] Successfully generated Document 1: {output_path}")


def build_manual_document(output_path):
    """Builds Document 2: Step-by-Step Tool Execution & Command Runbook."""
    doc = Document()

    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Title Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    t_run = title_p.add_run("K.J. SOMAIYA SCHOOL OF ENGINEERING\nDEPARTMENT OF COMPUTER ENGINEERING")
    t_run.bold = True
    t_run.font.name = "Arial"
    t_run.font.size = Pt(12)
    t_run.font.color.rgb = RGBColor(100, 100, 100)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    sub_run = sub_p.add_run(
        "Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)\n"
        "Technical Demonstration Runbook & Tool Execution Manual | Group 10"
    )
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(10)
    sub_run.font.color.rgb = RGBColor(120, 120, 120)

    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_after = Pt(14)
    h1_run = h1.add_run("SUNBURST DFIR CAPSTONE: TOOL EXECUTION & DEMO MANUAL")
    h1_run.bold = True
    h1_run.font.name = "Arial"
    h1_run.font.size = Pt(18)
    h1_run.font.color.rgb = RGBColor(167, 25, 48)

    add_callout_box(
        doc,
        "DEMO OPERATIONAL GOAL & SYNCHRONIZATION",
        "This manual details the exact sequence of PowerPoint slides, terminal commands, browser actions, and screen switches "
        "required to deliver a flawless, bug-free capstone demonstration. Follow this choreography precisely during recording or live viva presentation."
    )

    # Section 1: Pre-Demo Setup
    doc.add_heading("1. Pre-Demo Environment Checklist (2 Minutes Before Start)", level=2)
    doc.add_paragraph(
        "Ensure the following 4 applications are open and arranged across your workspace:\n\n"
        "• WINDOW 1 (PowerPoint Presentation):\n"
        "  Open docs/SUNBURST_Forensic_Investigation_Group10.pptx in Slide Show mode (Slide 1 ready).\n\n"
        "• WINDOW 2 (Web Browser — Google Chrome or Safari):\n"
        "  Open the interactive simulation model by navigating to:\n"
        "  file:///Users/mac/Developer/csfcl/docs/sunburst_simulation.html\n"
        "  (Tip: Launch directly from terminal using: open docs/sunburst_simulation.html)\n\n"
        "• WINDOW 3 (Terminal):\n"
        "  Open Terminal in your repository directory and activate the virtual environment:\n"
        "  cd /Users/mac/Developer/csfcl\n"
        "  source .venv/bin/activate\n\n"
        "• WINDOW 4 (VS Code / File Editor):\n"
        "  Open the project workspace in VS Code with legal_compliance/Section_63_BSA_Certificate.md ready to view."
    )

    # Section 2: Choreography Table
    doc.add_heading("2. Chronological Demo Choreography (Second-by-Second Runbook)", level=2)

    table = doc.add_table(rows=12, cols=6)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [0.7, 1.1, 1.2, 1.3, 1.7, 1.2]

    headers = ["Time", "Speaker", "PPT Slide", "Screen / Window", "Action / Exact Command Line", "Expected Visual Result"]
    for i, h in enumerate(headers):
        table.rows[0].cells[i].paragraphs[0].text = h

    choreography_data = [
        ("0:00", "Amandeep", "Slide 1 (Title)", "PPT Window", "Introduce Group 10 and Capstone Topic", "Somaiya title slide with student roster."),
        ("0:45", "Amandeep", "Slide 2 (Vector)", "Browser (Stage 1)", "Display 'The Attack' animated diagram", "Shows APT29 supply chain compromise of 18,000 victims."),
        ("1:30", "Amandeep", "Slide 3 (Evidence)", "Terminal", "bash scripts/verify_hashes.sh", "Green PASS output; SHA-256 baseline verified under ISO 27037."),
        ("2:15", "Amandeep", "Slide 4 (DiE Triage)", "Browser (Stage 4)", "Click 'Stage 4: Detect It Easy'", "PE section map scan beam, Roslyn C#, entropy staying at 6.21."),
        ("3:00", "Omik", "Slide 5 (Lifecycle)", "PPT Window", "Explain 8-stage state machine", "Visual diagram of 8-stage attack lifecycle."),
        ("3:30", "Omik", "Slide 6 (Strings)", "Terminal & Browser", "floss --version -> Click 'Decode all' live", "Mandiant FLOSS v3.1.1 verified; avsvmcloud.com decompressed."),
        ("4:15", "Omik", "Slide 7 (FNV Evasion)", "Browser (Stage 6)", "Click 'wireshark' -> 'Run the check'", "Animated 5-box pipeline showing FNV-1a 64-bit + XOR match."),
        ("4:45", "Omik", "Slide 7 (FNV Evasion)", "Terminal", "python3 scripts/run_forensics.py --check-process wireshark", "Terminal calculates 0xa84ff6500970f54d and confirms blacklist match."),
        ("5:15", "Omik", "Slide 8 (CAPA Rules)", "Terminal", "python3 scripts/run_forensics.py --simulate --simulate-behavior victim", "Terminal prints rich table with 14 MITRE ATT&CK techniques."),
        ("6:00", "Om", "Slide 9 (Cyber Law)", "Browser (Stage 10)", "Click finding buttons in 'Indian law mapping'", "Interactive buttons light up IT Act, CERT-In, and DPDP."),
        ("7:00", "Om", "Slide 10 (BSA 2023)", "Terminal & VS Code", "python3 scripts/generate_bsa_cert.py --format both", "Generates Section 63 BSA certificate embedding MAC & telemetry."),
    ]

    for row_idx, data in enumerate(choreography_data, start=1):
        for col_idx, val in enumerate(data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Arial"
            cell.paragraphs[0].runs[0].font.size = Pt(8)
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)

    format_table_headers(table, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 3: Deep Dive per Tool
    doc.add_heading("3. Tool-by-Tool Detailed Technical Reference", level=2)

    # Tool 1
    doc.add_heading("TOOL 1: Detect It Easy (DiE v3.10)", level=3)
    doc.add_paragraph(
        "• Purpose: Static identification of PE32 binary architecture, compiler signatures, digital certificates, and section entropy.\n"
        "• Primary Presenter: Amandeep Singh (Lead Investigator)\n"
        "• Key Metrics to Highlight to Evaluator:\n"
        "  - Format: PE32 console DLL for Intel 80386.\n"
        "  - Runtime: Microsoft .NET Framework v4.0.30319 (COMIMAGE_FLAGS_ILONLY).\n"
        "  - Compiler: Microsoft Roslyn C# (Visual Studio 2019).\n"
        "  - Section Entropy: .text (6.21), .rsrc (7.14), .reloc (0.11). Overall entropy: ~5.9.\n"
        "  - Core Takeaway: Stays strictly below 7.5 packed threshold. The malware avoided UPX/Themida packers to blend into benign software.\n"
        "  - Digital Signature: Valid Authenticode signature issued by DigiCert to SolarWinds Worldwide, LLC (Serial: 0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e).\n"
        "• File Location: outputs/die_inspection.txt"
    )

    # Tool 2
    doc.add_heading("TOOL 2: Mandiant FLOSS & Raw Deflate Decompressor", level=3)
    doc.add_paragraph(
        "• Purpose: Extraction of static, stack, and tight strings; automated decompression of obfuscated configuration tokens.\n"
        "• Primary Presenter: Omik Acharya (Reverse Engineer)\n"
        "• Terminal Verification Command:\n"
        "  floss --version\n"
        "• Exact Decompressed Indicator Tokens:\n"
        "  1. SywrLstNzskvTdFLzs8FAA==                      -> avsvmcloud.com (C2 Domain Apex)\n"
        "  2. C/Z3Cwl3DHKN8c1MLsovzk8riXEuqiwoyU8vSizIqAQA  -> SOFTWARE\\Microsoft\\Cryptography\n"
        "  3. 801MzsjMS3UvzUwBAA==                          -> MachineGuid (Victim Hardware ID)\n"
        "  4. C07NSU0uUdBScCvKz1UIz8wzNor3Sy0pzy/KdkxJL... -> Select * From Win32_NetworkAdapterConfiguration\n"
        "  5. C0otyC8qCU8sSc5ILQpKLSmqBAA=                  -> ReportWatcherRetry\n"
        "  6. SyzI1CvOz0ksKs/MSynWS87PBQA=                  -> api.solarwinds.com (Connectivity Canary)\n"
        "  7. C44MDnH1jXEuLSpKzStxzs8rKcrPCU4tiSlOLSrLTE4tBgA= -> SYSTEM\\CurrentControlSet\\services\n"
        "• File Location: outputs/floss_decoded_strings.txt"
    )

    # Tool 3
    doc.add_heading("TOOL 3: FNV-1a 64-Bit + XOR Defense Evasion Engine", level=3)
    doc.add_paragraph(
        "• Purpose: Mathematical verification of how SUNBURST evaluated 120+ analysis and security monitoring tools without plaintext strings.\n"
        "• Primary Presenter: Omik Acharya (Reverse Engineer)\n"
        "• Mathematical Formula:\n"
        "  Hash = FNV1a_64(lowercase(process_name)) XOR 0x5BAC903BA7D81967\n"
        "  Offset Basis: 0xcbf29ce484222325 | Prime: 0x100000001b3 | XOR Key: 6605813339339102567\n"
        "• Interactive Terminal Command:\n"
        "  python3 scripts/run_forensics.py --check-process wireshark\n"
        "• Target Outputs:\n"
        "  - wireshark -> 0xa84ff6500970f54d -> XOR: 17574002783607647274 (MATCH)\n"
        "  - procmon   -> 0x46240b85b6a1d8ed -> XOR: 2128122064571842954   (MATCH)\n"
        "  - x64dbg    -> 0x9f5627c8d228677c -> XOR: 14193859431895170587  (MATCH)\n"
        "• File Location: outputs/fnv_blocklist_hashes.txt"
    )

    # Tool 4
    doc.add_heading("TOOL 4: Mandiant CAPA (v9.4.0) & Behavioral Simulation", level=3)
    doc.add_paragraph(
        "• Purpose: Semantic rule matching of disassembled MSIL instructions against the MITRE ATT&CK Matrix.\n"
        "• Primary Presenter: Omik Acharya (Reverse Engineer)\n"
        "• Terminal Verification Command:\n"
        "  capa --version\n"
        "  python3 scripts/run_forensics.py --simulate --simulate-behavior victim\n"
        "• Flagship ATT&CK Techniques Identified:\n"
        "  - T1497.003: Time-Based Sandbox Evasion (12 to 14 day Thread.Sleep dormancy).\n"
        "  - T1071.004: DNS C2 Tunneling via avsvmcloud.com.\n"
        "  - T1562.001: Impair Defenses (Process blacklist hashing & termination).\n"
        "  - T1082: System Information Discovery (MachineGuid & DomainName queries).\n"
        "• File Location: outputs/capa_capabilities_report.txt and outputs/behavior_flow_reconstruction.txt"
    )

    # Section 4: Legal & CI Run
    doc.add_heading("4. Statutory Admissibility & CI/CD Verification Run", level=2)
    doc.add_paragraph(
        "• Primary Presenter: Om Lanke (Technical Auditor)\n"
        "• Statutory Certificate Generation Command:\n"
        "  python3 scripts/generate_bsa_cert.py --format both\n"
        "  Generates both legal_compliance/Section_63_BSA_Certificate.md and legal_compliance/Section_63_BSA_Certificate.txt.\n"
        "  Embeds hardware MAC address, machine telemetry, and dual affirmations by Amandeep Singh (Custodian) and Om Lanke/Omik Acharya (Experts).\n\n"
        "• CI/CD Automated Test Suite Run Command:\n"
        "  pytest tests/ -v\n"
        "  Executes all 22 test assertions across cryptographic hashes, Deflate inflation, FNV math, report parsers, and legal deliverables in ~0.20s."
    )

    # Section 5: Troubleshooting
    doc.add_heading("5. Emergency Troubleshooting & Backup Plans", level=2)
    doc.add_paragraph(
        "• Issue 1: Terminal prints 'pytest: command not found'.\n"
        "  Solution: Activate virtual environment first: source .venv/bin/activate\n\n"
        "• Issue 2: Terminal prints Python 3.9 SyntaxError on 'match typeid:'.\n"
        "  Solution: Ensure you are using the Python 3.11 virtual environment. Re-run: ./setup.sh\n\n"
        "• Issue 3: Browser does not open simulation.\n"
        "  Solution: Run in terminal: open docs/sunburst_simulation.html, or drag the HTML file directly into Chrome."
    )

    doc.save(output_path)
    print(f"[+] Successfully generated Document 2: {output_path}")


def main():
    docs_dir = Path("docs")
    docs_dir.mkdir(parents=True, exist_ok=True)

    doc1_path = docs_dir / "Presentation_Speaking_Script.docx"
    doc2_path = docs_dir / "Tool_Execution_and_Demo_Manual.docx"

    build_script_document(doc1_path)
    build_manual_document(doc2_path)


if __name__ == "__main__":
    main()
