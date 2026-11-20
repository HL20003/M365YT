# Lab 2 - Copilot trong Word

**Ứng dụng:** Microsoft Word

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Đọc một văn bản dài như người nhận: nắm ý chính và phát hiện chỗ còn thiếu, chưa rõ
- Viết lại văn bản cho đúng người đọc: đồng nghiệp đọc nhanh trên điện thoại, sản phụ không có kiến thức y khoa
- Đối chiếu một dự thảo hợp đồng với chính sách nội bộ, rồi soạn tờ trình đề xuất sửa

### Tính năng chính

| Tính năng | Mô tả |
|-----------|--------|
| **Summarize / Hỏi đáp trên tài liệu** | Tóm tắt và hỏi đáp về tài liệu đang mở |
| **Rewrite** | Viết lại đoạn văn hoặc cả tài liệu theo giọng văn, độ dài, người đọc |
| **Đối chiếu tài liệu** | Tham chiếu file khác bằng "/" để so sánh |
| **Draft with Copilot** | Soạn văn bản mới từ yêu cầu và tài liệu nguồn |

---

## Tình huống

> **Chị Mai** - *điều dưỡng hành chính khoa Sản*
>
> Phòng Hành chính - Nhân sự gửi bản nháp thông báo lịch trực Tết, dài và khó đọc, nhờ các khoa góp ý trước khi ban hành. Bác sĩ trưởng khoa muốn tờ hướng dẫn chăm sóc mẹ sau sinh được viết lại cho sản phụ dễ hiểu. Phòng Vật tư cũng gửi dự thảo hợp đồng cung ứng vật tư cho khoa Sản và Phòng mổ, nhờ khoa kiểm tra trước khi trình ký.

**Tài liệu demo:**

- [Thông báo lịch trực Tết 2027.docx](#file-tet)
- [Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx](#file-postpartum)
- [Dự thảo Hợp đồng cung ứng vật tư.docx](#file-contract) và [Chính sách Mua sắm nội bộ.pdf](#file-procurement)

Tất cả đã lưu trên OneDrive.

---

### Bài tập 1: Đọc và rút gọn thông báo lịch trực Tết

1. Mở thư mục **Training Copilot** trên OneDrive, bấm mở [Thông báo lịch trực Tết 2027.docx](#file-tet)
2. Bấm nút **Copilot** trên thanh **Home** (góc phải)
3. Dán prompt vào khung Copilot:

> **PROMPT:**
>
> Tôi là điều dưỡng hành chính khoa Sản, cần nắm thông báo này để phân ca cho khoa. Tóm tắt trong 5 gạch đầu dòng: thời gian nghỉ, nguyên tắc phân ca, hạn gửi danh sách, phụ cấp trực, đầu mối liên hệ. Sau đó liệt kê những thông tin còn thiếu hoặc chưa rõ khiến tôi chưa phân ca được, dưới dạng câu hỏi gửi lại Phòng Hành chính - Nhân sự.

> [!ANSWER]
> 5 ý chính:
>
> - Khối hành chính nghỉ từ **04/02 đến hết 10/02/2027**
> - Mỗi người trực **không quá 3 ca**, ưu tiên người đã trực Tết 2026
> - Gửi danh sách **trước 15/12/2026**
> - Phụ cấp **gấp 3** các ngày mùng 1-3, **gấp 2** các ngày còn lại
> - Đầu mối là chị Nguyễn Hoài An, máy lẻ 1010
>
> Các câu hỏi còn mở, ví dụ:
>
> - Có mẫu danh sách trực không?
> - "Nhân viên ở xa quê" được xác định thế nào?
> - Ca trực ngày Tết là ca 12 giờ hay 24 giờ?
> - Khoa thiếu người thì báo Phòng Điều dưỡng trước ngày nào?

4. Rút gọn đoạn văn lủng củng: bôi đen đoạn dài bắt đầu bằng *"Như anh chị em đã biết..."*, bấm biểu tượng **Copilot** nhỏ bên trái đoạn văn, chọn **Rewrite**, xem các phiên bản và bấm **Replace** nếu ưng ý. Hoặc gõ vào khung Copilot:

> **PROMPT:**
>
> Viết lại đoạn đã chọn thành 4 gạch đầu dòng ngắn, mỗi dòng một yêu cầu cụ thể, giọng thân thiện. Giữ nguyên hạn 15/12/2026 và quy định không quá 3 ca.

> [!ANSWER]
> Đoạn văn hơn 200 chữ được thay bằng 4 gạch đầu dòng rõ ràng:
>
> - các khoa trọng yếu phải đủ người trực;
> - gửi danh sách trước 15/12/2026;
> - mỗi người không quá 3 ca;
> - khoa thiếu người báo Phòng Điều dưỡng.

### Bài tập 2: Viết lại hướng dẫn cho sản phụ dễ hiểu

1. Mở [Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx](#file-postpartum)
2. Bấm **Copilot**, dán prompt:

> **PROMPT:**
>
> Viết lại tài liệu này cho sản phụ và người nhà đọc, nhiều người chưa có kiến thức y khoa. Yêu cầu: xưng "mẹ" và "bé", câu ngắn dưới 20 chữ, thay thuật ngữ chuyên môn bằng lời thường (nếu cần giữ thuật ngữ thì giải thích trong ngoặc), chia thành các mục có tiêu đề dạng câu hỏi như "Ra máu sau sinh bao lâu là bình thường?". Giữ nguyên nội dung và các con số chuyên môn, không thêm lời khuyên mới. Giữ đầy đủ mục "Dấu hiệu cần quay lại bệnh viện ngay" và đặt mục này lên đầu tài liệu.

3. Hỏi tiếp:

> **PROMPT:**
>
> Thêm cuối tài liệu mục "Câu hỏi mẹ hay hỏi" gồm 5 câu hỏi và trả lời, chỉ dựa trên nội dung tài liệu. Chỗ nào tài liệu không có thông tin, ghi [CẦN BÁC SĨ XÁC NHẬN] thay vì tự trả lời.

> [!ANSWER]
> Tài liệu mới có **tiêu đề dạng câu hỏi**, câu ngắn. Các từ *sản dịch*, *co hồi tử cung*, *tầng sinh môn* được giải thích bằng lời thường. Mục **Dấu hiệu cần quay lại bệnh viện ngay** nằm đầu tài liệu và đủ **9 dấu hiệu**. Các con số giữ nguyên: sốt từ 38 độ, thấm ướt hơn 1 băng vệ sinh trong 1 giờ, tái khám sau 6 tuần. Mục "Câu hỏi mẹ hay hỏi" đánh dấu [CẦN BÁC SĨ XÁC NHẬN] ở câu tài liệu không có thông tin, ví dụ khi nào được tắm gội.

> [!TIP]
> Copilot chỉ sửa cách diễn đạt. **Bác sĩ phụ trách phải duyệt lại nội dung chuyên môn** trước khi phát cho người bệnh. Đối chiếu từng con số với bản gốc trước khi gửi duyệt.

### Bài tập 3: Rà soát dự thảo hợp đồng theo chính sách nội bộ

1. Mở [Dự thảo Hợp đồng cung ứng vật tư.docx](#file-contract), bấm **Copilot**
2. Gõ **/** để tham chiếu [Chính sách Mua sắm nội bộ.pdf](#file-procurement), rồi dán prompt:

> **PROMPT:**
>
> Đối chiếu dự thảo hợp đồng này, kể cả phần Ghi chú của người soạn thảo, với Chính sách Mua sắm nội bộ. Lập bảng: Nội dung | Hợp đồng đang ghi | Chính sách yêu cầu (ghi mục) | Đề xuất sửa. Sau bảng, cho biết với giá trị hợp đồng này thì cấp nào có thẩm quyền phê duyệt và có cần Pháp chế rà soát không.

3. Soạn tờ trình. Mở một file Word mới, trong khung **Draft with Copilot** gõ **/** để chọn cả hai file, rồi dán prompt:

> **PROMPT:**
>
> Dựa trên dự thảo hợp đồng cung ứng vật tư và Chính sách Mua sắm nội bộ, soạn tờ trình một trang gửi Phó Giám đốc phụ trách hậu cần đề xuất sửa hợp đồng trước khi trình ký. Gồm: bối cảnh và nhu cầu nhận hàng từ 01/12, các điểm chưa đúng chính sách (dạng bảng), đề xuất sửa, và việc cần làm tiếp kèm người phụ trách. Văn phong hành chính, ngắn gọn. Chỗ nào cần thông tin tôi bổ sung thì ghi [CẦN XÁC NHẬN].

> [!ANSWER]
> **Bảng đối chiếu chỉ ra 4 điểm chưa đúng chính sách:**
>
> | Nội dung | Hợp đồng đang ghi | Chính sách yêu cầu |
> |----------|-------------------|--------------------|
> | Tạm ứng | **50%**, không có bảo lãnh | Tối đa **30%**, kèm bảo lãnh ngân hàng (Mục 4.1) |
> | Phạt chậm giao | **0,05%/ngày**, tối đa 5% | Tối thiểu **0,1%/ngày**, tối đa 8% (Mục 4.2) |
> | Thu hồi lô lỗi | **Không có** điều khoản | Bắt buộc thu hồi và thay thế trong 48 giờ (Mục 4.3) |
> | Số báo giá | **2** báo giá | Cần **3** báo giá (Mục 2.1) |
>
> **Thẩm quyền:** hợp đồng 7,8 tỷ đồng, thuộc mức **Tổng Giám đốc phê duyệt sau khi Pháp chế rà soát** (Mục 3).
>
> Tờ trình có đủ cấu trúc, bảng khớp với kết quả đối chiếu.

> [!TIP]
> Yêu cầu **ghi rõ mục tham chiếu** để anh/chị kiểm tra từng kết luận trong chính sách gốc, thay vì tin hoàn toàn vào Copilot.

---

## Lưu ý tuân thủ

> [!NOTE]
> Tài liệu phát cho người bệnh phải qua duyệt chuyên môn. Bảng đối chiếu và tờ trình do Copilot tạo chỉ là bản nháp: mọi con số, điều khoản và cấp phê duyệt phải được đối chiếu với văn bản gốc trước khi trình. Không đưa thông tin người bệnh thật vào tài liệu mẫu.

---

## Prompt đề xuất - Word

### Soạn thông báo nội bộ

> **PROMPT:**
>
> Soạn thông báo gửi điều dưỡng khoa Sản về buổi tập huấn phòng chống cháy nổ lúc 14:00 ngày 15/12 tại hội trường tầng 5: thành phần tham dự, nội dung chính (sử dụng bình chữa cháy, thoát hiểm, di chuyển người bệnh), lưu ý mang thẻ nhân viên và bố trí người trực thay. Dưới 150 chữ.

### Tin nhắn nhắc việc từ văn bản dài

> **PROMPT:**
>
> Từ toàn bộ thông báo này, soạn một tin nhắn Teams gửi nhóm điều dưỡng khoa Sản, không quá 80 chữ: nhắc thời gian nghỉ Tết, hạn đăng ký nguyện vọng trực với tôi là 10/12, và nguyên tắc ưu tiên. Kết thúc bằng một lời chúc ngắn.

### Chuẩn hóa quy trình

> **PROMPT:**
>
> Từ ghi chép rời rạc trong tài liệu này, soạn quy trình chuẩn (SOP) gồm: mục đích, phạm vi, người thực hiện, các bước dạng bảng (Bước | Người làm | Việc cần làm | Biểu mẫu), và các điểm kiểm tra. Chỗ chưa rõ ghi [CẦN XÁC NHẬN].

### Báo cáo sự cố

> **PROMPT:**
>
> Viết lại bản tường trình này theo văn phong khách quan, theo trình tự thời gian, tách riêng phần "sự việc" và "đề xuất cải tiến", bỏ các từ ngữ đổ lỗi cho cá nhân. Không thêm chi tiết không có trong bản gốc.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Tóm tắt và tìm chỗ còn thiếu trong văn bản | Summarize / Hỏi đáp |
| Viết lại cho đồng nghiệp đọc nhanh, cho sản phụ dễ hiểu | Rewrite |
| Đối chiếu hợp đồng với chính sách, soạn tờ trình | Đối chiếu tài liệu, Draft with Copilot |
