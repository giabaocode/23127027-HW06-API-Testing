# HW06 — Oral Defense Reference Notes (Optional Study Aid)

> [!NOTE]
> **OPTIONAL STUDY AID ONLY — NOT A MANDATORY SUBMISSION DELIVERABLE:**
> In accordance with official HW06 PDF Section 13, the Oral Defense is an oral examination conducted for a randomly selected 30% of students during the week following the deadline. 
> This document is strictly an optional personal study aid for student preparation and is **NOT** a required deliverable for the homework submission package under Section 14.

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Course:** Software Testing (Kiểm thử Phần mềm) — API Testing HW06
> - **Repository:** `https://github.com/giabaocode/23127027-HW06-API-Testing`

---

## 1. Feature Selection Rationale (FR-01, FR-07, FR-12)
- **Question:** *Why did you select these three specific features?*
- **Answer:**
  - **FR-01 (Pool A - Authentication/User):** Account registration (`POST /api/register`) is the foundational gateway of the application. It exercises strict string format validation, password hashing, and duplicate identity constraints.
  - **FR-07 (Pool B - Core Business Logic):** Shopping cart management (`/api/cart`) represents dynamic, state-dependent in-memory logic. It tests state transitions, item quantity boundary math, and idempotent/accumulation behavior.
  - **FR-12 (Pool C - Security/Administration):** Access control and administrative authorization tests the security boundary across 14 administrative and catalog mutation routes, enforcing role separation (`SEC-02` and `SEC-03`).

---

## 2. Oracle Classification Model (SPECIFIED vs INFERRED vs UNKNOWN)
- **Question:** *How did you classify your test expected results?*
- **Answer:**
  - **`SPECIFIED`:** The requirement is explicitly stated in the official course documentation (`README.md` or `api_specification.md`). E.g., `SEC-02` explicitly requires `401 Unauthorized` when no token is present; `SEC-03` requires `role === 'admin'`.
  - **`INFERRED`:** The behavior follows logical industry conventions or example schemas but is not formally mandated. E.g., returning `400 Bad Request` for a missing mandatory field is standard REST practice, but the course specification does not formally mandate 400.
  - **`UNKNOWN / SPEC-SILENT`:** The specification is completely silent regarding the exact HTTP status code (e.g., whether invalid cart quantity returns 400, 422, or remains unmodified). We assert the **semantic outcome** (cart not modified) rather than a rigid HTTP code.

---

## 3. Immutability of Original AI Generation
- **Question:** *Why is `generated-ai-original.md` kept immutable?*
- **Answer:**
  - To preserve truthful provenance and scientific auditability. The initial AI output represents historical evidence of raw AI capabilities and hallucinations. Corrections are formalized in `human-audit.md` and applied to `reviewed-ai-final.md`.

---

## 4. Key AI Mistakes Discovered During Audits
- **Question:** *Give specific examples of mistakes the AI made that required human intervention.*
- **Answer:**
  - **Domain Model Hallucination (FR-12):** The AI assumed the non-admin role was `'customer'`. In the actual SUT SQLite database and JWT claims, the role is `'user'`.
  - **Over-Specified HTTP Status (FR-12):** The AI claimed that valid admin actions must return `200/201` and unauthorized actions `401/403` by formal specification, when the specification only stated the access-control outcome.
  - **Over-Specified Rejection Envelopes (FR-07):** The AI required error responses to match `{"error": "..."}`, which is not part of the official contract.
  - **Counting Inconsistency (FR-12):** The AI claimed SEC-02 covered 10 test cases from `FR12-AI-029` to `FR12-AI-036`, which mathematically is only 8 cases.

---

## 5. Semantic Oracle Separation from HTTP Status
- **Question:** *Why did you separate semantic outcomes from HTTP status codes?*
- **Answer:**
  - In real-world and legacy APIs, endpoints often return `200 OK` with an error message in the payload, or vice versa. If a test asserts `400 Bad Request`, it will fail even if the server successfully rejected the invalid data. By decoupling them, we evaluate whether the business logic is sound separately from HTTP envelope conventions.

---

## 6. Side-Effect Assertions for Authorization Testing
- **Question:** *How do side-effect assertions detect broken access control?*
- **Answer:**
  - Many broken APIs return `403 Forbidden` in the UI but still execute the SQL query in the background, or conversely return `200 OK` while executing unauthorized actions.
  - In FR-12, when a non-admin caller sends `DELETE /api/admin/users/52`, we not only assert the response code, but we immediately follow up with a query verifying that User 52 **still exists** in the database. This dual-assertion pattern proved that standard users could actually delete accounts in this SUT (`DEF-FR12-01`).

---

## 7. Logical Test Cases vs HTTP Requests in Postman
- **Question:** *Why do 43 logical test cases produce 59 HTTP requests in FR-12?*
- **Answer:**
  - One logical test case design often requires multiple physical HTTP operations: a setup request to create an isolated probe entity, the primary test probe request, a side-effect verification query, and a teardown/cleanup request.

---

## 8. Major SUT Vulnerabilities Discovered (11 GitHub Issues)
- **Question:** *What were the most severe bugs found?*
- **Answer:**
  - **`DEF-FR01-01` (Issue #1):** Passwords stored in plaintext without bcrypt hashing (`SEC-01` violation).
  - **`DEF-FR07-01` (Issue #6):** Adding an existing item to cart creates a new row instead of incrementing quantity.
  - **`DEF-FR12-01` (Issue #8):** All `/api/admin/*` endpoints lack admin role checks; standard users can delete accounts and view all system orders.
  - **`DEF-FR12-02` (Issue #9):** Product mutations (`POST/PUT/DELETE /api/products`) completely lack authentication middleware; anonymous callers can wipe the public catalog.

---

## 9. CI/CD Architecture (Run A vs Run B)
- **Question:** *How is your GitHub Actions CI/CD structured?*
- **Answer:**
  - **Run A (Smoke / Health Run):** Runs 9 representative passing tests verifying backend startup, Newman execution, and `X-Student-Id` header injection.
  - **Run B (Intentional Failure Demo):** Runs an isolated test asserting a non-existent value to prove that the GitHub Actions quality gate fails and blocks deployment when a test fails.

---

## 10. Agent Skill Design Decisions
- **Question:** *How does your test generator work?*
- **Answer:**
  - It ingests an API specification and deterministically applies Equivalence Partitioning (nominal, omitted, type confusion) and Boundary Value Analysis (exact min, below min, max). For protected routes, it automatically synthesizes JWT security probes (`SEC-02`, `SEC-03`).

---

## 11. Ethical & Academic Integrity Disclosures
- **Question:** *How did you use AI ethically in this project?*
- **Answer:**
  - AI was used as a pair programmer and test case brainstormer. Every prompt and response is logged verbatim in `ai-audit.md`. External ChatGPT reference reviews are archived in `external-ai-transcripts/`. All test case verdicts and extension tests were audited and certified by the student. Real screenshots of Postman Console (`X-Student-Id`) and GitHub Issues were captured physically.
