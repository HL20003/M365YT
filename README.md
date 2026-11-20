# Copilot Overview Workshop - bản Phương Châu (y tế)

Site lab Microsoft 365 Copilot cho khách hàng Tập đoàn Y tế Phương Châu, dựng theo mẫu `m365copilot-overview-lab-general`
(cùng cấu trúc Module 1-3, Lab 1-8, Tổng kết, cùng giao diện và cách host). Nội dung viết cho người dùng phổ thông
(điều dưỡng, hành chính, chăm sóc khách hàng, nhân viên khoa phòng), mỗi bài có các bước bấm, prompt và đáp án mẫu thu gọn.

Tên khách hàng chỉ xuất hiện ở trang chủ. Toàn bộ file demo, số liệu và tình huống dùng một hệ thống bệnh viện giả định
gồm 4 cơ sở A, B, C, D, để số liệu đào tạo không bị hiểu là số liệu thật của khách hàng.

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `public/` | Site tĩnh: `index.html`, `js/app.js` (danh sách module và file demo), `css/style.css`, `labs/*/index.md`, `files/` |
| `public/labs/trainer/` | Trang "Chuẩn bị cho người hướng dẫn" (chỉ hiện ở chế độ Trainer) |
| `demo-files/` | Bản gốc các file demo và script tạo lại (`_gen/`), kèm đáp án cho người hướng dẫn |
| `wrangler.jsonc` | Cấu hình Cloudflare Workers (static assets từ `public/`) |

## Chạy thử và deploy lên Cloudflare Workers

```bash
npx wrangler dev        # chạy thử tại http://localhost:8787
npx wrangler deploy     # deploy, Worker tên m365copilot-phuongchau-lab
```

Lần đầu deploy, wrangler sẽ yêu cầu đăng nhập Cloudflare (`npx wrangler login`).
Không mở trực tiếp `index.html` bằng file:// vì trang tải nội dung lab bằng fetch; hãy chạy qua wrangler dev hoặc một web server bất kỳ.

## Chế độ Trainer

Mở site với `?trainer=1` (ví dụ `http://localhost:8787/?trainer=1`) để hiện nút **Trainer** trên thanh menu, dòng
"Chuẩn bị cho người hướng dẫn" trong lịch trình và trang `#trainer`. Trình duyệt ghi nhớ lựa chọn; mở `?trainer=0` để tắt.
Đây chỉ là ẩn khỏi giao diện, không phải bảo mật: ai biết địa chỉ vẫn mở được.

## Cú pháp Markdown riêng

| Viết trong Markdown | Hiển thị |
|---|---|
| `> **PROMPT:**` + nội dung | Thẻ prompt có nút Sao chép |
| `> **COPY:**` + nội dung | Thẻ "Nội dung mẫu" có nút Sao chép (email, tin nhắn mẫu) |
| `> [!ANSWER]` + nội dung | Khối "Đáp án mẫu" thu gọn, bấm để mở |
| `> [!TIP]`, `> [!NOTE]` | Khối TIP, NOTE |
| `[tên file](#file-<id>)` | Link tải file demo có id tương ứng trong `demoFiles` của `app.js` |
| `[download-files]` | Khối tải toàn bộ file demo |

## Sửa nội dung

- Thêm hoặc đổi lab: sửa file markdown trong `public/labs/`, cập nhật `modules` trong `public/js/app.js` và bảng lịch trình trong `public/index.html`.
- Đổi file demo: xem `demo-files/README.md`.
