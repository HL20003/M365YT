# Lab 3 - Copilot trong Excel

**Ứng dụng:** Microsoft Excel

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Hỏi Copilot về một file nhiều sheet bằng tiếng Việt, nhận câu trả lời có số liệu và nguồn
- Tạo cột phân loại theo tiêu chí của mình mà không cần biết viết công thức
- Tạo biểu đồ có tiêu đề nói lên phát hiện, sẵn sàng đưa vào báo cáo giao ban

### Tính năng chính

| Tính năng | Mô tả |
|-----------|--------|
| **Insights** | Hỏi đáp, tìm xu hướng và điểm bất thường trong số liệu |
| **Formula** | Tạo cột tính toán, phân loại theo tiêu chí |
| **Chart** | Trực quan hóa dữ liệu bằng biểu đồ |

---

## Tình huống

> **Chị Mai** - *điều dưỡng hành chính khoa Sản*
>
> Trước buổi giao ban tháng, điều dưỡng trưởng nhờ chị Mai chuẩn bị 3 thứ từ báo cáo quý 3: bức tranh chung trong 5 ý, danh sách khoa đang quá tải cần hỗ trợ nhân lực, và một biểu đồ cho thấy người bệnh đang phàn nàn nhiều nhất về điều gì. Chị Mai không giỏi Excel, nên nhờ Copilot viết công thức và vẽ biểu đồ.

**Tài liệu demo:** [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report). Dữ liệu đã ở dạng **Table**:

| Sheet | Nội dung |
|-------|----------|
| **Tổng hợp cơ sở** | Mỗi cơ sở một dòng: giường, công suất, ca sinh, điều dưỡng, nghỉ việc, giờ làm thêm, vật tư, hài lòng, thời gian chờ xuất viện |
| **Theo khoa** | 20 dòng (4 cơ sở x 5 khoa): giường, công suất, điều dưỡng, nghỉ việc, giờ làm thêm, sự cố được báo cáo |
| **Ca sinh theo tháng** | Số ca sinh tháng 7, 8, 9 |
| **Góp ý người bệnh** | Số góp ý quý 3 theo 6 nhóm và theo cơ sở |
| **Chỉ số hệ thống** | Kế hoạch, thực hiện và chuẩn ngành tham khảo |

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

### Bài tập 3: Biểu đồ góp ý của người bệnh

1. Chuyển sang sheet **Góp ý người bệnh**, bấm vào một ô trong bảng
2. Dán prompt:

> **PROMPT:**
>
> Vẽ biểu đồ cột thể hiện tổng số góp ý của 4 cơ sở theo từng nhóm, sắp xếp từ nhiều đến ít. Đặt tiêu đề nêu đúng phát hiện chính (nhóm nào nhiều nhất, chiếm bao nhiêu phần trăm, tập trung ở cơ sở nào), không chỉ ghi tên chỉ số.

3. Sau khi Copilot tạo, bấm **Add to a new sheet** để đưa biểu đồ vào file. Sao chép biểu đồ dán vào PowerPoint nếu cần.

> [!ANSWER]
> Biểu đồ cột 6 nhóm, cao nhất là **Thời gian chờ thủ tục xuất viện: 129/377 lượt (34%)**, tiếp theo là thời gian chờ khám (87) và thái độ giao tiếp (58). Tiêu đề gợi ý: *"Thời gian chờ xuất viện chiếm 34% góp ý, 86% đến từ Cơ sở D và C"*.

> [!TIP]
> Hỏi tiếp: *"Ở Cơ sở C, nhóm góp ý nào cao bất thường so với các cơ sở khác?"* Copilot sẽ chỉ ra **Thái độ giao tiếp (31 lượt)**, khớp với việc điểm hài lòng Cơ sở C giảm.

---

## Lưu ý tuân thủ

> [!NOTE]
> Chỉ dùng số liệu tổng hợp, không đưa danh sách người bệnh, mã hồ sơ vào file phân tích. Số liệu Copilot tính phải được đối chiếu với báo cáo chính thức trước khi đưa vào báo cáo giao ban.

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
> Từ sheet Ca sinh theo tháng, vẽ biểu đồ cột so sánh số ca sinh của 4 cơ sở theo từng tháng trong quý 3, tiêu đề nêu cơ sở có nhiều ca sinh nhất.

> [!NOTE]
> Với file Excel của khoa, hãy định dạng dữ liệu thành **Table** (Ctrl + T) và thay tên sheet, tên cột trong prompt cho khớp.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Nắm nhanh bức tranh chung, có số liệu và nguồn | Insights |
| Phân loại khoa theo tiêu chí riêng, không cần tự viết công thức | Formula |
| Biểu đồ có tiêu đề nêu phát hiện | Chart |
