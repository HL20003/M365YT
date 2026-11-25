"""Chép file demo vào thư mục files/ của site (đường dẫn ASCII) và đóng gói zip để tải một lần.

Chạy lại sau mỗi lần tạo lại file demo. Tên tiếng Việt đầy đủ được giữ khi tải về
nhờ thuộc tính download trong app.js, nên tên ở đây chỉ cần ổn định và không dấu.

Skill mẫu trong demo-files/skills được đóng gói thành zip chứa thư mục <tên skill>/SKILL.md:
giải nén rồi chép cả thư mục vào thư mục skills trên OneDrive.
"""
import shutil
import zipfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
DST = SRC.parent / "public" / "files"
SKILLS = SRC / "skills"

FILES = {  # đường dẫn trên site: tên file gốc
    "thong-bao-lich-truc-tet-2027.docx": "Thông báo lịch trực Tết 2027.docx",
    "huong-dan-cham-soc-me-sau-sinh.docx": "Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx",
    "bao-cao-hoat-dong-q3-2026.xlsx": "Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx",
    "gop-y-nguoi-benh-t9-t10-2026.xlsx": "Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx",
    "ke-hoach-hoat-dong-2027.docx": "Kế hoạch Hoạt động 2027 (dự thảo).docx",
    "tai-lieu-dao-tao-phung-su-tu-tam.docx": "Tài liệu đào tạo Phụng sự từ tâm.docx",
    "du-thao-hop-dong-cung-ung-vat-tu.docx": "Dự thảo Hợp đồng cung ứng vật tư.docx",
    "chinh-sach-mua-sam-noi-bo.pdf": "Chính sách Mua sắm nội bộ.pdf",
    "chinh-sach-nhan-su.pdf": "Chính sách Nhân sự.pdf",
}
SKILL_ZIPS = {  # đường dẫn trên site: (tên khi tải về, thư mục skill)
    "skill-excel-bao-cao-gop-y-nguoi-benh.zip": ("Skill Excel - bao-cao-gop-y-nguoi-benh.zip", "bao-cao-gop-y-nguoi-benh"),
}
ZIP_NAME = "copilot-workshop-demo-files.zip"

if DST.exists():
    shutil.rmtree(DST)
DST.mkdir(parents=True)
for site_name, src_name in FILES.items():
    shutil.copy2(SRC / src_name, DST / site_name)
for site_name, (_, folder) in SKILL_ZIPS.items():
    with zipfile.ZipFile(DST / site_name, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(SKILLS / folder / "SKILL.md", arcname=f"{folder}/SKILL.md")
with zipfile.ZipFile(DST / ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as z:
    for src_name in FILES.values():
        z.write(SRC / src_name, arcname=src_name)
    for site_name, (download_name, _) in SKILL_ZIPS.items():
        z.write(DST / site_name, arcname=f"Skill mẫu/{download_name}")
total = sum(p.stat().st_size for p in DST.iterdir())
print(f"{len(FILES)} file + {len(SKILL_ZIPS)} skill + zip -> {DST} ({total / 1024:.0f} KB)")
