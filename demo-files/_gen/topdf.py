"""Chuyển các file .docx trong _gen/_pdf_src sang PDF (lưu ở demo-files/) bằng Microsoft Edge headless.

Không cần Word hay thư viện PDF: đọc docx bằng python-docx, dựng HTML đơn giản (tiêu đề, đoạn, gạch đầu dòng,
bảng, chú thích chân trang), rồi để Edge in ra PDF khổ A4.
"""
import html
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

GEN = Path(__file__).resolve().parent
SRC, DST = GEN / "_pdf_src", GEN.parent
EDGE_PATHS = [Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
              Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")]

CSS = """
@page { size: A4; margin: 20mm 22mm; }
body { font-family: Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
.title { text-align: center; font-size: 16pt; font-weight: bold; color: #0B3D5C; margin: 0 0 4pt; }
.sub { text-align: center; font-style: italic; font-size: 9.5pt; margin: 0 0 14pt; }
h1 { font-size: 13pt; color: #0B3D5C; margin: 14pt 0 4pt; }
h2 { font-size: 11.5pt; color: #0B3D5C; margin: 10pt 0 4pt; }
p { margin: 0 0 6pt; text-align: justify; }
ul { margin: 0 0 6pt 18pt; padding: 0; } li { margin-bottom: 3pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 9.5pt; }
th { background: #0B3D5C; color: #fff; text-align: left; }
th, td { border: 1px solid #999; padding: 4pt 6pt; vertical-align: top; }
.foot { margin-top: 18pt; border-top: 1px solid #ccc; padding-top: 4pt; font-size: 8pt; font-style: italic; text-align: center; }
"""


def runs_html(p):
    out = []
    for r in p.runs:
        t = html.escape(r.text)
        out.append(f"<b>{t}</b>" if r.bold else t)
    return "".join(out)


def to_html(path):
    doc = Document(path)
    parts, in_list, n_title = [], False, 0
    for block in doc.element.body.iterchildren():
        tag = block.tag.rsplit("}", 1)[-1]
        if tag == "tbl":
            if in_list:
                parts.append("</ul>"); in_list = False
            t = Table(block, doc)
            rows = ["<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{html.escape(c.text)}</{'th' if i == 0 else 'td'}>"
                                     for c in row.cells) + "</tr>" for i, row in enumerate(t.rows)]
            parts.append("<table>" + "".join(rows) + "</table>")
            continue
        if tag != "p":
            continue
        p = Paragraph(block, doc)
        if not p.text.strip():
            continue
        style = p.style.name
        is_li = style.startswith("List")
        if in_list and not is_li:
            parts.append("</ul>"); in_list = False
        if is_li:
            if not in_list:
                parts.append("<ul>"); in_list = True
            parts.append(f"<li>{runs_html(p)}</li>")
        elif style == "Heading 1":
            parts.append(f"<h1>{html.escape(p.text)}</h1>")
        elif style.startswith("Heading"):
            parts.append(f"<h2>{html.escape(p.text)}</h2>")
        elif n_title < 2 and p.alignment is not None and int(p.alignment) == 1:  # tiêu đề và dòng phụ căn giữa
            parts.append(f"<p class='{'title' if n_title == 0 else 'sub'}'>{html.escape(p.text)}</p>")
            n_title += 1
        else:
            parts.append(f"<p>{runs_html(p)}</p>")
    if in_list:
        parts.append("</ul>")
    footer = " ".join(p.text for p in doc.sections[0].footer.paragraphs if p.text.strip())
    return (f"<!doctype html><html lang='vi'><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            + "".join(parts) + f"<p class='foot'>{html.escape(footer)}</p></body></html>")


def main():
    edge = next((p for p in EDGE_PATHS if p.exists()), None)
    if not edge:
        raise SystemExit("Không tìm thấy Microsoft Edge")
    with tempfile.TemporaryDirectory() as tmp:
        for i, src in enumerate(sorted(SRC.glob("*.docx"))):
            page = Path(tmp) / f"doc{i}.html"
            out = Path(tmp) / f"doc{i}.pdf"
            page.write_text(to_html(src), encoding="utf-8")
            subprocess.run([str(edge), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                            f"--user-data-dir={Path(tmp) / 'profile'}",
                            f"--print-to-pdf={out}", page.as_uri()], check=True, timeout=120,
                           stdin=subprocess.DEVNULL, capture_output=True)
            final = DST / (src.stem + ".pdf")
            final.write_bytes(out.read_bytes())
            print("pdf:", final.name, f"{final.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
