# Verbatim AI Transcript — Interaction CODEX-002

- **Session / Interaction ID:** CODEX-002
- **Date & Time:** 2026-09-03T18:19:28+07:00
- **AI Tool:** OpenAI Codex
- **Phase:** GitHub Bug-Evidence Completion and Final Repackaging

---

## 1. Verbatim Student Prompts

### Prompt 1

```text
Giờ sao có dudọcw ảnh lỗi để dans vào github issue
```

### Prompt 2

```text
mình vừa mở ra các report của 3 fr và chụp các ảnh tuongư ứng cho bug issue rồi
```

### Prompt 3

```text
mình đăng lên github issue luôn rồi á
```

---

## 2. Verbatim AI Guidance Output

Bạn có thể lấy ảnh lỗi thật trực tiếp từ các Newman report đã có, không cần chạy lại toàn bộ test.

1. Mở file HTML tương ứng bằng trình duyệt:

- FR-01: `hw06/newman/fr01/fr01-report.html`
- FR-07: `hw06/newman/fr07/fr07-report.html`
- FR-12: `hw06/newman/fr12/fr12-report.html`

2. Nhấn `Cmd + F`, tìm test ID liên quan.
3. Mở chi tiết assertion bị fail, bảo đảm ảnh thấy:

- Test ID
- Expected
- Actual
- AssertionError
- Tên request hoặc endpoint

4. Chụp bằng `Cmd + Shift + 4`.
5. Đặt tên, ví dụ `DEF-FR01-02-evidence.png`.
6. Vào GitHub Issue tương ứng → Edit hoặc Comment → kéo ảnh vào ô nội dung → đợi GitHub upload xong → Submit.

Ánh xạ test để tìm:

| Issue | Test ID nên chụp |
|---|---|
| #1 Plaintext password | Chạy script `verify-sec01-plaintext.js` rồi chụp Terminal |
| #2 Duplicate email | `FR01-AI-016` hoặc `FR01-AI-017` |
| #3 Password policy | `FR01-AI-025`, `026`, `029`, `030` hoặc `031` |
| #4 Missing fields | `FR01-AI-003`, `011`, `032` hoặc `035` |
| #5 Invalid email | `FR01-AI-013` hoặc `014` |
| #6 Duplicate cart row | `FR07-AI-009`, `010`, `011` hoặc `FR07-STU-004` |
| #7 Invalid quantity | `FR07-AI-014`–`018`, `020`, `021`, `023` hoặc `024` |
| #8 Missing admin role check | `FR12-AI-001`–`007`, `037`, `038` |
| #9 Anonymous product mutation | `FR12-AI-008`–`010` hoặc `029`–`031` |
| #10 Category authorization | `FR12-AI-011`–`013` |
| #11 Coupon listing authorization | `FR12-AI-014` |

Riêng Issue #1, chạy:

```bash
cd /Users/phamngocgiabao/eshop-sut
NODE_PATH=backend/node_modules node hw06/postman/scripts/verify-sec01-plaintext.js
```

Sau đó chụp phần Terminal thể hiện `stored_password === submitted_plaintext: true`.

Quan trọng: ảnh `fr07-bug-issue-001.png` và `fr12-bug-issue-001.png` hiện chỉ chụp trang Issue, chưa phải ảnh chứng minh hành vi lỗi. Bạn cần ảnh assertion/runtime như hướng dẫn trên cho đủ cả 11 issue.

---

## 3. Verbatim Final User-Facing AI Output

Đã xác minh xong: cả 11/11 GitHub Issues đều có ảnh bằng chứng trong body hoặc comment. Mình đã cập nhật README, main report, manifest, checklist và `MANUAL_TODO.md` từ trạng thái “thiếu ảnh” sang “đã hoàn thành”, đồng thời lưu chuỗi tương tác này vào AI Audit dưới mã `CODEX-002`.

Bốn PDF và file `23127027_HW06_AI_API_100.zip` đã được dựng lại; validator cục bộ và kiểm tra CRC của ZIP đều đạt 0 lỗi. Phần bug evidence theo đề hiện đã hoàn tất.

Còn ba bước thuộc trách nhiệm cá nhân của bạn: xác nhận diagram thật sự do bạn tự vẽ, xác nhận 15 extension test cùng AI critique phản ánh phán đoán của bạn, rồi commit/push các thay đổi và nộp ZIP lên Moodle.

---

## 4. Verification Evidence

- GitHub API result: Issues #1 through #11 each returned an image marker in the issue body or comments.
- No local image was synthesized or modified by the AI.
- Documentation status was updated only after online verification completed.
