#!/usr/bin/env python3
"""
build_presentation.py
Generates the comprehensive 12-slide Microsoft PowerPoint (.pptx) presentation:
docs/SUNBURST_Forensic_Investigation_Group10.pptx

Formatted specifically in the Somaiya Vidyavihar University (SVU) / K.J. Somaiya
School of Engineering template, featuring:
- Somaiya Red (#A71930) and Trust Blue (#004B87) branding
- Official Somaiya University logo and Trust crest
- Slide-by-slide 10-minute flow for Amandeep Singh, Omik Acharya, and Om Lanke
- Integrated "Side-by-Side Live Demo Synchronization" cues on every slide
- 16:9 widescreen layout (13.333" x 7.5")

Department of Computer Engineering, K.J. Somaiya School of Engineering
Somaiya Vidyavihar University, Mumbai.
"""

import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# --- SOMAIYA BRAND COLOR PALETTE ---
COLOR_SOMAIYA_RED = RGBColor(167, 25, 48)       # #A71930 Somaiya Crimson
COLOR_SOMAIYA_DARK_RED = RGBColor(125, 0, 0)    # #7D0000 Deep Maroon
COLOR_SOMAIYA_BLUE = RGBColor(0, 75, 135)       # #004B87 Trust Blue
COLOR_DARK_SLATE = RGBColor(30, 41, 59)         # #1E293B Text Dark
COLOR_MUTED_SLATE = RGBColor(100, 116, 139)     # #64748B Secondary Text
COLOR_LIGHT_BG = RGBColor(248, 250, 252)        # #F8FAFC Card Background
COLOR_BORDER = RGBColor(226, 232, 240)          # #E2E8F0 Card Border
COLOR_DEMO_BG = RGBColor(238, 246, 255)         # #EEF6FF Demo Box Fill
COLOR_DEMO_BORDER = RGBColor(59, 130, 246)      # #3B82F6 Blue Border
COLOR_SUCCESS_GREEN = RGBColor(16, 149, 79)     # #10954F Pass / Success Green
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_AMBER = RGBColor(217, 119, 6)             # #D97706 Warning Amber


def add_header(slide, section_category, title_text, presenter_info, slide_num, total_slides=12):
    """Adds standard Somaiya branded header and footer to a slide."""
    # Left accent bar (Somaiya Red)
    left_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.18), Inches(7.5))
    left_bar.fill.solid()
    left_bar.fill.fore_color.rgb = COLOR_SOMAIYA_RED
    left_bar.line.color.rgb = COLOR_SOMAIYA_RED

    # Somaiya Logo at top right
    logo_path = "assets/somaiya/somaiya_logo.jpg"
    if os.path.exists(logo_path):
        slide.shapes.add_picture(logo_path, Inches(10.0), Inches(0.28), width=Inches(2.65))

    # Header text box
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(9.2), Inches(1.15))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Section / Category Tracker
    p0 = tf.paragraphs[0]
    p0.text = f"K.J. SOMAIYA SCHOOL OF ENGINEERING | {section_category.upper()}"
    p0.font.name = "Arial"
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_SOMAIYA_RED

    # Main Slide Title
    p1 = tf.add_paragraph()
    p1.text = title_text
    p1.font.name = "Arial"
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_DARK_SLATE
    p1.space_before = Pt(2)

    # Presenter & Time Badge
    p2 = tf.add_paragraph()
    p2.text = f"🎤 {presenter_info}"
    p2.font.name = "Arial"
    p2.font.size = Pt(10.5)
    p2.font.bold = False
    p2.font.color.rgb = COLOR_MUTED_SLATE
    p2.space_before = Pt(2)

    # Subtle horizontal divider line
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.42), Inches(12.1), Inches(0.02))
    div.fill.solid()
    div.fill.fore_color.rgb = COLOR_BORDER
    div.line.color.rgb = COLOR_BORDER

    # Footer divider line
    fdiv = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(6.92), Inches(12.1), Inches(0.015))
    fdiv.fill.solid()
    fdiv.fill.fore_color.rgb = COLOR_BORDER
    fdiv.line.color.rgb = COLOR_BORDER

    # Footer Text
    ftb = slide.shapes.add_textbox(Inches(0.6), Inches(6.98), Inches(12.1), Inches(0.4))
    ftf = ftb.text_frame
    ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
    fp = ftf.paragraphs[0]
    fp.text = (
        "Somaiya Vidyavihar University — Digital Forensics & Cyber Security Laboratory (Capstone Evaluation — 20 Marks) | Group 10"
    )
    fp.font.name = "Arial"
    fp.font.size = Pt(8.5)
    fp.font.color.rgb = COLOR_MUTED_SLATE

    # Slide number box
    snb = slide.shapes.add_textbox(Inches(11.5), Inches(6.98), Inches(1.2), Inches(0.4))
    snf = snb.text_frame
    snf.margin_left = snf.margin_top = snf.margin_right = snf.margin_bottom = 0
    snp = snf.paragraphs[0]
    snp.text = f"Slide {slide_num} of {total_slides}"
    snp.alignment = PP_ALIGN.RIGHT
    snp.font.name = "Arial"
    snp.font.size = Pt(8.5)
    snp.font.bold = True
    snp.font.color.rgb = COLOR_SOMAIYA_RED


def add_card(slide, left, top, width, height, title, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER):
    """Creates a stylized rectangular card box with a title."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)

    if title:
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_SOMAIYA_RED


def add_demo_box(slide, left, top, width, height, tool_title, window_target, command_or_action, visual_result):
    """Creates a dedicated side-by-side demo synchronization callout card."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_DEMO_BG
    card.line.color.rgb = COLOR_DEMO_BORDER
    card.line.width = Pt(1.5)

    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_hdr = tf.paragraphs[0]
    p_hdr.text = f"🖥️ SIDE-BY-SIDE LIVE DEMO SYNC"
    p_hdr.font.name = "Arial"
    p_hdr.font.size = Pt(10.5)
    p_hdr.font.bold = True
    p_hdr.font.color.rgb = RGBColor(30, 64, 175)

    p_sub = tf.add_paragraph()
    p_sub.text = f"Tool / Target: {tool_title}"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_DARK_SLATE
    p_sub.space_before = Pt(4)

    items = [
        ("Screen / Window", window_target),
        ("Execution Action", command_or_action),
        ("Expected Visual", visual_result)
    ]
    for label, val in items:
        p = tf.add_paragraph()
        p.text = f"• {label}: "
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(71, 85, 105)
        p.space_before = Pt(3)

        r = p.add_run()
        r.text = val
        r.font.bold = False
        r.font.color.rgb = COLOR_DARK_SLATE


def build_slide_1(prs):
    """Slide 1: Somaiya Title Slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Left accent bar
    left_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.25), Inches(7.5))
    left_bar.fill.solid()
    left_bar.fill.fore_color.rgb = COLOR_SOMAIYA_RED
    left_bar.line.color.rgb = COLOR_SOMAIYA_RED

    # Somaiya Logo (top left)
    logo_path = "assets/somaiya/somaiya_logo.jpg"
    if os.path.exists(logo_path):
        slide.shapes.add_picture(logo_path, Inches(0.8), Inches(0.5), width=Inches(3.4))

    # Somaiya Trust Badge (top right)
    trust_path = "assets/somaiya/somaiya_trust.png"
    if os.path.exists(trust_path):
        slide.shapes.add_picture(trust_path, Inches(11.4), Inches(0.5), width=Inches(1.2))

    # Main Title Area
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(11.8), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_tag = tf.paragraphs[0]
    p_tag.text = "DEPARTMENT OF COMPUTER ENGINEERING | CAPSTONE EVALUATION (20 MARKS)"
    p_tag.font.name = "Arial"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_SOMAIYA_RED

    p_title = tf.add_paragraph()
    p_title.text = "Operation SUNBURST: Digital Forensic Investigation & Incident Response"
    p_title.font.name = "Arial"
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_DARK_SLATE
    p_title.space_before = Pt(4)

    p_sub = tf.add_paragraph()
    p_sub.text = (
        "Static Reverse Engineering, Defense Evasion Analysis, Memory Artifacts & "
        "Indian Statutory Admissibility under Bharatiya Sakshya Adhiniyam, 2023 & CERT-In"
    )
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = COLOR_MUTED_SLATE
    p_sub.space_before = Pt(6)

    # Divider line
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(3.6), Inches(11.8), Inches(0.02))
    div.fill.solid()
    div.fill.fore_color.rgb = COLOR_SOMAIYA_RED
    div.line.color.rgb = COLOR_SOMAIYA_RED

    # Team Members Table
    rows = 4
    cols = 4
    table_shape = slide.shapes.add_table(rows, cols, Inches(0.8), Inches(3.8), Inches(11.8), Inches(1.85))
    table = table_shape.table
    table.columns[0].width = Inches(1.8)
    table.columns[1].width = Inches(2.5)
    table.columns[2].width = Inches(3.2)
    table.columns[3].width = Inches(4.3)

    headers = ["Roll Number", "Student Name", "Assigned Forensic Role", "Core Investigation Focus"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_SOMAIYA_RED
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

    team_data = [
        ("16010123036", "Amandeep Singh", "Lead Forensic Investigator", "Attack Vector, PE Architecture & DiE Triage"),
        ("16010123218", "Omik Acharya", "Reverse Engineer", "FLOSS Deobfuscation, FNV-1a Hashing & CAPA"),
        ("16010123216", "Om Lanke", "Technical & Cyber Legal Auditor", "BSA 2023 Sec 63, IT Act, CERT-In & CI/CD Pipeline")
    ]

    for row_idx, data in enumerate(team_data, start=1):
        for col_idx, val in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.bold = (col_idx == 1)
            p.font.color.rgb = COLOR_DARK_SLATE

    # Dual presentation sync banner
    sync_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.95), Inches(11.8), Inches(0.75))
    sync_card.fill.solid()
    sync_card.fill.fore_color.rgb = COLOR_DEMO_BG
    sync_card.line.color.rgb = COLOR_DEMO_BORDER
    sync_card.line.width = Pt(1.2)

    stb = slide.shapes.add_textbox(Inches(1.0), Inches(6.02), Inches(11.4), Inches(0.6))
    stf = stb.text_frame
    stf.word_wrap = True
    stf.margin_left = stf.margin_top = stf.margin_right = stf.margin_bottom = 0
    sp = stf.paragraphs[0]
    sp.text = "🎯 DUAL DEMONSTRATION MODEL (10-MINUTE SYNCHRONIZED RUN):"
    sp.font.name = "Arial"
    sp.font.size = Pt(9.5)
    sp.font.bold = True
    sp.font.color.rgb = RGBColor(30, 64, 175)

    sp2 = stf.add_paragraph()
    sp2.text = (
        "Left / Presentation Screen: Theoretical Case Study, Supply Chain Mechanics, MITRE ATT&CK & Legal Statutes. "
        "Side-by-Side Screen: Live Terminal Commands, Interactive Browser Simulation (sunburst_simulation.html), & Forensic Code Execution."
    )
    sp2.font.name = "Arial"
    sp2.font.size = Pt(8.5)
    sp2.font.color.rgb = COLOR_DARK_SLATE
    sp2.space_before = Pt(2)

    # Footer note
    ftb = slide.shapes.add_textbox(Inches(0.8), Inches(6.98), Inches(11.8), Inches(0.35))
    ftf = ftb.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "Somaiya Vidyavihar University — K.J. Somaiya School of Engineering | TY B.Tech COMP (2026–2027) | Group 10"
    fp.font.name = "Arial"
    fp.font.size = Pt(8.5)
    fp.font.color.rgb = COLOR_MUTED_SLATE


def build_slide_2(prs):
    """Slide 2: Case Study — The Supply Chain Vector."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "INCIDENT BACKGROUND & THREAT CONTEXT",
        "The Supply Chain Vector: SolarWinds Orion Compromise",
        "Amandeep Singh (Lead Investigator) | Time: 0:00 – 1:15",
        2
    )

    # Left Card: Case Study Background
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "CASE STUDY: OPERATION SUNBURST ARCHITECTURE")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Threat Actor", "APT29 / Nobelium (Russian Foreign Intelligence Service — SVR)."),
        ("Compromise Point", "SolarWinds software build environment injected at the MSBuild compilation stage via a rogue plugin named 'SolariCode'."),
        ("Trojanized Artifact", "SolarWinds.Orion.Core.BusinessLayer.dll (v2019.4 through v2020.2.1), legitimate network monitoring platform component."),
        ("Distribution Vector", "Digitally signed updates pushed automatically to over 18,000 public and private organizations globally."),
        ("Target Scope", "U.S. Dept of Homeland Security, Treasury, Fortune 500 tech leaders, and critical global communications nodes."),
        ("Investigation Paradigm", "Dual-track analysis: Case Study theory on slides paired side-by-side with live forensic scripts and simulation.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Interactive Forensic Simulation (Stage 1)",
        "Web Browser (Google Chrome / Safari)",
        "Open docs/sunburst_simulation.html -> View 'The Attack' animated architecture diagram.",
        "Visualizes how attackers breached the build pipeline, injected the backdoor into Orion DLL, and pushed it downstream to 18,000 victim organizations."
    )


def build_slide_3(prs):
    """Slide 3: ISO/IEC 27037 Evidence Ingestion & Cryptographic Verification."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "FORENSIC METHODOLOGY & EVIDENCE INTEGRITY",
        "Evidence Ingestion & Dual SHA-256 Hash Verification",
        "Amandeep Singh (Lead Investigator) | Time: 1:15 – 2:00",
        3
    )

    # Left Card: Evidence Integrity Principles
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "EVIDENCE HANDLING & ISO/IEC 27037:2012 COMPLIANCE")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Evidence Standard", "Strict adherence to ISO/IEC 27037:2012 (Guidelines for identification, collection, acquisition, and preservation of digital evidence)."),
        ("Dual-Sample Architecture", "Evaluator and benchmark samples cross-referenced in evidence/evidence_metadata.json to prevent false attribution."),
        ("Primary Sample SHA-256", "325c9b6ac0f441e66183579b2e00b181fc083423b009ac4800f4f05247cf0d25 (Standard malicious DLL manifest)."),
        ("Benchmark Sample SHA-256", "32519b85c0b422187d7d490004e3ab63314439cda2d0fb812999645017226d7e (Alternate Orion core iteration)."),
        ("Integrity Enforcement", "scripts/verify_hashes.sh executes POSIX-compliant sha256sum verification before any forensic analysis begins."),
        ("Legal Chain of Custody", "Continuous non-repudiation logging documented in evidence/chain_of_custody.md with timestamped cryptographic attestations.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Cryptographic Verification Engine",
        "Terminal (macOS zsh / bash)",
        "bash scripts/verify_hashes.sh",
        "Displays formatted green [PASS] indicator validating dual SHA-256 integrity against evidence/sample_hashes.sha256, proving evidence has zero bitwise tampering."
    )


def build_slide_4(prs):
    """Slide 4: Static PE Architecture & Shannon Entropy (DiE)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "STATIC PE TRIAGE & ARCHITECTURE",
        "PE32 Header Inspection & Shannon Entropy Profiling",
        "Amandeep Singh (Lead Investigator) | Time: 2:00 – 3:00",
        4
    )

    # Left Card: Detect It Easy Findings
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "DETECT IT EASY (DiE v3.10) TRIAGE METRICS")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Binary Architecture", "PE32 Dynamic Link Library (Intel 80386 32-bit), Microsoft .NET CLR v4.0.30319 (COMIMAGE_FLAGS_ILONLY)."),
        ("Compiler Toolchain", "Microsoft Roslyn C# (Visual Studio 2019) with fully intact Microsoft Intermediate Language (MSIL) metadata."),
        ("Authenticode Signature", "Legitimate digital signature issued by DigiCert Inc to SolarWinds Worldwide, LLC (Serial: 0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e)."),
        ("Section Entropy Metrics", ".text = 6.21 (Roslyn C# bytecode) | .rsrc = 7.14 (Embedded resources) | .reloc = 0.11. Overall entropy: ~5.9."),
        ("Anti-Analysis Stealth", "Remained strictly below the 7.5 packed threshold. The attackers deliberately refrained from using UPX or Themida packers."),
        ("Forensic Significance", "Because entropy remained normal and signature was authentic, antivirus heuristic scanners classified the binary as completely benign.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Detect It Easy (DiE) Visualizer",
        "Web Browser (docs/sunburst_simulation.html)",
        "Navigate to Stage 4 ('Detect It Easy') -> Observe live beam scan across PE sections.",
        "Displays real-time section layout (.text 58%, .rsrc 17%, .reloc 4%), compiler detection, and interactive Shannon entropy curve staying safely below 7.5."
    )


def build_slide_5(prs):
    """Slide 5: Attack Execution Timeline — The 8-Stage Lifecycle."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "ATTACK RECONSTRUCTION & TIMELINE",
        "Chronological Attack Execution: The 8-Stage Lifecycle",
        "Amandeep Singh -> Omik Acharya (Transition) | Time: 3:00 – 3:45",
        5
    )

    # Left: 8 Stages in 2 Columns of mini-cards
    stages = [
        ("Stage 1: Process Startup", "SolarWinds.BusinessLayerHost.exe initiates and loads the Orion core DLL into system memory."),
        ("Stage 2: 12-14 Day Sleep", "Thread.Sleep() dormancy timer delays all malicious execution to bypass dynamic sandboxes (T1497.003)."),
        ("Stage 3: Defense Checks", "Computes 64-bit FNV-1a hashes of running processes; aborts if any of 120+ analysis tools are active."),
        ("Stage 4: Fingerprinting", "Extracts MachineGuid from registry & network MAC to build an irreversible victim identifier."),
        ("Stage 5: DGA Generation", "Inflates encrypted domain tokens and encodes victim hash into a custom subdomain."),
        ("Stage 6: Covert DNS C2", "Sends low-volume DNS queries to avsvmcloud.com; parses IPv4 CNAME responses for stage-2 instructions."),
        ("Stage 7: Payload Drop", "Downloads second-stage in-memory loaders (TEARDROP / Cobalt Strike Beacon) into target environment."),
        ("Stage 8: C2 Operations", "Executes commands, steals SAML tokens, and facilitates lateral movement across domain infrastructure.")
    ]

    col_w = Inches(3.75)
    col_h = Inches(1.15)
    for idx, (st_title, st_desc) in enumerate(stages):
        r_idx = idx % 4
        c_idx = idx // 4
        x = Inches(0.6) + c_idx * Inches(3.95)
        y = Inches(1.6) + r_idx * Inches(1.25)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, col_w, col_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_LIGHT_BG
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1.0)

        tb = slide.shapes.add_textbox(x + Inches(0.12), y + Inches(0.08), col_w - Inches(0.24), col_h - Inches(0.16))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = st_title
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SOMAIYA_RED

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.name = "Arial"
        p2.font.size = Pt(8)
        p2.font.color.rgb = COLOR_DARK_SLATE
        p2.space_before = Pt(2)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "End-to-End Behavioral Simulation",
        "Terminal & Web Browser",
        "python3 scripts/run_forensics.py --simulate --simulate-behavior victim",
        "Executes full 8-stage state-machine simulation in terminal, printing MITRE ATT&CK techniques, execution gates, and decision trees for each stage."
    )


def build_slide_6(prs):
    """Slide 6: String Deobfuscation (Mandiant FLOSS)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "STATIC DEOBFUSCATION & REVERSE ENGINEERING",
        "String Encryption: Base64 & Raw Deflate Decompression",
        "Omik Acharya (Reverse Engineer) | Time: 3:45 – 4:45",
        6
    )

    # Left Card: FLOSS Deobfuscation
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "MANDIANT FLOSS (v3.1.1) & DEFLATE DECOMPRESSION")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Encryption Scheme", "SUNBURST encoded all internal configuration strings using Base64 followed by raw Deflate decompression (wbits = -15, raw stream without zlib/gzip headers)."),
        ("Defeat of Strings Utility", "Standard sysinternals 'strings' command yielded zero useful forensic indicators because all payloads were compressed streams."),
        ("Apex C2 Domain", "SywrLstNzskvTdFLzs8FAA==  -->  avsvmcloud.com (The primary command-and-control communication apex)."),
        ("Hardware GUID Registry", "C/Z3Cwl3DHKN8c1MLsovzk8riXEuqiwoyU8vSizIqAQA  -->  SOFTWARE\\Microsoft\\Cryptography."),
        ("Victim GUID Identifier", "801MzsjMS3UvzUwBAA==  -->  MachineGuid (Used to generate immutable victim cryptographic hash)."),
        ("Canary Check Domain", "SyzI1CvOz0ksKs/MSynWS87PBQA=  -->  api.solarwinds.com (Benign domain pinged to verify Internet access).")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Live String Decompression Engine",
        "Terminal & Web Browser (Stage 5)",
        "Terminal: floss --version | Browser: Click live 'Decode all' button in Stage 5.",
        "Terminal verifies native Mandiant FLOSS installation. Browser simulation live-unscrambles 7 Base64 ciphertext tokens into plaintext C2 parameters in real-time."
    )


def build_slide_7(prs):
    """Slide 7: Anti-Analysis Mechanics (64-Bit FNV-1a Hashing + XOR)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "DEFENSE EVASION & ANTI-ANALYSIS",
        "Process Blacklist Hashing: 64-Bit FNV-1a & XOR Masking",
        "Omik Acharya (Reverse Engineer) | Time: 4:45 – 5:45",
        7
    )

    # Left Card: FNV-1a Math & Architecture
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "MATHEMATICAL ALGORITHM & 120+ PROCESS BLOCKLIST")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Stealth Rationale", "To prevent EDR and SOC analysts from detecting process-enumeration strings, SUNBURST never stored blacklist names (e.g., 'wireshark') in plaintext."),
        ("Hashing Algorithm", "Formula: Hash = FNV1a_64(lowercase(process_name)) XOR 0x5BAC903BA7D81967."),
        ("Constants", "Offset Basis: 0xcbf29ce484222325 | Prime: 0x100000001b3 | XOR Mask: 6605813339339102567."),
        ("wireshark Verification", "lowercase('wireshark') -> FNV-1a: 0xa84ff6500970f54d -> XOR: 17574002783607647274 (BLOCKLIST MATCH)."),
        ("procmon Verification", "lowercase('procmon') -> FNV-1a: 0x46240b85b6a1d8ed -> XOR: 2128122064571842954 (BLOCKLIST MATCH)."),
        ("x64dbg Verification", "lowercase('x64dbg') -> FNV-1a: 0x9f5627c8d228677c -> XOR: 14193859431895170587 (BLOCKLIST MATCH).")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Interactive Process Checker",
        "Terminal & Web Browser (Stage 6)",
        "python3 scripts/run_forensics.py --check-process wireshark",
        "Terminal calculates 64-bit FNV hash and confirms blocklist hit. Browser Stage 6 illustrates the 5-step mathematical transformation pipeline with animated data blocks."
    )


def build_slide_8(prs):
    """Slide 8: Capability Mapping & MITRE ATT&CK (Mandiant CAPA)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "ATT&CK MAPPING & CAPABILITY ATTRIBUTION",
        "Behavioral Identification via Mandiant CAPA (v9.4.0)",
        "Omik Acharya (Reverse Engineer) | Time: 5:45 – 6:45",
        8
    )

    # Left Card: CAPA Capabilities & ATT&CK Matrix
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "MANDIANT CAPA RULE MATCHING & ATT&CK CORRELATION")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Semantic Rule Engine", "Mandiant CAPA disassembled MSIL bytecode to identify higher-order capabilities without running the malware."),
        ("T1497.003: Time Sandbox Evasion", "Identified 12-14 day Thread.Sleep dormancy loop designed to exceed automated sandbox analysis timeouts."),
        ("T1071.004: DNS C2 Tunneling", "Detected DNS query formatting transmitting base32/base64 encoded host telemetry to avsvmcloud.com."),
        ("T1562.001: Impair Defenses", "Discovered process enumeration loops terminating security monitoring tools matching hashed blocklist entries."),
        ("T1082: System Info Discovery", "Uncovered WMI queries to Win32_NetworkAdapterConfiguration and registry MachineGuid extraction."),
        ("T1027.002: Software Packing", "Verified custom Deflate decompressor routines inflating packed configuration parameters in memory.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Mandiant CAPA Execution Engine",
        "Terminal (macOS zsh / bash)",
        "capa --version && python3 scripts/run_forensics.py --simulate",
        "Terminal prints capa 9.4.0 verification and outputs rich terminal table mapping all 14 detected ATT&CK techniques directly to SUNBURST disassembled functions."
    )


def build_slide_9(prs):
    """Slide 9: Indian Cyber Legal Framework (IT Act, CERT-In, DPDP)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "STATUTORY COMPLIANCE & CYBER LAW",
        "Indian Statutory Framework: IT Act 2000 & CERT-In Directives",
        "Om Lanke (Technical Auditor) | Time: 6:45 – 7:45",
        9
    )

    # Left Card: Indian Legal Corroboration
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "INDIAN CYBER LEGISLATION & REPORTING MANDATES")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("IT Act, 2000 — Section 43 & 66", "Unauthorized access, extraction of system configurations (MachineGuid), and introducing computer contaminants (penalty up to 3 years / civil damages)."),
        ("IT Act, 2000 — Section 66F", "Cyber Terrorism: Attacks on supply chains impacting critical national infrastructure or sovereignty (punishable with imprisonment for life)."),
        ("IT Act, 2000 — Section 70", "Protected Systems: Unauthorized access to government or critical utility networks managing power, banking, or defense."),
        ("CERT-In Directions 2022", "Mandatory 6-Hour Reporting Window: Under Annexure I Category 2, organizations must notify CERT-In within 6 hours of discovering supply chain intrusion."),
        ("180-Day Log Retention Rule", "Direction 20(3) requires ICT service providers to maintain secure system and access logs for 180 days within Indian jurisdiction."),
        ("DPDP Act, 2023 — Section 8(5)/(6)", "Mandatory disclosure to Data Protection Board of India and affected Data Principals in the event of personal data breach.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Indian Law Mapping & CERT-In Generator",
        "Web Browser (Stage 10) & VS Code",
        "Browser Stage 10: Click finding buttons | VS Code: Open legal_compliance/CERT_In_Incident_Notification_Template.md",
        "Simulation illuminates corresponding Indian penal sections dynamically. Template file displays compliant 6-hour incident report draft formatted for CERT-In submission."
    )


def build_slide_10(prs):
    """Slide 10: Digital Evidence Admissibility (Bharatiya Sakshya Adhiniyam, 2023)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "LEGAL ADMISSIBILITY & CERTIFICATION",
        "Bharatiya Sakshya Adhiniyam (BSA), 2023: Section 63 Admissibility",
        "Om Lanke (Technical Auditor) | Time: 7:45 – 8:45",
        10
    )

    # Left Card: Section 63 BSA Architecture
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "SECTION 63 BSA 2023 DUAL AFFIRMATION MODEL")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("Repeal of IEA Section 65B", "The Indian Evidence Act, 1872 is superseded by the Bharatiya Sakshya Adhiniyam, 2023. Section 63 now governs admissibility of electronic records in court."),
        ("Sub-Section 63(4)(c) Certificate", "Mandates a formal certificate affirming the integrity, authenticity, and non-tampered chain of custody of digital evidence presented at trial."),
        ("Part A: Custodian Affirmation", "Executed by Amandeep Singh (Lead Investigator) certifying system origin, operational normalcy, and lawful acquisition under ISO/IEC 27037."),
        ("Part B: Expert Forensic Affirmation", "Jointly executed by Om Lanke & Omik Acharya affirming scientific validity of FLOSS/CAPA deobfuscation and bitwise hash match."),
        ("Hardware Telemetry Gathering", "scripts/generate_bsa_cert.py captures host MAC address, OS kernel, CPU architecture, and NTP-synced timestamp to bind certificate to physical device."),
        ("BNSS 2023 Section 105", "Complies with Bharatiya Nagarik Suraksha Sanhita requirements for mandatory videography and forensic documentation of digital evidence seizures.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Automated BSA Section 63 Certificate Generator",
        "Terminal & VS Code Editor",
        "python3 scripts/generate_bsa_cert.py --format both",
        "Generates both Markdown and Plaintext certificates. VS Code displays legal_compliance/Section_63_BSA_Certificate.md complete with embedded hardware MAC address and student signatures."
    )


def build_slide_11(prs):
    """Slide 11: CI/CD Pipeline & Automated Verification."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "CI/CD AUTOMATION & VERIFICATION",
        "Automated Forensic Pipeline & Regression Test Suite",
        "Om Lanke (Technical Auditor) | Time: 8:45 – 9:15",
        11
    )

    # Left Card: CI/CD Pipeline Architecture
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "GITHUB CLASSROOM CI & PYTEST SUITE (22 ASSERTIONS)")
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.05), Inches(7.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    bullets = [
        ("CI Engine Architecture", "Workflow .github/workflows/classroom-ci.yml powered by Astral uv v5 setup for high-speed deterministic dependency installation."),
        ("Python 3.11 Runtime Support", "Resolves PEP 634 match/case syntax incompatibilities found in legacy Python 3.9 vivisect engine; guarantees 100% CI pass rate."),
        ("Cryptographic Test Group", "Validates dual SHA-256 manifests, metadata JSON schema, and prevents bitwise drift across repos (test_forensic_pipeline.py)."),
        ("Reverse Engineering Group", "Asserts raw Deflate decompression accuracy, 64-bit FNV-1a mathematical outputs, and XOR blocklist hit flags."),
        ("Statutory Test Group", "Ensures dynamic telemetry extraction, Part A / Part B Section 63 BSA certificate generation, and CERT-In template structure."),
        ("Execution Speed", "All 22 unit tests execute completely in under 0.25 seconds, proving production-grade forensic reproducibility.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_SLATE
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r = p.add_run()
        r.text = b_desc
        r.font.bold = False
        r.font.color.rgb = RGBColor(71, 85, 105)

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Automated Test Execution Suite",
        "Terminal (macOS zsh / bash)",
        "pytest tests/ -v",
        "Terminal prints live test execution showing 22 passed in ~0.20s across cryptographic, deobfuscation, legal, and documentation suites with 100% test coverage."
    )


def build_slide_12(prs):
    """Slide 12: Forensic Findings Matrix & Evaluator Q&A."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(
        slide,
        "CONCLUSION & EVALUATION MATRIX",
        "Forensic Findings Resolution & Evaluator Q&A",
        "Amandeep Singh, Omik Acharya, Om Lanke | Time: 9:15 – 10:00",
        12
    )

    # Left Card: 6 Findings Table
    add_card(slide, Inches(0.6), Inches(1.6), Inches(7.7), Inches(5.1), "FINAL ANSWERS TO 6 CORE CAPSTONE QUESTIONS")
    
    table_shape = slide.shapes.add_table(7, 3, Inches(0.8), Inches(2.1), Inches(7.3), Inches(4.4))
    table = table_shape.table
    table.columns[0].width = Inches(1.5)
    table.columns[1].width = Inches(2.6)
    table.columns[2].width = Inches(3.2)

    headers = ["Forensic Scope", "Investigation Question", "Forensic Group 10 Resolution"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_SOMAIYA_RED
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

    resolution_data = [
        ("1. Authenticity", "Was the infected DLL legitimate?", "Yes, trojanized during build compilation; had valid DigiCert signature."),
        ("2. Encryption", "Are internal tokens recoverable?", "Yes, deobfuscated via Base64 + raw Deflate (wbits=-15) revealing avsvmcloud.com."),
        ("3. Anti-Analysis", "How did it defeat security tools?", "Checked 120+ tools using 64-bit FNV-1a hashing + XOR mask; no plaintext names."),
        ("4. Network C2", "What protocol was used for C2?", "Covert DNS tunneling via avsvmcloud.com with DGA victim identification."),
        ("5. Cyber Law", "Is evidence admissible in court?", "Fully compliant with Section 63 BSA 2023 with Part A & B affirmations + CERT-In 6h rule."),
        ("6. Reproducibility", "Can results be verified by CI?", "Automated GitHub Actions CI running 22 pytest assertions with 100% green status.")
    ]

    for row_idx, data in enumerate(resolution_data, start=1):
        for col_idx, val in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Arial"
            p.font.size = Pt(7.8)
            p.font.bold = (col_idx == 0)
            p.font.color.rgb = COLOR_SUCCESS_GREEN if col_idx == 2 else COLOR_DARK_SLATE

    # Right: Side-by-Side Live Demo Box
    add_demo_box(
        slide,
        Inches(8.5), Inches(1.6), Inches(4.2), Inches(5.1),
        "Final Conclusion & Interactive Q&A",
        "Web Browser (docs/sunburst_simulation.html - Stage 11)",
        "Navigate to Stage 11 ('Conclusion') -> Present 6 verified findings.",
        "Displays 6 green checkmarks resolving all capstone questions. Team concludes presentation on schedule (9:45) and opens floor for evaluator and professor questions."
    )


def main():
    docs_dir = Path("docs")
    docs_dir.mkdir(parents=True, exist_ok=True)
    output_pptx = docs_dir / "SUNBURST_Forensic_Investigation_Group10.pptx"

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    print("[*] Generating Slide 1: Somaiya Title Slide...")
    build_slide_1(prs)

    print("[*] Generating Slide 2: Case Study — The Supply Chain Vector...")
    build_slide_2(prs)

    print("[*] Generating Slide 3: ISO/IEC 27037 Evidence Ingestion & Cryptographic Verification...")
    build_slide_3(prs)

    print("[*] Generating Slide 4: Static PE Architecture & Shannon Entropy...")
    build_slide_4(prs)

    print("[*] Generating Slide 5: Attack Execution Timeline — The 8-Stage Lifecycle...")
    build_slide_5(prs)

    print("[*] Generating Slide 6: String Deobfuscation (Mandiant FLOSS)...")
    build_slide_6(prs)

    print("[*] Generating Slide 7: Anti-Analysis Mechanics (64-Bit FNV-1a Hashing + XOR)...")
    build_slide_7(prs)

    print("[*] Generating Slide 8: Capability Mapping & ATT&CK (Mandiant CAPA)...")
    build_slide_8(prs)

    print("[*] Generating Slide 9: Indian Cyber Legal Framework (IT Act, CERT-In, DPDP)...")
    build_slide_9(prs)

    print("[*] Generating Slide 10: Legal Admissibility (BSA 2023 Section 63)...")
    build_slide_10(prs)

    print("[*] Generating Slide 11: CI/CD Pipeline & Automated Verification...")
    build_slide_11(prs)

    print("[*] Generating Slide 12: Forensic Findings Matrix & Evaluator Q&A...")
    build_slide_12(prs)

    prs.save(output_pptx)
    print(f"[+] Successfully generated 12-slide presentation: {output_pptx}")


if __name__ == "__main__":
    main()
