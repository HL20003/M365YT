# Lab 6 - Copilot trong Teams

**Ứng dụng:** Microsoft Teams

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp dùng cho đào tạo.** Tên nhân vật, người bệnh và đối tác là giả định. Copilot chỉ hỗ trợ công việc hành chính, truyền thông, đào tạo; **không dùng cho chẩn đoán hay quyết định điều trị**. **Không nhập thông tin người bệnh thật vào Copilot.**

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Bắt kịp cuộc họp khi vào muộn và phát hiện điểm còn chưa thống nhất để chốt
- Biến cuộc họp thành biên bản có quyết định, người phụ trách và thời hạn
- Nắm nhanh những gì đang diễn ra trong nhóm chat của khoa

### Tính năng chính

| Tính năng | Mô tả |
|-----------|--------|
| **Copilot trong cuộc họp** | Hỏi đáp về nội dung cuộc họp đang diễn ra |
| **Recap** | Ghi chú và việc cần làm sau cuộc họp |
| **Copilot trong chat** | Tóm tắt nhóm chat và kênh |

---

## Tình huống

> Anh/chị dự **cuộc họp 15 phút** do người hướng dẫn tổ chức (đã bật transcript) về **quy trình bàn giao người bệnh sau mổ lấy thai** giữa khoa Sản và khoa Gây mê hồi sức, có chuyên viên Quản lý chất lượng (QLCL) tham dự. Hai khoa chưa có phiếu bàn giao thống nhất và còn khác quan điểm về nơi bàn giao. Anh/chị vào họp muộn vài phút, cần bắt kịp, góp phần chốt vấn đề và sau đó gửi biên bản cho cả nhóm.

> [!NOTE]
> Copilot trong cuộc họp cần **bật Transcript**. Người chủ trì phải **thông báo cho người tham dự** trước khi bật Recording và Transcript.

---

### Bài tập 1: Vào họp muộn, bắt kịp và chốt điểm chưa thống nhất

1. Tham gia cuộc họp mẫu (đã bật transcript)
2. Bấm nút **Copilot** trên thanh công cụ cuộc họp, dán prompt:

> **PROMPT:**
>
> Tôi vừa vào cuộc họp. Trong 3 câu, cho tôi biết: cuộc họp đang bàn vấn đề gì, đã thống nhất được gì, và hiện mọi người đang tranh luận điểm nào.

3. Khi cuộc họp sắp kết thúc, hỏi tiếp:

> **PROMPT:**
>
> Trong cuộc họp này, vấn đề nào chưa thống nhất? Mỗi khoa đang giữ quan điểm gì và lý do là gì? Gợi ý cho tôi một câu hỏi để giúp hai bên chốt lại trước khi kết thúc họp.

> [!ANSWER]
> Cuộc họp bàn về việc **chưa có phiếu bàn giao thống nhất** sau mổ lấy thai. Hai khoa đã thống nhất làm phiếu bàn giao chung. Hiện đang tranh luận **nơi bàn giao**: phòng hồi tỉnh hay phòng bệnh.
>
> **Khoa Sản** muốn bàn giao tại **phòng hồi tỉnh**: để nữ hộ sinh theo dõi chảy máu sớm.
>
> **Khoa Gây mê hồi sức** muốn bàn giao tại **phòng bệnh**: vì phòng hồi tỉnh chật, điều dưỡng hồi tỉnh không đủ người đi kèm.
>
> Câu hỏi gợi ý: *"Hai khoa có đồng ý thử bàn giao tại phòng hồi tỉnh trong 1 tháng, QLCL theo dõi rồi quyết định không?"*

### Bài tập 2: Biên bản sau cuộc họp

1. Sau cuộc họp, mở Teams, vào **Calendar**, bấm vào cuộc họp mẫu, chọn tab **Recap**
2. Xem phần **Notes** và **Follow-up tasks** do Copilot tạo
3. Bấm **Copilot** trong tab Recap, dán prompt:

> **PROMPT:**
>
> Lập biên bản cuộc họp gồm: các quyết định đã chốt, bảng việc cần làm (Việc | Người phụ trách | Kết quả cần đạt | Thời hạn), và các vấn đề còn treo cần ai quyết định. Đánh dấu việc chưa có người phụ trách hoặc thời hạn rõ ràng.

4. Hỏi tiếp để gửi cho cả nhóm:

> **PROMPT:**
>
> Soạn tin nhắn Teams gửi nhóm họp: cảm ơn, tóm tắt quyết định chính, nhắc từng khoa việc của mình và thời hạn, nêu rõ điểm còn treo sẽ được quyết định thế nào. Dưới 120 chữ.

> [!ANSWER]
> Bảng biên bản có **3 đầu việc**:
>
> | Việc | Người phụ trách | Thời hạn |
> |------|-----------------|----------|
> | Cập nhật phiếu bàn giao | Khoa Sản | Trước 30/12 |
> | Tập huấn điều dưỡng hồi tỉnh | Khoa Gây mê hồi sức | Trước 15/1 |
> | Rà soát sau khi áp dụng | QLCL | Sau 1 tháng áp dụng |
>
> **Vấn đề còn treo:** nơi bàn giao, cần Ban Giám đốc hoặc Phòng Điều dưỡng quyết định nếu hai khoa không thống nhất.

> [!TIP]
> Nếu anh/chị chỉ là người tham dự, hỏi: *"Trong cuộc họp này, việc nào được giao cho khoa tôi và hạn khi nào?"*

### Bài tập 3: Tóm tắt nhóm chat

1. Mở nhóm chat **"Training Copilot"** (người hướng dẫn tạo sẵn, có tin nhắn mẫu)
2. Bấm biểu tượng **Copilot** góc phải trên của cuộc chat, dán prompt:

> **PROMPT:**
>
> Tóm tắt các trao đổi trong 7 ngày qua: thông báo nào áp dụng cho tôi (kèm ngày áp dụng), câu hỏi nào chưa được trả lời, và có ai đang chờ tôi phản hồi không?

> [!ANSWER]
> **Thông báo:**
>
> - gửi danh sách trực Tết trước 15/12;
> - giao ban chuyển sang 7:15 từ 07/12;
> - tập huấn phòng cháy 14:00 ngày 15/12.
>
> **Đang chờ anh/chị phản hồi:** xác nhận số người tham gia tập huấn trước thứ Sáu.

---

## Lưu ý tuân thủ

> [!NOTE]
> Thông báo cho mọi người khi bật ghi âm/transcript. Không thảo luận ca bệnh có thông tin định danh (họ tên, mã hồ sơ, số giường) trong cuộc họp được ghi lại. Biên bản do Copilot tạo phải được người chủ trì rà soát trước khi gửi.

---

## Prompt đề xuất - Teams

### Giao ban khoa

> **PROMPT:**
>
> Từ cuộc giao ban sáng nay, liệt kê các việc được giao cho điều dưỡng kèm người phụ trách và thời hạn, đánh dấu việc liên quan đến an toàn người bệnh lên đầu.

### Theo dõi qua nhiều cuộc họp

> **PROMPT:**
>
> So sánh cuộc họp này với cuộc họp trước cùng chủ đề: việc nào đã hoàn thành, việc nào bị lùi thời hạn, vấn đề nào lặp lại.

### Kênh của khoa

> **PROMPT:**
>
> Trong kênh của khoa tuần này, có thay đổi quy trình hay lịch trực nào tôi cần truyền đạt lại cho ca đêm không? Viết thành 3 gạch đầu dòng để tôi dán vào sổ bàn giao.

---

## Tổng kết

| Anh/chị đã học được | Tính năng |
|---------------------|-----------|
| Bắt kịp cuộc họp và chốt điểm chưa thống nhất | Copilot trong cuộc họp |
| Biên bản có người phụ trách và thời hạn | Recap |
| Nắm nhanh nhóm chat của khoa | Copilot trong chat |
