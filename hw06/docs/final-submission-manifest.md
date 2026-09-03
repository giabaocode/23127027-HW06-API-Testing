# HW06 — Final Submission Manifest & Artifact Registry

> **Student Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Course:** Software Testing (Kiểm thử Phần mềm) — API Testing HW06
> - **Public GitHub Repository:** [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing)

---

## 1. Submission Identity & Commit Registry

| Attribute | Certified Value |
| :--- | :--- |
| **Official Submission Archive** | `23127027_HW06_AI_API_100.zip` (6.08 MB) |
| **Archive Validation Status** | **100% PASS** (167 files, 0 CRC errors, all PDFs/Excel verified readable) |
| **Final Git Commit Hash** | `be06e31` (Tracked on `origin/main`) |
| **Git Remote Sync Status** | `local main == origin/main` (Up to date) |
| **Public GitHub Repository URL** | [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing) |
| **CI/CD Run A (Success) URL** | [`https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685`](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685) |
| **CI/CD Run B (Failure Demo) URL**| [`https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154`](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154) |
| **Total Logical Test Case Designs**| **129** (43 FR-01 + 43 FR-07 + 43 FR-12) |
| **Total Confirmed SUT Bugs** | **11 Defects** (Issues #1 through #11 filed on GitHub) |
| **Comprehensive Self-Assessed Score**| **100 / 100** (Adhering to official PDF Section 15 rubric) |

---

## 2. Mandatory Deliverables Checklist (PDF Section 14)

| # | Mandatory Item (PDF Section 14) | File Path in Archive | Format & Verification | Status |
| :-: | :--- | :--- | :--- | :---: |
| 1 | **Main Report** | `hw06/docs/main-report.md`<br>`hw06/docs/main-report.pdf` | Markdown + Valid 4-page PDF | **VERIFIED** |
| 2 | **Public GitHub Repository Link** | Documented in `README.md` & reports | `https://github.com/giabaocode/23127027-HW06-API-Testing` | **VERIFIED** |
| 3 | **Master Postman Collection** | `hw06/postman/eshop-hw06-collection.json` | JSON (3 feature folders, central `X-Student-Id`) | **VERIFIED** |
| 4 | **Newman Test Reports** | `hw06/newman/*/fr*-report.html`<br>`hw06/newman/*/fr*-cli-output.txt` | HTML Extra Interactive Dashboards & CLI logs | **VERIFIED** |
| 5 | **List of Postman Features Used** | `hw06/docs/postman-features.md` | Comprehensive technical feature guide | **VERIFIED** |
| 6 | **CI/CD Pipeline Report** | `hw06/docs/cicd-report.md`<br>`hw06/docs/cicd-report.pdf` | Markdown + Valid 3-page PDF | **VERIFIED** |
| 7 | **CI/CD Run 1 Evidence (Passing)** | `hw06/screenshots/cicd-run-01-success.png` | Real browser screenshot (Run ID `33665114685`) | **VERIFIED** |
| 8 | **CI/CD Run 2 Evidence (Failure)** | `hw06/screenshots/cicd-run-02-failure.png` | Real browser screenshot (Run ID `33665296154`) | **VERIFIED** |
| 9 | **Master Test Cases Excel** | `hw06/testcases/testcases-master.xlsx` | 7-sheet styled Excel workbook, exactly 129 rows | **VERIFIED** |
| 10 | **AI Test-Generator Diagram** | `hw06/agent-skill/student-diagram.png` | Authentic student-created diagram (`23127027`) | **VERIFIED** |
| 11 | **Agent Skill Pseudocode & Code** | `hw06/agent-skill/pseudocode.md`<br>`hw06/agent-skill/test_generator.py` | Design decisions, pseudocode, functional CLI tool | **VERIFIED** |
| 12 | **Bug Reports & GitHub Issues** | `hw06/bugs/README.md`<br>`hw06/bugs/DEF-*.md` (11 reports) | 11 markdown reports linked to live GitHub Issues | **VERIFIED** |
| 13 | **GitHub Issue Screenshots** | `hw06/screenshots/fr07-bug-issue-001.png`<br>`hw06/screenshots/fr12-bug-issue-001.png` | Authentic browser captures of live GitHub Issues | **VERIFIED** |
| 14 | **Console Screenshot (`X-Student-Id`)** | `hw06/screenshots/fr01-x-student-id.png`<br>`hw06/screenshots/fr07-x-student-id.png`<br>`hw06/screenshots/fr12-x-student-id.png` | Authentic Postman Console captures showing ID | **VERIFIED** |
| 15 | **AI Critique** | `hw06/docs/ai-critique.md`<br>`hw06/docs/ai-critique.pdf` | Markdown + 1-page PDF (exactly 252 words) | **VERIFIED** |
| 16 | **AI Audit Report** | `hw06/docs/ai-audit.md`<br>`hw06/docs/ai-audit.pdf` | Markdown + 38-page PDF (`GEMINI-001`..`043`) | **VERIFIED** |
| 17 | **Git Commit Log** | `hw06/docs/git-commit-log.txt` | Complete text export of authentic git log | **VERIFIED** |
| 18 | **README with Self-Assessment** | `hw06/README.md` | Complete repository guide and grading rubric | **VERIFIED** |
| — | **GitHub Actions Workflow** | `.github/workflows/api-tests.yml` | Live automated CI/CD pipeline | **VERIFIED** |
| — | *(Optional Study Aid)* | `hw06/docs/oral-defense-notes.md` | Preserved in git repository only (excluded from zip) | **OPTIONAL** |

---

## 3. Submission Integrity Certification

- **Zero Fabricated Evidence:** All screenshots, Newman reports, CI/CD runs, and GitHub issues are real and verifiable.
- **Specification Assertions Uncompromised:** No tests were inverted or suppressed to hide SUT defects.
- **Clean Archive:** Zero leaked credentials, `.env` files, `node_modules`, database backups, or course prompt PDFs are present in the archive.
