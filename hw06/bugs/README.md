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

---

## FR-07 (Shopping Cart) Defect Index

| Defect ID | GitHub Issue | Severity | Category | Requirement Trace | Summary | Failing Test Cases | Detailed Report |
| :---: | :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **`DEF-FR07-01`** / `FR07-BUG-001` | [#6](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/6) | **High** | Business Logic | `FR-07` (`README.md` L96) | Duplicate product addition appends separate row instead of accumulating quantity | `FR07-AI-009`, `010`, `011`, `FR07-STU-004` | [`DEF-FR07-01.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR07-01.md)<br>[`FR07-BUG-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/fr07/FR07-BUG-001-duplicate-product-accumulation.md) |
| **`DEF-FR07-02`** / `FR07-BUG-002` | [#7](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/7) | **High** | Input Validation | `FR-07` (`README.md` L86) | `POST /api/cart` accepts invalid, negative, zero, and fractional quantities with HTTP 200 | `FR07-AI-014`..`018`, `020`, `021`, `023`, `024` | [`DEF-FR07-02.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/DEF-FR07-02.md)<br>[`FR07-BUG-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/fr07/FR07-BUG-002-missing-quantity-validation.md) |
