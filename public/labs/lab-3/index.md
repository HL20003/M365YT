# Lab 3 - Copilot trong Excel

**Ứng dụng:** Microsoft Excel

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Hỏi Copilot về một file nhiều sheet bằng tiếng Việt, nhận câu trả lời có số liệu và nguồn, rồi hỏi tiếp **vì sao**
- Tạo cột phân loại theo tiêu chí của mình mà không cần biết viết công thức
- Tạo **skill** để Copilot tự làm sạch file góp ý xuất từ hệ thống và lập báo cáo giao ban mỗi tháng, có biểu đồ và nhận xét

### Tính năng chính

| Tính năng | Mô tả |
|-----------|--------|
| **Insights** | Hỏi đáp, tìm xu hướng và điểm bất thường trong số liệu |
| **Formula** | Tạo cột tính toán, phân loại theo tiêu chí |
| **Skills** | Dạy Copilot một quy trình nhiều bước một lần, sau đó gọi lại bằng **@tên-skill** mỗi tháng |

---

## Tình huống

> **Chị Mai** - *điều dưỡng hành chính khoa Sản*
>
> Trước buổi giao ban tháng, điều dưỡng trưởng nhờ chị Mai chuẩn bị bức tranh chung quý 3 trong 5 ý và danh sách khoa đang quá tải cần hỗ trợ nhân lực. Ngoài ra, đầu mỗi tháng chị Mai còn phải làm báo cáo góp ý người bệnh từ file xuất của hệ thống: lọc dòng trùng, sửa tên cơ sở, đếm theo nhóm, vẽ biểu đồ. Việc này lặp lại tháng nào cũng như tháng nào. Chị Mai không giỏi Excel, nên nhờ Copilot viết công thức và làm báo cáo.

**Tài liệu demo** (tải lên **OneDrive** trước khi bắt đầu):

- [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report) cho Bài tập 1 và 2. Dữ liệu đã ở dạng **Table**:

| Sheet | Nội dung |
|-------|----------|
| **Tổng hợp cơ sở** | Mỗi cơ sở một dòng: giường, công suất, ca sinh, điều dưỡng, nghỉ việc, giờ làm thêm, vật tư, hài lòng, thời gian chờ xuất viện |
| **Theo khoa** | 20 dòng (4 cơ sở x 5 khoa): giường, công suất, điều dưỡng, nghỉ việc, giờ làm thêm, sự cố được báo cáo |
| **Ca sinh theo tháng** | Số ca sinh tháng 7, 8, 9 |
| **Góp ý người bệnh** | Số góp ý quý 3 theo 6 nhóm và theo cơ sở |
| **Chỉ số hệ thống** | Kế hoạch, thực hiện và chuẩn ngành tham khảo |

- [Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx](#file-feedback) cho Bài tập 3: hai sheet **T9** và **T10**, mỗi dòng là một phiếu góp ý (không có tên hay mã hồ sơ người bệnh). Dữ liệu **chưa làm sạch**, giống file xuất từ phần mềm thật.

---

### Bài tập 1: Bức tranh quý 3 trong 5 ý

1. Mở [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report) **từ OneDrive** (bắt buộc mở từ OneDrive)
2. Bấm nút **Copilot** trên thanh **Home**, dán prompt:

> **PROMPT:**
>
> Tôi cần chuẩn bị cho buổi giao ban. Dựa trên toàn bộ file này, quý 3 hệ thống đang làm tốt ở đâu và đáng lo ở đâu so với kế hoạch và chuẩn ngành? Trả lời trong đúng 5 gạch đầu dòng, mỗi ý có con số cụ thể và ghi tên sheet lấy số liệu. Ý đáng lo nhất để lên đầu.

> [!ANSWER]
> 5 ý có số liệu, ví dụ:
>
> - **Cơ sở D quá tải**: công suất giường 96%, khoa Sản 102%, trong khi Cơ sở B chỉ 58% (Tổng hợp cơ sở, Theo khoa)
> - **Nghỉ việc điều dưỡng 18%** so với chuẩn 12%, giờ làm thêm bình quân **16,4 giờ/tháng** so với kế hoạch 12 (Chỉ số hệ thống)
> - **Chi phí vật tư vượt 27%** (61 so với 48 tỷ)
> - **Hài lòng Cơ sở C** giảm từ 4,5 xuống 4,1
> - **Điểm tích cực:** tổng ca sinh **4.180**, vượt kế hoạch 4.000

3. Hỏi tiếp để tìm nguyên nhân, không dừng ở con số:

> **PROMPT:**
>
> Vì sao điểm hài lòng Cơ sở C giảm? Tìm bằng chứng từ ít nhất 2 sheet khác nhau, so sánh Cơ sở C với 3 cơ sở còn lại. Ghi rõ điều nào là số liệu cho thấy, điều nào chỉ là giả thuyết cần kiểm tra thêm.

> [!ANSWER]
> - Sheet **Góp ý người bệnh**: Cơ sở C có **31 góp ý về thái độ giao tiếp**, cao nhất trong 4 cơ sở (D 18, A 6, B 3), dù Cơ sở D lớn hơn nhiều
> - Sheet **Tổng hợp cơ sở**: thời gian chờ xuất viện **2,9 giờ** (chỉ sau D), giờ làm thêm **16,7 giờ/tháng**, nghỉ việc điều dưỡng **18,5%**
> - **Giả thuyết cần kiểm tra:** điều dưỡng làm thêm nhiều, thiếu người nên giao tiếp với người bệnh kém đi. Số liệu chỉ cho thấy các chỉ số cùng xấu, chưa chứng minh nguyên nhân; cần hỏi trực tiếp khoa hoặc xem góp ý chi tiết.

> [!TIP]
> Nếu nút Copilot bị mờ, file chưa được lưu trên OneDrive hoặc dữ liệu chưa ở dạng bảng. Báo người hướng dẫn.

### Bài tập 2: Phân loại khoa cần hỗ trợ nhân lực

1. Chuyển sang sheet **Theo khoa**, bấm vào một ô trong bảng
2. Dán prompt:

> **PROMPT:**
>
> Thêm cột "Mức cảnh báo" cho từng khoa: "Đỏ" nếu công suất giường trên 90% và giờ làm thêm bình quân trên 20 giờ/tháng; "Vàng" nếu chỉ có một trong hai điều kiện; còn lại là "Xanh". Tô nền đỏ, vàng, xanh tương ứng. Sau đó cho tôi biết có bao nhiêu khoa mỗi mức, và liệt kê các khoa Đỏ, Vàng kèm số liệu.

> [!ANSWER]
> **2 Đỏ, 3 Vàng, 15 Xanh.**
>
> | Mức | Khoa | Công suất giường | Giờ làm thêm/tháng |
> |-----|------|------------------|---------------------|
> | Đỏ | Sản, Cơ sở D | 102% | 26 giờ |
> | Đỏ | Nhi - Sơ sinh, Cơ sở D | 98% | 22 giờ |
> | Vàng | Ngoại - Gây mê hồi sức, Cơ sở D | 93% | |
> | Vàng | Cấp cứu, Cơ sở D | | 24 giờ |
> | Vàng | Sản, Cơ sở C | | 21 giờ |
>
> Hai khoa Đỏ cũng là nơi có nhiều điều dưỡng nghỉ việc nhất (8 và 6 người trong quý).

> [!TIP]
> Bấm vào một ô trong cột mới để xem công thức Copilot đã viết. Muốn đổi ngưỡng, hỏi tiếp: *"Đổi ngưỡng giờ làm thêm thành 18 giờ"* thay vì làm lại từ đầu.

### Bài tập 3: Tạo skill làm báo cáo góp ý người bệnh hằng tháng

Mỗi đầu tháng, phòng Chăm sóc khách hàng gửi file góp ý xuất từ hệ thống: có dòng ghi chú phía trên, dòng trống, dòng trùng, tên cơ sở chỗ ghi "CS D" chỗ ghi "Cơ sở D", nhóm góp ý chỗ ghi "Chờ xuất viện" chỗ ghi đầy đủ, ngày lẫn nhiều kiểu. Thay vì mỗi tháng làm sạch và lập báo cáo bằng tay, anh/chị dạy Copilot làm **một lần**, tháng sau chỉ cần gọi tên skill.

1. Mở [Góp ý người bệnh T9-T10 2026 (xuất từ hệ thống).xlsx](#file-feedback) **từ OneDrive**, chọn sheet **T9**. Lướt qua để thấy dữ liệu chưa sạch
2. Bấm **Copilot**, gõ **@skill-builder** và mô tả công việc:

> **PROMPT:**
>
> @skill-builder Tạo skill tên "bao-cao-gop-y-nguoi-benh" để làm báo cáo góp ý người bệnh hằng tháng cho buổi giao ban, từ sheet dữ liệu thô xuất từ hệ thống. Các bước: (1) bỏ các dòng ghi chú phía trên dòng tiêu đề có cột STT; (2) trong một sheet mới tên "<tên sheet> sạch": bỏ dòng trống và dòng trùng, chuẩn hóa Cơ sở về 4 tên (Cơ sở A, Cơ sở B, Cơ sở C, Cơ sở D), Nhóm góp ý về 6 nhóm (Thời gian chờ thủ tục xuất viện, Thời gian chờ khám, Thái độ giao tiếp, Viện phí và thanh toán, Cơ sở vật chất, Ăn uống và vệ sinh), Mức độ về Cao/Trung bình/Thấp, Ngày nhận về kiểu ngày dd/mm/yyyy, định dạng thành Table; (3) ghi lại đã bỏ bao nhiêu dòng và sửa bao nhiêu giá trị; (4) trong sheet "<tên sheet> báo cáo": bảng đếm Nhóm góp ý theo Cơ sở có tổng, và tỷ lệ mức độ Cao theo nhóm; (5) biểu đồ cột chồng theo nhóm góp ý, tiêu đề nêu phát hiện chính; (6) 3 nhận xét có số liệu, so sánh với tháng trước nếu có. Không sửa sheet gốc. Giá trị không xác định được, kể cả ô trống, thì đánh dấu "Cần kiểm tra", không tự đoán. Không đưa thông tin nhận diện người bệnh vào nhận xét.

3. Copilot hiển thị nội dung skill (tên, mô tả, các bước). Đọc lại, trả lời nếu Copilot hỏi thêm, rồi chọn **lưu**. Skill được lưu vào thư mục **skills** trên OneDrive
4. Chạy skill cho tháng 9:

> **PROMPT:**
>
> @bao-cao-gop-y-nguoi-benh Làm báo cáo cho sheet T9.

5. **Kiểm tra trước khi dùng:** mở sheet **T9 sạch**, đối chiếu số dòng Copilot báo với số dòng trong Table, lọc cột **Cơ sở** để tìm dòng **Cần kiểm tra**
6. Chạy lại cho tháng 10. Không cần mô tả lại các bước:

> **PROMPT:**
>
> @bao-cao-gop-y-nguoi-benh Làm báo cáo cho sheet T10 và so sánh với báo cáo tháng 9.

> [!ANSWER]
> **Tháng 9:**
>
> - Từ 138 dòng, bỏ **3 dòng trống** và **8 dòng trùng**, còn **127 góp ý**. Có **1 dòng bỏ trống Cơ sở** được đánh dấu "Cần kiểm tra"
> - **Thời gian chờ thủ tục xuất viện** nhiều nhất: **44 góp ý (35%)**, trong đó **38 (86%)** ở Cơ sở D và C; một nửa là mức độ Cao (22/44)
> - Cơ sở D nhiều góp ý nhất (**57/127**), tiếp theo là Cơ sở C (43)
> - Tiêu đề biểu đồ gợi ý: *"Chờ xuất viện chiếm 35% góp ý tháng 9, 86% đến từ Cơ sở D và C"*
>
> **Tháng 10:**
>
> - Bỏ 3 dòng trống và 6 dòng trùng, còn **136 góp ý**
> - Chờ xuất viện vẫn nhiều nhất (**42**, 31%), nhưng **Thái độ giao tiếp tăng từ 19 lên 29** (15% lên 21%), riêng **Cơ sở C từ 10 lên 19**. Đây là tín hiệu cần đưa lên giao ban, khớp với việc điểm hài lòng Cơ sở C giảm ở Bài tập 1

> [!TIP]
> **Chưa tạo được skill?** Tải [Skill Excel - bao-cao-gop-y-nguoi-benh.zip](#file-skill-excel) về máy và giải nén. Trong khung Copilot của Excel, bấm **...** > **Manage plugins & skills** > **Custom skills** > **Create OneDrive folder** > **Open skills folder**, chép thư mục **bao-cao-gop-y-nguoi-benh** vào đó và bấm **Refresh**. Sau đó chạy tiếp bước 4.

> [!TIP]
> Muốn sửa skill, ví dụ thêm bảng đếm theo khoa, chỉ cần nói: *"Cập nhật skill bao-cao-gop-y-nguoi-benh: thêm bảng đếm Nhóm góp ý theo Khoa."* Tháng sau gọi skill là có luôn bảng mới.

---

## Lưu ý tuân thủ

> [!NOTE]
> Chỉ dùng số liệu tổng hợp hoặc phiếu góp ý **đã bỏ tên, số điện thoại, mã hồ sơ** người bệnh. Nếu file xuất từ hệ thống có các cột này, xóa cột trước khi mở Copilot. Không ghi mật khẩu, thông tin người bệnh hay số liệu mật vào nội dung skill. Số liệu Copilot tính phải được đối chiếu với báo cáo chính thức trước khi đưa vào báo cáo giao ban.

---

## Prompt đề xuất - Excel

### Hỏi nhanh

> **PROMPT:**
>
> 1. Cơ sở nào có nhiều ca sinh nhất quý 3? Cơ sở nào có công suất giường cao nhất và thấp nhất?
> 2. Sắp xếp bảng theo công suất giường từ cao xuống thấp và tô đỏ các dòng có công suất trên 90%.

### So sánh và giải thích

> **PROMPT:**
>
> So sánh Cơ sở C và Cơ sở D: khác nhau ở đâu về công suất giường, giờ làm thêm, nghỉ việc điều dưỡng và các nhóm góp ý? Điều gì có thể giải thích việc điểm hài lòng Cơ sở C giảm?

### Công thức

> **PROMPT:**
>
> Thêm cột "Tỷ lệ nghỉ việc năm hóa" bằng số điều dưỡng nghỉ việc trong quý nhân 4 chia số điều dưỡng, định dạng phần trăm, và tô đỏ các khoa trên 12%.

### Biểu đồ

> **PROMPT:**
>
> Từ sheet Góp ý người bệnh, vẽ biểu đồ cột thể hiện tổng số góp ý của 4 cơ sở theo từng nhóm, sắp xếp từ nhiều đến ít. Đặt tiêu đề nêu đúng phát hiện chính (nhóm nào nhiều nhất, chiếm bao nhiêu phần trăm, tập trung ở cơ sở nào), không chỉ ghi tên chỉ số.

### Skill cho việc lặp lại

> **PROMPT:**
>
> @skill-builder Tạo skill "bao-cao-cong-suat-giuong-tuan" để mỗi tuần, từ file công suất giường theo khoa: tính công suất từng khoa, đánh dấu khoa trên 90%, so sánh với tuần trước, vẽ biểu đồ cột theo khoa và viết 3 nhận xét cho điều dưỡng trưởng.

> [!NOTE]
> Với file Excel của khoa, hãy định dạng dữ liệu thành **Table** (Ctrl + T) và thay tên sheet, tên cột trong prompt cho khớp.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Nắm nhanh bức tranh chung, có số liệu và nguồn, rồi hỏi tiếp "vì sao" | Insights |
| Phân loại khoa theo tiêu chí riêng, không cần tự viết công thức | Formula |
| Làm sạch file xuất từ hệ thống và lập báo cáo tháng chỉ bằng một câu gọi skill | Skills |
