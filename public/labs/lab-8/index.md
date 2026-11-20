# Lab 8 - Agent Builder in Copilot Chat

**Ứng dụng:** Microsoft 365 Copilot Chat, Agent Builder

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

> [!TIP]
> Nếu tài khoản chưa được phép tạo agent, người hướng dẫn sẽ trình diễn Phần A-C, và anh/chị dùng agent dựng sẵn để làm Phần D.

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Tạo một trợ lý AI cho cả khoa chỉ bằng tiếng Việt, không cần lập trình
- Cấu hình instructions, knowledge và starter prompts để agent trả lời đúng phạm vi
- Kiểm tra câu trả lời của agent, kể cả câu hỏi ngoài phạm vi và tình huống có dữ liệu nhạy cảm, trước khi chia sẻ với đồng nghiệp

---

## Khái niệm cần biết

| Khái niệm | Giải thích |
|-----------|------------|
| **Agent** | Trợ lý AI anh/chị tự tạo cho một việc cụ thể, trả lời dựa trên instructions và knowledge đã cấu hình |
| **Instructions** | Lời dặn cho agent: làm gì, trả lời theo giọng điệu nào và không được làm gì |
| **Knowledge** | Tài liệu agent dùng để trả lời (file, thư mục SharePoint), giúp câu trả lời chính xác và có nguồn |
| **Starter prompts** | Câu hỏi gợi ý hiện sẵn trên giao diện chat để người dùng bấm vào và bắt đầu |

Agent Builder có hai cách làm việc, lab này dùng lần lượt từng cách:

| Cách | Dùng để | Trong lab |
|------|---------|-----------|
| **Mô tả bằng prompt** (Describe) | Gõ mô tả agent bằng tiếng Việt rồi nhấn **Send**; Agent Builder tự điền cấu hình | Phần B |
| **Configure** | Xem và chỉnh trực tiếp từng trường: Name, Description, Instructions, Knowledge, Starter prompts | Phần C |

Khung chat thử nghiệm bên phải màn hình luôn hiển thị để anh/chị thử agent bất cứ lúc nào (Phần D).

---

## Tình huống

> Mỗi tháng, Phòng Nhân sự và các điều dưỡng trưởng nhận hàng chục câu hỏi lặp lại: được nghỉ phép bao nhiêu ngày, trực Tết được phụ cấp bao nhiêu, đổi ca phải báo ai, cần bao nhiêu tiết đào tạo liên tục. Anh/chị tạo **HR Assistant** để nhân viên tự tra cứu 24/7. Agent chỉ trả lời dựa trên Chính sách Nhân sự và luôn ghi rõ mục tham chiếu.

**Knowledge:** [Chính sách Nhân sự.pdf](#file-hr) - tải file và lưu vào **OneDrive** của anh/chị trước khi bắt đầu (xem [cách tải file về và đưa lên OneDrive](#module-1/cach-tai-file-ve-may-va-dua-len-onedrive)).

**Kết quả cuối lab:** một agent tên **HR Assistant**, trả lời từ Chính sách Nhân sự, có dẫn mục, từ chối câu hỏi ngoài phạm vi, nhắc không chia sẻ dữ liệu cá nhân và có link chia sẻ cho đồng nghiệp.

---

## Phần A: Mở Agent Builder

### Bước 1: Mở Agent Builder

1. Vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) bằng **tài khoản công ty**, mở **Copilot**
2. Ở thanh điều hướng bên trái, tìm mục **Agents**, chọn **New Agent** (hoặc **Create agent**)
3. Màn hình Agent Builder mở ra: ô mô tả agent ở giữa, nút **Configure** để chỉnh chi tiết, khung chat thử nghiệm ở bên phải

> [!TIP]
> Agent Builder còn cho phép **chọn một template có sẵn** rồi tuỳ chỉnh bằng **Configure**. Lab này tạo agent từ đầu bằng prompt để anh/chị nắm được từng phần cấu hình.

> [!NOTE]
> Giao diện Copilot được Microsoft cập nhật thường xuyên, nên vị trí nút và tên gọi trên máy anh/chị có thể hơi khác hướng dẫn. Nếu không thấy **New Agent**, nhấn `Ctrl + F5` để tải lại trang, hoặc báo người hướng dẫn.

---

## Phần B: Mô tả agent bằng prompt

Nhập lần lượt **cả 3 prompt** dưới đây vào ô mô tả, mỗi prompt nhấn **Send**. Đợi Agent Builder trả lời xong rồi mới gửi prompt tiếp theo. Agent Builder có thể hỏi thêm để làm rõ; 3 prompt dưới đây đã trả lời sẵn các câu hỏi thường gặp, nên anh/chị chỉ cần gửi prompt tiếp theo.

### Bước 2: Mô tả mục đích của agent

> **PROMPT:**
>
> Tôi muốn tạo trợ lý tra cứu chính sách nhân sự tên "HR Assistant" cho toàn bộ nhân viên bệnh viện, phần lớn là điều dưỡng, nữ hộ sinh làm việc theo ca. Trợ lý trả lời về thời giờ làm việc, đổi ca, nghỉ phép năm, nghỉ việc riêng, phụ cấp trực, đào tạo liên tục và thẩm quyền phê duyệt.

### Bước 3: Quy định giọng điệu và cách trình bày

> **PROMPT:**
>
> Giọng thân thiện, dễ hiểu, xưng "mình" và gọi người hỏi là "anh/chị", phù hợp với nhân viên đang tranh thủ hỏi giữa ca. Trả lời ngắn gọn, có ví dụ tính cụ thể khi người hỏi nêu số năm làm việc hoặc số ca trực. Trình bày định mức và cấp phê duyệt dạng bảng khi có thể. Cuối mỗi câu trả lời ghi rõ mục tương ứng, ví dụ "(Nguồn: Chính sách Nhân sự, Mục 3.2)".

### Bước 4: Định nghĩa giới hạn của agent

> **PROMPT:**
>
> Agent chỉ trả lời dựa trên Chính sách Nhân sự được cung cấp. Nếu tài liệu không có thông tin, nói rõ là chưa có thông tin và hướng dẫn liên hệ Phòng Nhân sự (máy lẻ 1010). Không trả lời câu hỏi ngoài chính sách nhân sự, không tư vấn chuyên môn y khoa. Không tự phê duyệt hay hứa thay cấp có thẩm quyền. Không trả lời về lương, kỷ luật của một cá nhân cụ thể. Nếu người dùng nhập số CCCD, số tài khoản hoặc thông tin sức khỏe, nhắc họ không chia sẻ thông tin này trong cuộc trò chuyện.

> [!NOTE]
> Sau 3 prompt, Agent Builder đã tự điền **tên**, **mô tả**, **instructions** và **starter prompts**. Nội dung tự sinh có thể hơi khác nhau giữa các học viên, điều này là bình thường. Phần C sẽ kiểm tra và chỉnh lại.

---

## Phần C: Kiểm tra và hoàn thiện trong Configure

### Bước 5: Kiểm tra Name, Description và Instructions

1. Chọn **Configure**
2. Kiểm tra từng trường:

| Trường | Cần thấy | Nếu chưa đúng |
|--------|----------|---------------|
| **Name** | HR Assistant | Sửa trực tiếp trong ô Name |
| **Description** | Một câu mô tả agent giúp nhân viên tra cứu chính sách nhân sự của bệnh viện | Sửa trực tiếp |
| **Instructions** | Có đủ: phạm vi, giọng điệu, dẫn mục, không tư vấn y khoa, không phê duyệt thay, không trả lời về cá nhân cụ thể, nhắc không chia sẻ CCCD/sức khỏe | Bổ sung câu còn thiếu vào cuối ô Instructions |

> [!TIP]
> Từ đây trở đi, nên chỉnh trực tiếp trong **Configure** thay vì quay lại gõ prompt mô tả. Prompt mô tả mới có thể khiến Agent Builder viết lại toàn bộ Instructions và làm mất phần anh/chị đã sửa tay.

### Bước 6: Thêm Chính sách Nhân sự làm knowledge

1. Kéo xuống phần **Knowledge**
2. Thêm file [Chính sách Nhân sự.pdf](#file-hr): chọn file đã lưu trên **OneDrive**, hoặc tải file lên trực tiếp
3. Bật toggle **Only use specified sources** để agent chỉ dùng tài liệu đã chọn, không dùng kiến thức chung hay nội dung web

> [!NOTE]
> Với agent trả lời về chính sách, nên luôn bật **Only use specified sources**: câu trả lời kiểm chứng được và agent không tự "bịa" số ngày phép hay mức phụ cấp. Đổi lại, agent sẽ không trả lời được câu hỏi nằm ngoài tài liệu, và đó chính là hành vi mong muốn.

### Bước 7: Chỉnh starter prompts

Kéo xuống phần **Starter prompts**. Giữ hoặc thay để có các câu hỏi nhân viên hay hỏi nhất, ví dụ:

| Title | Message |
|-------|---------|
| Ngày phép | Tôi làm 6 năm thì được bao nhiêu ngày phép? |
| Phụ cấp trực Tết | Điều dưỡng trực đêm mùng 2 Tết được phụ cấp bao nhiêu? |
| Đổi ca | Muốn đổi ca thì làm thế nào, báo ai? |
| Đào tạo liên tục | Tôi cần bao nhiêu tiết đào tạo liên tục mỗi năm? |

---

## Phần D: Test agent trước khi tạo

### Bước 8: Thử agent trong khung chat thử nghiệm

Nhập lần lượt các câu hỏi dưới đây vào khung chat thử nghiệm bên phải, nhấn **Send**, rồi mở phần đáp án để so sánh.

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
> | Câu hỏi | Câu trả lời đúng (theo Chính sách Nhân sự) |
> |---------|---------------------------------------------|
> | Phép năm, 6 năm làm việc | 12 + 1 = **13 ngày** (đủ 5 năm cộng 1 ngày). Phép cũ chỉ chuyển **tối đa 5 ngày**, dùng trước 31/03. Nguồn: Mục 3.2, 3.3 |
> | Trực Tết | Mùng 2 Tết **300.000 x 3 = 900.000 đồng**, mùng 5 Tết **300.000 x 2 = 600.000 đồng**. Không đăng ký nghỉ phép trong 7 ngày Tết khi đã có tên trong lịch trực. Nguồn: Mục 5, 5.1, 3.5 |
> | Đổi ca với hộ lý | **Không được**, vì đổi ca phải giữa hai người **cùng chức danh**. Nếu đổi với một điều dưỡng khác: đề nghị trên hệ thống, Điều dưỡng trưởng khoa duyệt **trước 24 giờ**. Nguồn: Mục 2.4 |
> | Giá vàng | Agent **từ chối** lịch sự vì ngoài phạm vi chính sách nhân sự |
> | Số CCCD | Agent nhắc **không chia sẻ số CCCD**, hướng dẫn tra cứu trên hệ thống nhân sự hoặc liên hệ Phòng Nhân sự. Nguồn: Mục 8 |

Nếu câu trả lời chưa đạt (không dẫn mục, sai số liệu, vẫn trả lời câu hỏi giá vàng, không nhắc về số CCCD), quay lại **Configure**: kiểm tra toggle **Only use specified sources** đã bật chưa, và bổ sung vào ô **Instructions** quy tắc còn thiếu. Sau đó test lại.

---

## Phần E: Tạo và chia sẻ agent

### Bước 9: Tạo agent và lấy link chia sẻ

1. Khi đã hài lòng với kết quả test, chọn **Create**
2. Khi tạo xong, màn hình hiện liên kết tới agent. Nhấn **Copy** để sao chép liên kết
3. Chọn **Change sharing settings** và chọn phạm vi chia sẻ. Vì agent dùng file trên OneDrive/SharePoint làm knowledge, nên chọn **Specific users in your organization** và nhập tên đồng nghiệp hoặc nhóm cần dùng
4. Nhấn **Save**
5. Dán liên kết vào email hoặc Teams chat để gửi cho đồng nghiệp
6. Mở agent từ mục **Agents** ở thanh điều hướng bên trái và hỏi lại một câu trong Bước 8

> [!NOTE]
> - Người nhận chỉ dùng được agent, **không sửa được**; chỉ chủ sở hữu agent mới chỉnh sửa được.
> - Agent tôn trọng phân quyền: người không có **quyền đọc** file Chính sách Nhân sự thì agent không trả lời từ file đó cho người ấy. Trong thực tế, nên đặt tài liệu trong một **thư mục hoặc site SharePoint** do Phòng Nhân sự quản lý và cấp quyền đọc cho đúng nhóm nhân viên; khi chính sách được cập nhật, agent tự dùng phiên bản mới.

> [!TIP]
> Để chia sẻ lại sau này: chọn **HR Assistant** ở thanh điều hướng bên trái → **... (More)** → **Share**. Menu **...** này cũng là nơi mở lại agent để chỉnh sửa.

---

## Lưu ý tuân thủ

> [!NOTE]
> - Chỉ chia sẻ agent khi tài liệu nguồn đã được phê duyệt phát hành.
> - Agent tự tạo chỉ dùng trong nội bộ; knowledge phải là thư mục SharePoint có phân quyền.
> - Không dùng agent để tư vấn chẩn đoán, điều trị, và không đưa thông tin người bệnh vào knowledge.
> - Bật **Only use specified sources** với mọi agent trả lời về chính sách, định mức, quy trình.

---

## Tự thực hành: agent cho khoa của anh/chị

Lặp lại quy trình trên với một chủ đề của riêng anh/chị. Một vài ý tưởng:

| Ý tưởng | Knowledge | Starter prompts gợi ý |
|---------|-----------|------------------------|
| **Trợ lý điều dưỡng mới** | Sổ tay định hướng, quy trình của khoa | "Ngày đầu tiên tôi cần làm gì?", "Bàn giao ca gồm những gì?" |
| **Trợ lý SOP khoa** | Thư mục SOP đã ban hành | "Quy trình chuẩn bị sản phụ trước mổ?", "Biểu mẫu nào dùng khi chuyển khoa?" |
| **Trợ lý chăm sóc khách hàng** | Bảng giá dịch vụ, câu hỏi thường gặp | "Gói sinh thường gồm những gì?", "Giờ thăm người bệnh?" |

1. **Chủ đề** - Agent hỗ trợ việc gì, cho ai?
2. **Người dùng và giọng điệu** - Điều dưỡng, hành chính hay khách hàng? Thân thiện hay trang trọng?
3. **Knowledge** - Thư mục SharePoint nào làm nguồn? Ai đang có quyền đọc?
4. **Giới hạn** - Agent không được trả lời hoặc cam kết điều gì?
5. **Starter prompts** - 3-4 câu hỏi người dùng hay hỏi nhất
6. **Bộ câu test** - 3 câu có đáp án rõ trong tài liệu và 1 câu ngoài phạm vi để kiểm tra agent có từ chối không

---

## Tổng kết

| Anh/chị đã làm được | Ở bước |
|---------------------|--------|
| Mô tả agent bằng tiếng Việt, không cần lập trình | Mô tả bằng prompt (Bước 2-4) |
| Kiểm tra và chỉnh Name, Description, Instructions | Configure (Bước 5) |
| Gắn Chính sách Nhân sự làm knowledge, giới hạn agent chỉ dùng nguồn này | Configure (Bước 6) |
| Thiết kế starter prompts | Configure (Bước 7) |
| Test bằng bộ câu hỏi có đáp án, kể cả câu ngoài phạm vi và dữ liệu nhạy cảm | Khung chat thử nghiệm (Bước 8) |
| Tạo agent và chia sẻ link cho đồng nghiệp | Create (Bước 9) |
