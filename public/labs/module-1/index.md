# Module 1 - Giới thiệu Copilot và chuẩn bị

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Bối cảnh workshop

Workshop dành cho **người dùng phổ thông**: điều dưỡng, nhân viên hành chính, chăm sóc khách hàng và nhân viên khoa phòng. Mỗi Lab gồm các bài tập có **các bước bấm cụ thể**, **prompt để sao chép** và **đáp án mẫu** để anh/chị tự kiểm tra.

Các bài thực hành dùng chung bộ tài liệu của **một hệ thống bệnh viện giả định gồm 4 cơ sở (A, B, C, D)**. Số liệu trong file demo là số liệu minh họa, không phải số liệu thật của bất kỳ bệnh viện nào.

### Mỗi lab dùng được cho ai?

| Lab | Ứng dụng | Điều dưỡng, nữ hộ sinh | Hành chính khoa, CSKH | Trưởng khoa, điều dưỡng trưởng |
|-----|----------|------------------------|------------------------|--------------------------------|
| 1 | Copilot Chat | Nắm việc cần làm sau ca nghỉ | Gom yêu cầu báo cáo, góp ý người bệnh | Góp ý kế hoạch bằng số liệu |
| 2 | Word | Viết lại hướng dẫn cho sản phụ dễ hiểu | Rút gọn thông báo, rà soát hợp đồng theo chính sách | Kiểm tra điểm sai chính sách trước khi trình ký |
| 3 | Excel | Đọc nhanh số liệu khoa | Chuẩn bị số liệu, biểu đồ giao ban | Biết khoa nào cần hỗ trợ nhân lực |
| 4 | PowerPoint | Bài trình bày đào tạo, tình huống giao tiếp | Slide giao ban tháng | Truyền thông kế hoạch cho khoa |
| 5 | Outlook | Xử lý hộp thư sau ca | Trả lời góp ý của người bệnh | Chuẩn bị cuộc họp xử lý vấn đề |
| 6 | Teams | Bắt kịp giao ban, biết việc của mình | Biên bản họp có người phụ trách | Chốt điểm chưa thống nhất giữa các khoa |
| 7 | Researcher | Tìm hiểu chủ đề chăm sóc | Tìm thông tin cho đề xuất cải tiến | Đề xuất có dẫn chứng cho Ban Giám đốc |
| 8 | Agent Builder | Tra cứu chính sách nhân sự | Trợ lý câu hỏi thường gặp | Trợ lý định hướng điều dưỡng mới |

> [!TIP]
> Trong các prompt, phần đặt trong ngoặc vuông như **[tên khoa]**, **[tên file]** là chỗ anh/chị thay bằng thông tin của mình.

---

## Bắt đầu trong 3 bước

1. Mở trình duyệt, vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) và đăng nhập bằng **tài khoản công ty**
2. Tìm nút **Copilot** ở thanh bên trái và bấm vào
3. Kiểm tra nút **Work IQ** ở **góc trên bên trái** màn hình Chat đang **bật** (chữ Work IQ không bị gạch ngang)

### Work IQ là gì?

**Work IQ** là lớp "hiểu công việc" của Copilot: Copilot biết anh/chị làm việc với ai, đang có cuộc họp, email, tài liệu nào. Trước đây Copilot Chat có nút chuyển **Work / Web**; nay nút này được thay bằng **một nút Work IQ bật/tắt**, và khi bật, Copilot **tự quyết định** lấy thông tin từ dữ liệu công việc, từ web, hay cả hai.

<div class="compare-2">
  <div class="compare-card">
    <h4>✓ Work IQ bật (mặc định)</h4>
    <ul>
      <li>Email, lịch, cuộc họp, chat Teams của anh/chị</li>
      <li>File trên OneDrive, SharePoint anh/chị có quyền xem</li>
      <li>File anh/chị đính kèm vào prompt</li>
      <li>Thông tin công khai trên web khi cần</li>
    </ul>
    <div class="use"><b>Dùng khi:</b> hỏi về công việc của mình, tổng hợp email và cuộc họp, đối chiếu tài liệu nội bộ.</div>
  </div>
  <div class="compare-card off">
    <h4><s>Work IQ</s> tắt</h4>
    <ul>
      <li>Chỉ file anh/chị đính kèm vào prompt</li>
      <li>Thông tin công khai trên web</li>
      <li>Hồ sơ và thiết lập cá nhân hóa của anh/chị</li>
      <li><b>Không</b> đọc email, lịch, file, chat của anh/chị</li>
    </ul>
    <div class="use"><b>Dùng khi:</b> chỉ cần thông tin công khai (kiến thức chung, tin tức ngành), không muốn kết quả lẫn dữ liệu nội bộ.</div>
  </div>
</div>

> [!TIP]
> Không cần tắt Work IQ để giới hạn nguồn: có thể nói thẳng trong prompt, ví dụ *"Chỉ dùng email và file của tôi, không tìm trên web"* hoặc *"Chỉ dùng thông tin công khai trên web"*. Khi bấm tắt hoặc bật Work IQ, Copilot sẽ mở cuộc trò chuyện mới.

---

## Microsoft 365 Copilot là gì?

Microsoft 365 Copilot là trợ lý AI nằm ngay trong các ứng dụng anh/chị dùng hằng ngày: Outlook, Word, Excel, PowerPoint, Teams. Anh/chị giao việc bằng tiếng Việt, Copilot soạn nháp, tóm tắt, phân tích, và anh/chị là người kiểm tra, quyết định.

### Copilot nhìn thấy gì?

| Copilot có thể | Copilot không thể |
|----------------|-------------------|
| Đọc email, lịch, chat của chính anh/chị | Đọc email của đồng nghiệp |
| Đọc file trên OneDrive/SharePoint anh/chị có quyền | Mở file anh/chị không được chia sẻ |
| Dùng transcript cuộc họp anh/chị tham dự (đã bật transcript) | Truy cập cuộc họp anh/chị không tham dự |
| Tìm thông tin công khai trên web khi cần | Đọc phần mềm quản lý bệnh viện (HIS), bệnh án điện tử, phần mềm xét nghiệm |

> [!NOTE]
> Copilot không cấp thêm quyền cho ai. Nó chỉ giúp anh/chị **tìm nhanh hơn** những gì anh/chị vốn đã có quyền xem.

### Câu hỏi thường gặp

| Câu hỏi | Trả lời |
|---------|---------|
| Dữ liệu của bệnh viện có được dùng để huấn luyện AI không? | **Không.** Prompt, câu trả lời và dữ liệu trong Microsoft 365 của công ty không được dùng để huấn luyện mô hình AI. |
| Đồng nghiệp có xem được câu hỏi của tôi không? | **Không.** Lịch sử trò chuyện với Copilot chỉ hiển thị với anh/chị. |
| Copilot có luôn đúng không? | **Không.** Copilot có thể trả lời sai một cách rất tự tin. Hãy bấm vào trích dẫn để kiểm tra lại. |
| Copilot có biết số giường trống hôm nay không? | **Không.** Copilot không đọc hệ thống quản lý bệnh viện. Số liệu thời gian thực phải xem trên phần mềm nghiệp vụ. |

---

## Những điều KHÔNG làm

| Không làm | Vì sao |
|-----------|--------|
| Nhập **họ tên, mã hồ sơ, số điện thoại, kết quả xét nghiệm** của người bệnh vào prompt | Đây là thông tin sức khỏe cá nhân, phải được bảo mật tuyệt đối |
| Dùng Copilot để **chẩn đoán, chỉ định thuốc hay quyết định điều trị** | Copilot chỉ hỗ trợ việc hành chính, truyền thông, đào tạo |
| Gửi ngay câu trả lời của Copilot mà **không đọc lại** | Copilot có thể sai hoặc thiếu ý |
| Dùng tài khoản AI cá nhân (ChatGPT, Gemini...) cho tài liệu của bệnh viện | Dữ liệu ra khỏi môi trường được bảo vệ của công ty |
| Phát tài liệu cho người bệnh khi **chưa được bác sĩ, điều dưỡng trưởng duyệt** | Nội dung chuyên môn phải do người có chuyên môn chịu trách nhiệm |

> [!TIP]
> Khi cần nói về một trường hợp cụ thể, hãy mô tả chung, ví dụ *"một sản phụ sinh con lần đầu"*, thay vì ghi tên hay mã hồ sơ.

---

## Chuẩn bị

1. Đăng nhập Microsoft 365 bằng **tài khoản công ty** đã được cấp licence **Microsoft 365 Copilot**
2. Kiểm tra licence theo bảng bên dưới
3. Tải các file demo và lưu vào **OneDrive** (xem [cách tải file về máy](#module-1/cach-tai-file-ve-may-va-dua-len-onedrive))

### Kiểm tra licence

| Ứng dụng | Cách kiểm tra |
|----------|---------------|
| **Outlook** | Mở Outlook (bản web hoặc New Outlook), thấy biểu tượng **Copilot** trên thanh công cụ |
| **Word, Excel, PowerPoint** | Mở một file bất kỳ, thấy nút **Copilot** trên thanh **Home** |
| **Teams** | Trong một cuộc họp hoặc khung chat, thấy biểu tượng **Copilot** |
| **Copilot Chat** | Vào [m365.cloud.microsoft](https://m365.cloud.microsoft/), thấy nút **Work IQ** ở góc trên bên trái màn hình Chat. Nếu không thấy nút này, tài khoản có thể chưa có licence Microsoft 365 Copilot |

> [!TIP]
> Nếu không thấy biểu tượng Copilot, hãy báo ngay người hướng dẫn để kiểm tra licence hoặc nhận tài khoản dự phòng.

### Tải file demo

[download-files]

### Cách tải file về máy và đưa lên OneDrive

1. Bấm vào từng file demo ở trên để tải về máy, hoặc bấm **Tải tất cả (.zip)** rồi giải nén
2. Mở [OneDrive](https://m365.cloud.microsoft/onedrive) bằng tài khoản công ty, tạo thư mục **Training Copilot**
3. Chọn **Add new** (hoặc **Upload**) > **Files**, chọn các file vừa tải về

> [!TIP]
> Copilot chỉ đọc được file lưu trên OneDrive hoặc SharePoint. Nếu người hướng dẫn đã chia sẻ sẵn thư mục **Training Copilot**, anh/chị dùng luôn thư mục đó.

---

Tiếp theo: **[Module 2 - Viết prompt hiệu quả](#module-2)**.
