#!/usr/bin/env python3
"""
build_demo_docs.py
Generates two comprehensive, professionally formatted Microsoft Word (.docx) documents:
1. docs/Presentation_Speaking_Script.docx
2. docs/Tool_Execution_and_Demo_Manual.docx

Department of Computer Engineering, KJ Somaiya School of Engineering
Somaiya Vidyavihar University, Mumbai.
Digital Forensics & Cyber Security Laboratory (Group 10)
"""

import os
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
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
    """Sets internal padding for a cell."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_callout_box(doc, title, text, bg_hex="F0F4F8", border_hex="003366"):
    """Adds a stylish callout box with a colored border and background."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"📌 {title}\n")
    run_t.bold = True
    run_t.font.name = "Arial"
    run_t.font.size = Pt(11)
    run_t.font.color.rgb = RGBColor(0, 51, 102)

    run_body = p.add_run(text)
    run_body.font.name = "Arial"
    run_body.font.size = Pt(10)
    run_body.font.color.rgb = RGBColor(50, 50, 50)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)


def format_table_headers(table, col_widths, bg_hex="003366"):
    """Styles the header row of a table."""
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(hdr_cells):
        set_cell_background(title, bg_hex)
        set_cell_margins(title, top=120, bottom=120, left=120, right=120)
        p = title.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.bold = True
            run.font.name = "Arial"
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(255, 255, 255)
    
    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = Inches(w)


def build_script_document(output_path):
    """Builds Document 1: End-to-End Presentation Speaking Script."""
    doc = Document()

    # Page Margins
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Title Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    t_run = title_p.add_run("K.J. SOMAIYA SCHOOL OF ENGINEERING\nSOMAIYA VIDYAVIHAR UNIVERSITY, MUMBAI")
    t_run.bold = True
    t_run.font.name = "Arial"
    t_run.font.size = Pt(12)
    t_run.font.color.rgb = RGBColor(100, 100, 100)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    sub_run = sub_p.add_run("Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)\nAcademic Year 2026–2027 | Class: TY B.Tech Computer Engineering | Group 10")
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(10)
    sub_run.font.color.rgb = RGBColor(120, 120, 120)

    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_after = Pt(14)
    h1_run = h1.add_run("SUNBURST FORENSICS & STATUTORY AUDIT: END-TO-END SPEAKING SCRIPT")
    h1_run.bold = True
    h1_run.font.name = "Arial"
    h1_run.font.size = Pt(18)
    h1_run.font.color.rgb = RGBColor(0, 51, 102)

    add_callout_box(
        doc,
        "DEMO TIMING & STRATEGY SUMMARY",
        "Total Target Duration: 8 to 9 Minutes (~2.5 to 3 minutes per speaker).\n"
        "• Part 1: Avantdeep (0:00 – 2:45) — Intro, Attack Vector, Evidence Hash Check, DiE PE Triage.\n"
        "• Part 2: Omik (2:45 – 5:45) — String Deobfuscation (Deflate), FNV-1a Process Blacklist, CAPA.\n"
        "• Part 3: Om (5:45 – 8:30) — Indian Cyber Law, Section 63 BSA 2023 Certificate, Pytest CI Run."
    )

    # Roster Table
    doc.add_heading("Team Member Roster & Responsibilities", level=2)
    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [1.5, 1.2, 2.2, 1.6]
    
    headers = ["Speaker Name", "Roll Number", "Forensic Specialization", "Assigned Speaking Time"]
    for i, h in enumerate(headers):
        table.rows[0].cells[i].paragraphs[0].text = h
    
    roster_data = [
        ("Avantdeep (Amandeep)", "16010123036", "Lead Investigator: PE Triage & Hash Baseline", "0:00 – 2:45 (~2.5 min)"),
        ("Omik Acharya", "16010123218", "Reverse Engineer: FLOSS & CAPA Attribution", "2:45 – 5:45 (~3.0 min)"),
        ("Om Lanke", "16010123216", "Cyber Legal Auditor: IT Act & BSA 2023", "5:45 – 8:30 (~2.5 min)")
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
    doc.add_heading("PART 1: AVANTDEEP (0:00 – 2:45)", level=2)
    doc.add_paragraph("Role: Lead Investigator | Focus: Case Overview, Supply Chain Attack Vector, Cryptographic Hashing, DiE PE Triage").runs[0].bold = True

    p1_cues = doc.add_paragraph()
    p1_cues.add_run("🎬 SCREEN ACTIONS FOR AVANTDEEP:\n").bold = True
    p1_cues.add_run(
        "1. Start screen recording with Chrome showing 'docs/sunburst_simulation.html' (Stage 1: The Attack).\n"
        "2. Switch to Terminal and run: 'bash scripts/verify_hashes.sh'. Show the green integrity output.\n"
        "3. Switch back to Chrome and click 'Stage 4: Detect It Easy'. Point out the PE section map and entropy curve."
    )
    p1_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Exact Word-for-Word Speaking Script:", level=3)
    p1_script = doc.add_paragraph()
    p1_script.paragraph_format.line_spacing = 1.25
    p1_script.add_run(
        "“Good morning respected evaluators and professors. We are Group 10 from the Department of Computer Engineering, "
        "KJ Somaiya School of Engineering. Our capstone digital forensics project is the Static Forensic Analysis and Legal Compliance "
        "Audit of the SolarWinds SUNBURST Malware.\n\n"
        "I am Avantdeep, Lead Investigator. My teammates are Omik Acharya, who handled Reverse Engineering and Deobfuscation, "
        "and Om Lanke, who handled Cyber Legal Compliance and Indian Statutory Admissibility.\n\n"
        "[Action: Show Stage 1 in Browser]\n"
        "The SolarWinds intrusion in 2020 was a landmark software supply chain attack. Attackers from state-sponsored group UNC2452 "
        "— attributed to Russia's Foreign Intelligence Service (SVR) — did not break into customer perimeters directly. Instead, they compromised "
        "SolarWinds' internal build environment, deploying an in-memory injector called SUNSPOT. When the automated MSBuild compiler executed, "
        "it swapped in a malicious C# source file, trojanizing the core library: SolarWinds.Orion.Core.BusinessLayer.dll.\n\n"
        "Because this occurred inside the official build system, the trojanized DLL received a genuine, valid Authenticode digital signature "
        "from DigiCert. Over 18,000 corporate, defense, and government organizations deployed this update willingly because it looked completely legitimate.\n\n"
        "[Action: Switch to Terminal and run: bash scripts/verify_hashes.sh]\n"
        "In digital forensics, rule number one is: never execute live malware, and strictly maintain the chain of custody. "
        "As you can see on the terminal, our verification script computes the cryptographic hash of our evidence artifact under ISO/IEC 27037 standards. "
        "The SHA-256 digest ending in '...7a4d73' matches the official CISA and FireEye threat advisories bit-for-bit. Integrity is mathematically verified.\n\n"
        "[Action: Switch to Browser, click Stage 4: Detect It Easy]\n"
        "Next, we performed PE Header Triage using Detect It Easy (DiE v3.10). Notice three critical findings on screen:\n"
        "First, it is a 32-bit PE dynamic link library for Intel 80386 running the .NET CLR v4.0.30319, compiled with Microsoft Roslyn C#.\n"
        "Second, look at the entropy curve: it stays at 6.21 across the code section, strictly below the 7.5 packed threshold. The attackers "
        "deliberately did not pack the binary with UPX or Themida so it would not trigger heuristic antivirus flags.\n"
        "Third, it bears a valid Authenticode digital signature issued to SolarWinds Worldwide, LLC. This is classic Subversion of Trust Controls (T1553.002).\n\n"
        "I now hand over to Omik to demonstrate how we cracked their obfuscated strings and defense evasion.”"
    )
    doc.add_page_break()

    # ==================== PART 2 ====================
    doc.add_heading("PART 2: OMIK ACHARYA (2:45 – 5:45)", level=2)
    doc.add_paragraph("Role: Reverse Engineer | Focus: String Deobfuscation (Deflate), FNV-1a Hashed Blacklist, CAPA MITRE ATT&CK Mapping").runs[0].bold = True

    p2_cues = doc.add_paragraph()
    p2_cues.add_run("🎬 SCREEN ACTIONS FOR OMIK:\n").bold = True
    p2_cues.add_run(
        "1. Browser: Go to 'Stage 5: FLOSS strings' $\rightarrow$ click the 'Decode all' button live.\n"
        "2. Browser: Go to 'Stage 6: Hidden blocklist' $\rightarrow$ type/click 'wireshark' $\rightarrow$ click 'Run the check'.\n"
        "3. Switch to Terminal $\rightarrow$ run:\n"
        "   floss --version\n"
        "   capa --version\n"
        "   python3 scripts/run_forensics.py --check-process wireshark\n"
        "   python3 scripts/run_forensics.py --simulate --simulate-behavior victim\n"
        "4. Browser: Show 'Stage 7: CAPA capabilities' and 'Stage 8: Behaviour simulation'."
    )
    p2_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Exact Word-for-Word Speaking Script:", level=3)
    p2_script = doc.add_paragraph()
    p2_script.paragraph_format.line_spacing = 1.25
    p2_script.add_run(
        "“Thank you, Avantdeep. I am Omik Acharya, and my focus was reverse engineering the backdoor's internal evasion routines "
        "and command channels.\n\n"
        "[Action: In Terminal, run 'floss --version', then switch to Browser Stage 5]\n"
        "When we ran Mandiant FLOSS (v3.1.1), it extracted 2,146 static strings, highlighting suspicious internal classes like "
        "OrionImprovementBusinessLayer and DeflateStream. However, the attackers protected their critical network and registry strings using "
        "a two-tier scheme: raw Deflate compression over Base64-encoded strings.\n\n"
        "[Action: Click 'Decode all' button in the browser]\n"
        "As you see live on screen, our deobfuscation engine inflates these strings in real time:\n"
        "• The first token decodes directly to the primary C2 domain: avsvmcloud.com.\n"
        "• The subsequent tokens reveal registry fingerprint paths like SOFTWARE\\Microsoft\\Cryptography, the MachineGuid key, and WMI queries "
        "used to profile the victim host.\n\n"
        "[Action: In Browser, click Stage 6: Hidden blocklist]\n"
        "Next, how did SUNBURST evade security software? If the backdoor contained plaintext strings like 'wireshark' or 'procmon', antivirus "
        "signatures would catch it immediately. Instead, the attackers converted process names to lowercase, calculated their 64-bit FNV-1a hash, "
        "and XORed the value with the secret constant 0x5BAC903BA7D81967.\n\n"
        "[Action: In Stage 6 input box, click 'wireshark' and click 'Run the check']\n"
        "Look at the pipeline: 'wireshark' is hashed to 0xa84ff6500970f54d, XORed, and matches the hardcoded table. If Wireshark, Sysmon, or "
        "x64dbg is running, the backdoor terminates immediately without beaconing.\n\n"
        "[Action: Switch to Terminal and run: python3 scripts/run_forensics.py --check-process wireshark]\n"
        "Our CLI tool verifies this mathematical check in milliseconds, outputting the exact decimal value 17574002783607647274.\n\n"
        "[Action: In Terminal, run: python3 scripts/run_forensics.py --simulate --simulate-behavior victim]\n"
        "Using Mandiant CAPA (v9.4.0), we mapped the binary's capabilities directly to MITRE ATT&CK:\n"
        "• T1497.003: A hardcoded Thread.Sleep delay of 288 hours — 12 to 14 full days — to outlast dynamic analysis sandboxes.\n"
        "• T1071.004: Covert DNS tunneling exfiltrating host GUIDs via subdomains of avsvmcloud.com.\n"
        "• T1562.001: Impairing defensive tools.\n\n"
        "[Action: Switch to Browser Stage 8: Behaviour simulation]\n"
        "We reconstructed the full 8-step execution gate: on an analyst machine with Wireshark, it terminates at Step 4; on an offline machine, "
        "it terminates at Step 5. Only on a genuine enterprise server does it proceed to open the HTTP command channel.\n\n"
        "I now invite Om Lanke to explain our Indian cyber legal audit and court admissibility certification.”"
    )
    doc.add_page_break()

    # ==================== PART 3 ====================
    doc.add_heading("PART 3: OM LANKE (5:45 – 8:30)", level=2)
    doc.add_paragraph("Role: Cyber Legal Auditor | Focus: IT Act 2000, CERT-In Directions 2022, Section 63 BSA 2023, BNSS 2023, Pytest CI Run").runs[0].bold = True

    p3_cues = doc.add_paragraph()
    p3_cues.add_run("🎬 SCREEN ACTIONS FOR OM:\n").bold = True
    p3_cues.add_run(
        "1. Browser: Show 'Stage 10: Indian law mapping'. Click through the finding buttons to show statutory provisions lighting up.\n"
        "2. Switch to Terminal $\rightarrow$ run:\n"
        "   python3 scripts/generate_bsa_cert.py --format both\n"
        "3. Open and display 'legal_compliance/Section_63_BSA_Certificate.md' in VS Code/Terminal.\n"
        "4. Switch to Terminal $\rightarrow$ run:\n"
        "   pytest tests/ -v\n"
        "5. Conclude and state opening for questions."
    )
    p3_cues.paragraph_format.space_after = Pt(8)

    doc.add_heading("Exact Word-for-Word Speaking Script:", level=3)
    p3_script = doc.add_paragraph()
    p3_script.paragraph_format.line_spacing = 1.25
    p3_script.add_run(
        "“Thank you, Omik. I am Om Lanke, Cyber Legal Auditor for Group 10.\n\n"
        "A forensic investigation is incomplete without establishing legal culpability and statutory admissibility under Indian law.\n\n"
        "[Action: In Browser, show Stage 10: Indian law mapping]\n"
        "We mapped the technical findings against five core Indian legal frameworks:\n"
        "1. Information Technology Act, 2000:\n"
        "   • Sections 43 & 66: Introducing a computer contaminant and criminal hacking, carrying civil compensation and up to 3 years imprisonment.\n"
        "   • Section 66F (Cyber Terrorism): SUNBURST targeted government ministries and critical infrastructure. Under Section 66F(1)(B), introducing "
        "malicious code intending to threaten national sovereignty or disrupt essential infrastructure carries a mandatory penalty of Imprisonment for Life.\n"
        "   • Section 70: Unauthorized access to declared Protected Systems (up to 10 years imprisonment).\n"
        "   • Section 43A: Companies that deployed unverified vendor updates without vendor risk assessments face uncapped civil liability for negligence.\n\n"
        "2. CERT-In Directions (28 April 2022):\n"
        "   • Mandates reporting supply chain intrusions to CERT-In within 6 hours of discovery.\n"
        "   • Mandates secure log retention for 180 days within Indian jurisdiction.\n\n"
        "3. Digital Personal Data Protection (DPDP) Act, 2023: Mandatory breach notifications to the Data Protection Board of India.\n\n"
        "[Action: Switch to Terminal and run: python3 scripts/generate_bsa_cert.py --format both]\n"
        "Now, how is this digital evidence admitted in an Indian court? With the repeal of the Indian Evidence Act, 1872, the old Section 65B "
        "certificate is legally obsolete. Today, electronic records must be certified under Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), 2023.\n\n"
        "[Action: Open legal_compliance/Section_63_BSA_Certificate.md in Editor]\n"
        "Our automation script generates this court-ready affidavit under Section 63(4)(c) of the BSA 2023 and Section 105 of the Bharatiya Nagarik "
        "Suraksha Sanhita (BNSS), 2023:\n"
        "• Part A (Custodian Affirmation): Executed by Avantdeep, certifying workstation MAC address, hardware write-blocking, and continuous custody.\n"
        "• Part B (Forensic Expert Certificate): Executed jointly by Omik and myself, certifying cryptographic hash equality under NIST FIPS 180-4 and "
        "deterministic tool validation. This renders our findings substantive primary evidence in judicial proceedings.\n\n"
        "[Action: Switch to Terminal and run: pytest tests/ -v]\n"
        "Finally, to guarantee enterprise software quality, we implemented a continuous integration test suite running on uv. All 22 automated "
        "tests pass in under 0.3 seconds, proving our cryptographic hashing, Deflate decompression, FNV blocklist, and legal templates are 100% verified.\n\n"
        "In conclusion, Group 10 has demonstrated a complete, static, non-destructive autopsy of a nation-state supply chain intrusion, backed by "
        "mathematical proof and full statutory admissibility under the new BSA 2023.\n\n"
        "Thank you professors. We are now open for your questions.”"
    )
    doc.add_page_break()

    # ==================== Q&A SECTION ====================
    doc.add_heading("EVALUATOR Q&A CHEAT-SHEET (Top 5 Questions & Bulletproof Answers)", level=2)
    
    qa_list = [
        ("Q1: Why did you not execute the malware in a dynamic sandbox?",
         "Answer: SUNBURST has a built-in 12 to 14 day dormancy timer (T1497.003) and checks for sandbox hooks. A standard 5-minute sandbox detonation "
         "shows zero malicious activity. Static analysis using DiE, FLOSS, and CAPA allowed us to reverse-engineer 100% of the malware's logic safely "
         "without risking host infection or C2 network leakage."),
        
        ("Q2: What is the exact difference between Section 65B (IEA 1872) and Section 63 (BSA 2023)?",
         "Answer: The Bharatiya Sakshya Adhiniyam 2023 repealed the Indian Evidence Act 1872. Section 63 BSA modernizes electronic evidence admissibility. "
         "It introduces explicit statutory recognition for distributed storage and mandates a clear dual-certification structure: Part A by the Custodian "
         "proving lawful management and operational integrity, and Part B by the Technical Expert certifying cryptographic hash matching and zero tampering."),
        
        ("Q3: Why did the attackers XOR the FNV-1a hash with 0x5BAC903BA7D81967?",
         "Answer: Plain FNV-1a hashes can be reversed using precomputed rainbow tables. XORing the 64-bit digest with a hardcoded constant added an extra "
         "layer of cryptographic obfuscation, preventing security researchers from identifying the targeted security tools without decompiling the specific DLL routine."),
        
        ("Q4: How did the malware achieve persistence without setting normal Run keys?",
         "Answer: SUNBURST achieved persistence via DLL component hijacking (T1574.002). Because it was embedded inside the core SolarWinds Orion Business "
         "Layer DLL, it executed automatically every time the legitimate Windows service 'SolarWinds.BusinessLayerHost.exe' started, without needing unusual registry Run keys."),
        
        ("Q5: What are the mandatory reporting deadlines under CERT-In Directions 2022?",
         "Answer: Under Direction 5(i) of the 28 April 2022 Directions, any supply chain or critical system compromise must be reported to CERT-In within "
         "6 hours of detection. Under Direction 5(v), all system and network logs must be maintained within Indian jurisdiction for 180 days.")
    ]

    for q, a in qa_list:
        p_q = doc.add_paragraph()
        p_q.add_run(q + "\n").bold = True
        p_q.runs[0].font.color.rgb = RGBColor(0, 51, 102)
        p_a = p_q.add_run(a)
        p_a.font.size = Pt(10)
        p_q.paragraph_format.space_after = Pt(8)

    doc.save(output_path)
    print(f"[+] Successfully generated Document 1: {output_path}")


def build_manual_document(output_path):
    """Builds Document 2: Step-by-Step Tool Execution & Command Runbook."""
    doc = Document()

    # Page Margins
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
    sub_run = sub_p.add_run("Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks)\nTechnical Demonstration Runbook & Tool Execution Manual | Group 10")
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(10)
    sub_run.font.color.rgb = RGBColor(120, 120, 120)

    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_after = Pt(14)
    h1_run = h1.add_run("SUNBURST DFIR CAPSTONE: TOOL EXECUTION & DEMO MANUAL")
    h1_run.bold = True
    h1_run.font.name = "Arial"
    h1_run.font.size = Pt(18)
    h1_run.font.color.rgb = RGBColor(0, 51, 102)

    add_callout_box(
        doc,
        "DEMO OPERATIONAL GOAL",
        "This manual details the exact sequence of terminal commands, UI clicks, and visual screens required to deliver a "
        "flawless, bug-free capstone demonstration. Follow this choreography precisely during recording or live viva presentation."
    )

    # Section 1: Pre-Demo Setup
    doc.add_heading("1. Pre-Demo Environment Checklist (2 Minutes Before Start)", level=2)
    doc.add_paragraph(
        "Ensure the following 3 windows are opened on your Mac and arranged across your workspace:\n\n"
        "• WINDOW 1 (Web Browser — Google Chrome or Safari):\n"
        "  Open the interactive simulation model by navigating to:\n"
        "  file:///Users/mac/Developer/csfcl/docs/sunburst_simulation.html\n"
        "  (Tip: You can launch this directly from terminal using: open docs/sunburst_simulation.html)\n\n"
        "• WINDOW 2 (Terminal):\n"
        "  Open Terminal in your repository directory and activate the Python 3.11 virtual environment:\n"
        "  cd /Users/mac/Developer/csfcl\n"
        "  source .venv/bin/activate\n\n"
        "• WINDOW 3 (VS Code / File Editor):\n"
        "  Open the project workspace in VS Code to quickly show legal files and report outputs if requested."
    )

    # Section 2: Choreography Table
    doc.add_heading("2. Chronological Demo Choreography (Second-by-Second Runbook)", level=2)
    
    table = doc.add_table(rows=10, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [0.8, 1.1, 1.6, 1.8, 1.2]
    
    headers = ["Time", "Speaker", "Screen / Window", "Action / Exact Command Line", "Expected Visual Result"]
    for i, h in enumerate(headers):
        table.rows[0].cells[i].paragraphs[0].text = h
    
    choreography_data = [
        ("0:00", "Avantdeep", "Browser (Stage 1)", "Display 'The Attack' animated diagram", "Shows APT29 supply chain vector and 18,000 victim reach."),
        ("1:15", "Avantdeep", "Terminal", "bash scripts/verify_hashes.sh", "Green PASS output; SHA-256 baseline verified under ISO/IEC 27037."),
        ("1:50", "Avantdeep", "Browser (Stage 4)", "Click 'Stage 4: Detect It Easy'", "PE section map scan beam, Roslyn C#, entropy curve staying at 6.21."),
        ("2:45", "Omik", "Terminal", "floss --version", "Prints 'floss 3.1.1'; proves native Mandiant tool is installed."),
        ("3:00", "Omik", "Browser (Stage 5)", "Click 'Decode all' button live", "Real-time raw Deflate decompression revealing 'avsvmcloud.com'."),
        ("3:45", "Omik", "Browser (Stage 6)", "Click 'wireshark' -> 'Run the check'", "Animated 5-box pipeline showing FNV-1a 64-bit + XOR key match."),
        ("4:20", "Omik", "Terminal", "python3 scripts/run_forensics.py --check-process wireshark", "Terminal calculates 0xa84ff6500970f54d and confirms blacklist match."),
        ("4:50", "Omik", "Terminal", "python3 scripts/run_forensics.py --simulate --simulate-behavior victim", "Terminal prints rich table with 14 MITRE ATT&CK techniques."),
        ("5:45", "Om", "Browser (Stage 10)", "Click finding buttons in 'Indian law mapping'", "Interactive buttons light up IT Act, CERT-In, DPDP, and BSA 2023."),
    ]

    for row_idx, data in enumerate(choreography_data, start=1):
        for col_idx, val in enumerate(data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Arial"
            cell.paragraphs[0].runs[0].font.size = Pt(8.5)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
    
    format_table_headers(table, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 3: Deep Dive per Tool
    doc.add_heading("3. Tool-by-Tool Detailed Technical Reference", level=2)

    # Tool 1
    doc.add_heading("TOOL 1: Detect It Easy (DiE v3.10)", level=3)
    doc.add_paragraph(
        "• Purpose: Static identification of PE32 binary architecture, compiler signatures, digital certificates, and section entropy.\n"
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
        "• Statutory Certificate Generation Command:\n"
        "  python3 scripts/generate_bsa_cert.py --format both\n"
        "  Generates both legal_compliance/Section_63_BSA_Certificate.md and legal_compliance/Section_63_BSA_Certificate.txt.\n"
        "  Embeds hardware MAC address, machine telemetry, and dual affirmations by Avantdeep (Custodian) and Omik/Om (Experts).\n\n"
        "• CI/CD Automated Test Suite Run Command:\n"
        "  pytest tests/ -v\n"
        "  Executes all 22 test assertions across cryptographic hashes, Deflate inflation, FNV math, report parsers, and legal deliverables."
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
