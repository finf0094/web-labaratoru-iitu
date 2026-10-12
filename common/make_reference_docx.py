"""Build common/reference.docx — the Word style template used by pandoc.

Starts from pandoc's default reference document and restyles it to typical
university report requirements: Times New Roman 12 pt, 1.5 line spacing,
justified body text, 2 cm / 3 cm margins, black headings, bordered tables.
"""
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

FONT = "Times New Roman"
OUT = Path(__file__).with_name("reference.docx")


def set_font(style, size=None, bold=None, italic=None):
    style.font.name = FONT
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.append(fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), FONT)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        fonts.attrib.pop(qn(attr), None)
    if size is not None:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic


def table_borders(style):
    tblpr = style.element.find(qn("w:tblPr"))
    if tblpr is None:
        tblpr = OxmlElement("w:tblPr")
        style.element.append(tblpr)
    old = tblpr.find(qn("w:tblBorders"))
    if old is not None:
        tblpr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblpr.append(borders)


def main():
    subprocess.run(
        ["pandoc", "-o", str(OUT), "--print-default-data-file", "reference.docx"],
        check=True,
    )
    doc = Document(str(OUT))

    for section in doc.sections:
        section.page_height, section.page_width = Cm(29.7), Cm(21.0)
        section.top_margin = section.bottom_margin = Cm(2)
        section.left_margin, section.right_margin = Cm(3), Cm(1.5)

    styles = {s.name: s for s in doc.styles}
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if name in styles:
            st = styles[name]
            set_font(st, 12)
            pf = st.paragraph_format
            pf.line_spacing = 1.5 if name != "Compact" else 1.15
            pf.space_before, pf.space_after = Pt(0), Pt(6 if name != "Compact" else 0)
            if name in ("Body Text", "First Paragraph"):
                pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                pf.first_line_indent = Cm(1.25)

    sizes = {"Title": 16, "Subtitle": 14, "Heading 1": 14, "Heading 2": 13,
             "Heading 3": 12, "Heading 4": 12}
    for name, size in sizes.items():
        st = styles[name]
        set_font(st, size, bold=True, italic=False)
        st.paragraph_format.space_before = Pt(12)
        st.paragraph_format.space_after = Pt(6)
        st.paragraph_format.keep_with_next = True
        if name in ("Title", "Subtitle"):
            st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for name in ("Author", "Date", "Abstract"):
        if name in styles:
            set_font(styles[name], 12)
            styles[name].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for name in ("Table Caption", "Image Caption", "Caption"):
        if name in styles:
            set_font(styles[name], 12, bold=False, italic=False)

    if "Bibliography" in styles:
        st = styles["Bibliography"]
        set_font(st, 12)
        st.paragraph_format.line_spacing = 1.15
        st.paragraph_format.space_after = Pt(4)

    if "Table" in styles:
        st = styles["Table"]
        set_font(st, 11)
        table_borders(st)

    for name in ("Source Code", "Verbatim Char"):
        if name in styles:
            styles[name].font.size = Pt(10)

    doc.save(str(OUT))
    print(f"written {OUT}")


if __name__ == "__main__":
    sys.exit(main())
