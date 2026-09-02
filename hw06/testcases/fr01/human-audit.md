# FR-01: Account Registration — Human Audit Worksheet

> **Notice to Student (Pham Ngoc Gia Bao - ID: `23127027`):**
> This worksheet is prepared for your mandatory independent human-in-the-loop review of the 38 AI-generated test cases for **FR-01 (Account Registration)**.
> - **Instructions:** For each test case, inspect the test design in [`generated-ai-original.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/generated-ai-original.md), judge its validity independently against the authoritative specifications, and personally fill in the four student fields.
> - **Allowed Student Verdicts:** `VALID` | `INVALID` | `INCOMPLETE`
> - **Academic Integrity Rule:** No AI review hints or suggested verdicts are provided. All student audit fields are initially empty.

---

## Human Audit Table

| Test ID | Coverage ID | Short Test Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **FR01-AI-001** | `COV-FR01-01` | Standard valid ASCII name registration | | | | |
| **FR01-AI-002** | `COV-FR01-02` | Vietnamese Unicode name with diacritics | | | | |
| **FR01-AI-003** | `COV-FR01-03` | Omitted mandatory name field rejection | | | | |
| **FR01-AI-004** | `COV-FR01-04` | Empty string name value rejection | | | | |
| **FR01-AI-005** | `COV-FR01-05` | Non-string integer name data type rejection | | | | |
| **FR01-AI-006** | `COV-FR01-06` | Extreme upper length name robustness (1000 chars) | | | | |
| **FR01-AI-007** | `COV-FR01-07` | Literal SQL syntax handling in name (SEC-05) | | | | |
| **FR01-AI-008** | `COV-FR01-08` | HTML script tag robustness probe in name | | | | |
| **FR01-AI-009** | `COV-FR01-09` | Standard valid RFC email format registration | | | | |
| **FR01-AI-010** | `COV-FR01-10` | Advanced RFC email with plus-addressing | | | | |
| **FR01-AI-011** | `COV-FR01-11` | Omitted mandatory email field rejection | | | | |
| **FR01-AI-012** | `COV-FR01-12` | Empty string email value rejection | | | | |
| **FR01-AI-013** | `COV-FR01-13` | Malformed email missing at-symbol (@) rejection | | | | |
| **FR01-AI-014** | `COV-FR01-13` | Malformed email missing domain part rejection | | | | |
| **FR01-AI-015** | `COV-FR01-14` | Non-string integer email data type rejection | | | | |
| **FR01-AI-016** | `COV-FR01-15` | Duplicate registration of pre-seeded email rejection | | | | |
| **FR01-AI-017** | `COV-FR01-15` | Duplicate registration via dynamic sequential call | | | | |
| **FR01-AI-018** | `COV-FR01-16` | Case-insensitive duplicate email rejection | | | | |
| **FR01-AI-019** | `COV-FR01-17` | SQL-like syntax handling in email (SEC-05) | | | | |
| **FR01-AI-020** | `COV-FR01-18` | Standard strong password meeting all 5 criteria | | | | |
| **FR01-AI-021** | `COV-FR01-19` | Documented special symbol coverage: at-sign (@) | | | | |
| **FR01-AI-022** | `COV-FR01-19` | Documented special symbol coverage: dollar-sign ($) | | | | |
| **FR01-AI-023** | `COV-FR01-19` | Documented special symbol coverage: ampersand (&) | | | | |
| **FR01-AI-024** | `COV-FR01-20` | Required special symbol plus extra symbol (!#) | | | | |
| **FR01-AI-025** | `COV-FR01-21` | Missing required special character from set rejection | | | | |
| **FR01-AI-026** | `COV-FR01-22` | Password length boundary: 7 chars (min - 1) rejection | | | | |
| **FR01-AI-027** | `COV-FR01-22` | Password length boundary: 8 chars (exact minimum) | | | | |
| **FR01-AI-028** | `COV-FR01-22` | Password length boundary: 9 chars (min + 1) | | | | |
| **FR01-AI-029** | `COV-FR01-23` | Missing uppercase letter in password rejection | | | | |
| **FR01-AI-030** | `COV-FR01-23` | Missing lowercase letter in password rejection | | | | |
| **FR01-AI-031** | `COV-FR01-23` | Missing numeric digit in password rejection | | | | |
| **FR01-AI-032** | `COV-FR01-24` | Empty string password value rejection | | | | |
| **FR01-AI-033** | `COV-FR01-25` | Non-string integer password data type rejection | | | | |
| **FR01-AI-034** | `COV-FR01-26` | Extreme upper length password robustness (128 chars) | | | | |
| **FR01-AI-035** | `COV-FR01-27` | Empty JSON body rejection | | | | |
| **FR01-AI-036** | `COV-FR01-28` | Unexpected extra field (confirmPassword) robustness | | | | |
| **FR01-AI-037** | `COV-FR01-29` | Password plaintext storage verification (SEC-01 DB inspection) | | | | |
| **FR01-AI-038** | `COV-FR01-30` | Security hardening: credential non-leakage in response | | | | |
