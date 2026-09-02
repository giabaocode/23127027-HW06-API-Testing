# FR-12: Access Control — Compact Human Review Sheet

> **Auditor:** Phạm Ngọc Gia Bảo (`23127027`) | **Total Cases:** 38 | **Student Verdicts:** PENDING REVIEW

| Test ID | Endpoint | Caller Identity | One-Sentence Condition | Requirement / Oracle | Student Final Verdict | Student Note |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `FR12-AI-001` | `GET /api/admin/users` | user | Standard user (role: 'user') calls GET /api/admin/users | Semantic access denied (SEC-03); 403 (Inferred) | | |
| `FR12-AI-002` | `DELETE /api/admin/users/:id` | user | Standard user calls DELETE /api/admin/users/:id on disposable user | Semantic access denied (SEC-03); target user not deleted | | |
| `FR12-AI-003` | `GET /api/admin/orders` | user | Standard user calls GET /api/admin/orders | Semantic access denied (SEC-03); zero foreign order data exposed | | |
| `FR12-AI-004` | `PUT /api/admin/orders/:id/status` | user | Standard user calls PUT /api/admin/orders/:id/status with body status: 'delivered' | Semantic access denied (SEC-03); order status remains 'pending' | | |
| `FR12-AI-005` | `POST /api/admin/import-products` | user | Standard user calls POST /api/admin/import-products with product array | Semantic access denied (SEC-03); product not inserted into catalog | | |
| `FR12-AI-006` | `POST /api/admin/coupons` | user | Standard user calls POST /api/admin/coupons with coupon payload | Semantic access denied (SEC-03); coupon code not stored | | |
| `FR12-AI-007` | `DELETE /api/admin/coupons/:id` | user | Standard user calls DELETE /api/admin/coupons/:id on disposable coupon | Semantic access denied (SEC-03); coupon remains intact in database | | |
| `FR12-AI-008` | `POST /api/products` | user | Standard user calls POST /api/products with product payload | Semantic access denied (SEC-03); product not added to catalog | | |
| `FR12-AI-009` | `PUT /api/products/:id` | user | Standard user calls PUT /api/products/:id with altered price | Semantic access denied (SEC-03); product attributes unchanged | | |
| `FR12-AI-010` | `DELETE /api/products/:id` | user | Standard user calls DELETE /api/products/:id on disposable product | Semantic access denied (SEC-03); product still exists in catalog | | |
| `FR12-AI-011` | `POST /api/categories` | user | Standard user calls POST /api/categories with category name | Semantic access denied (SEC-03); category not created in database | | |
| `FR12-AI-012` | `PUT /api/categories/:id` | user | Standard user calls PUT /api/categories/:id with new name | Semantic access denied (SEC-03); category name remains unchanged | | |
| `FR12-AI-013` | `DELETE /api/categories/:id` | user | Standard user calls DELETE /api/categories/:id on disposable category | Semantic access denied (SEC-03); category still exists in database | | |
| `FR12-AI-014` | `GET /api/coupons` | user | Standard user calls GET /api/coupons | Semantic access denied (SEC-03); coupon master list not exposed | | |
| `FR12-AI-015` | `GET /api/admin/users` | admin | Admin user (role: 'admin') calls GET /api/admin/users | AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred) | | |
| `FR12-AI-016` | `DELETE /api/admin/users/:id` | admin | Admin calls DELETE /api/admin/users/:id on disposable user | AUTHORIZED (Not blocked by SEC-02/03); disposable user deleted | | |
| `FR12-AI-017` | `GET /api/admin/orders` | admin | Admin calls GET /api/admin/orders | AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred) | | |
| `FR12-AI-018` | `PUT /api/admin/orders/:id/status` | admin | Admin calls PUT /api/admin/orders/:id/status with valid status | AUTHORIZED (Not blocked by SEC-02/03); order status updated | | |
| `FR12-AI-019` | `POST /api/admin/import-products` | admin | Admin calls POST /api/admin/import-products with valid payload | AUTHORIZED (Not blocked by SEC-02/03); products imported | | |
| `FR12-AI-020` | `POST /api/admin/coupons` | admin | Admin calls POST /api/admin/coupons with valid coupon payload | AUTHORIZED (Not blocked by SEC-02/03); coupon created | | |
| `FR12-AI-021` | `DELETE /api/admin/coupons/:id` | admin | Admin calls DELETE /api/admin/coupons/:id on disposable coupon | AUTHORIZED (Not blocked by SEC-02/03); disposable coupon deleted | | |
| `FR12-AI-022` | `POST /api/products` | admin | Admin calls POST /api/products with valid product body | AUTHORIZED (Not blocked by SEC-02/03); product created | | |
| `FR12-AI-023` | `PUT /api/products/:id` | admin | Admin calls PUT /api/products/:id on disposable product | AUTHORIZED (Not blocked by SEC-02/03); product updated | | |
| `FR12-AI-024` | `DELETE /api/products/:id` | admin | Admin calls DELETE /api/products/:id on disposable product | AUTHORIZED (Not blocked by SEC-02/03); disposable product deleted | | |
| `FR12-AI-025` | `POST /api/categories` | admin | Admin calls POST /api/categories with valid category body | AUTHORIZED (Not blocked by SEC-02/03); category created | | |
| `FR12-AI-026` | `PUT /api/categories/:id` | admin | Admin calls PUT /api/categories/:id on disposable category | AUTHORIZED (Not blocked by SEC-02/03); category updated | | |
| `FR12-AI-027` | `DELETE /api/categories/:id` | admin | Admin calls DELETE /api/categories/:id on disposable category | AUTHORIZED (Not blocked by SEC-02/03); disposable category deleted | | |
| `FR12-AI-028` | `GET /api/coupons` | admin | Admin calls GET /api/coupons | AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred) | | |
| `FR12-AI-029` | `POST /api/products` | None | Anonymous caller calls POST /api/products with product payload | Semantic access denied (SEC-02); 401 (Inferred); product not created | | |
| `FR12-AI-030` | `PUT /api/products/:id` | None | Anonymous caller calls PUT /api/products/:id on disposable product | Semantic access denied (SEC-02); 401 (Inferred); product unchanged | | |
| `FR12-AI-031` | `DELETE /api/products/:id` | None | Anonymous caller calls DELETE /api/products/:id on disposable product | Semantic access denied (SEC-02); 401 (Inferred); product not deleted | | |
| `FR12-AI-032` | `GET /api/admin/users` | None | Anonymous caller calls GET /api/admin/users | Semantic access denied (SEC-02); 401 (Inferred); zero user data exposed | | |
| `FR12-AI-033` | `POST /api/categories` | None | Anonymous caller calls POST /api/categories without token | Semantic access denied (SEC-02); 401 (Inferred); category not inserted | | |
| `FR12-AI-034` | `GET /api/coupons` | None | Anonymous caller calls GET /api/coupons without token | Semantic access denied (SEC-02); 401 (Inferred); zero coupon data exposed | | |
| `FR12-AI-035` | `GET /api/admin/users` | admin | Expired admin token (exp < now) sent to GET /api/admin/users | Semantic access denied (SEC-02); 403 (Inferred); expired token rejected | | |
| `FR12-AI-036` | `GET /api/admin/orders` | admin (claimed in payload) | Forged signature token sent to GET /api/admin/orders | Semantic access denied (SEC-02); 403 (Inferred); forged signature rejected | | |
| `FR12-AI-037` | `POST /api/admin/coupons` | None (Omitted claim) | Valid JWT omitting 'role' claim sent to POST /api/admin/coupons | Semantic access denied (SEC-03); coupon not created | | |
| `FR12-AI-038` | `DELETE /api/admin/users/:id` | ADMIN (Uppercase) | Token with uppercase role: 'ADMIN' sent to DELETE /api/admin/users/:id | Semantic access denied (SEC-03); user not deleted | | |
