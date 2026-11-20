# Lab 1 - Copilot Chat

**Ứng dụng:** Microsoft 365 Copilot Chat

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Gom email, lịch họp và tin nhắn của mình thành danh sách việc cần làm có hạn chót và nguồn
- Đặt hai tài liệu cạnh nhau để Copilot chỉ ra điểm khớp và điểm còn thiếu
- Bật, tắt **Work IQ** để chọn nguồn thông tin: dữ liệu công việc của mình hay thông tin công khai trên web

### Tính năng chính

| Tính năng | Mô tả |
|-----------|--------|
| **Work grounding** | Trả lời dựa trên email, lịch, cuộc họp, file mà anh/chị có quyền truy cập |
| **Phân tích nhiều tài liệu** | Đính kèm nhiều file bằng "/" và hỏi xuyên suốt các file |
| **Work IQ** | Bật: dùng dữ liệu công việc (và web khi cần). Tắt: chỉ dùng web công khai và file đính kèm |

---

## Tình huống

> **Chị Mai** - *điều dưỡng hành chính khoa Sản, Cơ sở D*
>
> Sáng thứ Hai, chị Mai vừa hết 2 ngày nghỉ. Hộp thư có thư nhắc gửi danh sách trực Tết, một chuỗi góp ý của gia đình người bệnh và thư nhà cung cấp hỏi số lượng vật tư. Trưởng khoa nhờ chị đọc dự thảo **Kế hoạch Hoạt động 2027** và gửi góp ý của khoa trước ngày 30/11, đồng thời chuẩn bị vài ý chia sẻ cho buổi giao ban sáng thứ Tư.

**Tài liệu demo:** [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report) và [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), đã lưu trên OneDrive. Email mẫu do người hướng dẫn gửi trước buổi học.

---

### Bài tập 1: Tuần này tôi cần làm gì?

1. Mở trình duyệt, vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/), đăng nhập tài khoản công ty
2. Bấm **Copilot** ở thanh bên trái, kiểm tra nút **Work IQ** ở góc trên bên trái đang **bật**
3. Dán prompt, bấm **Gửi**:

> **PROMPT:**
>
> Tôi là điều dưỡng hành chính khoa Sản, vừa nghỉ 2 ngày. Dựa trên email, lịch họp và tin nhắn Teams của tôi trong 7 ngày qua, lập bảng các việc tôi cần làm trong tuần này gồm: Việc cần làm | Ai yêu cầu | Hạn chót | Nguồn (email hay cuộc họp nào). Xếp việc có hạn gần nhất lên đầu, đánh dấu việc liên quan đến người bệnh hoặc gia đình người bệnh. Nếu email không nêu hạn chót, ghi [CHƯA CÓ HẠN].

> [!ANSWER]
> Bảng 3 đến 6 việc, có các việc từ email mẫu:
>
> - Xác nhận số lượng vật tư với nhà cung cấp, **hạn 25/11**
> - Gửi danh sách trực Tết về Phòng Hành chính - Nhân sự, **hạn 15/12**
> - Phản hồi góp ý của gia đình người bệnh về thủ tục xuất viện, **[CHƯA CÓ HẠN]**, được đánh dấu là việc liên quan đến người bệnh
>
> Mỗi dòng có **số trích dẫn** dẫn về email gốc.

> [!TIP]
> Bấm vào số trích dẫn để mở email gốc. Nếu anh/chị là trưởng khoa, đổi cột "Ai yêu cầu" thành "Giao cho ai" và hỏi tiếp: *"Việc nào tôi có thể giao cho điều dưỡng trưởng hoặc hành chính khoa?"*

### Bài tập 2: Đối chiếu kế hoạch 2027 với số liệu thực tế

1. Bấm **New chat** để mở cuộc trò chuyện mới, Work IQ vẫn **bật**
2. Gõ **/** rồi gõ "Báo cáo Hoạt động", chọn [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report). Gõ **/** lần nữa, chọn [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan)
3. Dán prompt:

> **PROMPT:**
>
> Khoa tôi được mời góp ý cho dự thảo Kế hoạch Hoạt động 2027. Đặt kế hoạch cạnh báo cáo quý 3 và lập bảng: Vấn đề trong số liệu (kèm con số và tên sheet) | Kế hoạch đã có giải pháp chưa | Giải pháp trong kế hoạch (ghi mục) | Nhận xét. Sau bảng, đề xuất 2 góp ý cụ thể nên gửi Phòng Kế hoạch tổng hợp, mỗi góp ý nêu lý do bằng số liệu. Chỉ dùng thông tin trong 2 file, không tự thêm số liệu.

> [!ANSWER]
> **Kế hoạch đã có giải pháp cho:**
>
> - nghỉ việc điều dưỡng **18%**, ngành 12% (Mục 3.1);
> - điểm hài lòng Cơ sở C giảm từ **4,5 xuống 4,1** (Mục 3.2).
>
> **Kế hoạch chưa đề cập:**
>
> - **Cơ sở D quá tải**: công suất giường **96%**, khoa Sản **102%**, trong khi **Cơ sở B chỉ 58%**;
> - **chi phí vật tư vượt kế hoạch 27%** (61 tỷ so với 48 tỷ);
> - **thời gian chờ thủ tục xuất viện**: 3,4 giờ ở Cơ sở D, là nhóm góp ý lớn nhất (129 lượt).
>
> **Hai góp ý hợp lý:**
>
> - bổ sung phương án điều phối người bệnh hoặc mở rộng giường cho Cơ sở D;
> - bổ sung mục kiểm soát chi phí vật tư.

> [!TIP]
> Yêu cầu **ghi mục và tên sheet** giúp anh/chị kiểm tra từng kết luận trong vài giây. Hỏi tiếp: *"Viết 2 góp ý trên thành email gửi Phòng Kế hoạch tổng hợp, giọng xây dựng, dưới 150 chữ."*

### Bài tập 3: Tắt Work IQ để tìm thông tin chuyên ngành công khai

1. Bấm nút **Work IQ** ở góc trên bên trái để **tắt** (chữ Work IQ bị gạch ngang). Copilot tự mở cuộc trò chuyện mới và từ đây chỉ dùng thông tin công khai trên web, không đọc email hay file của anh/chị

<div class="ui-mock">
  <div class="mock-bar">
    <span class="mock-chip mock-workiq off">Work IQ</span>
    <span class="mock-bar-right"><span class="mock-chip">+ New chat</span><span class="mock-chip">⋯</span></span>
  </div>
  <div class="mock-callouts">
    <div><b>Work IQ tắt:</b> chỉ dùng web công khai và file anh/chị đính kèm.</div>
    <div><b>Bấm lại để bật:</b> quay về dùng dữ liệu công việc, Copilot mở cuộc trò chuyện mới.</div>
  </div>
</div>

2. Dán prompt:

> **PROMPT:**
>
> Tóm tắt những khuyến nghị gần đây của các tổ chức y tế uy tín (như WHO, Bộ Y tế) về chăm sóc sản phụ trong 6 tuần sau sinh và về giao tiếp thấu cảm với sản phụ. Với mỗi khuyến nghị, nêu một việc điều dưỡng khoa Sản có thể áp dụng ngay. Tối đa 5 ý, mỗi ý kèm nguồn.

3. Hỏi tiếp để đưa vào giao ban:

> **PROMPT:**
>
> Từ các ý trên, soạn 3 thông điệp ngắn để tôi chia sẻ trong giao ban sáng thứ Tư, mỗi thông điệp không quá 2 câu, giọng gần gũi. Không đưa ra chỉ định chuyên môn.

> [!ANSWER]
> Khoảng 5 khuyến nghị có đường dẫn nguồn, ví dụ: thăm khám sau sinh nhiều lần trong 6 tuần đầu, hỗ trợ nuôi con bằng sữa mẹ, sàng lọc sức khỏe tinh thần của mẹ, hướng dẫn dấu hiệu nguy hiểm trước khi xuất viện. Câu hỏi tiếp cho ra 3 thông điệp ngắn, dễ nói. Câu trả lời **không** nhắc tới email hay file nội bộ nào, vì Work IQ đang tắt.

4. Bấm lại nút **Work IQ** để **bật** trước khi sang lab tiếp theo

> [!TIP]
> Không bắt buộc phải tắt Work IQ: khi Work IQ bật, Copilot tự chọn lấy thông tin từ dữ liệu công việc, từ web, hoặc cả hai. Tắt Work IQ hữu ích khi anh/chị muốn chắc chắn câu trả lời **chỉ** dựa trên thông tin công khai. Luôn mở nguồn để kiểm tra trước khi chia sẻ, đặc biệt với thông tin chuyên môn.

---

## Lưu ý tuân thủ

> [!NOTE]
> Không dán thông tin người bệnh vào prompt. Khi nhắc tới một trường hợp cụ thể, mô tả chung (ví dụ *"một sản phụ sinh mổ lần đầu"*). Thông tin từ web phải kiểm tra nguồn trước khi chia sẻ, và không dùng thay cho phác đồ của bệnh viện.

---

## Prompt đề xuất - Copilot Chat

### Điều dưỡng, nữ hộ sinh

> **PROMPT:**
>
> Trong email và tin nhắn Teams 3 ngày qua, có thông báo nào về thay đổi quy trình, lịch trực hoặc tập huấn mà tôi cần biết? Liệt kê ngắn gọn, ghi rõ áp dụng từ ngày nào.

### Hành chính khoa

> **PROMPT:**
>
> Tổng hợp các yêu cầu báo cáo mà khoa tôi nhận được từ các phòng chức năng trong tháng này: tên báo cáo, phòng yêu cầu, hạn nộp, đã nộp hay chưa (dựa trên email đã gửi). Trình bày dạng bảng.

### Chăm sóc khách hàng

> **PROMPT:**
>
> Dựa trên các email góp ý của người bệnh tôi nhận được trong 2 tuần qua, nhóm theo chủ đề (thời gian chờ, thái độ, viện phí, cơ sở vật chất), đếm số lượt mỗi nhóm và nêu nhóm nào đang tăng. Không nêu tên người bệnh.

### Trưởng khoa, điều dưỡng trưởng

> **PROMPT:**
>
> Chuẩn bị cho tôi nội dung giao ban tuần: các việc khoa đã cam kết với Ban Giám đốc trong các cuộc họp tháng này, tiến độ hiện tại theo email, và 3 vấn đề cần tôi quyết định. Mỗi ý ghi nguồn.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Gom việc cần làm từ email, lịch, Teams có hạn chót và nguồn | Work grounding |
| Đối chiếu kế hoạch với số liệu để tìm điểm còn thiếu | Phân tích nhiều tài liệu |
| Chọn nguồn thông tin: dữ liệu công việc hay web công khai | Work IQ bật / tắt |
