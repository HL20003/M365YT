# Chuẩn bị cho người hướng dẫn

> [!NOTE]
> Trang này chỉ hiển thị khi bật **chế độ Trainer**: mở site với `?trainer=1` ở cuối địa chỉ (ví dụ `https://.../?trainer=1`). Trình duyệt sẽ ghi nhớ chế độ này; mở `?trainer=0` để tắt trước khi trình chiếu cho học viên.

---

## Làm trước buổi học 1 ngày

1. Kiểm tra mọi học viên đã được gán licence **Microsoft 365 Copilot** và thấy nút Copilot trong Word, Excel, PowerPoint, Outlook, Teams.
2. Tạo thư mục **Training Copilot** trên OneDrive hoặc SharePoint, tải bộ file demo lên và chia sẻ quyền xem/chỉnh sửa cho học viên.
3. Gửi trước cho mỗi học viên các [email mẫu](#trainer/email-mau-gui-truoc-cho-hoc-vien): email lịch trực Tết, email nhà cung cấp và **chuỗi 4 thư** góp ý xuất viện (Lab 1, Lab 5).
4. Gửi lời mời họp **"Họp cải tiến quy trình xuất viện"** cho học viên (Lab 5 Bài 3), xem [nội dung lời mời](#trainer/loi-moi-hop-cho-lab-5).
5. Tạo nhóm chat Teams **"Training Copilot"** với học viên và đăng các [tin nhắn mẫu](#trainer/tin-nhan-mau-cho-nhom-chat-training-copilot) (Lab 6 Bài 3).
6. **Lab 6:** tạo cuộc họp Teams 15 phút với học viên, bật **Recording** và **Transcript**, đọc [kịch bản họp mẫu](#trainer/kich-ban-hop-mau-cho-lab-6). Nên cho học viên vào họp muộn 3-4 phút để làm Bài 1.
7. **Lab 7:** kiểm tra học viên thấy **Researcher** trong mục **Agents** của Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)). Nếu không, trình diễn trên máy chiếu. Nên chạy thử đề bài trước 1 ngày vì Researcher mất 3-10 phút.
8. **Lab 8:** kiểm tra tenant cho phép tạo agent trong Copilot Chat. Nếu không, chuyển sang trình diễn và dựng sẵn agent **HR Assistant** để học viên làm Phần D (Bước 8).
9. Chuẩn bị **tài khoản dự phòng** cho học viên gặp lỗi licence.

**Thời lượng gợi ý:** mỗi Lab 25 đến 30 phút. Nghỉ giải lao 15 phút sau Lab 4. Mỗi lab có 3 bài; nếu thiếu thời gian, làm Bài 1-2 trên lớp và để Bài 3 cho học viên tự làm sau.

---

## Bộ file demo

Mọi file dùng **đơn vị và số liệu giả định** (4 cơ sở A, B, C, D), không gắn với bệnh viện có thật.

| File | Dùng ở Lab | Nội dung và số liệu cài sẵn |
|------|-----------|------------------------------|
| [Thông báo lịch trực Tết 2027.docx](#file-tet) | 2 | Bản nháp dài, một đoạn hơn 200 chữ bắt đầu bằng "Như anh chị em đã biết...", bảng trực lãnh đạo 4 cơ sở; thiếu mẫu danh sách, giờ ca trực Tết |
| [Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx](#file-postpartum) | 2 | Văn phong chuyên môn (sản dịch, co hồi tử cung...), mục "Dấu hiệu cần quay lại bệnh viện ngay" có 9 dấu hiệu |
| [Dự thảo Hợp đồng cung ứng vật tư.docx](#file-contract) | 2 | 7,8 tỷ đồng; tạm ứng 50% không bảo lãnh; phạt chậm 0,05%/ngày tối đa 5%; không có điều khoản thu hồi; ghi chú: mới 2 báo giá |
| [Chính sách Mua sắm nội bộ.pdf](#file-procurement) | 2 | Tạm ứng tối đa 30% kèm bảo lãnh (4.1); phạt chậm tối thiểu 0,1%/ngày, trần 8% (4.2); thu hồi lô lỗi trong 48 giờ (4.3); 3 báo giá (2.1); từ 5 tỷ: Tổng Giám đốc sau Pháp chế (Mục 3) |
| [Báo cáo Hoạt động Q3 2026 - 4 cơ sở.xlsx](#file-report) | 1, 3, 7 | 5 sheet dạng Table, xem [số liệu cài sẵn](#trainer/so-lieu-cai-san-trong-file-excel) |
| [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan) | 1, 4, 7 | Có giải pháp cho nghỉ việc điều dưỡng và hài lòng Cơ sở C; **không đề cập** quá tải Cơ sở D, chi phí vật tư, thời gian chờ xuất viện |
| [Tài liệu đào tạo Phụng sự từ tâm.docx](#file-culture) | 4 | Câu chuyện hệ thống, 6 giá trị cốt lõi, quy tắc giao tiếp, 4 bước xử lý khi người bệnh không hài lòng, 3 tình huống |
| [Chính sách Nhân sự.pdf](#file-hr) | 8 | Đổi ca (2.4), phép năm (Mục 3), nghỉ việc riêng (Mục 4), phụ cấp trực (Mục 5), đào tạo liên tục 48 tiết/2 năm (Mục 6), thẩm quyền (Mục 7), bảo mật (Mục 8) |

[download-files]

### Số liệu cài sẵn trong file Excel

| Chỉ số | Cơ sở A | Cơ sở B | Cơ sở C | Cơ sở D | Toàn hệ thống |
|---|---|---|---|---|---|
| Công suất giường | 72% | **58%** | 81% | **96%** (khoa Sản 102%) | 79% (chuẩn 85%) |
| Ca sinh Q3 | 785 | 465 | 1.045 | **1.885** | 4.180 (KH 4.000) |
| Nghỉ việc điều dưỡng (năm hóa) | 13,3% | 14,3% | 18,5% | 21,0% | **18%** (chuẩn 12%) |
| Giờ làm thêm / điều dưỡng / tháng | 10,5 | 7,2 | 16,7 | 21,9 | 16,4 (KH 12) |
| Vật tư KH / TH (tỷ) | 8,0 / 9,4 | 6,0 / 7,0 | 14,0 / 17,2 | 20,0 / 27,4 | 48 / 61 (**vượt 27%**) |
| Hài lòng Q2 → Q3 | 4,4 → 4,5 | 4,3 → 4,4 | **4,5 → 4,1** | 4,6 → 4,5 | 4,4 |
| Chờ xuất viện TB (giờ) | 2,1 | 1,8 | 2,9 | **3,4** | 2,6 (KH 2,0) |
| Góp ý về xuất viện | 12 | 6 | 47 | **64** | 129/377 (34%) |
| Góp ý về thái độ giao tiếp | 6 | 3 | **31** | 18 | 58 |

---

## Email mẫu gửi trước cho học viên

### Email 1: Lịch trực Tết

**Người gửi:** người hướng dẫn (đóng vai Phòng Hành chính - Nhân sự). **Tiêu đề:** Gửi danh sách trực Tết 2027 trước ngày 15/12

> **COPY:**
>
> Chào các anh chị,
>
> Phòng Hành chính - Nhân sự đề nghị các khoa gửi danh sách trực Tết Nguyên đán 2027 (từ 04/02 đến 10/02/2027) về phòng trước ngày 15/12/2026, theo thông báo đính kèm. Lưu ý mỗi nhân viên trực không quá 3 ca trong 7 ngày Tết, ưu tiên nghỉ cho người đã trực Tết năm 2026.
>
> Khoa nào gửi trễ sẽ ảnh hưởng tới việc tổng hợp chung và chi trả phụ cấp trực Tết.
>
> Trân trọng,
> Nguyễn Hoài An - Phòng Hành chính - Nhân sự

### Email 2: Nhà cung cấp

**Tiêu đề:** Xác nhận số lượng vật tư giao tháng 12

> **COPY:**
>
> Kính gửi khoa Sản,
>
> Công ty chúng tôi chuẩn bị đợt giao vật tư tiêu hao tháng 12 (găng tay phẫu thuật, gạc vô khuẩn, chỉ khâu tự tiêu). Đề nghị khoa xác nhận số lượng đặt hàng trước ngày 25/11 để chúng tôi kịp giao trong tuần đầu tháng 12. Nếu khoa có thay đổi so với tháng trước, vui lòng ghi rõ trong thư trả lời.
>
> Trân trọng,
> Phòng Kinh doanh - Công ty cung ứng vật tư y tế (giả định)

### Email 3: Chuỗi "Góp ý về thủ tục xuất viện" (4 thư)

Gửi lần lượt **trong cùng một chuỗi** (dùng Reply / Forward để giữ tiêu đề), cách nhau vài phút. Có thể nhờ trợ giảng gửi thư 3 và 4 để chuỗi có nhiều người tham gia. Thêm học viên vào To hoặc Cc ở cả 4 thư.

**Thư 1 - Gia đình người bệnh gửi bệnh viện:**

> **COPY:**
>
> Kính gửi bệnh viện,
>
> Tôi là chồng của một sản phụ vừa sinh tại khoa Sản. Sáng thứ Sáu vừa rồi, bác sĩ cho vợ tôi xuất viện lúc 8 giờ, nhưng đến hơn 11 giờ gia đình mới làm xong thủ tục. Chúng tôi phải chờ hơn 3 tiếng, đi qua lại giữa quầy thanh toán và khoa nhiều lần, nhưng không ai giải thích vì sao phải chờ lâu như vậy. Vợ tôi vừa sinh còn mệt, em bé quấy khóc, cả nhà rất mệt mỏi.
>
> Chúng tôi rất hài lòng với bác sĩ và điều dưỡng trong thời gian nằm viện, nên càng tiếc vì trải nghiệm cuối cùng không tốt. Mong bệnh viện báo trước cho gia đình thời gian chờ dự kiến và gom các bước thủ tục về một chỗ.
>
> Trân trọng,
> Gia đình người bệnh

**Thư 2 - Phòng Chăm sóc khách hàng chuyển khoa Sản (Forward):**

> **COPY:**
>
> Chào khoa Sản,
>
> Phòng CSKH chuyển góp ý của gia đình sản phụ xuất viện sáng thứ Sáu tuần trước. Đây là góp ý thứ 5 về thời gian chờ xuất viện của khoa trong tháng này. Đề nghị khoa phản hồi gia đình trong 48 giờ và cho phòng biết nguyên nhân để tổng hợp báo cáo Ban Giám đốc.
>
> Cảm ơn khoa,
> Phòng Chăm sóc khách hàng

**Thư 3 - Điều dưỡng trưởng khoa Sản trả lời (Reply all):**

> **COPY:**
>
> Chào Phòng CSKH,
>
> Khoa đã kiểm tra: sáng hôm đó bác sĩ ký giấy ra viện sau giao ban, khoảng 9 giờ 15, và phải chờ thêm kết quả xét nghiệm công thức máu đến gần 10 giờ. Sau đó gia đình xuống quầy thanh toán thì phải chờ tiếp. Khoa chưa có ai được giao báo trước thời gian chờ cho gia đình.
>
> Khoa đề xuất họp với Phòng Tài chính và khoa Xét nghiệm để rút ngắn thủ tục. Nhờ chị Mai soạn thư trả lời gia đình.
>
> Điều dưỡng trưởng khoa Sản

**Thư 4 - Phòng Tài chính trả lời (Reply all):**

> **COPY:**
>
> Chào các anh chị,
>
> Phòng Tài chính xác nhận khung 8 đến 10 giờ sáng là giờ cao điểm xuất viện, nhưng quầy thanh toán khu nội trú chỉ có 1 nhân viên vì 1 người đang nghỉ thai sản. Phòng có thể điều thêm 1 người từ quầy ngoại trú trong khung giờ này nếu Ban Giám đốc đồng ý. Phòng sẵn sàng tham gia cuộc họp.
>
> Phòng Tài chính

---

## Lời mời họp cho Lab 5

Tạo cuộc họp Teams trong lịch, mời học viên. **Tiêu đề:** Họp cải tiến quy trình xuất viện. **Thời gian:** một ngày trong tuần sau buổi học, 30 phút.

> **COPY:**
>
> Thành phần: khoa Sản, khoa Xét nghiệm, Phòng Tài chính, Phòng Chăm sóc khách hàng.
>
> Nội dung: rà soát nguyên nhân thời gian chờ thủ tục xuất viện kéo dài (xem chuỗi email "Góp ý về thủ tục xuất viện"), thống nhất giải pháp và người phụ trách.

---

## Tin nhắn mẫu cho nhóm chat "Training Copilot"

Đăng lần lượt các tin nhắn sau (có thể nhờ trợ giảng đăng một vài tin). Thay `@[tên học viên]` bằng mention thật để Copilot nhận ra "người đang chờ phản hồi".

> **COPY:**
>
> 1. Nhắc cả nhà: các khoa gửi danh sách trực Tết về Phòng Hành chính - Nhân sự trước 15/12 nhé.
> 2. Từ thứ Hai 07/12, giao ban sáng chuyển từ 7:00 sang 7:15 để ca đêm bàn giao kịp.
> 3. Buổi tập huấn phòng chống cháy nổ lúc 14:00 ngày 15/12 tại hội trường tầng 5, nhớ mang thẻ nhân viên.
> 4. Khoa mình có bao nhiêu người tham gia tập huấn phòng cháy? Chị cần số trước thứ Sáu để đặt phòng. @[tên học viên] xác nhận giúp chị nha.

---

## Kịch bản họp mẫu cho Lab 6

Người hướng dẫn và 2 trợ giảng đóng vai **Trưởng khoa Sản**, **Trưởng khoa Gây mê hồi sức** và **chuyên viên QLCL**, đọc trong 10 đến 15 phút. Nhớ thông báo cho người tham dự trước khi bật Recording và Transcript. Nói rõ ràng, gọi tên vai trò khi phát biểu để transcript ghi nhận đúng.

**Phần 1 (khoảng 3 phút) - Trưởng khoa Sản mở đầu:**

> **COPY:**
>
> Hôm nay mình họp về bàn giao người bệnh sau mổ lấy thai giữa khoa Sản và khoa Gây mê hồi sức. Hiện hai khoa chưa có phiếu bàn giao thống nhất, mỗi ca bàn giao một kiểu. Tháng này đã có 2 lần thiếu thông tin về thuốc giảm đau đã dùng và lượng máu mất. Mục tiêu hôm nay là thống nhất phiếu bàn giao, nơi bàn giao và ai làm gì tiếp theo.

**Phần 2 (khoảng 4 phút) - Thống nhất phiếu bàn giao:** QLCL đề xuất phiếu chung gồm thuốc đã dùng, lượng máu mất, dấu hiệu sinh tồn, tình trạng co hồi tử cung, đường truyền. Hai khoa **đồng ý** dùng phiếu chung, khoa Sản soạn bản cập nhật.

**Phần 3 (khoảng 4 phút) - Tranh luận nơi bàn giao (không chốt):**

> **COPY:**
>
> Trưởng khoa Sản: Khoa Sản muốn bàn giao tại phòng hồi tỉnh, để nữ hộ sinh của khoa nhận người bệnh sớm và theo dõi chảy máu sau mổ ngay từ đầu.
>
> Trưởng khoa Gây mê hồi sức: Phòng hồi tỉnh đang chật, điều dưỡng hồi tỉnh không đủ người để vừa theo dõi vừa bàn giao. Khoa Gây mê muốn đưa người bệnh về phòng bệnh rồi bàn giao tại đó.
>
> QLCL: Hai phương án đều có lý do. Hôm nay mình chưa chốt được điểm này, sẽ cần thêm số liệu.

**Phần 4 (khoảng 3 phút) - Chốt 3 đầu việc:**

- Khoa Sản cập nhật phiếu bàn giao, **trước 30/12**
- Khoa Gây mê hồi sức tập huấn điều dưỡng hồi tỉnh về phiếu mới, **trước 15/1**
- QLCL rà soát việc áp dụng **sau 1 tháng**

---

## Đáp án tổng hợp

| Lab | Bài | Đáp án chính |
|-----|-----|--------------|
| 1 | 1 | Bảng việc: vật tư hạn 25/11, danh sách trực Tết hạn 15/12, trả lời gia đình người bệnh [CHƯA CÓ HẠN] |
| 1 | 2 | Đã có giải pháp: nghỉ việc ĐD (3.1), hài lòng Cơ sở C (3.2). Chưa có: quá tải D 96%/B 58%, vật tư +27%, chờ xuất viện |
| 2 | 1 | 5 ý chính, câu hỏi còn mở (mẫu danh sách, giờ ca trực Tết, "ở xa quê"), đoạn dài rút còn 4 gạch đầu dòng |
| 2 | 2 | Mục dấu hiệu nguy hiểm lên đầu, đủ 9 dấu hiệu, giữ nguyên con số |
| 2 | 3 | Tạm ứng 50% (4.1), phạt 0,05% (4.2), thiếu thu hồi (4.3), 2 báo giá (2.1); 7,8 tỷ: Tổng Giám đốc sau Pháp chế |
| 3 | 1 | Quá tải D, nghỉ việc 18%, làm thêm 16,4 giờ, vật tư +27%, hài lòng C giảm; ca sinh 4.180 vượt KH |
| 3 | 2 | Đỏ: Sản D, Nhi D. Vàng: Ngoại-GMHS D, Cấp cứu D, Sản C. Tổng 2/3/15 |
| 3 | 3 | Chờ xuất viện 129/377 (34%), 86% từ D và C; Cơ sở C nổi bật về thái độ giao tiếp (31) |
| 4 | 1-3 | 8 slide, 2 slide tình huống, notes 10 phút, 5 câu hỏi khó |
| 5 | 1 | Chờ bác sĩ ký giấy ra viện, chờ xét nghiệm, quầy thanh toán 1 người; chưa ai báo thời gian chờ |
| 5 | 2-3 | Thư xin lỗi không đổ lỗi, không hứa mốc, Coaching chỉ ra câu nghe như biện minh; 3 câu hỏi cho cuộc họp |
| 6 | 1-2 | Đồng ý phiếu chung; chưa chốt nơi bàn giao; 3 việc: Sản 30/12, GMHS 15/1, QLCL sau 1 tháng |
| 6 | 3 | 3 thông báo; chờ học viên xác nhận số người tập huấn |
| 7 | 1-2 | Memo có bảng tóm tắt; ưu tiên Sản D, Nhi D (nghỉ việc, làm thêm cao nhất); Kế hoạch 3.1 chưa có giải pháp giảm làm thêm, điều phối giữa cơ sở; 3 đề xuất có chỉ số |
| 8 | 3 | 13 ngày, chuyển tối đa 5; 900.000 + 600.000 đồng; không đổi ca với hộ lý; từ chối giá vàng; nhắc không chia sẻ CCCD |

---

## Xử lý sự cố thường gặp

| Hiện tượng | Cách xử lý |
|------------|------------|
| Không thấy nút Copilot | Kiểm tra licence, đăng xuất và đăng nhập lại, dùng tài khoản dự phòng |
| Copilot trong Excel bị mờ | Mở file từ OneDrive (không mở bản tải về máy), bấm vào trong bảng |
| Copilot Chat không thấy email mẫu | Kiểm tra nút **Work IQ** (góc trên bên trái) đang bật, không bị gạch ngang; email vừa gửi có thể cần vài phút để Copilot tìm thấy |
| Không có tab Recap | Cuộc họp chưa bật Transcript, hoặc học viên không phải người tham dự |
| Không thấy Researcher hoặc Create agent trong mục Agents | Chuyển sang trình diễn trên máy chiếu |
| Không thấy nút Work IQ | Giao diện mới có thể chưa được bật cho tenant, hoặc tài khoản chưa có licence Microsoft 365 Copilot; dùng tài khoản dự phòng |
| Kết quả khác đáp án mẫu | Bình thường: Copilot trả lời khác nhau mỗi lần. Kiểm tra ý chính và con số, không cần giống từng chữ |
