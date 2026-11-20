# Lab 8 - Agent Builder in Copilot Chat

**Ứng dụng:** Microsoft 365 Copilot Chat, Agent Builder

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

> [!TIP]
> Nếu tài khoản chưa được phép tạo agent, người hướng dẫn sẽ trình diễn Bài tập 1-2, và anh/chị dùng agent dựng sẵn để làm Bài tập 3.

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Tạo một trợ lý AI cho cả khoa chỉ bằng tiếng Việt, không cần lập trình
- Cấu hình instructions, knowledge và starter prompts để agent trả lời đúng phạm vi
- Kiểm thử agent với câu hỏi thật, câu hỏi ngoài phạm vi và tình huống có dữ liệu nhạy cảm

### Khái niệm cần biết

| Khái niệm | Giải thích |
|-----------|------------|
| **Agent** | Trợ lý AI anh/chị tự tạo cho một việc cụ thể |
| **Instructions** | Lời dặn cho agent: trả lời thế nào, được và không được làm gì |
| **Knowledge** | Tài liệu agent dùng để trả lời (file, thư mục SharePoint) |
| **Starter prompts** | Câu hỏi gợi ý hiện sẵn để người dùng bấm vào |

---

## Tình huống

> Mỗi tháng, Phòng Nhân sự và các điều dưỡng trưởng nhận hàng chục câu hỏi lặp lại: được nghỉ phép bao nhiêu ngày, trực Tết được phụ cấp bao nhiêu, đổi ca phải báo ai, cần bao nhiêu tiết đào tạo liên tục. Anh/chị tạo **HR Assistant** để nhân viên tự tra cứu 24/7. Agent chỉ trả lời dựa trên Chính sách Nhân sự và luôn ghi rõ mục tham chiếu.

**Knowledge:** [Chính sách Nhân sự.pdf](#file-hr), đã lưu trên OneDrive.

---

### Bài tập 1: Tạo agent bằng mô tả tiếng Việt

1. Vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) bằng **tài khoản công ty**, mở **Copilot**
2. Ở thanh bên trái, tìm mục **Agents**, bấm **Create agent** (hoặc **New agent**)

> [!TIP]
> Nếu không thấy nút tạo agent, nhấn `Ctrl + F5` để tải lại trang, hoặc báo người hướng dẫn.

3. Ở tab **Describe**, dán mô tả sau và bấm **Gửi**:

> **PROMPT:**
>
> Tôi muốn tạo trợ lý tra cứu chính sách nhân sự cho toàn bộ nhân viên bệnh viện, phần lớn là điều dưỡng, nữ hộ sinh làm việc theo ca. Trợ lý trả lời về thời giờ làm việc, đổi ca, nghỉ phép năm, nghỉ việc riêng, phụ cấp trực, đào tạo liên tục và thẩm quyền phê duyệt. Trả lời ngắn gọn, có ví dụ tính cụ thể khi người hỏi nêu số năm làm việc hoặc số ca trực, và luôn ghi rõ mục trong Chính sách Nhân sự.

4. Agent Builder tự tạo tên, mô tả, instructions và starter prompts. Nếu tên chưa đúng, gõ tiếp:

> **PROMPT:**
>
> Đặt tên agent là "HR Assistant". Giọng thân thiện, xưng "mình" và gọi người hỏi là "anh/chị". Trình bày định mức và cấp phê duyệt dạng bảng khi có thể.

### Bài tập 2: Đặt giới hạn, thêm knowledge và tạo agent

1. Chuyển sang tab **Configure**, kiểm tra ô **Instructions** có đủ các ý dưới đây. Nếu thiếu, dán thêm:

> **PROMPT:**
>
> Chỉ trả lời dựa trên Chính sách Nhân sự được cung cấp và ghi rõ mục tham chiếu. Nếu tài liệu không có thông tin, nói rõ là chưa có thông tin và hướng dẫn liên hệ Phòng Nhân sự (máy lẻ 1010). Không trả lời câu hỏi ngoài chính sách nhân sự, không tư vấn chuyên môn y khoa. Không tự phê duyệt hay hứa thay cấp có thẩm quyền. Không trả lời về lương, kỷ luật của một cá nhân cụ thể. Nếu người dùng nhập số CCCD, số tài khoản hoặc thông tin sức khỏe, nhắc họ không chia sẻ thông tin này trong cuộc trò chuyện.

2. Trong tab **Configure**, kéo xuống **Knowledge**, bấm thêm file, chọn [Chính sách Nhân sự.pdf](#file-hr)
3. Bật **Only use specified sources** (nếu có) để agent chỉ trả lời từ tài liệu đã chọn
4. Ở **Starter prompts**, thêm 4 câu gợi ý:
   - Tôi làm 6 năm thì được bao nhiêu ngày phép?
   - Điều dưỡng trực đêm mùng 2 Tết được phụ cấp bao nhiêu?
   - Muốn đổi ca thì làm thế nào?
   - Tôi cần bao nhiêu tiết đào tạo liên tục?
5. Bấm **Create**

> [!NOTE]
> Với agent trả lời về chính sách, nên luôn bật **Only use specified sources**: agent chính xác hơn và không "bịa" định mức. Trong thực tế, nên dùng **thư mục SharePoint do Phòng Nhân sự quản lý** làm knowledge, để agent luôn dùng phiên bản chính sách mới nhất.

### Bài tập 3: Kiểm thử agent

Hỏi lần lượt trong khung **Test** bên phải (hoặc trong agent đã tạo):

> **PROMPT:**
>
> Mình là điều dưỡng, đã làm ở bệnh viện 6 năm. Năm nay mình được bao nhiêu ngày phép? Phép năm ngoái còn 7 ngày thì được chuyển sang không?

> **PROMPT:**
>
> Mình là điều dưỡng, có tên trong lịch trực đêm mùng 2 Tết và đêm mùng 5 Tết. Phụ cấp trực của mình là bao nhiêu? Mình có được xin nghỉ phép trong 7 ngày Tết không?

> **PROMPT:**
>
> Mình muốn đổi ca đêm thứ Bảy với một bạn hộ lý cùng khoa có được không? Cần báo ai, trước bao lâu?

> **PROMPT:**
>
> Giá vàng hôm nay bao nhiêu?

> **PROMPT:**
>
> Số CCCD của mình là 0790xxxxxxxx, kiểm tra giúp mình còn bao nhiêu ngày phép.

> [!ANSWER]
> - **Câu 1:** 12 + 1 = **13 ngày** (đủ 5 năm cộng 1 ngày). Phép cũ chỉ chuyển **tối đa 5 ngày**, dùng trước 31/03 (**Mục 3.2, 3.3**).
> - **Câu 2:** mùng 2 Tết **300.000 x 3 = 900.000 đồng**, mùng 5 Tết **300.000 x 2 = 600.000 đồng** (**Mục 5, 5.1**). Không đăng ký nghỉ phép trong 7 ngày Tết khi đã có tên trong lịch trực (**Mục 3.5**).
> - **Câu 3:** **không được**, vì đổi ca phải giữa hai người **cùng chức danh**. Nếu đổi với một điều dưỡng khác, đề nghị trên hệ thống và được Điều dưỡng trưởng khoa duyệt **trước 24 giờ** (**Mục 2.4**).
> - **Câu 4:** từ chối lịch sự, nhắc phạm vi chính sách nhân sự.
> - **Câu 5:** nhắc **không chia sẻ số CCCD**, hướng dẫn tra cứu trên hệ thống nhân sự hoặc liên hệ Phòng Nhân sự (**Mục 8**).

> [!TIP]
> Nếu agent trả lời sai hoặc không ghi mục, sửa **Instructions** rồi hỏi lại. Đây là cách cải thiện agent nhanh nhất.

---

## Lưu ý tuân thủ

> [!NOTE]
> Chỉ chia sẻ agent khi tài liệu nguồn đã được phê duyệt phát hành. Agent chỉ trả lời trong phạm vi quyền truy cập của người dùng: người không có quyền đọc file thì agent cũng không trả lời từ file đó. Agent tự tạo chỉ dùng trong nội bộ.

---

## Tự thực hành: agent cho khoa của anh/chị

| Ý tưởng | Knowledge | Starter prompts gợi ý |
|---------|-----------|------------------------|
| **Trợ lý điều dưỡng mới** | Sổ tay định hướng, quy trình của khoa | "Ngày đầu tiên tôi cần làm gì?", "Bàn giao ca gồm những gì?" |
| **Trợ lý SOP khoa** | Thư mục SOP đã ban hành | "Quy trình chuẩn bị sản phụ trước mổ?", "Biểu mẫu nào dùng khi chuyển khoa?" |
| **Trợ lý chăm sóc khách hàng** | Bảng giá dịch vụ, câu hỏi thường gặp | "Gói sinh thường gồm những gì?", "Giờ thăm người bệnh?" |

1. **Chủ đề:** agent hỗ trợ việc gì, cho ai?
2. **Giọng điệu:** thân thiện hay trang trọng?
3. **Knowledge:** thư mục SharePoint nào, ai đang có quyền đọc?
4. **Giới hạn:** agent không được trả lời điều gì?

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Tạo trợ lý không cần lập trình | Agent Builder (Describe) |
| Giới hạn phạm vi và bảo vệ dữ liệu | Instructions, Only use specified sources |
| Trả lời có nguồn | Knowledge |
| Kiểm thử với câu hỏi thật và câu hỏi khó | Test pane |
