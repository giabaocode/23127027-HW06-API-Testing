# FR-01: Account Registration — Human Audit Worksheet

> **Auditor Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature:** FR-01 — Account Registration (`POST /api/register`)
> - **Status:** COMPLETED (All 38 AI-generated test cases audited personally by student)
> - **Academic Integrity Statement:** All verdicts, reasoning, and corrections below reflect the student's personal judgment based on authoritative course specifications (`README.md`, `api_specification.md`, and course requirements).

---

## 1. Human Audit Summary

- **Total Audited Test Cases:** 38 / 38
- **Human Verdict Distribution:**
  - **VALID:** 25 (65.8%)
  - **INCOMPLETE:** 12 (31.6%)
  - **INVALID:** 1 (2.6%)
  - **Total:** 38 (100.0%)

---

## 2. Complete Human Audit Register

| Test ID | Coverage ID | Short Test Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **FR01-AI-001** | `COV-FR01-01` | Standard valid ASCII name registration | VALID | Happy-path hợp lệ, đủ field bắt buộc và password đáp ứng policy. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-002** | `COV-FR01-02` | Vietnamese Unicode name with diacritics | INCOMPLETE | Spec không nói rõ Unicode/diacritics bắt buộc phải được chấp nhận. | Đổi thành robustness/characterization; nếu accept thì kiểm tra lưu UTF-8 đúng. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-003** | `COV-FR01-03` | Omitted mandatory name field rejection | VALID | name là field bắt buộc nên thiếu name phải bị reject; status lỗi cụ thể vẫn UNKNOWN. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-004** | `COV-FR01-04` | Empty string name value rejection | INCOMPLETE | Spec yêu cầu cung cấp họ tên nhưng không định nghĩa rõ empty string/trim behavior. | Giữ rejection là INFERRED hoặc xem đây là robustness test. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-005** | `COV-FR01-05` | Non-string integer name data type rejection | INCOMPLETE | Kiểu string của name chỉ suy ra từ JSON example, chưa có formal schema. | Đổi thành type-robustness test; không coi rejection là requirement chính thức. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-006** | `COV-FR01-06` | Extreme upper length name robustness (1000 chars) | INCOMPLETE | Spec không có max length cho name nên 1000 ký tự không phải boundary chính thức. | Xem đây là robustness test; accept hoặc reject sạch đều có thể hợp lệ, chỉ fail nếu crash hoặc làm hỏng DB. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-007** | `COV-FR01-07` | Literal SQL syntax handling in name (SEC-05) | VALID | Kiểm tra SEC-05 hợp lý vì dấu apostrophe có thể đi tới database insert và phải được xử lý như dữ liệu. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-008** | `COV-FR01-08` | HTML script tag robustness probe in name | INCOMPLETE | SEC-04 không áp dụng trực tiếp cho JSON API và test chưa nói rõ cách verify dữ liệu được lưu nguyên dạng. | Giữ như robustness test hoặc thêm bước DB verification. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-009** | `COV-FR01-09` | Standard valid RFC email format registration | VALID | Email dạng user@domain.com phù hợp trực tiếp với format FR-01 và là happy-path hợp lệ. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-010** | `COV-FR01-10` | Advanced RFC email with plus-addressing | INCOMPLETE | Plus-addressing hợp lệ theo chuẩn email rộng hơn nhưng spec không bắt buộc phải hỗ trợ. | Xem như characterization; nếu accept thì kiểm tra 200 và dữ liệu được lưu đúng. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-011** | `COV-FR01-11` | Omitted mandatory email field rejection | VALID | email là field bắt buộc nên thiếu email phải bị reject; status cụ thể vẫn UNKNOWN. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-012** | `COV-FR01-12` | Empty string email value rejection | VALID | Empty email không thể thỏa yêu cầu email hợp lệ nên semantic rejection là hợp lý. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-013** | `COV-FR01-13` | Malformed email missing at-symbol (@) rejection | VALID | Email thiếu @ rõ ràng vi phạm format requirement. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-014** | `COV-FR01-13` | Malformed email missing domain part rejection | VALID | Email thiếu domain sau @ rõ ràng vi phạm format requirement. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-015** | `COV-FR01-14` | Non-string integer email data type rejection | INCOMPLETE | Kiểu string của email chỉ suy ra từ example, chưa có formal schema. | Đổi thành type-robustness/characterization test. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-016** | `COV-FR01-15` | Duplicate registration of pre-seeded email rejection | VALID | Email uniqueness là requirement rõ ràng nên đăng ký email đã tồn tại phải bị reject. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-017** | `COV-FR01-15` | Duplicate registration via dynamic sequential call | VALID | State-dependent test tốt: email chưa tồn tại -> đăng ký thành công -> đăng ký lại cùng email phải bị reject. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-018** | `COV-FR01-16` | Case-insensitive duplicate email rejection | INCOMPLETE | Spec không nói uniqueness có case-insensitive hay không. | Xem như characterization test, không coi rejection theo case là requirement chính thức. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-019** | `COV-FR01-17` | SQL-like syntax handling in email (SEC-05) | INVALID | Payload email SQL-like lại malformed nên có thể bị chặn ở validation trước khi chạm DB, vì vậy không chứng minh được SEC-05. | Dùng SQL-like input ở field name hoặc một payload hợp lệ về format nhưng vẫn đi tới persistence layer. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-020** | `COV-FR01-18` | Standard strong password meeting all 5 criteria | VALID | Password đáp ứng đầy đủ 5 tiêu chí được mô tả trong FR-01. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-021** | `COV-FR01-19` | Documented special symbol coverage: at-sign (@) | VALID | @ nằm trong documented special-character set và các rule password khác đều đạt. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-022** | `COV-FR01-19` | Documented special symbol coverage: dollar-sign ($) | VALID | $ nằm trong documented special-character set và các rule password khác đều đạt. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-023** | `COV-FR01-19` | Documented special symbol coverage: ampersand (&) | VALID | & nằm trong documented special-character set và các rule password khác đều đạt. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-024** | `COV-FR01-20` | Required special symbol plus extra symbol (!#) | VALID | Password có ! nên đã thỏa yêu cầu special char; spec không cấm thêm #. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-025** | `COV-FR01-21` | Missing required special character from set rejection | VALID | Password không có ký tự nào thuộc required special-character set nên vi phạm policy rõ ràng. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-026** | `COV-FR01-22` | Password length boundary: 7 chars (min - 1) rejection | VALID | Boundary 7 ký tự là min-1 và vẫn giữ các character class khác để isolate length condition. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-027** | `COV-FR01-22` | Password length boundary: 8 chars (exact minimum) | VALID | 8 ký tự đúng minimum và password vẫn thỏa các rule khác. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-028** | `COV-FR01-22` | Password length boundary: 9 chars (min + 1) | VALID | 9 ký tự là min+1 và vẫn thỏa toàn bộ password policy. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-029** | `COV-FR01-23` | Missing uppercase letter in password rejection | VALID | Test isolate đúng trường hợp thiếu uppercase trong password. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-030** | `COV-FR01-23` | Missing lowercase letter in password rejection | VALID | Test isolate đúng trường hợp thiếu lowercase trong password. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-031** | `COV-FR01-23` | Missing numeric digit in password rejection | VALID | Test isolate đúng trường hợp thiếu numeric digit trong password. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-032** | `COV-FR01-24` | Empty string password value rejection | VALID | Empty password vi phạm rõ minimum length và các character-class requirements. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-033** | `COV-FR01-25` | Non-string integer password data type rejection | INCOMPLETE | Integer password rejection dựa trên type contract chỉ suy ra từ JSON example. | Đổi thành type-safety robustness test; exact semantic behavior để UNKNOWN. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-034** | `COV-FR01-26` | Extreme upper length password robustness (128 chars) | INCOMPLETE | Spec không có max password length và testcase suy diễn thêm bcrypt/argon2/CPU exhaustion. | Giữ như robustness test; không yêu cầu thuật toán hash cụ thể, chỉ kiểm tra xử lý an toàn và DB integrity. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-035** | `COV-FR01-27` | Empty JSON body rejection | VALID | Empty JSON body thiếu toàn bộ các field bắt buộc nên phải bị semantic rejection. | — | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-036** | `COV-FR01-28` | Unexpected extra field (confirmPassword) robustness | INCOMPLETE | Contract không định nghĩa cách xử lý extra property như confirmPassword. | Xem như robustness/characterization; accept hoặc clean reject đều có thể hợp lệ, fail nếu crash hoặc có side effect bất thường. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-037** | `COV-FR01-29` | Password plaintext storage verification (SEC-01 DB inspection) | INCOMPLETE | SEC-01 chỉ yêu cầu password không được lưu plaintext, nhưng test nâng yêu cầu thành phải dùng bcrypt/argon2. | Oracle nên chỉ là stored password != submitted plaintext; không yêu cầu thuật toán cụ thể nếu spec không nói. | 2026-09-02T13:46:21+07:00 |
| **FR01-AI-038** | `COV-FR01-30` | Security hardening: credential non-leakage in response | VALID | Credential non-leakage là security-hardening test hợp lý và đã được label đúng là hardening chứ không giả làm explicit FR/SEC requirement. | — | 2026-09-02T13:46:21+07:00 |
