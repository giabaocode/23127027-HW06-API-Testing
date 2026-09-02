# FR-12: Access Control — Human Audit Worksheet

> **Academic Integrity Notice & Student Ownership:**
> - **Auditor:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Source Test Suite:** `hw06/testcases/fr12/generated-ai-original.md` (38 AI-generated cases)
> - **Evaluation Rule:** Every AI-generated testcase must be independently evaluated by the student into one of three distinct verdicts:
>   - **VALID:** The testcase is logically sound, correctly mapped to FR-12/SEC-02/SEC-03, has realistic oracles, and is ready for execution.
>   - **INCOMPLETE:** The testcase has technical merit but requires calibrated headers, side-effect checks, or oracle corrections.
>   - **INVALID:** The testcase violates specification boundaries, tests out-of-scope functional logic, or targets nonexistent routes.
> - **Student Ownership Policy:** All student verdict, reasoning, and correction columns are initially completely **BLANK** to ensure honest human review without AI bias.

---

| Test ID | Coverage ID | Short Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| `FR12-AI-001` | `COV-FR12-02` | Standard user denied access to GET /api/admin/users | | | | |
| `FR12-AI-002` | `COV-FR12-04` | Standard user denied DELETE /api/admin/users/:id + user not deleted | | | | |
| `FR12-AI-003` | `COV-FR12-07` | Standard user denied access to GET /api/admin/orders | | | | |
| `FR12-AI-004` | `COV-FR12-09` | Standard user denied PUT /api/admin/orders/:id/status + status unchanged | | | | |
| `FR12-AI-005` | `COV-FR12-12` | Standard user denied POST /api/admin/import-products + catalog unmutated | | | | |
| `FR12-AI-006` | `COV-FR12-18` | Standard user denied POST /api/admin/coupons + coupon not created | | | | |
| `FR12-AI-007` | `COV-FR12-20` | Standard user denied DELETE /api/admin/coupons/:id + coupon not deleted | | | | |
| `FR12-AI-008` | `COV-FR12-22` | Standard user denied POST /api/products + product not created | | | | |
| `FR12-AI-009` | `COV-FR12-25` | Standard user denied PUT /api/products/:id + product unchanged | | | | |
| `FR12-AI-010` | `COV-FR12-28` | Standard user denied DELETE /api/products/:id + product not deleted | | | | |
| `FR12-AI-011` | `COV-FR12-30` | Standard user denied POST /api/categories + category not created | | | | |
| `FR12-AI-012` | `COV-FR12-32` | Standard user denied PUT /api/categories/:id + category unchanged | | | | |
| `FR12-AI-013` | `COV-FR12-33` | Standard user denied DELETE /api/categories/:id + category not deleted | | | | |
| `FR12-AI-014` | `COV-FR12-15` | Standard user denied access to GET /api/coupons | | | | |
| `FR12-AI-015` | `COV-FR12-03` | Admin authorized for GET /api/admin/users | | | | |
| `FR12-AI-016` | `COV-FR12-05` | Admin authorized for DELETE /api/admin/users/:id on disposable user | | | | |
| `FR12-AI-017` | `COV-FR12-08` | Admin authorized for GET /api/admin/orders | | | | |
| `FR12-AI-018` | `COV-FR12-10` | Admin authorized for PUT /api/admin/orders/:id/status | | | | |
| `FR12-AI-019` | `COV-FR12-13` | Admin authorized for POST /api/admin/import-products | | | | |
| `FR12-AI-020` | `COV-FR12-19` | Admin authorized for POST /api/admin/coupons | | | | |
| `FR12-AI-021` | `COV-FR12-21` | Admin authorized for DELETE /api/admin/coupons/:id on disposable coupon | | | | |
| `FR12-AI-022` | `COV-FR12-23` | Admin authorized for POST /api/products | | | | |
| `FR12-AI-023` | `COV-FR12-26` | Admin authorized for PUT /api/products/:id on disposable product | | | | |
| `FR12-AI-024` | `COV-FR12-27` | Admin authorized for DELETE /api/products/:id on disposable product | | | | |
| `FR12-AI-025` | `COV-FR12-31` | Admin authorized for POST /api/categories | | | | |
| `FR12-AI-026` | `COV-FR12-32` | Admin authorized for PUT /api/categories/:id on disposable category | | | | |
| `FR12-AI-027` | `COV-FR12-34` | Admin authorized for DELETE /api/categories/:id on disposable category | | | | |
| `FR12-AI-028` | `COV-FR12-16` | Admin authorized for GET /api/coupons | | | | |
| `FR12-AI-029` | `COV-FR12-21` | Anonymous denied POST /api/products + product not created | | | | |
| `FR12-AI-030` | `COV-FR12-24` | Anonymous denied PUT /api/products/:id + product unchanged | | | | |
| `FR12-AI-031` | `COV-FR12-27` | Anonymous denied DELETE /api/products/:id + product not deleted | | | | |
| `FR12-AI-032` | `COV-FR12-01` | Anonymous denied access to GET /api/admin/users | | | | |
| `FR12-AI-033` | `COV-FR12-29` | Anonymous denied POST /api/categories + category not created | | | | |
| `FR12-AI-034` | `COV-FR12-14` | Anonymous denied access to GET /api/coupons | | | | |
| `FR12-AI-035` | `COV-FR12-35` | Expired admin token denied GET /api/admin/users | | | | |
| `FR12-AI-036` | `COV-FR12-36` | Forged signature token denied GET /api/admin/orders | | | | |
| `FR12-AI-037` | `COV-FR12-37` | Missing role claim token denied POST /api/admin/coupons | | | | |
| `FR12-AI-038` | `COV-FR12-38` | Uppercase role 'ADMIN' denied DELETE /api/admin/users/:id | | | | |
