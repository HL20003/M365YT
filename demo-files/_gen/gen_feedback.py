"""Tạo Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx cho Lab 3 Bài tập 3 (tạo skill).

Mô phỏng file xuất từ hệ thống tiếp nhận góp ý: dòng ghi chú phía trên tiêu đề, dòng trống, dòng trùng, tên cơ sở /
nhóm góp ý / mức độ viết không thống nhất, ngày lẫn kiểu ngày và kiểu chữ. Hai sheet T9 và T10 cùng cấu trúc để học viên
tạo skill trên T9 rồi chạy lại trên T10. Không có cột nào chứa thông tin người bệnh (không tên, không mã hồ sơ).

Số góp ý hợp lệ theo cơ sở và nhóm được cố định trong COUNTS, khớp với báo cáo quý 3 (T9 xấp xỉ 1/3 quý):
  - T9: "Thời gian chờ thủ tục xuất viện" lớn nhất (44/127), 86% ở Cơ sở D và C
  - T10: "Thái độ giao tiếp" tăng từ 19 lên 29, riêng Cơ sở C từ 10 lên 19
  - T9 có 1 dòng bỏ trống Cơ sở: skill phải đánh dấu "Cần kiểm tra", không tự đoán
Chạy xong in đáp án cho người hướng dẫn.
"""
import random
from collections import Counter
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

OUT = Path(__file__).resolve().parent.parent / "Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx"
random.seed(2609)

SITES = ["Cơ sở A", "Cơ sở B", "Cơ sở C", "Cơ sở D"]
SITE_VARIANTS = {s: [s, f"CS {s[-1]}", f"CS{s[-1]}", f"cơ sở {s[-1].lower()}", f"CS-{s[-1]}"] for s in SITES}
GROUPS = ["Thời gian chờ thủ tục xuất viện", "Thời gian chờ khám", "Thái độ giao tiếp",
          "Viện phí và thanh toán", "Cơ sở vật chất", "Ăn uống và vệ sinh"]
GROUP_VARIANTS = {
    "Thời gian chờ thủ tục xuất viện": ["Thời gian chờ thủ tục xuất viện", "Chờ xuất viện", "TG chờ xuất viện",
                                        "thoi gian cho xuat vien"],
    "Thời gian chờ khám": ["Thời gian chờ khám", "Chờ khám", "thời gian chờ khám", "Thoi gian cho kham"],
    "Thái độ giao tiếp": ["Thái độ giao tiếp", "Thái độ", "thai do giao tiep", "Thái độ phục vụ"],
    "Viện phí và thanh toán": ["Viện phí và thanh toán", "Viện phí", "Thanh toán", "vien phi"],
    "Cơ sở vật chất": ["Cơ sở vật chất", "CSVC", "co so vat chat"],
    "Ăn uống và vệ sinh": ["Ăn uống và vệ sinh", "Ăn uống, vệ sinh", "Vệ sinh", "an uong ve sinh"],
}
LEVEL_VARIANTS = {"Cao": ["Cao", "cao", "CAO", "High"], "Trung bình": ["Trung bình", "TB", "trung bình", "Medium"],
                  "Thấp": ["Thấp", "thấp", "Low"]}
LEVEL_W = {"Thời gian chờ thủ tục xuất viện": [50, 40, 10], "Thời gian chờ khám": [35, 50, 15],
           "Thái độ giao tiếp": [55, 35, 10], "Viện phí và thanh toán": [20, 50, 30],
           "Cơ sở vật chất": [15, 45, 40], "Ăn uống và vệ sinh": [10, 45, 45]}
DEPTS = ["Sản", "Nhi - Sơ sinh", "Ngoại - Gây mê hồi sức", "Nội tổng hợp", "Cấp cứu", "Khám bệnh"]
CHANNELS = ["Hotline", "Zalo OA", "Hòm thư góp ý", "Khảo sát khi xuất viện", "Fanpage"]
STATUS = ["Đã xử lý", "Đang xử lý", "Mới", "đã xử lý"]

TEXTS = {
    "Thời gian chờ thủ tục xuất viện": ["Chờ hơn 4 giờ mới nhận được giấy ra viện", "Đã báo xuất viện từ sáng, chiều mới làm xong thủ tục",
                                        "Không ai thông báo phải chờ bao lâu để ra viện", "Chờ kết quả xét nghiệm cuối cùng nên trễ xuất viện"],
    "Thời gian chờ khám": ["Lấy số từ 6 giờ sáng, 10 giờ mới được khám", "Chờ đọc kết quả siêu âm quá lâu",
                           "Bảng gọi số không hoạt động, phải hỏi lại nhiều lần"],
    "Thái độ giao tiếp": ["Người nhà hỏi tình trạng sản phụ nhưng được trả lời cộc lốc", "Nhân viên quầy tiếp đón không hướng dẫn rõ",
                          "Ca đêm gọi chuông lâu không có người đến, khi đến lại tỏ ra khó chịu", "Bị nói to trước mặt người bệnh khác"],
    "Viện phí và thanh toán": ["Bảng kê chi phí khó hiểu, không ai giải thích", "Quầy thanh toán chỉ có 1 người làm",
                               "Chưa rõ khoản nào bảo hiểm chi trả"],
    "Cơ sở vật chất": ["Điều hòa phòng bệnh không mát", "Thiếu ghế chờ ở khu khám", "Thang máy chờ lâu giờ cao điểm"],
    "Ăn uống và vệ sinh": ["Nhà vệ sinh khu nội trú chưa sạch buổi tối", "Suất ăn cho sản phụ ít lựa chọn",
                           "Thùng rác hành lang đầy chưa được thu gom"],
}

# Số góp ý hợp lệ: cơ sở -> số lượt theo thứ tự GROUPS
COUNTS = {
    "T9": {"Cơ sở A": (4, 5, 2, 2, 2, 1), "Cơ sở B": (2, 3, 1, 1, 2, 1),
           "Cơ sở C": (16, 7, 10, 5, 3, 2), "Cơ sở D": (22, 14, 6, 7, 5, 3)},
    "T10": {"Cơ sở A": (4, 5, 2, 3, 2, 1), "Cơ sở B": (2, 3, 1, 1, 1, 1),
            "Cơ sở C": (15, 8, 19, 5, 3, 2), "Cơ sở D": (21, 15, 7, 7, 5, 3)},
}
MONTHS = [("T9", 9, 8, 3, 1), ("T10", 10, 6, 3, 0)]  # (sheet, tháng, số dòng trùng, số dòng trống, số dòng thiếu cơ sở)
UNKNOWN = "Cần kiểm tra"


def make_rows(name, month, n_unknown):
    rows = []
    cells = [(s, g, n) for s, ns in COUNTS[name].items() for g, n in zip(GROUPS, ns)]
    cells += [(UNKNOWN, "Cơ sở vật chất", 1)] * n_unknown
    for site, group, n in cells:
        for _ in range(n):
            dept = "Khám bệnh" if group == "Thời gian chờ khám" else random.choice(DEPTS[:5])
            level = random.choices(["Cao", "Trung bình", "Thấp"], weights=LEVEL_W[group])[0]
            channel = "Khảo sát khi xuất viện" if group.endswith("xuất viện") and random.random() < 0.5 else random.choice(CHANNELS)
            day = date(2026, month, random.randint(1, 30 if month == 9 else 31))
            rows.append(dict(day=day, site=site, dept=dept, channel=channel, group=group, level=level,
                             text=random.choice(TEXTS[group]), status=random.choice(STATUS)))
    rows.sort(key=lambda r: r["day"])
    for i, r in enumerate(rows, 1):
        r["code"] = f"GY-{month:02d}26-{i:03d}"
    return rows


def messy(r):
    d = r["day"]
    fmt = random.random()
    day_val = d if fmt < 0.55 else d.strftime("%d/%m/%Y") if fmt < 0.85 else d.isoformat()
    site = None if r["site"] == UNKNOWN else random.choice(SITE_VARIANTS[r["site"]])
    return [r["code"], day_val, site, r["dept"], r["channel"], random.choice(GROUP_VARIANTS[r["group"]]),
            random.choice(LEVEL_VARIANTS[r["level"]]), r["text"], r["status"]]


wb = Workbook()
wb.remove(wb.active)
answers = {}
for name, month, n_dup, n_blank, n_unknown in MONTHS:
    rows = make_rows(name, month, n_unknown)
    data = [messy(r) for r in rows]
    for i in random.sample(range(len(data)), n_dup):  # dòng trùng: chép y nguyên, chèn ngay sau dòng gốc
        data.insert(data.index(data[i]) + 1, list(data[i]))
    for _ in range(n_blank):
        data.insert(random.randint(5, len(data) - 5), [None] * 9)

    ws = wb.create_sheet(name)
    ws["A1"] = "DỮ LIỆU XUẤT TỪ HỆ THỐNG TIẾP NHẬN GÓP Ý NGƯỜI BỆNH"
    ws["A1"].font = Font(bold=True)
    ws["A2"] = (f"Kỳ: tháng {month}/2026 | Ngày xuất: 0{1 if month == 9 else 3}/{month + 1}/2026 07:45 | Người xuất: system | "
                "Số liệu giả định dùng cho đào tạo, không chứa thông tin người bệnh")
    ws.append([])
    ws.append(["STT", "Mã phiếu", "Ngày nhận", "Cơ sở", "Khoa", "Kênh tiếp nhận", "Nhóm góp ý", "Mức độ",
               "Nội dung tóm tắt", "Trạng thái"])
    stt = 0
    for row in data:
        if row[0] is None:
            ws.append([None] * 10)
            continue
        stt += 1
        ws.append([stt] + row)
        if isinstance(row[1], date):
            ws.cell(row=ws.max_row, column=3).number_format = "dd/mm/yyyy"
    for col, w in zip("ABCDEFGHIJ", [6, 14, 12, 12, 22, 22, 30, 11, 62, 12]):
        ws.column_dimensions[col].width = w

    answers[name] = dict(raw=len(data), dup=n_dup, blank=n_blank, valid=len(rows), unknown=n_unknown,
                         by_group=Counter(r["group"] for r in rows), by_site=Counter(r["site"] for r in rows),
                         rows=rows)

wb.save(OUT)
print("Đã tạo", OUT.name)
for name, a in answers.items():
    v, rows, unknown = a["valid"], a["rows"], a["unknown"]
    note = f", trong đó {unknown} dòng thiếu Cơ sở" if unknown else ""
    print(f"\n{name}: {a['raw']} dòng dữ liệu (gồm {a['dup']} trùng, {a['blank']} trống) -> {v} góp ý hợp lệ{note}")
    print("  Theo nhóm:", ", ".join(f"{k} {n} ({n / v:.0%})" for k, n in a["by_group"].most_common()))
    print("  Theo cơ sở:", ", ".join(f"{k} {n}" for k, n in sorted(a["by_site"].items())))
    for g in GROUPS:
        gr = [r for r in rows if r["group"] == g]
        high = sum(r["level"] == "Cao" for r in gr)
        dc = sum(r["site"] in ("Cơ sở C", "Cơ sở D") for r in gr)
        print(f"  {g}: Cao {high}/{len(gr)} ({high / len(gr):.0%}), C+D {dc}/{len(gr)} ({dc / len(gr):.0%})")
    high = sum(r["level"] == "Cao" for r in rows)
    print(f"  Mức độ Cao toàn bộ: {high}/{v} ({high / v:.0%})")
