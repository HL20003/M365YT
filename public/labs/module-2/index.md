# Module 2 - Viết prompt hiệu quả

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau module này, anh/chị sẽ:

- Viết prompt rõ ràng theo công thức 4 thành phần
- Biết hỏi tiếp để chỉnh kết quả thay vì viết lại từ đầu
- Dùng 5 kỹ thuật giúp câu trả lời an toàn và chính xác hơn, đặc biệt quan trọng trong môi trường y tế
- Có sẵn bộ prompt mẫu theo nhịp làm việc và theo vai trò

---

## Prompt là gì?

**Prompt** là câu anh/chị gõ để giao việc cho Copilot, giống như nhờ một đồng nghiệp. Giao việc càng rõ, kết quả càng sát ý.

| Prompt chưa tốt | Prompt tốt hơn |
|-----------------|----------------|
| "Viết thông báo." | "Soạn thông báo gửi điều dưỡng khoa Sản về lịch tập huấn phòng cháy lúc 14:00 ngày 15/12 tại hội trường tầng 5, dưới 100 chữ, giọng thân thiện, nhắc mang thẻ nhân viên." |
| "Tóm tắt file." | "Tóm tắt báo cáo quý 3 trong 5 ý cho điều dưỡng trưởng, mỗi ý có một con số, ý đáng lo nhất để lên đầu." |
| "Trả lời email." | "Soạn thư trả lời gia đình người bệnh phàn nàn chờ xuất viện lâu: cảm ơn, xin lỗi cụ thể, không hứa mốc thời gian, dưới 150 chữ, giọng ấm áp." |

---

## Công thức 4 thành phần

| Thành phần | Tự hỏi | Ví dụ |
|------------|--------|-------|
| **Mục tiêu** | Tôi cần Copilot làm gì? | Soạn thông báo |
| **Ngữ cảnh** | Cho ai, để làm gì, tôi là ai? | gửi điều dưỡng khoa Sản, tôi là điều dưỡng hành chính |
| **Nguồn** | Dựa trên thông tin nào? | về lịch tập huấn phòng cháy ngày 15/12, theo file /Kế hoạch tập huấn |
| **Kỳ vọng** | Kết quả trông như thế nào? | dưới 100 chữ, giọng thân thiện, có gạch đầu dòng |

> **PROMPT:**
>
> Soạn thông báo gửi điều dưỡng khoa Sản về buổi tập huấn phòng chống cháy nổ lúc 14:00 ngày 15/12 tại hội trường tầng 5. Tôi là điều dưỡng hành chính của khoa. Nêu thành phần tham dự, nội dung chính, nhắc mang thẻ nhân viên và sắp xếp người trực thay. Dưới 100 chữ, giọng thân thiện.

> [!TIP]
> Không cần đủ 4 thành phần trong mọi prompt. Việc đơn giản thì một câu là đủ. Khi kết quả chưa sát ý, hãy bổ sung thành phần còn thiếu.

---

## Hỏi tiếp để cải thiện

Không cần viết đúng ngay lần đầu. Hãy hỏi tiếp trong cùng cuộc trò chuyện:

| Lần | Anh/chị gõ | Kết quả |
|-----|------------|---------|
| 1 | "Tóm tắt email chưa đọc." | Danh sách dài, khó biết việc nào gấp |
| 2 | "Chỉ giữ email của trưởng khoa, phòng chức năng và người bệnh, cho tôi biết việc cần làm." | Gọn hơn, có việc cần làm |
| 3 | "Trình bày dạng bảng, thêm cột hạn chót, xếp việc gấp lên đầu." | Dùng được ngay đầu ca |

Một số câu hỏi tiếp hay dùng: *"ngắn hơn"*, *"trình bày dạng bảng"*, *"giọng ấm áp hơn"*, *"viết lại cho người không có chuyên môn y tế"*, *"ghi rõ nguồn cho từng ý"*.

---

## 5 kỹ thuật để câu trả lời an toàn và chính xác hơn

### 1. Giao vai cho Copilot

> **PROMPT:**
>
> Bạn là chuyên viên Quản lý chất lượng của bệnh viện. Đọc quy trình bàn giao này và chỉ ra các bước có nguy cơ gây sai sót, mỗi nguy cơ kèm một đề xuất kiểm soát.

### 2. Đặt ràng buộc an toàn

Ngăn Copilot tự "điền" thông tin chưa chắc chắn, đặc biệt là con số và cam kết.

> **PROMPT:**
>
> Soạn thư trả lời người bệnh hỏi về chi phí gói sinh mổ. Không nêu con số nào không có trong file /Bảng giá dịch vụ. Chỗ nào chưa chắc chắn ghi [CẦN XÁC NHẬN].

### 3. Yêu cầu trích dẫn nguồn

> **PROMPT:**
>
> Điều dưỡng trực đêm cuối tuần được phụ cấp bao nhiêu? Trả lời dựa trên file /Chính sách Nhân sự và ghi rõ mục tham chiếu. Nếu tài liệu không có thông tin, nói rõ là không có.

### 4. Bảo Copilot hỏi lại khi thiếu thông tin

> **PROMPT:**
>
> Tôi cần soạn tờ trình xin bổ sung 2 điều dưỡng cho khoa Sản. Trước khi viết, hãy hỏi tôi những thông tin còn thiếu.

### 5. Đưa mẫu đầu ra

> **PROMPT:**
>
> Tóm tắt cuộc giao ban theo đúng mẫu sau cho từng khoa: "[Khoa] - Việc cần làm: [nội dung] - Người phụ trách: [tên] - Hạn: [ngày] - Liên quan an toàn người bệnh: [có/không]".

---

## Bài tập 5 phút: Sửa một prompt chưa tốt

Đây là prompt chưa tốt: **"viết thông báo"**. Hãy viết lại cho đủ 4 thành phần, chọn một tình huống quen thuộc ở khoa của anh/chị, rồi dán vào [Copilot Chat](https://m365.cloud.microsoft/) để xem kết quả.

> [!ANSWER]
> Ví dụ một prompt đủ 4 thành phần:
>
> *"Soạn thông báo **(mục tiêu)** gửi toàn bộ điều dưỡng và hộ lý khoa Nhi, tôi là điều dưỡng trưởng **(ngữ cảnh)**, về việc giao ban sáng chuyển từ 7:00 sang 7:15 bắt đầu từ thứ Hai 07/12 để ca đêm bàn giao kịp **(nguồn)**. Dưới 80 chữ, giọng thân thiện, kết thúc bằng lời cảm ơn **(kỳ vọng)**."*
>
> Kiểm tra lại: prompt của anh/chị đã nói rõ **làm gì**, **cho ai**, **thông tin gì** và **trông ra sao** chưa?

---

## Đính kèm file và Prompt Gallery

- **Copilot Chat, Outlook, PowerPoint:** gõ `/` rồi gõ vài chữ trong tên file để chọn file trên OneDrive/SharePoint
- **Word, Excel:** Copilot làm việc trực tiếp với file đang mở
- **Prompt Gallery:** xem và lưu prompt hay tại [Copilot Prompt Gallery](https://copilot.cloud.microsoft/prompts), chia sẻ cho đồng nghiệp trong khoa

---

## Thư viện prompt theo nhịp làm việc

### Đầu ca, đầu ngày

> **PROMPT:**
>
> Tóm tắt email và tin nhắn Teams từ hôm qua, chia thành: việc cần tôi xử lý trong ca này, người đang chờ tôi phản hồi, thông báo thay đổi quy trình hoặc lịch trực.

### Trước một cuộc họp

> **PROMPT:**
>
> Chuẩn bị cho tôi cuộc họp [tên cuộc họp]: tóm tắt email và tài liệu liên quan, những gì đã thống nhất lần trước, và 3 câu hỏi nên đặt.

### Sau cuộc họp

> **PROMPT:**
>
> Liệt kê việc cần làm của từng khoa trong cuộc họp vừa rồi, kèm thời hạn, đánh dấu việc chưa có người phụ trách rõ ràng.

### Cuối tuần

> **PROMPT:**
>
> Tóm tắt những việc quan trọng tôi đã xử lý trong tuần dựa trên email, cuộc họp và tài liệu, và liệt kê việc còn tồn chuyển sang tuần sau.

---

## Gợi ý prompt theo vai trò

| Vai trò | Ví dụ prompt |
|---------|--------------|
| **Điều dưỡng, nữ hộ sinh** | "Viết lại hướng dẫn cho con bú trong file /[tên file] thành 5 bước ngắn cho sản phụ lần đầu sinh con, xưng 'mẹ', không thêm lời khuyên mới." |
| **Hành chính khoa** | "Từ email của các phòng chức năng tháng này, lập bảng các báo cáo khoa phải nộp: tên báo cáo, phòng yêu cầu, hạn nộp, đã nộp chưa." |
| **Chăm sóc khách hàng** | "Nhóm các góp ý của người bệnh trong file /[tên file] theo chủ đề, đếm số lượt và đề xuất 3 câu trả lời mẫu cho nhóm nhiều nhất." |
| **Trưởng khoa, điều dưỡng trưởng** | "Từ file /[báo cáo tháng], soạn 5 ý báo cáo Ban Giám đốc: kết quả so với kế hoạch, vấn đề nổi bật kèm số liệu, đề xuất cần hỗ trợ." |
| **Quản lý chất lượng** | "Từ các báo cáo sự cố trong file /[tên file] đã ẩn danh, nhóm theo loại sự cố và khoa, chỉ ra 3 xu hướng cần chú ý." |
| **Nhân sự, đào tạo** | "Soạn kế hoạch đào tạo định hướng 2 tuần cho điều dưỡng mới khoa Sản: mục tiêu từng ngày, người hướng dẫn, cách đánh giá." |

---

## Tóm lại

| Nguyên tắc | Ý chính |
|------------|---------|
| **Rõ ràng** | Mục tiêu, ngữ cảnh, nguồn, kỳ vọng |
| **Hỏi tiếp** | Bắt đầu đơn giản, chỉnh dần trong cùng cuộc trò chuyện |
| **An toàn** | Giao vai, ràng buộc, yêu cầu trích dẫn, bảo Copilot hỏi lại |
| **Chỉ đúng nguồn** | Gõ "/" để đính kèm file |
| **Bảo mật** | Không đưa thông tin người bệnh vào prompt |

Tiếp theo: **[Module 3 - Personalization in Copilot](#module-3)**.
