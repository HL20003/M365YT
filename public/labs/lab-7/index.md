# Lab 7 - Researcher Agent

**Ứng dụng:** Microsoft 365 Copilot Chat, agent Researcher

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

> [!TIP]
> Nếu tài khoản không thấy **Researcher** trong mục **Agents**, người hướng dẫn sẽ trình diễn trên máy chiếu.

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Biết khi nào dùng Researcher thay vì hỏi Copilot Chat thông thường
- Giao cho Researcher một đề bài dạng câu hỏi cụ thể, có đính kèm số liệu nội bộ
- Định hình báo cáo theo người đọc và kiểm tra nguồn trước khi dùng

### Researcher làm việc thế nào?

**Researcher** là agent nghiên cứu chuyên sâu của Microsoft 365 Copilot. Researcher lấy thông tin từ **web** và từ **nội dung công việc** anh/chị có quyền xem (file, email, cuộc họp, chat), có thể hỏi lại để làm rõ đề bài, rồi viết thành báo cáo có trích dẫn. Anh/chị nói rõ trong prompt muốn dùng nguồn nội bộ, web hay cả hai.

| | Copilot Chat thông thường | Researcher |
|---|---------------------------|------------|
| **Dùng khi** | Câu hỏi nhanh, việc hằng ngày | Đề bài cần tìm hiểu kỹ từ nhiều nguồn, cần dẫn chứng |
| **Thời gian** | Vài giây | 3 đến 10 phút |
| **Kết quả** | Câu trả lời ngắn | Báo cáo nhiều mục, có trích nguồn, có thể mở thành file Word |

---

## Tình huống

> **Chị Lan** - *Phó phòng Điều dưỡng*
>
> Tỷ lệ nghỉ việc của điều dưỡng toàn hệ thống đang ở mức **18%**, cao hơn chuẩn ngành 12%. Số liệu quý 3 cho thấy nghỉ việc và giờ làm thêm tập trung ở vài khoa quá tải. Dự thảo **Kế hoạch Hoạt động 2027** đã có nhóm giải pháp giữ chân điều dưỡng (Mục 3.1), nhưng Giám đốc muốn biết các giải pháp này **đã đủ chưa** trước khi trình Hội đồng quản trị.
>
> Chị Lan được giao chuẩn bị một memo 2-3 trang cho cuộc họp Ban Giám đốc tuần sau: các bệnh viện khác đã làm gì, khoa nào của mình cần ưu tiên, và kế hoạch 2027 nên bổ sung gì. Chị không có thời gian tự đọc hàng chục nghiên cứu, nên giao cho Researcher.

**Tài liệu đính kèm:** [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report) (sheet **Theo khoa**, **Chỉ số hệ thống**) và [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), đã lưu trên OneDrive.

---

### Bài tập 1: Giao đề bài cho Researcher

1. Vào [https://m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat), đăng nhập bằng **tài khoản công ty**
2. Trong Chat, tìm mục **Agents** và chọn **Researcher**
3. Gõ **/** để đính kèm [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report), gõ **/** lần nữa để đính kèm [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan)
4. Dán prompt, bấm **Gửi**:

> **PROMPT:**
>
> Tôi là Phó phòng Điều dưỡng của một hệ thống 4 bệnh viện tư, khoảng 1.000 điều dưỡng, tỷ lệ nghỉ việc 18% so với chuẩn ngành 12%. Tôi cần chuẩn bị memo cho Ban Giám đốc. Hãy trả lời 3 câu hỏi:
> 1. Các bệnh viện ở Việt Nam và châu Á đã áp dụng những giải pháp nào để giảm nghỉ việc của điều dưỡng, đặc biệt ở khoa đông người bệnh? Nêu 5 giải pháp, mỗi giải pháp có ví dụ, kết quả đạt được và điều kiện áp dụng.
> 2. Dựa trên sheet Theo khoa và Chỉ số hệ thống trong file Báo cáo Hoạt động, những khoa nào cần ưu tiên và vì sao (nêu công suất giường, giờ làm thêm, số người nghỉ việc)?
> 3. Đặt các giải pháp ở câu 1 cạnh Mục 3.1 của Kế hoạch Hoạt động 2027: kế hoạch đã có gì, còn thiếu gì, và đề xuất 3 điều nên bổ sung, mỗi điều có chỉ số đo kết quả.
>
> Dùng cả file nội bộ đính kèm và nguồn trên web. Mỗi giải pháp và số liệu bên ngoài phải có trích dẫn nguồn. Số liệu nội bộ ghi rõ tên sheet hoặc mục tài liệu.

> [!TIP]
> Đề bài tốt cho Researcher là **câu hỏi cụ thể**, không chỉ "tìm hiểu về nghỉ việc của điều dưỡng". Nói rõ **mình là ai**, **người đọc là ai**, và **đính kèm số liệu nội bộ** để báo cáo bám sát thực tế của mình.

### Bài tập 2: Trả lời câu hỏi làm rõ và kiểm tra báo cáo

1. Researcher thường hỏi lại để làm rõ phạm vi. Đây là lúc định hình báo cáo theo người đọc. Trả lời:

> **PROMPT:**
>
> Ưu tiên nguồn trong 5 năm gần đây, từ bệnh viện, hiệp hội điều dưỡng, cơ quan y tế hoặc tạp chí chuyên ngành. Người đọc là Ban Giám đốc nên viết dạng memo 2-3 trang: mở đầu bằng bảng tóm tắt (Giải pháp | Kế hoạch 2027 đã có chưa | Chi phí ước tính thấp/trung bình/cao | Thời gian triển khai | Mức ưu tiên), phần phân tích để sau.

2. Đợi 3 đến 10 phút. Anh/chị có thể làm việc khác và quay lại khi báo cáo xong
3. Khi có báo cáo, bấm vào **2-3 trích dẫn** bất kỳ để kiểm tra nguồn, rồi hỏi tiếp:

> **PROMPT:**
>
> Trong báo cáo, kết luận nào dựa trên một nguồn duy nhất hoặc nguồn cũ hơn 5 năm? Đánh dấu để tôi kiểm tra lại trước khi trình.

> [!ANSWER]
> Memo mở đầu bằng **bảng tóm tắt**.
>
> **Giải pháp thường gặp từ bên ngoài:**
>
> - định biên điều dưỡng theo số người bệnh, giới hạn giờ làm thêm;
> - xếp ca linh hoạt, cho điều dưỡng tự đăng ký ca;
> - kèm cặp điều dưỡng mới trong năm đầu;
> - lộ trình nghề nghiệp gắn với đãi ngộ;
> - hỗ trợ sức khỏe tinh thần, phòng kiệt sức;
> - khảo sát gắn kết, phỏng vấn nghỉ việc.
>
> **Khoa cần ưu tiên** (sheet Theo khoa):
>
> | Khoa | Công suất giường | Giờ làm thêm/tháng | Điều dưỡng nghỉ việc trong quý |
> |------|------------------|---------------------|--------------------------------|
> | Sản, Cơ sở D | 102% | 26 giờ | 8 người |
> | Nhi - Sơ sinh, Cơ sở D | 98% | 22 giờ | 6 người |
> | Cấp cứu, Cơ sở D | | 24 giờ | |
> | Sản, Cơ sở C | | 21 giờ | |
>
> Trong khi đó **Cơ sở B** chỉ dùng 58% giường, giờ làm thêm 7,2 giờ.
>
> **So với Kế hoạch 2027, Mục 3.1:**
>
> - **Đã có:** phụ cấp, lộ trình 4 bậc, kèm cặp, khảo sát gắn kết.
> - **Còn thiếu:** giải pháp **giảm giờ làm thêm và định biên** cho khoa quá tải, **điều phối người bệnh hoặc nhân lực** giữa Cơ sở D và B.
>
> **3 đề xuất có chỉ số**, ví dụ:
>
> - giờ làm thêm dưới 12 giờ/tháng ở các khoa Đỏ;
> - tỷ lệ nghỉ việc ở Cơ sở D dưới 15% cuối 2027;
> - 100% điều dưỡng mới có người kèm cặp.

> [!TIP]
> Hỏi tiếp: *"Chuyển bảng tóm tắt thành 3 slide cho cuộc họp Ban Giám đốc"*, hoặc mở báo cáo thành file Word để chỉnh sửa trước khi gửi.

---

## Lưu ý tuân thủ

> [!NOTE]
> Không đưa dữ liệu cá nhân của nhân viên (tên người nghỉ việc, lương, đánh giá) hay dữ liệu người bệnh vào đề bài. Báo cáo của Researcher là tài liệu tham khảo: luôn mở nguồn trích dẫn để kiểm tra, và kiểm tra lại các con số nội bộ với báo cáo gốc trước khi trình.

---

## Prompt đề xuất - Researcher

### Cải tiến trải nghiệm người bệnh

> **PROMPT:**
>
> Các bệnh viện sản khoa ở Việt Nam và châu Á đã làm gì để rút ngắn thời gian chờ thủ tục xuất viện? Nêu 5 giải pháp có ví dụ và kết quả. Đặt cạnh sheet Tổng hợp cơ sở và Góp ý người bệnh trong file /Báo cáo Hoạt động Q3 2026 - 4 cơ sở, cho biết cơ sở nào cần ưu tiên và đề xuất lộ trình 90 ngày. Kèm nguồn.

### Quản lý chất lượng

> **PROMPT:**
>
> Tổng hợp các chỉ số an toàn người bệnh phổ biến mà bệnh viện đạt chuẩn quốc tế theo dõi cho khoa Sản (ví dụ tỷ lệ băng huyết sau sinh, nhiễm trùng vết mổ), cách tính từng chỉ số và tần suất báo cáo. Kèm nguồn.

### Đào tạo

> **PROMPT:**
>
> Tìm các mô hình đào tạo định hướng cho điều dưỡng mới ở khoa Sản và Nhi tại các bệnh viện trong khu vực: thời lượng, nội dung, cách đánh giá. Đề xuất một chương trình 4 tuần phù hợp với file /Tài liệu đào tạo Phụng sự từ tâm.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Mở Researcher từ mục Agents trong Chat | Researcher |
| Đề bài dạng câu hỏi cụ thể, kết hợp file nội bộ và web | Researcher + file đính kèm |
| Định hình báo cáo theo người đọc, kiểm tra nguồn | Câu hỏi làm rõ, trích dẫn |
