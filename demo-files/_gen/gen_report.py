"""Tạo Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx (Lab 1, Lab 3).

Hệ thống bệnh viện giả định, 4 cơ sở ẩn danh A-D (không gắn với bệnh viện có thật). Số liệu được thiết kế để có các
"điểm đáng chú ý" mà đáp án trong lab dựa vào:
  - Công suất giường Cơ sở D 96% (khoa Sản 102%), Cơ sở B chỉ 58%: một nơi quá tải, một nơi còn trống
  - Tỷ lệ nghỉ việc điều dưỡng toàn hệ thống 18% (ngành 12%), giờ làm thêm cao ở các khoa quá tải
  - Chi phí vật tư y tế vượt kế hoạch 27%
  - Điểm hài lòng Cơ sở C giảm từ 4,5 xuống 4,1, góp ý về thái độ giao tiếp cao bất thường ở Cơ sở C
  - "Thời gian chờ xuất viện" là nhóm góp ý lớn nhất, tập trung ở Cơ sở D và C
Số liệu cấp cơ sở được tính từ số liệu cấp khoa nên luôn khớp nhau. Mọi ô là giá trị (không công thức),
không cần mở Excel để tính lại. Chạy xong in đáp án tham khảo cho Lab 3.
"""
from collections import Counter
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

OUT = Path(__file__).resolve().parent.parent / "Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx"

F = "Arial"
TITLE = Font(name=F, bold=True, size=14, color="0B3D5C")
NOTE = Font(name=F, italic=True, size=9, color="595959")
BODY = Font(name=F, size=10)
HDR = Font(name=F, bold=True, size=10, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor="0B3D5C")
DISCLAIMER = "Số liệu giả định, chỉ dùng cho workshop Copilot. Không chứa thông tin người bệnh."

SITES = ["Cơ sở A", "Cơ sở B", "Cơ sở C", "Cơ sở D"]  # D cố ý nằm cuối để bài sắp xếp thấy rõ thay đổi
DEPTS = ["Sản", "Nhi - Sơ sinh", "Ngoại - Gây mê hồi sức", "Nội tổng hợp", "Cấp cứu"]

# Theo khoa: (giường, công suất, điều dưỡng, ĐD nghỉ việc trong quý, giờ làm thêm BQ/ĐD/tháng, sự cố an toàn báo cáo)
DEPT_DATA = {
    "Cơ sở A": [(50, 0.80, 60, 2, 12, 3), (35, 0.74, 40, 1, 10, 2), (25, 0.70, 30, 1, 9, 1), (25, 0.62, 30, 1, 8, 1), (15, 0.60, 20, 1, 13, 2)],
    "Cơ sở B": [(70, 0.66, 45, 2, 8, 2), (45, 0.60, 30, 1, 7, 1), (35, 0.55, 25, 1, 6, 1), (30, 0.50, 25, 0, 6, 1), (20, 0.43, 15, 1, 9, 1)],
    "Cơ sở C": [(70, 0.89, 90, 4, 21, 5), (45, 0.84, 60, 3, 17, 3), (35, 0.77, 45, 2, 12, 2), (30, 0.70, 35, 1, 10, 2), (20, 0.66, 30, 2, 18, 3)],
    "Cơ sở D": [(100, 1.02, 140, 8, 26, 9), (70, 0.98, 95, 6, 22, 6), (50, 0.93, 75, 3, 19, 4), (50, 0.88, 60, 2, 14, 3), (30, 0.89, 50, 3, 24, 5)],
}
# Cấp cơ sở: (khám ngoại trú Q3, vật tư KH, vật tư TH (tỷ), hài lòng Q2, hài lòng Q3, chờ xuất viện TB (giờ))
SITE_DATA = {
    "Cơ sở A": (42800, 8.0, 9.4, 4.4, 4.5, 2.1),
    "Cơ sở B": (27600, 6.0, 7.0, 4.3, 4.4, 1.8),
    "Cơ sở C": (61200, 14.0, 17.2, 4.5, 4.1, 2.9),
    "Cơ sở D": (98500, 20.0, 27.4, 4.6, 4.5, 3.4),
}
BIRTHS = {"Cơ sở A": (260, 270, 255), "Cơ sở B": (150, 160, 155), "Cơ sở C": (340, 355, 350), "Cơ sở D": (610, 645, 630)}
FEEDBACK_GROUPS = ["Thời gian chờ thủ tục xuất viện", "Thời gian chờ khám", "Thái độ giao tiếp",
                   "Viện phí và thanh toán", "Cơ sở vật chất", "Ăn uống và vệ sinh"]
FEEDBACK = {  # số góp ý, phàn nàn trong quý 3 theo nhóm
    "Cơ sở A": (12, 15, 6, 7, 5, 4),
    "Cơ sở B": (6, 9, 3, 4, 6, 3),
    "Cơ sở C": (47, 22, 31, 14, 8, 6),
    "Cơ sở D": (64, 41, 18, 22, 15, 9),
}

wb = Workbook()


def sheet(ws, title, note, head, rows, fmts, table_name, widths):
    ws["A1"], ws["A2"] = title, note
    ws["A1"].font, ws["A2"].font = TITLE, NOTE
    for i, h in enumerate(head, 1):
        c = ws.cell(row=4, column=i, value=h)
        c.font, c.fill = HDR, HDR_FILL
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for r, row in enumerate(rows, 5):
        for i, v in enumerate(row, 1):
            c = ws.cell(row=r, column=i, value=v)
            c.font = BODY
            if fmts[i - 1]:
                c.number_format = fmts[i - 1]
    t = Table(displayName=table_name, ref=f"A4:{get_column_letter(len(head))}{4 + len(rows)}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(t)
    ws.row_dimensions[4].height = 45
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "B5"


def agg(site):
    d = DEPT_DATA[site]
    beds = sum(x[0] for x in d)
    occ = sum(x[0] * x[1] for x in d) / beds
    nurses = sum(x[2] for x in d)
    quits = sum(x[3] for x in d)
    ot = sum(x[2] * x[4] for x in d) / nurses
    return beds, occ, nurses, quits, ot


# ---------------------------------------------------------------- Sheet 1: tổng hợp theo cơ sở
rows = []
for s in SITES:
    beds, occ, nurses, quits, ot = agg(s)
    opd, sk, st, s2, s3, wait = SITE_DATA[s]
    rows.append([s, beds, round(occ, 3), sum(BIRTHS[s]), opd, nurses, quits, round(quits * 4 / nurses, 3), round(ot, 1),
                 sk, st, round(st / sk - 1, 3), s2, s3, wait])
sheet(wb.active, "Báo cáo Hoạt động Q3/2026 - 4 cơ sở",
      "Kỳ báo cáo: 01/07/2026 - 30/09/2026. Chi phí vật tư: tỷ đồng. Hài lòng: thang điểm 5. " + DISCLAIMER,
      ["Cơ sở", "Số giường", "Công suất giường", "Số ca sinh Q3", "Lượt khám ngoại trú Q3", "Số điều dưỡng",
       "Điều dưỡng nghỉ việc trong quý", "Tỷ lệ nghỉ việc điều dưỡng (năm hóa)", "Giờ làm thêm BQ / điều dưỡng / tháng",
       "Chi phí vật tư kế hoạch (tỷ)", "Chi phí vật tư thực hiện (tỷ)", "Vật tư vượt kế hoạch", "Điểm hài lòng Q2",
       "Điểm hài lòng Q3", "Thời gian chờ xuất viện TB (giờ)"],
      rows, [None, "#,##0", "0%", "#,##0", "#,##0", "#,##0", "#,##0", "0.0%", "0.0", "0.0", "0.0", "0.0%", "0.0", "0.0", "0.0"],
      "TongHopCoSo", [14, 10, 12, 11, 13, 11, 13, 14, 13, 13, 13, 12, 11, 11, 13])
wb.active.title = "Tổng hợp cơ sở"

# ---------------------------------------------------------------- Sheet 2: theo khoa
ws = wb.create_sheet("Theo khoa")
dept_rows = []
for s in SITES:
    for dept, (beds, occ, nurses, quits, ot, inc) in zip(DEPTS, DEPT_DATA[s]):
        dept_rows.append([s, dept, beds, occ, nurses, quits, ot, inc])
sheet(ws, "Số liệu theo khoa - Q3/2026", "Công suất giường có thể vượt 100% khi phải kê thêm giường. " + DISCLAIMER,
      ["Cơ sở", "Khoa", "Số giường", "Công suất giường", "Số điều dưỡng",
       "Điều dưỡng nghỉ việc trong quý", "Giờ làm thêm BQ / điều dưỡng / tháng", "Sự cố an toàn được báo cáo"],
      dept_rows, [None, None, "#,##0", "0%", "#,##0", "#,##0", "0", "#,##0"],
      "TheoKhoa", [11, 24, 10, 12, 12, 14, 15, 13])

# ---------------------------------------------------------------- Sheet 3: ca sinh theo tháng
ws = wb.create_sheet("Ca sinh theo tháng")
sheet(ws, "Số ca sinh theo tháng - Q3/2026", DISCLAIMER, ["Cơ sở", "Tháng 7", "Tháng 8", "Tháng 9", "Tổng Q3"],
      [[s, *BIRTHS[s], sum(BIRTHS[s])] for s in SITES], [None, "#,##0", "#,##0", "#,##0", "#,##0"],
      "CaSinhTheoThang", [14, 11, 11, 11, 11])

# ---------------------------------------------------------------- Sheet 4: góp ý người bệnh
ws = wb.create_sheet("Góp ý người bệnh")
fb_rows = [[s, *FEEDBACK[s], sum(FEEDBACK[s])] for s in SITES]
sheet(ws, "Góp ý và phàn nàn của người bệnh theo nhóm - Q3/2026",
      "Số lượt góp ý qua hòm thư, mã QR, email và tổng đài, đã phân nhóm. " + DISCLAIMER,
      ["Cơ sở", *FEEDBACK_GROUPS, "Tổng"], fb_rows, [None] + ["#,##0"] * 7,
      "GopYNguoiBenh", [14, 16, 13, 13, 14, 13, 13, 10])

# ---------------------------------------------------------------- Sheet 5: chỉ số hệ thống + chuẩn ngành
tot_beds = sum(agg(s)[0] for s in SITES)
occ_all = sum(agg(s)[0] * agg(s)[1] for s in SITES) / tot_beds
nurses_all = sum(agg(s)[2] for s in SITES)
turnover = sum(agg(s)[3] for s in SITES) * 4 / nurses_all
ot_all = sum(agg(s)[2] * agg(s)[4] for s in SITES) / nurses_all
sup_kh, sup_th = sum(SITE_DATA[s][1] for s in SITES), sum(SITE_DATA[s][2] for s in SITES)
births = sum(sum(b) for b in BIRTHS.values())
ws = wb.create_sheet("Chỉ số hệ thống")
sheet(ws, "Chỉ số toàn hệ thống và chuẩn tham khảo - Q3/2026", DISCLAIMER,
      ["Chỉ số", "Kế hoạch Q3", "Thực hiện Q3", "Chuẩn ngành tham khảo", "Ghi chú"],
      [
          ["Tổng số ca sinh", 4000, births, None, ""],
          ["Công suất giường bình quân", 0.80, round(occ_all, 3), 0.85, "Cơ sở D 96%, Cơ sở B 58%"],
          ["Tỷ lệ nghỉ việc điều dưỡng (năm hóa)", 0.12, round(turnover, 3), 0.12, "Cao nhất tại Cơ sở D"],
          ["Giờ làm thêm BQ / điều dưỡng / tháng", 12, round(ot_all, 1), 12, "Cao nhất tại khoa Sản Cơ sở D"],
          ["Chi phí vật tư y tế (tỷ đồng)", sup_kh, sup_th, None, f"Vượt kế hoạch {sup_th / sup_kh - 1:.0%}"],
          ["Điểm hài lòng người bệnh bình quân (thang 5)", 4.5, 4.4, 4.5, "Cơ sở C giảm từ 4,5 xuống 4,1"],
          ["Thời gian chờ thủ tục xuất viện TB (giờ)", 2.0, 2.6, 2.0, "Nhiều góp ý tại Cơ sở D và Cơ sở C"],
      ],
      [None, "General", "General", "General", None], "ChiSoHeThong", [44, 13, 13, 14, 36])
for r, fmt in zip(range(5, 12), ["#,##0", "0.0%", "0.0%", "0.0", "0.0", "0.0", "0.0"]):
    for col in (2, 3, 4):
        ws.cell(row=r, column=col).number_format = fmt

wb.save(OUT)

# ---------------------------------------------------------------- đáp án tham khảo
print(f"saved {OUT.name}")
print(f"system: occ {occ_all:.1%}, turnover {turnover:.1%}, OT {ot_all:.1f}h, supplies {sup_kh}->{sup_th} "
      f"({sup_th / sup_kh - 1:.1%}), births {births}")
for s in SITES:
    b, o, n, q, ot = agg(s)
    print(f"  {s}: beds {b} occ {o:.1%} nurses {n} quits {q} turnover {q * 4 / n:.1%} OT {ot:.1f}")


def level(occ, ot):
    hits = (occ > 0.9) + (ot > 20)
    return ["Xanh", "Vàng", "Đỏ"][hits]


levels = Counter()
for s in SITES:
    for dept, (beds, occ, nurses, quits, ot, inc) in zip(DEPTS, DEPT_DATA[s]):
        lv = level(occ, ot)
        levels[(s, lv)] += 1
        if lv != "Xanh":
            print(f"  Lab 3 BT2: {s} - {dept}: {lv} (occ {occ:.0%}, OT {ot})")
print("  Lab 3 BT2 totals:", {lv: sum(v for (s, l), v in levels.items() if l == lv) for lv in ("Đỏ", "Vàng", "Xanh")})
tot = [sum(FEEDBACK[s][i] for s in SITES) for i in range(len(FEEDBACK_GROUPS))]
all_fb = sum(tot)
for g, t in sorted(zip(FEEDBACK_GROUPS, tot), key=lambda x: -x[1]):
    print(f"  Lab 3 BT3: {g}: {t} ({t / all_fb:.0%})")
dc = FEEDBACK["Cơ sở D"][0] + FEEDBACK["Cơ sở C"][0]
print(f"  discharge D+C: {dc}/{tot[0]} = {dc / tot[0]:.0%}; total feedback {all_fb}")
