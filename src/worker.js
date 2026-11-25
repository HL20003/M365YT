// Chặn toàn bộ site bằng một mật khẩu chung cho lớp học.
//
// - Mật khẩu là Secret LAB_PASSWORD trên Cloudflare (Worker > Settings > Variables and Secrets),
//   KHÔNG ghi vào code vì repo GitHub đang public. Chạy local: tạo file .dev.vars với dòng LAB_PASSWORD=...
// - Đăng nhập đúng: trình duyệt nhận cookie ký HMAC, có hạn SESSION_DAYS ngày.
//   Đổi mật khẩu thì mọi cookie cũ hết hiệu lực, mọi người phải đăng nhập lại.
// - Không có nút đăng xuất: phiên tự hết hạn sau SESSION_DAYS ngày.

const COOKIE = 'lab_session';
const SESSION_DAYS = 1; // hết hạn thì nhập lại cùng mật khẩu; đổi LAB_PASSWORD thì mọi phiên hết hiệu lực ngay
const enc = new TextEncoder();

export default {
    async fetch(request, env) {
        const url = new URL(request.url);
        const password = env.LAB_PASSWORD;

        // Chưa cấu hình mật khẩu: đóng site thay vì mở công khai
        if (!password) {
            return htmlResponse(page('Site chưa sẵn sàng', '<p class="msg">Quản trị viên chưa cấu hình mật khẩu cho site này.</p>'), 503);
        }

        // Logo và hình thương hiệu dùng trên trang đăng nhập: không cần đăng nhập
        if (url.pathname.startsWith('/brand/')) {
            return env.ASSETS.fetch(request);
        }

        if (url.pathname === '/login') {
            if (request.method === 'POST') return handleLogin(request, url, password);
            if (await isLoggedIn(request, password)) return redirect('/');
            return htmlResponse(loginPage(safeNext(url.searchParams.get('next')), false));
        }

        if (await isLoggedIn(request, password)) {
            const res = await env.ASSETS.fetch(request);
            // Trang và file sau đăng nhập không được lưu ở cache dùng chung
            const out = new Response(res.body, res);
            out.headers.set('Cache-Control', 'private, no-cache');
            return out;
        }

        // Chưa đăng nhập: trang HTML thì chuyển tới /login, file khác (md, js, docx...) trả 401
        const wantsHtml = (request.headers.get('Accept') || '').includes('text/html');
        if (request.method === 'GET' && wantsHtml) {
            return redirect('/login?next=' + encodeURIComponent(url.pathname + url.search));
        }
        return new Response('Cần đăng nhập', { status: 401, headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
    },
};

async function handleLogin(request, url, password) {
    const form = await request.formData();
    const input = String(form.get('password') || '');
    const next = safeNext(String(form.get('next') || ''));
    const hash = String(form.get('hash') || '');

    // So sánh qua HMAC để thời gian so sánh không phụ thuộc nội dung mật khẩu
    const ok = (await sign(password, 'check:' + input)) === (await sign(password, 'check:' + password));
    if (!ok) {
        await new Promise(r => setTimeout(r, 800)); // làm chậm việc dò mật khẩu
        return htmlResponse(loginPage(next, true), 401);
    }

    const expires = Date.now() + SESSION_DAYS * 86400 * 1000;
    const token = `${expires}.${await sign(password, 'session:' + expires)}`;
    const cookie = `${COOKIE}=${token}; Path=/; Max-Age=${SESSION_DAYS * 86400}; HttpOnly; Secure; SameSite=Lax`;
    const target = next + (/^#[\w\-/]*$/.test(hash) ? hash : '');
    return redirect(target, cookie);
}

async function isLoggedIn(request, password) {
    const match = (request.headers.get('Cookie') || '').match(new RegExp(`(?:^|;\\s*)${COOKIE}=([^;]+)`));
    if (!match) return false;
    const [expires, sig] = match[1].split('.');
    if (!expires || !sig || Number(expires) < Date.now()) return false;
    return sig === (await sign(password, 'session:' + expires));
}

async function sign(secret, data) {
    const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
    const mac = await crypto.subtle.sign('HMAC', key, enc.encode(data));
    return btoa(String.fromCharCode(...new Uint8Array(mac))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

// Chỉ cho phép chuyển về đường dẫn trong chính site (chặn chuyển hướng sang trang ngoài)
function safeNext(next) {
    return next && next.startsWith('/') && !next.startsWith('//') && !next.startsWith('/\\') ? next : '/';
}

function redirect(location, cookie) {
    const headers = { Location: location, 'Cache-Control': 'no-store' };
    if (cookie) headers['Set-Cookie'] = cookie;
    return new Response(null, { status: 302, headers });
}

function htmlResponse(html, status = 200) {
    return new Response(html, {
        status,
        headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', 'X-Frame-Options': 'DENY' },
    });
}

function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function loginPage(next, failed) {
    return page('Đăng nhập', `
        <p class="msg">Nhập mật khẩu lớp học do người hướng dẫn cung cấp để vào các bài lab.</p>
        <form method="post" action="/login">
            <input type="hidden" name="next" value="${escapeHtml(next)}">
            <input type="hidden" name="hash" id="hash">
            <label for="password">Mật khẩu lớp học</label>
            <div class="field">
                <input type="password" id="password" name="password" autocomplete="current-password" required autofocus
                       ${failed ? 'aria-invalid="true" aria-describedby="err"' : ''}>
                <button type="button" class="toggle" id="toggle" aria-label="Hiện mật khẩu" aria-pressed="false">Hiện</button>
            </div>
            ${failed ? '<p class="error" id="err" role="alert">Mật khẩu chưa đúng. Anh/chị kiểm tra lại và thử lần nữa.</p>' : ''}
            <button type="submit" class="submit">Vào lab</button>
        </form>
        <p class="help">Chưa có mật khẩu? Liên hệ người hướng dẫn buổi học.</p>
        <script>
            document.getElementById('hash').value = location.hash;
            const pw = document.getElementById('password'), t = document.getElementById('toggle');
            t.addEventListener('click', () => {
                const show = pw.type === 'password';
                pw.type = show ? 'text' : 'password';
                t.textContent = show ? 'Ẩn' : 'Hiện';
                t.setAttribute('aria-pressed', String(show));
                t.setAttribute('aria-label', show ? 'Ẩn mật khẩu' : 'Hiện mật khẩu');
                pw.focus();
            });
        </script>`);
}

// Logo chính thức đặt tại public/brand/softwareone-logo.svg; chưa có file thì hiện chữ thay thế
const LOGO = `<img class="logo" src="/brand/softwareone-logo.svg" alt="SoftwareOne"
    onerror="this.replaceWith(Object.assign(document.createElement('span'), {className: 'logo-text', textContent: 'SoftwareOne'}))">`;

function page(title, body) {
    return `<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>${title} - Copilot Workshop</title>
<style>
    :root {
        --ink: #0b1420; --navy: #0a2a4e; --navy-900: #061b33; --blue: #1c5fb0; --blue-tint: #eef4fb;
        --text: #16202c; --muted: #55606e; --border: #ccd5df; --bg: #ffffff; --error: #b42318; --error-tint: #fef3f2;
    }
    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body { margin: 0; background: var(--bg); color: var(--text); font: 16px/1.55 "Segoe UI", system-ui, -apple-system, sans-serif; }
    .wrap { min-height: 100vh; display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); }

    /* Cột trái: giới thiệu workshop */
    .hero { position: relative; overflow: hidden; color: #fff; padding: 56px 64px; display: flex; flex-direction: column; justify-content: space-between;
            background: radial-gradient(circle at 85% 15%, rgba(28, 95, 176, 0.55), transparent 45%),
                        radial-gradient(circle at 10% 90%, rgba(28, 95, 176, 0.35), transparent 40%),
                        linear-gradient(160deg, var(--navy-900), var(--navy) 65%); }
    .hero::after { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: 0.08;
                   background-image: linear-gradient(#fff 1px, transparent 1px), linear-gradient(90deg, #fff 1px, transparent 1px);
                   background-size: 44px 44px; }
    .hero > * { position: relative; z-index: 1; }
    .eyebrow { font-size: 0.8rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #a9c4e6; }
    .hero h2 { margin: 14px 0 16px; font-size: clamp(1.9rem, 3vw, 2.6rem); line-height: 1.15; font-weight: 700; max-width: 14ch; }
    .hero p { margin: 0; max-width: 42ch; color: #d6e2f1; font-size: 1.05rem; }
    .points { list-style: none; margin: 32px 0 0; padding: 0; display: grid; gap: 14px; max-width: 44ch; }
    .points li { display: flex; gap: 12px; align-items: flex-start; color: #e8eff8; }
    .points li::before { content: ""; flex: none; width: 8px; height: 8px; margin-top: 9px; border-radius: 50%; background: #7fb0ea; }
    .hero small { color: #a9c4e6; font-size: 0.85rem; }

    /* Cột phải: form */
    .panel { display: flex; align-items: center; justify-content: center; padding: 48px 24px; }
    main { width: 100%; max-width: 380px; }
    .logo { display: block; height: 34px; width: auto; margin-bottom: 40px; }
    .logo-text { display: inline-block; margin-bottom: 40px; font-size: 1.6rem; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
    h1 { margin: 0 0 8px; font-size: 1.75rem; color: var(--ink); }
    .msg { margin: 0 0 28px; color: var(--muted); }
    label { display: block; font-weight: 600; margin-bottom: 8px; }
    .field { position: relative; }
    input[type=password], input[type=text] { width: 100%; padding: 12px 64px 12px 14px; font: inherit; color: var(--text);
            border: 1px solid var(--border); border-radius: 10px; background: #fff; }
    input:focus { outline: 3px solid rgba(28, 95, 176, 0.25); border-color: var(--blue); }
    input[aria-invalid=true] { border-color: var(--error); }
    .toggle { position: absolute; right: 6px; top: 50%; transform: translateY(-50%); padding: 6px 10px; font: inherit; font-size: 0.85rem;
              font-weight: 600; color: var(--blue); background: transparent; border: 0; border-radius: 6px; cursor: pointer; }
    .toggle:hover { background: var(--blue-tint); }
    .error { margin: 10px 0 0; padding: 10px 12px; font-size: 0.92rem; color: var(--error); background: var(--error-tint); border-radius: 8px; }
    .submit { margin-top: 20px; width: 100%; padding: 13px; font: inherit; font-weight: 600; color: #fff; background: var(--ink);
              border: 0; border-radius: 10px; cursor: pointer; transition: background 0.15s; }
    .submit:hover { background: var(--navy); }
    .submit:focus-visible, .toggle:focus-visible { outline: 3px solid rgba(28, 95, 176, 0.35); outline-offset: 2px; }
    .help { margin: 20px 0 0; font-size: 0.9rem; color: var(--muted); }

    @media (max-width: 860px) {
        .wrap { grid-template-columns: 1fr; }
        .hero { padding: 28px 16px 32px; }
        .hero h2 { margin: 10px 0 8px; font-size: 1.6rem; max-width: none; }
        .points, .hero small { display: none; }
        .panel { padding: 32px 16px 48px; align-items: flex-start; }
        .logo, .logo-text { margin-bottom: 28px; }
    }
</style>
</head>
<body>
<div class="wrap">
    <section class="hero" aria-label="Giới thiệu workshop">
        <div>
            <div class="eyebrow">SoftwareOne Vietnam</div>
            <h2>Microsoft 365 Copilot Workshop</h2>
            <p>Thực hành Copilot trên những việc hành chính quen thuộc mỗi ngày: email, cuộc họp, báo cáo, bảng tính và bài trình bày.</p>
            <ul class="points">
                <li>Bài lab có hướng dẫn từng bước và đáp án mẫu</li>
                <li>File demo tải về dùng ngay, prompt sao chép một chạm</li>
                <li>Tự tạo agent tra cứu chính sách cho cả khoa, phòng</li>
            </ul>
        </div>
        <small>Tài liệu dành cho học viên workshop. Vui lòng không chia sẻ mật khẩu ra ngoài lớp học.</small>
    </section>
    <div class="panel">
        <main>
            ${LOGO}
            <h1>${title}</h1>
            ${body}
        </main>
    </div>
</div>
</body>
</html>`;
}
