# Module 3 - Personalization in Copilot

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

- Biết **Customize Copilot** dùng để làm gì
- Dán một mẫu hướng dẫn có sẵn, chỉnh cho đúng công việc của mình và lưu lại
- So sánh câu trả lời trước và sau khi thiết lập

---

## Customize Copilot là gì?

**Customize Copilot** là nơi anh/chị cho Copilot biết **mình là ai** và **muốn nhận câu trả lời như thế nào**. Thiết lập một lần, Copilot áp dụng cho mọi cuộc trò chuyện sau đó, nên anh/chị không phải nhắc lại trong từng câu hỏi.

| Chưa thiết lập | Đã thiết lập |
|----------------|--------------|
| Mỗi lần hỏi phải nhắc: "tôi là điều dưỡng khoa Sản, trả lời ngắn gọn, bằng tiếng Việt..." | Chỉ cần hỏi, Copilot tự trả lời đúng phong cách |
| Câu trả lời dài, chung chung | Câu trả lời ngắn, đúng việc của anh/chị |

---

## Các bước thiết lập

1. Mở [Copilot Chat](https://m365.cloud.microsoft/) bằng tài khoản công ty
2. Bấm biểu tượng **ba chấm (...)** hoặc ảnh đại diện, chọn **Settings**
3. Chọn **Personalization**, tại mục **Customize Copilot** bật công tắc và bấm **Manage**
4. Dán một mẫu bên dưới vào ô hướng dẫn, sửa phần trong ngoặc vuông cho đúng với mình
5. Bấm **Save**

> [!NOTE]
> Nếu không thấy mục **Customize Copilot**, tính năng có thể chưa được quản trị viên bật. Hãy hỏi người hướng dẫn.

### Các gợi ý có sẵn hữu ích

Màn hình Customize Copilot có sẵn một số gợi ý, bấm vào là thêm vào ô hướng dẫn:

| Gợi ý | Tác dụng | Khi nào hữu ích |
|-------|----------|-----------------|
| **Use clear and simple language** | Câu chữ rõ ràng, dễ hiểu | Viết thông báo, tài liệu cho người bệnh |
| **Prioritize my manager** | Ưu tiên yêu cầu từ quản lý trực tiếp | Không bỏ sót việc trưởng khoa giao |
| **Highlight decisions in meeting notes** | Làm nổi bật quyết định trong tóm tắt họp | Theo dõi kết luận giao ban |
| **Focus on internal sources** | Ưu tiên tài liệu nội bộ | Câu hỏi về quy trình, chính sách |
| **Use bullet points for summaries** | Tóm tắt dạng gạch đầu dòng | Đọc nhanh trên điện thoại giữa ca |

---

## 4 mẫu có sẵn

Chọn mẫu gần nhất với công việc của anh/chị, bấm **Sao chép**, rồi sửa phần trong ngoặc vuông.

### Mẫu 1: Điều dưỡng

> **PROMPT:**
>
> Tôi là điều dưỡng khoa [tên khoa], thường làm việc theo ca, hay cần soạn thông báo, báo cáo ca và tài liệu hướng dẫn cho người bệnh. Khi trả lời tôi: viết tiếng Việt, ngắn gọn, ý chính trước; dùng gạch đầu dòng để dễ đọc trên điện thoại; khi viết cho người bệnh thì dùng câu ngắn, tránh thuật ngữ chuyên môn. Không đưa ra lời khuyên chẩn đoán hay điều trị. Chỗ chưa chắc chắn ghi [CẦN XÁC NHẬN].

### Mẫu 2: Hành chính khoa

> **PROMPT:**
>
> Tôi là nhân viên hành chính khoa [tên khoa], phụ trách lịch trực, văn bản, tổng hợp báo cáo và liên hệ với các phòng chức năng. Khi trả lời tôi: viết tiếng Việt, văn phong hành chính rõ ràng; dùng bảng khi có lịch, danh sách hoặc số liệu; nêu rõ người phụ trách và thời hạn cho mỗi việc. Không tự điền số liệu không có trong nguồn, chỗ chưa chắc chắn ghi [CẦN XÁC NHẬN].

### Mẫu 3: Chăm sóc khách hàng

> **PROMPT:**
>
> Tôi là nhân viên chăm sóc khách hàng, thường trả lời câu hỏi, góp ý và phàn nàn của người bệnh và gia đình qua email, điện thoại và tin nhắn. Khi trả lời tôi: viết tiếng Việt, giọng ấm áp, lịch sự, thấu cảm; luôn cảm ơn và ghi nhận cảm xúc của người bệnh trước khi giải thích; không hứa hẹn điều bệnh viện chưa xác nhận. Thư gửi người bệnh dưới 150 chữ.

### Mẫu 4: Trưởng khoa

> **PROMPT:**
>
> Tôi là trưởng khoa [tên khoa], quản lý [số người] nhân viên, báo cáo cho Ban Giám đốc và phối hợp với Phòng Điều dưỡng, Phòng Quản lý chất lượng. Khi trả lời tôi: ý chính trước, chi tiết sau; dùng bảng khi so sánh; với mỗi vấn đề nêu việc cần làm, người phụ trách và thời hạn; góp ý thẳng thắn. Không đưa ra quyết định chuyên môn thay tôi. Chỗ chưa chắc chắn ghi [CẦN XÁC NHẬN].

> [!NOTE]
> **Không đưa thông tin người bệnh hay số liệu nội bộ chi tiết** vào hướng dẫn. Chỉ mô tả vai trò và cách anh/chị muốn nhận câu trả lời.

---

## Thực hành

1. **Trước khi thiết lập**, mở cuộc trò chuyện mới, hỏi câu dưới đây và giữ lại kết quả:

> **PROMPT:**
>
> Soạn thông báo gửi nhân viên khoa về lịch tập huấn phòng cháy lúc 14:00 ngày 15/12 tại hội trường tầng 5.

2. Thiết lập Customize Copilot theo các bước ở trên với mẫu phù hợp, bấm **Save**
3. Mở **cuộc trò chuyện mới** (bấm **New chat**), hỏi lại đúng câu ở bước 1 và so sánh hai kết quả

> [!ANSWER]
> Câu trả lời sau khi thiết lập thường **ngắn gọn hơn**, **đúng giọng văn** đã chọn (ví dụ dạng gạch đầu dòng với mẫu Điều dưỡng, có bảng và người phụ trách với mẫu Hành chính khoa), và đánh dấu **[CẦN XÁC NHẬN]** ở chỗ thiếu thông tin, ví dụ thành phần tham dự.

> [!TIP]
> Nếu kết quả chưa như ý, quay lại **Customize Copilot** để chỉnh. Hướng dẫn tốt thường được hoàn thiện sau 2-3 lần thử.

---

Tiếp theo: bắt đầu thực hành với **[Lab 1 - Copilot Chat](#lab-1)**.
