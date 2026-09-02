# Verbatim AI Transcript — Interaction GEMINI-020

- **Session / Interaction ID:** GEMINI-020
- **Date & Time:** 2026-09-02T16:33:27+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 5 & 6 — Human Screenshot Verification, Defect Reporting & GitHub Issues Filing

---

## 1. Verbatim Student Prompt

```text
mình vừa đạt vào hw06/screenshot rồi đó
```

---

## 2. Verbatim Conversational AI Response

Ảnh chụp màn hình bạn vừa cung cấp đã được kiểm tra và xác thực hoàn hảo!

---

### 1. Xác thực bằng chứng Postman Console (`hw06/screenshots/fr01-x-student-id.png` & `.jpg`)

- **File đã lưu:** [`hw06/screenshots/fr01-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr01-x-student-id.png)
- **Các thông tin hiển thị đạt 100% chuẩn yêu cầu:**
  - **Workspace & Environment:** `Ngọc Gia Bảo Phạm's Workspace` | `EShop Local Environment`
  - **Collection Structure:** Đầy đủ 8 folders (`01` đến `08`)
  - **Request Executed:** `FR01-AI-001 — Standard Valid ASCII Registration` (`POST {{baseUrl}}/api/register`) $\rightarrow$ `200 OK`
  - **Console Request Headers:** Hiển thị rõ ràng dòng:
    ```text
    X-Student-Id: "23127027"
    ```
- **Commit Git cục bộ:** `8439f1f` (`test(fr01): add authentic Postman Console screenshot evidence`).

---

### 2. Đã tạo thành công 5 GitHub Issues chính thức trên Repository

Dựa trên bằng chứng runtime từ Newman và SQLite probe, 5 lỗi SUT đã được phân tích nguyên nhân gốc rễ (Root Cause Analysis) và được tạo thành công trên repository [`giabaocode/23127027-HW06-API-Testing/issues`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues):

| Issue # | Defect ID | Mức độ | Tiêu đề Issue & Link | Vi phạm |
| :---: | :---: | :---: | :--- | :---: |
| **[#1](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/1)** | `DEF-FR01-01` | **Critical** | `[DEF-FR01-01] Critical: User Passwords Stored in Plaintext in SQLite Database` | `SEC-01` |
| **[#2](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/2)** | `DEF-FR01-02` | **High** | `[DEF-FR01-02] High: Duplicate Email Registration Succeeds with HTTP 200` | `FR-01` |
| **[#3](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/3)** | `DEF-FR01-03` | **High** | `[DEF-FR01-03] High: Missing Password Complexity Policy Enforcement` | `FR-01` |
| **[#4](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/4)** | `DEF-FR01-04` | **High** | `[DEF-FR01-04] High: Missing Mandatory Field Validation for Name, Email, and Password` | `FR-01` |
| **[#5](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/5)** | `DEF-FR01-05` | **Medium** | `[DEF-FR01-05] Medium: Missing Email Format Syntax Validation` | `FR-01` |

- **Defect Register & Reports:** Đã lưu đầy đủ tại [`hw06/bugs/`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/) và commit cục bộ tại `7f7c771` & `9f8c6cf`.
- **Hành động manual còn lại (tùy chọn / làm sau):** Bạn có thể mở trang Issues trên GitHub, chụp ảnh danh sách issues hoặc chi tiết từng issue và lưu vào `hw06/bugs/evidence/` để bổ sung vào báo cáo sau này.

---

### Toàn bộ công việc của FR-01 (Account Registration) đã hoàn tất!

Bạn đã sẵn sàng để chúng ta chuyển sang tính năng tiếp theo trong phạm vi bài tập chưa:
👉 **Pool B: FR-07 — Shopping Cart (`GET /api/cart`, `POST /api/cart`)**?
