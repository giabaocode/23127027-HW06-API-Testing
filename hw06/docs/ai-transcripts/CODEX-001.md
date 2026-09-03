# Verbatim AI Transcript — Interaction CODEX-001

- **Session / Interaction ID:** CODEX-001
- **Date & Time:** 2026-09-03T11:46:29+07:00
- **AI Tool:** OpenAI Codex
- **Phase:** Independent Final Audit, Correction, and Packaging

---

## 1. Verbatim Student Prompt

```text
bạn hãy đọc file pdf về yêu cầu homework 6 sau đó rà soát toàn bộ thuư mục hiện tại xem thử còn cânf làm những gì để hoàn thành homework , phânf nào bạn có thêr chỉnh sửa thì bạn chỉnh sửa giúp mình để hoàn thiện bài làm luôn nhé. Nêus được bạn hãy giúp mình lưu prompt này vào AI-audit luôn để giữ đúng rule của đề bài
```

---

## 2. Verbatim Final User-Facing AI Output

Đã hoàn thiện toàn bộ phần có thể xử lý tự động và dựng lại bộ nộp. Mình đã đọc đủ 8 trang đề, đối chiếu toàn bộ `hw06/`, sửa số liệu báo cáo sai lệch, sửa các validator cũ, chuẩn hóa liên kết, cập nhật checklist/trạng thái trung thực, lưu prompt này vào AI Audit, dựng lại PDF và ZIP, rồi kiểm tra CRC.

Kết quả xác minh: 129 test case logic; audit 114 AI case = 76 VALID, 37 INCOMPLETE, 1 INVALID; Newman thực tế = 169 request, 541 assertion, 457 passed, 84 failed; 11 lỗi SUT; [Run A GitHub Actions](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685) thực sự success và [Run B](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154) thực sự failure. Toàn bộ kiểm tra cục bộ hiện đạt 0 lỗi.

Còn bốn việc bắt buộc cần chính bạn hoàn tất: đính kèm ảnh lỗi thật vào từng [GitHub Issue #1–#11](https://github.com/giabaocode/23127027-HW06-API-Testing/issues) (hiện cả body lẫn comment của cả 11 issue đều chưa có ảnh), xác nhận diagram là do bạn tự vẽ, xác nhận 15 extension test và AI critique phản ánh phán đoán cá nhân của bạn, rồi commit/push và nộp ZIP lên Moodle. Hai transcript lịch sử `CHATGPT-001` và `GEMINI-043` thiếu nguyên văn không thể phục hồi; mình đã khai báo khoảng trống trung thực thay vì bịa nội dung.

Các tệp chính: `hw06/MANUAL_TODO.md`, `hw06/submission-checklist.md`, `hw06/docs/main-report.md`, `hw06/docs/ai-audit.md`, và `23127027_HW06_AI_API_100.zip`.

---

## 3. Actions and Verification Summary

- Read the authoritative eight-page HW06 PDF and mapped Sections 5–14 to repository artifacts.
- Inspected all project deliverables, Markdown reports, Postman JSON, Excel sheets, screenshots, CI workflow, Newman CLI/HTML reports, validators, and Git history.
- Verified the public repository, all 11 GitHub Issues, and both recorded GitHub Actions runs through the GitHub API.
- Corrected runtime totals and per-feature audit distributions without changing genuine test outcomes.
- Preserved anti-cheat human gates and explicitly identified missing per-issue image attachments.
- Ran detailed suite validators, the agent generator sample, JSON parsing, Python compilation, the enhanced submission validator, PDF validation, and ZIP CRC validation.
