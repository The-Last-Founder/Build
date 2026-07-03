#!/usr/bin/env python3
"""Generate Build one-pager PDF from ONE_PAGER.md content."""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --- Fonts ---
FONT_DIR = "/usr/share/fonts/truetype/lato"
pdfmetrics.registerFont(TTFont("Lato", f"{FONT_DIR}/Lato-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Bold", f"{FONT_DIR}/Lato-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Italic", f"{FONT_DIR}/Lato-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Light", f"{FONT_DIR}/Lato-Light.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Black", f"{FONT_DIR}/Lato-Black.ttf"))

# --- Brand colours ---
DARK_BG    = HexColor("#0D1117")   # GitHub-dark near-black
ACCENT     = HexColor("#FF6B35")   # warm orange
ACCENT2    = HexColor("#4ECDC4")   # teal
MID_GREY   = HexColor("#8B949E")   # muted text
LIGHT_GREY = HexColor("#21262D")   # card / panel bg
BORDER     = HexColor("#30363D")   # border / divider
TEXT_LIGHT = HexColor("#E6EDF3")   # body text on dark bg
TEXT_DIM   = HexColor("#8B949E")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm

# --- Styles ---
def make_styles():
    styles = {}

    styles["title"] = ParagraphStyle(
        "title",
        fontName="Lato-Black",
        fontSize=32,
        leading=38,
        textColor=white,
        spaceAfter=2 * mm,
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle",
        fontName="Lato",
        fontSize=13,
        leading=18,
        textColor=TEXT_LIGHT,
        spaceAfter=6 * mm,
    )
    styles["section_header"] = ParagraphStyle(
        "section_header",
        fontName="Lato-Bold",
        fontSize=13,
        leading=17,
        textColor=ACCENT,
        spaceBefore=5 * mm,
        spaceAfter=2 * mm,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Lato",
        fontSize=9.5,
        leading=14,
        textColor=TEXT_LIGHT,
        spaceAfter=2 * mm,
    )
    styles["body_dim"] = ParagraphStyle(
        "body_dim",
        fontName="Lato",
        fontSize=9,
        leading=13,
        textColor=TEXT_DIM,
        spaceAfter=1.5 * mm,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Lato",
        fontSize=9.5,
        leading=14,
        textColor=TEXT_LIGHT,
        leftIndent=10,
        spaceAfter=1 * mm,
        bulletIndent=0,
    )
    styles["cta_label"] = ParagraphStyle(
        "cta_label",
        fontName="Lato-Bold",
        fontSize=10,
        leading=14,
        textColor=ACCENT2,
        spaceAfter=1 * mm,
    )
    styles["footer"] = ParagraphStyle(
        "footer",
        fontName="Lato",
        fontSize=8,
        leading=11,
        textColor=TEXT_DIM,
        alignment=1,  # center
    )
    styles["tag"] = ParagraphStyle(
        "tag",
        fontName="Lato-Bold",
        fontSize=8,
        leading=11,
        textColor=ACCENT,
    )
    return styles


def build_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Build — One Pager",
        author="The Last Founder",
        subject="Build — Open-Source Builder MMO",
    )

    S = make_styles()
    story = []

    col_width = PAGE_W - 2 * MARGIN

    # ── HERO HEADER ─────────────────────────────────────────────────────────
    hero_data = [[
        Paragraph("<font color='#FF6B35'><b>Build</b></font>", S["title"]),
        Paragraph(
            "The open-source learn-by-shipping community<br/>"
            "for people building real products with AI agents.",
            S["subtitle"],
        ),
    ]]
    hero_table = Table(
        hero_data,
        colWidths=[col_width * 0.28, col_width * 0.72],
        rowHeights=[None],
    )
    hero_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (0, -1), 10),
        ("RIGHTPADDING",  (0, 0), (0, -1), 4),
        ("LEFTPADDING",   (1, 0), (1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [4]),
    ]))
    story.append(hero_table)
    story.append(Spacer(1, 4 * mm))

    # ── DIVIDER ─────────────────────────────────────────────────────────────
    story.append(HRFlowable(
        width="100%", thickness=1, color=ACCENT, spaceAfter=4 * mm
    ))

    # ── TWO-COLUMN LAYOUT: problem / solution ───────────────────────────────
    problem_items = [
        "Passive learning — courses exist but most people don't ship.",
        "No shared workflow for agent-first teams.",
        "Isolated builders without co-builders or accountability.",
        "Powerful AI tools, but no community lifecycle to tie them together.",
    ]
    solution_items = [
        "Ship real products in the open with builders at all skill levels.",
        "AI agents as first-class team members, not just coding assistants.",
        "A shared, evolving methodology — we capture what works.",
        "GitHub-native ops: Issues, PRs, and markdown are the source of truth.",
    ]

    def make_bullet_list(items, style):
        return [Paragraph(f"• {item}", style) for item in items]

    problem_cell = [
        Paragraph("The Problem", S["section_header"]),
    ] + make_bullet_list(problem_items, S["bullet"])

    solution_cell = [
        Paragraph("Our Solution", S["section_header"]),
    ] + make_bullet_list(solution_items, S["bullet"])

    two_col = Table(
        [[problem_cell, solution_cell]],
        colWidths=[col_width * 0.48, col_width * 0.48],
        spaceBefore=0,
    )
    two_col.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), LIGHT_GREY),
        ("BACKGROUND",    (1, 0), (1, 0), LIGHT_GREY),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("ROUNDEDCORNERS", [4]),
        ("LINEBEFORE",    (1, 0), (1, 0), 1, BORDER),
        ("RIGHTPADDING",  (0, 0), (0, 0), 6),
    ]))
    story.append(two_col)
    story.append(Spacer(1, 4 * mm))

    # ── COMPETITIVE LANDSCAPE ───────────────────────────────────────────────
    story.append(Paragraph("Existing Solutions — and Why Build is Different", S["section_header"]))

    comp_data = [
        [
            Paragraph("<b>Solution</b>", S["body"]),
            Paragraph("<b>Gap</b>", S["body"]),
            Paragraph("<b>Build Advantage</b>", S["body"]),
        ],
        [
            Paragraph("Online courses / bootcamps", S["body"]),
            Paragraph("Passive; ends at graduation", S["body_dim"]),
            Paragraph("Persistent, real shipping, ongoing community", S["body"]),
        ],
        [
            Paragraph("Accelerators", S["body"]),
            Paragraph("Expensive, exclusive, short-term cohort", S["body_dim"]),
            Paragraph("Open to all skill levels, no cost barrier", S["body"]),
        ],
        [
            Paragraph("Open-source contribution", S["body"]),
            Paragraph("Steep onboarding; rarely agent-native", S["body_dim"]),
            Paragraph("Agent-native from day 0; guided methodology", S["body"]),
        ],
        [
            Paragraph("Discord / Slack communities", S["body"]),
            Paragraph("Discussion-heavy; no structured build process", S["body_dim"]),
            Paragraph("GitHub-native ops; ship first, then discuss", S["body"]),
        ],
        [
            Paragraph("Hackathons", S["body"]),
            Paragraph("Short burst; projects die after the weekend", S["body_dim"]),
            Paragraph("Persistent quests; ongoing parties; real launches", S["body"]),
        ],
    ]

    comp_widths = [col_width * 0.28, col_width * 0.36, col_width * 0.36]
    comp_table = Table(comp_data, colWidths=comp_widths)
    comp_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_BG),
        ("TEXTCOLOR",     (0, 0), (-1, 0), ACCENT),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [LIGHT_GREY, HexColor("#1C2128")]),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("GRID",          (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 4 * mm))

    # ── ADVANTAGES + PILOT PROJECT side by side ─────────────────────────────
    adv_items = [
        ("Agent-native from day 0", "Agents are collaborators, not just assistants."),
        ("Open-source everything", "Code, methodology, and lessons are all public."),
        ("Human-first MMO model", "Quests, parties, XP — keeps builders engaged."),
        ("Real products", "Quest Board is our dogfooded example."),
        ("GitHub-native", "No extra platform; Issues & PRs are the source of truth."),
        ("Learn by shipping", "Fastest path: build real things in public."),
    ]

    adv_rows = []
    for title, desc in adv_items:
        adv_rows.append(Paragraph(
            f"<font color='#FF6B35'><b>{title}</b></font> — {desc}",
            S["body"]
        ))

    pilot_content = [
        Paragraph("Pilot Project: Quest Board", S["section_header"]),
        Paragraph(
            "A GitHub-native, spec-first board where humans and AI agents propose, "
            "rank, build, and launch open-source projects together.",
            S["body"],
        ),
        Spacer(1, 2 * mm),
        Paragraph("This is Build's first quest — and its proof of concept.", S["body_dim"]),
        Spacer(1, 2 * mm),
        Paragraph(
            "→ <u>github.com/The-Last-Founder/quest-board</u>",
            S["cta_label"],
        ),
    ]

    bottom_two = Table(
        [[
            [Paragraph("Unique Advantages", S["section_header"])] + adv_rows,
            pilot_content,
        ]],
        colWidths=[col_width * 0.50, col_width * 0.46],
    )
    bottom_two.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (0, 0), 8),
        ("BACKGROUND",    (1, 0), (1, 0), LIGHT_GREY),
        ("LEFTPADDING",   (1, 0), (1, 0), 10),
        ("RIGHTPADDING",  (1, 0), (1, 0), 10),
        ("TOPPADDING",    (1, 0), (1, 0), 8),
        ("BOTTOMPADDING", (1, 0), (1, 0), 8),
        ("ROUNDEDCORNERS", [4]),
    ]))
    story.append(bottom_two)
    story.append(Spacer(1, 5 * mm))

    # ── FOOTER ──────────────────────────────────────────────────────────────
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BORDER, spaceAfter=3 * mm
    ))

    footer_data = [[
        Paragraph(
            "<b>Join the Community</b><br/>"
            "💬 WhatsApp: chat.whatsapp.com/DgKpG63438y8N7D3pHJ57t",
            S["footer"],
        ),
        Paragraph(
            "<b>GitHub</b><br/>"
            "github.com/The-Last-Founder/Build",
            S["footer"],
        ),
        Paragraph(
            "<b>Website</b><br/>"
            "thelastfounder.com",
            S["footer"],
        ),
    ]]
    footer_table = Table(
        footer_data,
        colWidths=[col_width * 0.50, col_width * 0.26, col_width * 0.24],
    )
    footer_table.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE",    (1, 0), (-1, -1), 0.5, BORDER),
    ]))
    story.append(footer_table)

    # ── BUILD ────────────────────────────────────────────────────────────────
    doc.build(story)
    print(f"✓  PDF written to {output_path}")


if __name__ == "__main__":
    out = "/home/runner/work/Build/Build/artifacts/build-one-pager.pdf"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build_pdf(out)
