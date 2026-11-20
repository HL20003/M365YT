"""Chép file demo vào thư mục files/ của site (đường dẫn ASCII) và đóng gói zip để tải một lần.

Chạy lại sau mỗi lần tạo lại file demo. Tên tiếng Việt đầy đủ được giữ khi tải về
nhờ thuộc tính download trong app.js, nên tên ở đây chỉ cần ổn định và không dấu.
"""
import shutil
import zipfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
DST = SRC.parent / "public" / "files"

FILES = {  # đường dẫn trên site: tên file gốc
    "thong-bao-lich-truc-tet-2027.docx": "Thông báo lịch trực Tết 2027.docx",
    "huong-dan-cham-soc-me-sau-sinh.docx": "Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx",
    "bao-cao-hoat-dong-q3-2026.xlsx": "Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx",
    "ke-hoach-hoat-dong-2027.docx": "Kế hoạch Hoạt động 2027 (dự thảo).docx",
    "tai-lieu-dao-tao-phung-su-tu-tam.docx": "Tài liệu đào tạo Phụng sự từ tâm.docx",
    "du-thao-hop-dong-cung-ung-vat-tu.docx": "Dự thảo Hợp đồng cung ứng vật tư.docx",
    "chinh-sach-mua-sam-noi-bo.pdf": "Chính sách Mua sắm nội bộ.pdf",
    "chinh-sach-nhan-su.pdf": "Chính sách Nhân sự.pdf",
}
ZIP_NAME = "copilot-workshop-demo-files.zip"

if DST.exists():
    shutil.rmtree(DST)
DST.mkdir(parents=True)
for site_name, src_name in FILES.items():
    shutil.copy2(SRC / src_name, DST / site_name)
with zipfile.ZipFile(DST / ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as z:
    for src_name in FILES.values():
        z.write(SRC / src_name, arcname=src_name)
total = sum(p.stat().st_size for p in DST.iterdir())
print(f"{len(FILES)} file + zip -> {DST} ({total / 1024:.0f} KB)")
