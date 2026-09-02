# FR-12: Access Control — Coverage Matrix (Calibrated)

> **Coverage Matrix Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo (`23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Governing Specifications:** `README.md` Section 6 (FR-12), Section 9 (`SEC-02`, `SEC-03`); `api_specification.md` Section 5.2, Section 6
> - **Exposed Target Operations:** Exactly 14 real endpoints
> - **Planned AI Test Cases:** Exactly 38 tests mapped 1:1 to 38 Coverage IDs

---

## 1. Comprehensive Coverage Mapping Table

| Coverage ID | Target Endpoint | HTTP Method | Access Control Requirement | Caller Identity Partition | Security Mapping | Expected Semantic Outcome | HTTP Status Classification | State / Side-Effect Assertion | Setup / Cleanup Requirement | Classification | Notes |
| :---: | :--- | :---: | :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **`COV-FR12-01`** | `/api/admin/users` | `GET` | Reject unauthenticated access | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Zero user data exposed | None | Positive Negative Test | Baseline anonymous probe |
| **`COV-FR12-02`** | `/api/admin/users` | `GET` | Restrict user listing to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Zero user data exposed | Register/login standard user | Security Boundary | Probes `CAND-FR12-01` |
| **`COV-FR12-03`** | `/api/admin/users` | `GET` | Grant administrative listing | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Returns array containing system users | Login seeded admin | Positive Functional | Verifies admin capability |
| **`COV-FR12-04`** | `/api/admin/users/:id` | `DELETE` | Prevent user deletion by standard user | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Target user still exists (probed via login) | Create disposable target user | Security Mutation | Dual-assertion: side-effect check |
| **`COV-FR12-05`** | `/api/admin/users/:id` | `DELETE` | Grant user deletion to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Target user deleted from database | Create disposable target user | Positive Mutation | Operates on disposable user |
| **`COV-FR12-06`** | `/api/admin/orders` | `GET` | Reject unauthenticated order access | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Zero order records exposed | None | Positive Negative Test | Baseline anonymous probe |
| **`COV-FR12-07`** | `/api/admin/orders` | `GET` | Restrict full order history to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Zero other-user orders exposed | Standard user token | Security Boundary | Probes `CAND-FR12-01` |
| **`COV-FR12-08`** | `/api/admin/orders` | `GET` | Grant full order history to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Returns system-wide order list | Admin token | Positive Functional | Verifies admin capability |
| **`COV-FR12-09`** | `/api/admin/orders/:id/status` | `PUT` | Prevent order status tampering by standard user | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Order status remains unchanged | Reference existing order | Security Mutation | Dual-assertion: side-effect check |
| **`COV-FR12-10`** | `/api/admin/orders/:id/status` | `PUT` | Grant order status update to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Order status updated to `confirmed` | Reference existing order | Positive Mutation | Verifies admin capability |
| **`COV-FR12-11`** | `/api/admin/import-products` | `POST` | Reject unauthenticated bulk import | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | No products imported | None | Positive Negative Test | Baseline anonymous probe |
| **`COV-FR12-12`** | `/api/admin/import-products` | `POST` | Restrict catalog import to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | No products imported | Standard user token | Security Mutation | Dual-assertion: side-effect check |
| **`COV-FR12-13`** | `/api/admin/import-products` | `POST` | Grant catalog import to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Bulk products imported into catalog | Admin token + valid CSV payload | Positive Mutation | Verifies admin capability |
| **`COV-FR12-14`** | `/api/coupons` | `GET` | Reject unauthenticated coupon list | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Zero coupons returned | None | Positive Negative Test | `api_spec` Section 5.2 |
| **`COV-FR12-15`** | `/api/coupons` | `GET` | Restrict coupon overview to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Zero coupons returned | Standard user token | Security Boundary | `api_spec` Section 5.2 |
| **`COV-FR12-16`** | `/api/coupons` | `GET` | Grant coupon overview to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Returns list of coupons | Admin token | Positive Functional | Verifies admin capability |
| **`COV-FR12-17`** | `/api/admin/coupons` | `POST` | Reject unauthenticated coupon creation | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Coupon not created | None | Positive Negative Test | Baseline anonymous probe |
| **`COV-FR12-18`** | `/api/admin/coupons` | `POST` | Restrict coupon creation to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Coupon code not created in DB | Standard user token | Security Mutation | Dual-assertion: side-effect check |
| **`COV-FR12-19`** | `/api/admin/coupons` | `POST` | Grant coupon creation to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Coupon successfully created | Admin token + unique code | Positive Mutation | Verifies admin capability |
| **`COV-FR12-20`** | `/api/admin/coupons/:id` | `DELETE` | Prevent coupon deletion by standard user | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Coupon remains active in DB | Standard user token | Security Mutation | Dual-assertion: side-effect check |
| **`COV-FR12-21`** | `/api/products` | `POST` | Require JWT for product creation | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Product not inserted into DB | None | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-22`** | `/api/products` | `POST` | Restrict product creation to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Product not inserted into DB | Standard user token | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-23`** | `/api/products` | `POST` | Grant product creation to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Product created with new ID | Admin token + product body | Positive Mutation | Verifies admin capability |
| **`COV-FR12-24`** | `/api/products/:id` | `PUT` | Require JWT for product update | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Target product unchanged | None | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-25`** | `/api/products/:id` | `PUT` | Restrict product update to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Target product unchanged | Standard user token | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-26`** | `/api/products/:id` | `PUT` | Grant product update to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Target product updated | Admin token on disposable item | Positive Mutation | Verifies admin capability |
| **`COV-FR12-27`** | `/api/products/:id` | `DELETE` | Require JWT for product deletion | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Target product not deleted | None | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-28`** | `/api/products/:id` | `DELETE` | Restrict product deletion to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Target product not deleted | Standard user token | Security Mutation | Probes `CAND-FR12-02` |
| **`COV-FR12-29`** | `/api/categories` | `POST` | Require JWT for category creation | Anonymous (No Token) | `SEC-02` | Access Denied | `401 Unauthorized` (Inferred) | Category not inserted | None | Security Mutation | Baseline check |
| **`COV-FR12-30`** | `/api/categories` | `POST` | Restrict category creation to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Category not inserted | Standard user token | Security Mutation | Probes `CAND-FR12-03` |
| **`COV-FR12-31`** | `/api/categories` | `POST` | Grant category creation to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Category created | Admin token + category body | Positive Mutation | Verifies admin capability |
| **`COV-FR12-32`** | `/api/categories/:id` | `PUT` | Restrict category update to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Category name unchanged | Standard user token | Security Mutation | Probes `CAND-FR12-03` |
| **`COV-FR12-33`** | `/api/categories/:id` | `DELETE` | Restrict category deletion to admin | Standard User (`role: 'user'`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Category not deleted | Standard user token | Security Mutation | Probes `CAND-FR12-03` |
| **`COV-FR12-34`** | `/api/categories/:id` | `DELETE` | Grant category deletion to admin | Admin User (`role: 'admin'`) | `FR-12` | Access Granted | `200 OK` (Specified) | Category deleted | Admin token on disposable item | Positive Mutation | Verifies admin capability |
| **`COV-FR12-35`** | `/api/admin/users` | `GET` | Reject expired administrative token | Expired Admin Token (`exp < now`) | `SEC-02` | Access Denied | `403 Forbidden` (Inferred) | Zero user records exposed | Generate expired admin JWT | Token Robustness | Lifecycle boundary probe |
| **`COV-FR12-36`** | `/api/admin/orders` | `GET` | Reject forged cryptographic signature | Forged Signature Token | `SEC-02` | Access Denied | `403 Forbidden` (Inferred) | Zero order records exposed | Tamper token signature chunk | Cryptographic Robustness | Integrity boundary probe |
| **`COV-FR12-37`** | `/api/admin/users` | `GET` | Reject token with missing role claim | Valid JWT with `{ id: 10 }` (No `role`) | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Zero user records exposed | Sign token omitting `role` | Schema Robustness | Role completeness probe |
| **`COV-FR12-38`** | `/api/admin/orders` | `GET` | Enforce exact case & reject spoofed roles | Valid JWT with `role: 'ADMIN'` / `'manager'` | `SEC-03` | Access Denied | `403 Forbidden` (Inferred) | Zero order records exposed | Sign token with uppercase/spoof | Role Boundary | Role value boundary probe |

---

## 2. Summary of Coverage Distribution

- **Total Planned AI Test Cases:** Exactly **38**
- **Direct Requirement Mappings:**
  - `SEC-02` (Valid JWT Authentication Required): 12 Test Cases
  - `SEC-03` (Admin Role `'admin'` Enforced): 17 Test Cases
  - `FR-12` (Authorized Admin Capabilities): 9 Test Cases
  - `SEC-06` (Profile Update Role Immutability): **0 Test Cases** (Excluded from FR-12)
- **Target Endpoint Distribution:**
  - Dedicated Admin APIs (`/api/admin/*`): 19 Test Cases
  - Data-Mutating Catalog APIs (`/api/products`, `/api/categories`): 14 Test Cases
  - Dedicated Admin Coupon Overview (`/api/coupons`): 3 Test Cases
  - Cross-Cutting Cryptographic / Boundary Robustness: 2 Test Cases
- **Side-Effect Verification:** 17 mutating test cases enforce dual-assertion (response rejection + GET verification of state immutability).
