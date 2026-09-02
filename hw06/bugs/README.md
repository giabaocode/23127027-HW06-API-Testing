# FR-01 Defect Register & Bug Index

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Target Feature:** FR-01 — Account Registration (`POST /api/register`)
> - **Repository:** `giabaocode/23127027-HW06-API-Testing`

---

## Confirmed SUT Defects Summary

All defects listed below have been **reproduced and confirmed via real runtime execution** against the local SUT (`http://localhost:3000`) using Newman v6.2.2 and standalone SQLite database verification.

| Defect ID | GitHub Issue | Severity | Category | Requirement Trace | Summary | Failing Test Cases | Detailed Report |
| :---: | :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **`DEF-FR01-01`** | [#1](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/1) | **Critical** | Security Storage | `SEC-01` | User passwords stored as plaintext in SQLite without hashing | `FR01-AI-037` | [`DEF-FR01-01.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR01-01.md) |
| **`DEF-FR01-02`** | [#2](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/2) | **High** | Data Integrity | `FR-01` | Duplicate email registration permitted with HTTP 200 OK | `FR01-AI-016`, `FR01-AI-017` | [`DEF-FR01-02.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR01-02.md) |
| **`DEF-FR01-03`** | [#3](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/3) | **High** | Password Policy | `FR-01` | Password complexity policy completely unenforced | `FR01-AI-025`, `026`, `029`, `030`, `031` | [`DEF-FR01-03.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR01-03.md) |
| **`DEF-FR01-04`** | [#4](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/4) | **High** | Input Validation | `FR-01` | Missing mandatory fields (`name`, `email`, `password`) accepted with HTTP 200 OK | `FR01-AI-003`, `004`, `011`, `012`, `032`, `035` | [`DEF-FR01-04.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR01-04.md) |
| **`DEF-FR01-05`** | [#5](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/5) | **Medium** | Input Validation | `FR-01` | Syntactically malformed emails missing `@` or domain accepted with HTTP 200 OK | `FR01-AI-013`, `FR01-AI-014` | [`DEF-FR01-05.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR01-05.md) |
