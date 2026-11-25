---
name: bao-cao-gop-y-nguoi-benh
description: Làm sạch dữ liệu góp ý người bệnh xuất từ hệ thống tiếp nhận góp ý và lập báo cáo tháng gồm bảng tổng hợp, biểu đồ và 3 nhận xét có số liệu cho buổi giao ban. Dùng khi người dùng muốn làm báo cáo góp ý người bệnh của một tháng từ sheet dữ liệu thô.
---

# Báo cáo góp ý người bệnh tháng

Skill mẫu của workshop Copilot (dữ liệu giả định). Áp dụng cho sheet dữ liệu thô có các cột:
STT, Mã phiếu, Ngày nhận, Cơ sở, Khoa, Kênh tiếp nhận, Nhóm góp ý, Mức độ, Nội dung tóm tắt, Trạng thái.

## Các bước

1. **Xác định dữ liệu.** Dùng sheet người dùng chỉ định hoặc sheet đang mở. Dòng tiêu đề là dòng có ô "STT"; bỏ qua các dòng ghi chú xuất hệ thống phía trên.
2. **Làm sạch** trong một sheet mới tên `<tên sheet> sạch`, không sửa sheet gốc:
   - Bỏ dòng trống và dòng trùng hoàn toàn (so sánh mọi cột trừ STT).
   - Chuẩn hóa **Cơ sở** về đúng 4 tên: Cơ sở A, Cơ sở B, Cơ sở C, Cơ sở D (ví dụ CS D, CSD, CS-D, cơ sở d → Cơ sở D).
   - Chuẩn hóa **Nhóm góp ý** về đúng 6 nhóm: Thời gian chờ thủ tục xuất viện, Thời gian chờ khám, Thái độ giao tiếp, Viện phí và thanh toán, Cơ sở vật chất, Ăn uống và vệ sinh (ví dụ Chờ xuất viện → Thời gian chờ thủ tục xuất viện; Thái độ phục vụ → Thái độ giao tiếp).
   - Chuẩn hóa **Mức độ** về Cao, Trung bình, Thấp (High → Cao, Medium/TB → Trung bình, Low → Thấp).
   - Chuyển **Ngày nhận** về kiểu ngày, định dạng dd/mm/yyyy.
   - Định dạng kết quả thành Table và đánh lại STT.
3. **Ghi nhận việc đã làm:** số dòng ban đầu, số dòng trống và dòng trùng đã bỏ, số giá trị đã chuẩn hóa ở mỗi cột, số dòng "Cần kiểm tra", số dòng còn lại.
4. **Tổng hợp** trong sheet mới tên `<tên sheet> báo cáo`:
   - Bảng đếm Nhóm góp ý (dòng) theo Cơ sở (cột), có dòng và cột tổng, sắp xếp nhóm từ nhiều đến ít.
   - Bảng tỷ lệ góp ý mức độ Cao theo từng nhóm.
5. **Biểu đồ:** biểu đồ cột chồng số góp ý theo nhóm, chia màu theo cơ sở. Tiêu đề biểu đồ nêu phát hiện chính (nhóm nào nhiều nhất, chiếm bao nhiêu phần trăm, tập trung ở cơ sở nào), không chỉ ghi tên chỉ số.
6. **Nhận xét:** viết đúng 3 nhận xét ngắn cho buổi giao ban, mỗi nhận xét có con số cụ thể. Nếu workbook có sheet báo cáo của tháng trước, so sánh với tháng trước và nêu nhóm tăng nhiều nhất.

## Quy tắc

- Không xóa hay sửa sheet dữ liệu gốc.
- Giá trị không xác định được cơ sở hoặc nhóm (kể cả ô trống) thì đánh dấu "Cần kiểm tra", không tự đoán, và vẫn đếm riêng trong bảng tổng hợp.
- Không đưa tên, số điện thoại hay thông tin nhận diện người bệnh vào nhận xét. Nếu dữ liệu có cột như vậy, nhắc người dùng xóa trước khi phân tích.
