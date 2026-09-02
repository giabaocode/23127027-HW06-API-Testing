# Verbatim AI Transcript — Interaction GEMINI-012

- **Session / Interaction ID:** GEMINI-012
- **Date & Time:** 2026-09-02T13:46:21+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 2 — Student Human Audit Execution (All 38 FR-01 Cases Reviewed)

---

## 1. Verbatim Student Prompt

```text
001 V | Happy-path hợp lệ, đủ field bắt buộc và password đáp ứng policy.

002 I | Spec không nói rõ Unicode/diacritics bắt buộc phải được chấp nhận. | Đổi thành robustness/characterization; nếu accept thì kiểm tra lưu UTF-8 đúng.

003 V | name là field bắt buộc nên thiếu name phải bị reject; status lỗi cụ thể vẫn UNKNOWN.

004 I | Spec yêu cầu cung cấp họ tên nhưng không định nghĩa rõ empty string/trim behavior. | Giữ rejection là INFERRED hoặc xem đây là robustness test.

005 I | Kiểu string của name chỉ suy ra từ JSON example, chưa có formal schema. | Đổi thành type-robustness test; không coi rejection là requirement chính thức.

006 I | Spec không có max length cho name nên 1000 ký tự không phải boundary chính thức. | Xem đây là robustness test; accept hoặc reject sạch đều có thể hợp lệ, chỉ fail nếu crash hoặc làm hỏng DB.

007 V | Kiểm tra SEC-05 hợp lý vì dấu apostrophe có thể đi tới database insert và phải được xử lý như dữ liệu.

008 I | SEC-04 không áp dụng trực tiếp cho JSON API và test chưa nói rõ cách verify dữ liệu được lưu nguyên dạng. | Giữ như robustness test hoặc thêm bước DB verification.

009 V | Email dạng user@domain.com phù hợp trực tiếp với format FR-01 và là happy-path hợp lệ.

010 I | Plus-addressing hợp lệ theo chuẩn email rộng hơn nhưng spec không bắt buộc phải hỗ trợ. | Xem như characterization; nếu accept thì kiểm tra 200 và dữ liệu được lưu đúng.

011 V | email là field bắt buộc nên thiếu email phải bị reject; status cụ thể vẫn UNKNOWN.

012 V | Empty email không thể thỏa yêu cầu email hợp lệ nên semantic rejection là hợp lý.

013 V | Email thiếu @ rõ ràng vi phạm format requirement.

014 V | Email thiếu domain sau @ rõ ràng vi phạm format requirement.

015 I | Kiểu string của email chỉ suy ra từ example, chưa có formal schema. | Đổi thành type-robustness/characterization test.

016 V | Email uniqueness là requirement rõ ràng nên đăng ký email đã tồn tại phải bị reject.

017 V | State-dependent test tốt: email chưa tồn tại -> đăng ký thành công -> đăng ký lại cùng email phải bị reject.

018 I | Spec không nói uniqueness có case-insensitive hay không. | Xem như characterization test, không coi rejection theo case là requirement chính thức.

019 X | Payload email SQL-like lại malformed nên có thể bị chặn ở validation trước khi chạm DB, vì vậy không chứng minh được SEC-05. | Dùng SQL-like input ở field name hoặc một payload hợp lệ về format nhưng vẫn đi tới persistence layer.

020 V | Password đáp ứng đầy đủ 5 tiêu chí được mô tả trong FR-01.

021 V | @ nằm trong documented special-character set và các rule password khác đều đạt.

022 V | $ nằm trong documented special-character set và các rule password khác đều đạt.

023 V | & nằm trong documented special-character set và các rule password khác đều đạt.

024 V | Password có ! nên đã thỏa yêu cầu special char; spec không cấm thêm #.

025 V | Password không có ký tự nào thuộc required special-character set nên vi phạm policy rõ ràng.

026 V | Boundary 7 ký tự là min-1 và vẫn giữ các character class khác để isolate length condition.

027 V | 8 ký tự đúng minimum và password vẫn thỏa các rule khác.

028 V | 9 ký tự là min+1 và vẫn thỏa toàn bộ password policy.

029 V | Test isolate đúng trường hợp thiếu uppercase trong password.

030 V | Test isolate đúng trường hợp thiếu lowercase trong password.

031 V | Test isolate đúng trường hợp thiếu numeric digit trong password.

032 V | Empty password vi phạm rõ minimum length và các character-class requirements.

033 I | Integer password rejection dựa trên type contract chỉ suy ra từ JSON example. | Đổi thành type-safety robustness test; exact semantic behavior để UNKNOWN.

034 I | Spec không có max password length và testcase suy diễn thêm bcrypt/argon2/CPU exhaustion. | Giữ như robustness test; không yêu cầu thuật toán hash cụ thể, chỉ kiểm tra xử lý an toàn và DB integrity.

035 V | Empty JSON body thiếu toàn bộ các field bắt buộc nên phải bị semantic rejection.

036 I | Contract không định nghĩa cách xử lý extra property như confirmPassword. | Xem như robustness/characterization; accept hoặc clean reject đều có thể hợp lệ, fail nếu crash hoặc có side effect bất thường.

037 I | SEC-01 chỉ yêu cầu password không được lưu plaintext, nhưng test nâng yêu cầu thành phải dùng bcrypt/argon2. | Oracle nên chỉ là stored password != submitted plaintext; không yêu cầu thuật toán cụ thể nếu spec không nói.

038 V | Credential non-leakage là security-hardening test hợp lý và đã được label đúng là hardening chứ không giả làm explicit FR/SEC requirement.
```

---

## 2. Verbatim Conversational AI Response

=== FR-01 STUDENT HUMAN AUDIT VALIDATION COMPLETE ===

All **38 test cases** have been reviewed personally by the student and populated into [hw06/testcases/fr01/human-audit.md](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/human-audit.md) and [hw06/testcases/fr01/human-review-compact.md](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/human-review-compact.md).

---

### 1. Programmatic Integrity & Validation Results

Programmatically verified across all 38 test case rows:
- **Verdicts Populated:** Exactly **38 / 38** (100%)
- **Valid Verdict Domain:** Every verdict $\in \{\text{VALID}, \text{INCOMPLETE}, \text{INVALID}\}$
- **Student Reasoning:** Present and preserved verbatim on all 38 rows
- **Student Correction for INCOMPLETE:** Present on all 12 INCOMPLETE test cases
- **Student Correction for INVALID:** Present on `FR01-AI-019`
- **Review Timestamps:** Present on all 38 rows (`2026-09-02T13:46:21+07:00`)
- **Original AI Test Set Integrity:** [`hw06/testcases/fr01/generated-ai-original.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/generated-ai-original.md) has **ZERO diff / 0 bytes modified** (remains 100% immutable as committed in `d961f6f`).

---

### 2. Final Student Human Verdict Distribution

```text
============================================================
FINAL STUDENT AUDIT DISTRIBUTION (FR-01)
============================================================
VALID:       25  (65.8%)
INCOMPLETE:  12  (31.6%)
INVALID:      1  ( 2.6%)  [FR01-AI-019]
------------------------------------------------------------
TOTAL:       38  (100.0%)
============================================================
```

#### Detailed Breakdown by Category:
- **VALID (25 cases):**
  - Standard Happy-Path: `FR01-AI-001`, `FR01-AI-009`, `FR01-AI-020`
  - Required Field Omission: `FR01-AI-003` (name), `FR01-AI-011` (email), `FR01-AI-035` (empty body)
  - Clear Validation / Boundary Violations: `FR01-AI-012` (blank email), `FR01-AI-013` (missing `@`), `FR01-AI-014` (missing domain), `FR01-AI-025` (no symbol), `FR01-AI-026` (len 7), `FR01-AI-029` (no upper), `FR01-AI-030` (no lower), `FR01-AI-031` (no digit), `FR01-AI-032` (blank password)
  - Exact Policy & Boundary Confirmations: `FR01-AI-021` (`@`), `FR01-AI-022` (`$`), `FR01-AI-023` (`&`), `FR01-AI-024` (`!#`), `FR01-AI-027` (len 8), `FR01-AI-028` (len 9)
  - Duplicate Email Enforcement: `FR01-AI-016` (pre-seeded), `FR01-AI-017` (dynamic state transition)
  - Core Security Dimensions: `FR01-AI-007` (SEC-05 parameterized query via name), `FR01-AI-038` (credential non-leakage hardening)
- **INCOMPLETE (12 cases):**
  - Characterization & Inferred Rules: `FR01-AI-002` (Unicode/diacritics), `FR01-AI-004` (empty string name), `FR01-AI-010` (plus-addressing), `FR01-AI-018` (case-insensitive duplicate)
  - Inferred JSON Type Rules: `FR01-AI-005` (integer name), `FR01-AI-015` (integer email), `FR01-AI-033` (integer password)
  - Unspecified Boundaries & Robustness: `FR01-AI-006` (1000 char name), `FR01-AI-034` (128 char password), `FR01-AI-036` (unexpected `confirmPassword` field)
  - Over-Specified Security Oracles: `FR01-AI-008` (SEC-04 UI scope vs API DB persistence), `FR01-AI-037` (SEC-01 algorithm inference vs stored != plaintext)
- **INVALID (1 case):**
  - `FR01-AI-019`: Email SQL-like payload (`' OR '1'='1'@domain.com`) is syntactically malformed and will be rejected at the input-validation layer before ever touching the database, failing to demonstrate SEC-05 parameterized-query behavior. Correction: use SQL characters in `name` or a syntactically valid email payload that reaches persistence.

---

### 3. External AI Audit Transcripts & Traceability Setup

Created dedicated external audit files in [`hw06/docs/external-ai-transcripts/`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/):
1. **[`CHATGPT-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-001.md):** Setup & prompt engineering transcript template with student placeholders.
2. **[`CHATGPT-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-002.md):** Complete verbatim transcript of ChatGPT's reference review of all 38 test cases.
3. **[`hw06/docs/ai-audit.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-audit.md):** Section 3 updated with explicit markdown links to both external transcript files, clearly distinguishing AI reference material from student-authored audit decisions.

---

### 4. Git Diff Summary

```text
Changes to be committed:
  modified:   hw06/docs/ai-audit.md                       (linked external transcripts, added GEMINI-011 & 012)
  modified:   hw06/docs/ai-transcripts/GEMINI-010.md      (finalized verbatim response)
  modified:   hw06/testcases/fr01/human-audit.md          (populated all 38 student verdicts & reasoning)
  modified:   hw06/testcases/fr01/human-review-compact.md (synchronized with student decisions)

Untracked files:
  hw06/docs/ai-transcripts/GEMINI-011.md
  hw06/docs/ai-transcripts/GEMINI-012.md
  hw06/docs/external-ai-transcripts/CHATGPT-001.md
  hw06/docs/external-ai-transcripts/CHATGPT-002.md

Untracked non-submission files:
  2026.HW06.API Testing_En.pdf (excluded from git staging)
```

---

### 5. Proposed Local Git Commit

As instructed, no commit has been executed yet. We propose committing the completed human audit with the following message:

```text
test(fr01): complete student audit of AI-generated registration tests
```

**Files to include in commit:**
- `hw06/testcases/fr01/human-audit.md`
- `hw06/testcases/fr01/human-review-compact.md`
- `hw06/docs/external-ai-transcripts/CHATGPT-001.md`
- `hw06/docs/external-ai-transcripts/CHATGPT-002.md`
- `hw06/docs/ai-audit.md`
- `hw06/docs/ai-transcripts/GEMINI-010.md`
- `hw06/docs/ai-transcripts/GEMINI-011.md`
- `hw06/docs/ai-transcripts/GEMINI-012.md`

**Please confirm if you approve executing this local commit.** Once approved, we will execute the commit locally (zero remote push) and prepare for Phase 3 (Human Corrections & Student Extension Tests).
