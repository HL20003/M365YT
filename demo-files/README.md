# File demo - Copilot Workshop (bản Phương Châu)

Tài liệu nháp dùng cho đào tạo. Đơn vị là một hệ thống bệnh viện **giả định** gồm 4 cơ sở A, B, C, D; không có tên công ty
hay bệnh viện thật trong file. Đây là bản gốc; site phục vụ bản sao trong `public/files/` (tên không dấu, khi tải về vẫn giữ tên đầy đủ).

| id trong app.js | File | Dùng ở |
|---|---|---|
| `tet` | Thông báo lịch trực Tết 2027.docx | Lab 2 Word (Bài 1) |
| `postpartum` | Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx | Lab 2 Word (Bài 2) |
| `contract` | Dự thảo Hợp đồng cung ứng vật tư.docx | Lab 2 Word (Bài 3) |
| `procurement` | Chính sách Mua sắm nội bộ.pdf | Lab 2 Word (Bài 3, tài liệu đối chiếu) |
| `report` | Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx | Lab 1, Lab 3 (Bài 1-2) |
| `feedback` | Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx | Lab 3 Excel (Bài 3, tạo skill) |
| `skill-excel` | Skill Excel - bao-cao-gop-y-nguoi-benh.zip (từ `skills/bao-cao-gop-y-nguoi-benh/SKILL.md`) | Lab 3 Excel (Bài 3, dự phòng) |
| `plan` | Kế hoạch Hoạt động 2027 (dự thảo).docx | Lab 1, Lab 4 (prompt đề xuất) |
| `culture` | Tài liệu đào tạo Phụng sự từ tâm.docx | Lab 4 PowerPoint |
| `hr` | Chính sách Nhân sự.pdf | Lab 7 Agent Builder (knowledge) |

Email mẫu, lời mời họp, tin nhắn Teams mẫu, kịch bản họp Lab 6 và đáp án tổng hợp nằm ở trang Trainer
(`public/labs/trainer/index.md`, mở site với `?trainer=1`).

## Tạo lại file

Cần Python với `python-docx` và `openpyxl`, và Microsoft Edge (để in PDF). Không cần Excel hay Word.

```bash
cd _gen
python gen_report.py         # file Excel (chỉ có giá trị, không có công thức) + in đáp án Lab 3
python gen_feedback.py       # file góp ý thô T9-T10 cho bài skill + in đáp án Lab 3 Bài 3
python gen_docs.py           # 5 file Word + bản nguồn của 2 file PDF trong _pdf_src/
python topdf.py              # in _pdf_src/*.docx ra PDF bằng Edge headless
python sync_site_files.py    # chép sang public/files, đóng gói skill mẫu + zip
```

Trên Windows, đặt `PYTHONIOENCODING=utf-8` nếu terminal báo lỗi in tiếng Việt.
Nếu đổi số liệu, cập nhật lại đáp án trong `public/labs/lab-1`, `lab-3` và trang trainer.

## Điểm cài sẵn để đáp án mẫu có căn cứ

- **Excel:**
  - Cơ sở D quá tải (96%, khoa Sản 102%), Cơ sở B 58%.
  - Nghỉ việc điều dưỡng 18% (chuẩn 12%), giờ làm thêm 16,4 giờ/tháng (KH 12).
  - Vật tư vượt 27% (61 so với 48 tỷ).
  - Hài lòng Cơ sở C 4,5 → 4,1, góp ý thái độ giao tiếp ở Cơ sở C cao (31).
  - Góp ý chờ xuất viện 129/377 (34%), 86% từ D và C.
  - Phân loại khoa (công suất > 90% và làm thêm > 20 giờ): 2 Đỏ (Sản D, Nhi D), 3 Vàng (Ngoại-GMHS D, Cấp cứu D, Sản C), 15 Xanh.
    Không khoa nào có công suất đúng 90% để tránh tranh cãi ở ngưỡng.
- **Góp ý người bệnh T9-T10 (dữ liệu thô):**
  - T9: 138 dòng, gồm 3 dòng trống và 8 dòng trùng, còn 127 góp ý; 1 dòng trống Cơ sở để kiểm tra skill có đánh dấu "Cần kiểm tra" thay vì tự đoán.
  - T9: chờ xuất viện 44 (35%), 38/44 (86%) ở D và C, khớp báo cáo quý 3.
  - T10: 3 trống + 6 trùng, còn 136; thái độ giao tiếp tăng từ 19 lên 29, Cơ sở C từ 10 lên 19.
  - Không có cột tên hay mã hồ sơ người bệnh. Đổi số liệu trong `COUNTS` của `gen_feedback.py` thì cập nhật Lab 3 Bài 3 và trang trainer.
- **Kế hoạch 2027:** có giải pháp cho nghỉ việc điều dưỡng và hài lòng Cơ sở C; không đề cập quá tải Cơ sở D, vật tư, chờ xuất viện.
- **Hợp đồng vật tư và Chính sách Mua sắm:**
  - Tạm ứng 50% không bảo lãnh (chính sách tối đa 30% kèm bảo lãnh, Mục 4.1).
  - Phạt chậm 0,05%/ngày, trần 5% (chính sách tối thiểu 0,1%/ngày, trần 8%, Mục 4.2).
  - Không có điều khoản thu hồi lô lỗi (Mục 4.3).
  - Mới 2 báo giá (cần 3, Mục 2.1).
  - Giá trị 7,8 tỷ: Tổng Giám đốc phê duyệt sau khi Pháp chế rà soát (Mục 3).
- **Chính sách Nhân sự:**
  - 6 năm làm việc được 13 ngày phép, chuyển tối đa 5 ngày sang năm sau (Mục 3).
  - Phụ cấp trực của điều dưỡng: 300.000 đồng/ca, gấp 3 từ mùng 1 đến mùng 3 Tết, gấp 2 các ngày Tết còn lại (Mục 5).
  - Đổi ca chỉ giữa hai người cùng chức danh, đề nghị trước 24 giờ (Mục 2.4).
  - Đào tạo liên tục 48 tiết trong 2 năm (Mục 6).
  - Không chia sẻ CCCD (Mục 8).
