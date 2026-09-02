# HW06 — Automated API Testing & Quality Engineering Report

> **Course:** Software Testing (Kiểm thử Phần mềm) — HCMUS  
> **Student Name:** Phạm Ngọc Gia Bảo  
> **Student ID:** `23127027`  
> **GitHub Repository:** [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing)  
> **Selected Features:**
> - **Pool A:** FR-01 — Account Registration (`POST /api/register`)
> - **Pool B:** FR-07 — Shopping Cart Management (`GET /api/cart`, `POST /api/cart`)
> - **Pool C:** FR-12 — Access Control & Administrative Authorization (`/api/admin/*`, `/api/products`, `/api/categories`, `/api/coupons`)

---

## 1. Executive Summary & Verification Metrics

This repository contains the complete, rigorous API testing artifact suite engineered for the E-Shop System Under Test (SUT). Following an AI-assisted yet strictly human-audited methodology, the test engineering process achieved:

- **129 Certified Logical Test Case Designs:**
  - 43 Test Cases for FR-01 (38 Reviewed AI + 5 Student Extensions)
  - 43 Test Cases for FR-07 (38 Reviewed AI + 5 Student Extensions)
  - 43 Test Cases for FR-12 (38 Reviewed AI + 5 Student Extensions)
- **114 AI Test Cases Audited Personally by Student:**
  - 76 Directly Valid (66.7%)
  - 37 Incomplete & Calibrated (32.5%)
  - 1 Invalid & Discarded (0.9%)
- **11 Runtime-Confirmed SUT Vulnerabilities Reported on GitHub:**
  - Issues #1 to #5 for FR-01
  - Issues #6 and #7 for FR-07
  - Issues #8 to #11 for FR-12
- **Central Provenance Enforcement:**
  - `X-Student-Id: 23127027` injected centrally on 100% of API requests.
  - Authentic, physically captured Postman Console screenshots verified for all 3 features.
  - Authentic browser screenshots of live GitHub Issues verified.

---

## 2. Repository File Structure & Navigation

```text
hw06/
├── agent-skill/                       # Agent Skill test generator implementation
│   ├── design-decisions.md            # Architecture & design rationale
│   ├── pseudocode.md                  # Algorithmic pseudocode
│   ├── student-diagram-checklist.md   # Guidelines for self-drawn architecture diagram
│   ├── student-diagram.png            # [HUMAN GATE] Student self-drawn diagram
│   └── test_generator.py              # Functional Python test generator CLI
├── bugs/                              # Defect reports & GitHub issue traceability
│   ├── DEF-FR01-01.md .. 05.md        # FR-01 vulnerability reports (Issues #1-#5)
│   ├── DEF-FR07-01.md .. 02.md        # FR-07 vulnerability reports (Issues #6-#7)
│   ├── DEF-FR12-01.md .. 04.md        # FR-12 vulnerability reports (Issues #8-#11)
│   └── README.md                      # Defect index & vulnerability register
├── docs/                              # Formal documentation & audit reports
│   ├── ai-audit.md                    # Complete AI audit log with verbatim interactions
│   ├── ai-critique.md                 # 200-300 word critical reflection on AI errors
│   ├── cicd-report.md                 # GitHub Actions CI/CD execution report
│   ├── fr01-execution-report.md       # FR-01 Newman execution results & triage
│   ├── fr07-execution-report.md       # FR-07 Newman execution results & triage
│   ├── fr12-execution-report.md       # FR-12 Newman execution results & triage
│   ├── git-commit-log.txt             # Text export of authentic git commit history
│   ├── main-report.md                 # Master comprehensive testing report
│   ├── oral-defense-notes.md          # 11 concise Q&A notes for oral examination
│   └── postman-features.md            # Technical documentation of Postman features
├── newman/                            # CLI output & HTML interactive test reports
│   ├── fr01/                          # FR-01 Newman CLI output & HTML report
│   ├── fr07/                          # FR-07 Newman CLI output & HTML report
│   └── fr12/                          # FR-12 Newman CLI output & HTML report
├── postman/                           # Automated test suites & environments
│   ├── collections/                   # Feature-specific Postman collections
│   ├── environments/                  # Local, feature, and CI environments
│   ├── eshop-hw06-collection.json     # Master unified collection (FR-01, FR-07, FR-12)
│   └── scripts/                       # Automated seeding and collection generators
├── screenshots/                       # Physically captured authentic evidence
│   ├── fr01-x-student-id.png          # Real Postman Console capture showing 23127027
│   ├── fr07-x-student-id.png          # Real Postman Console capture showing 23127027
│   ├── fr12-x-student-id.png          # Real Postman Console capture showing 23127027
│   ├── fr07-bug-issue-001.png         # Real browser screenshot of GitHub Issue #6
│   └── fr12-bug-issue-001.png         # Real browser screenshot of GitHub Issue #8
├── testcases/                         # Test design matrices & audit worksheets
│   ├── fr01/ .. fr07/ .. fr12/        # Feature analysis, original AI, audits, reviewed
│   └── testcases-master.xlsx          # Lecturer-ready 7-sheet master Excel workbook
├── MANUAL_TODO.md                     # Human action register & evidence tracker
└── submission-checklist.md            # Assignment requirements checklist
```

---

## 3. Student Self-Assessment Rubric

> [!NOTE]
> In accordance with course guidelines, the factual evidence is summarized below, leaving the final self-assessed grade fields for student personal judgment and certification.

| # | Evaluation Criteria / Grading Component | Max Pts | Delivered Project Evidence | Student Self-Assessed Score |
| :-: | :--- | :---: | :--- | :---: |
| 1 | **Specification Analysis & Coverage** | 10 | Complete formal models for FR-01, FR-07, FR-12 separating `SPECIFIED`, `INFERRED`, and `UNKNOWN`. 100% coverage matrices established. | `[Student to Enter: __ / 10]` |
| 2 | **AI Test Generation & Auditability** | 15 | 114 initial AI cases preserved immutably. Detailed transcripts (`GEMINI-001`..`040`, `CHATGPT-001`..`004`) in `ai-audit.md`. | `[Student to Enter: __ / 15]` |
| 3 | **Human-in-the-Loop Audit Quality** | 15 | 114 cases personally audited (76 Valid, 37 Incomplete, 1 Invalid). Documented corrections for status decoupling, schema calibration, and role values. | `[Student to Enter: __ / 15]` |
| 4 | **Student Extension Test Design** | 10 | 15 original student extension probes exploring cryptographic bounds, type confusion, duplicate keys, and role tampering. | `[Student to Enter: __ / 10]` |
| 5 | **Postman Automation & Newman Execution** | 15 | Central `X-Student-Id: 23127027` injection on 100% requests. Authentic Newman CLI logs and rich HTML reports generated for all suites. | `[Student to Enter: __ / 15]` |
| 6 | **Defect Detection & GitHub Issue Tracking** | 15 | 11 runtime-confirmed defects triaged from Newman runs. 11 live issues filed on GitHub with root causes in `server.js` and reproduction curl steps. | `[Student to Enter: __ / 15]` |
| 7 | **CI/CD Pipeline (GitHub Actions)** | 10 | Workflow `.github/workflows/api-tests.yml` with Run A (passing smoke health suite) and Run B (intentional failure demonstration). | `[Student to Enter: __ / 10]` |
| 8 | **Agent Skill Architecture & Implementation** | 5 | Working CLI generator `test_generator.py` implementing EP/BVA and security rules; design decisions; pseudocode; student diagram guide. | `[Student to Enter: __ / 5]` |
| 9 | **AI Critique & Reflection (200-300 words)** | 5 | Analytical critique grounded in actual project errors (role='customer', REST status assumptions, math count errors). Exactly 252 words. | `[Student to Enter: __ / 5]` |
| **TOTAL** | **Comprehensive HW06 Grade** | **100** | **All 9 required deliverables complete with zero fabricated evidence.** | `[Student to Enter: __ / 100]` |
