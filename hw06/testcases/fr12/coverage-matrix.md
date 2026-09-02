# FR-12: Access Control — Coverage Matrix

> **Coverage Matrix Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo (`23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Governing Specifications:** `README.md` Section 6 (FR-12), Section 9 (`SEC-02`, `SEC-03`); `api_specification.md` Section 6

---

## 1. Coverage Dimension Mapping

| Coverage ID | Target Area / Endpoint | Subject Identity Condition | Method | Expected Semantic Outcome | Requirement Trace |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **`COV-FR12-01`** | `/api/admin/users` | Anonymous (No Token) | `GET` | Denied | `SEC-02` |
| **`COV-FR12-02`** | `/api/admin/users` | Customer Token (`role: customer`) | `GET` | Denied | `SEC-03` |
| **`COV-FR12-03`** | `/api/admin/users` | Admin Token (`role: admin`) | `GET` | Authorized (200 OK) | `FR-12` |
| **`COV-FR12-04`** | `/api/admin/users/:id` | Anonymous (No Token) | `DELETE` | Denied | `SEC-02` |
| **`COV-FR12-05`** | `/api/admin/users/:id` | Customer Token (`role: customer`) | `DELETE` | Denied | `SEC-03` |
| **`COV-FR12-06`** | `/api/admin/users/:id` | Admin Token (`role: admin`) | `DELETE` | Authorized | `FR-12` |
| **`COV-FR12-07`** | `/api/admin/orders` | Anonymous (No Token) | `GET` | Denied | `SEC-02` |
| **`COV-FR12-08`** | `/api/admin/orders` | Customer Token (`role: customer`) | `GET` | Denied | `SEC-03` |
| **`COV-FR12-09`** | `/api/admin/orders` | Admin Token (`role: admin`) | `GET` | Authorized (200 OK) | `FR-12` |
| **`COV-FR12-10`** | `/api/admin/orders/:id/status` | Anonymous (No Token) | `PUT` | Denied | `SEC-02` |
| **`COV-FR12-11`** | `/api/admin/orders/:id/status` | Customer Token (`role: customer`) | `PUT` | Denied | `SEC-03` |
| **`COV-FR12-12`** | `/api/admin/orders/:id/status` | Admin Token (`role: admin`) | `PUT` | Authorized | `FR-12` |
| **`COV-FR12-13`** | `/api/admin/import-products` | Anonymous (No Token) | `POST` | Denied | `SEC-02` |
| **`COV-FR12-14`** | `/api/admin/import-products` | Customer Token (`role: customer`) | `POST` | Denied | `SEC-03` |
| **`COV-FR12-15`** | `/api/admin/import-products` | Admin Token (`role: admin`) | `POST` | Authorized | `FR-12` |
| **`COV-FR12-16`** | `/api/admin/coupons` | Anonymous (No Token) | `POST` | Denied | `SEC-02` |
| **`COV-FR12-17`** | `/api/admin/coupons` | Customer Token (`role: customer`) | `POST` | Denied | `SEC-03` |
| **`COV-FR12-18`** | `/api/admin/coupons` | Admin Token (`role: admin`) | `POST` | Authorized | `FR-12` |
| **`COV-FR12-19`** | `/api/admin/coupons/:id` | Anonymous (No Token) | `DELETE` | Denied | `SEC-02` |
| **`COV-FR12-20`** | `/api/admin/coupons/:id` | Customer Token (`role: customer`) | `DELETE` | Denied | `SEC-03` |
| **`COV-FR12-21`** | `/api/admin/coupons/:id` | Admin Token (`role: admin`) | `DELETE` | Authorized | `FR-12` |
| **`COV-FR12-22`** | `/api/products` (Create) | Anonymous (No Token) | `POST` | Denied | `SEC-02` / `FR-12` |
| **`COV-FR12-23`** | `/api/products` (Create) | Customer Token (`role: customer`) | `POST` | Denied | `SEC-03` / `FR-12` |
| **`COV-FR12-24`** | `/api/products` (Create) | Admin Token (`role: admin`) | `POST` | Authorized | `FR-12` |
| **`COV-FR12-25`** | `/api/products/:id` (Update/Del) | Anonymous (No Token) | `PUT`/`DELETE` | Denied | `SEC-02` / `FR-12` |
| **`COV-FR12-26`** | `/api/products/:id` (Update/Del) | Customer Token (`role: customer`) | `PUT`/`DELETE` | Denied | `SEC-03` / `FR-12` |
| **`COV-FR12-27`** | `/api/products/:id` (Update/Del) | Admin Token (`role: admin`) | `PUT`/`DELETE` | Authorized | `FR-12` |
| **`COV-FR12-28`** | `/api/categories` (Mutation) | Anonymous (No Token) | `POST`/`PUT`/`DELETE` | Denied | `SEC-02` / `FR-12` |
| **`COV-FR12-29`** | `/api/categories` (Mutation) | Customer Token (`role: customer`) | `POST`/`PUT`/`DELETE` | Denied | `SEC-03` / `FR-12` |
| **`COV-FR12-30`** | `/api/categories` (Mutation) | Admin Token (`role: admin`) | `POST`/`PUT`/`DELETE` | Authorized | `FR-12` |
| **`COV-FR12-31`** | Token Integrity Probes | Forged Signature / Tampered Payload | All Methods | Denied | `SEC-02` |
| **`COV-FR12-32`** | Token Lifecycle Probes | Expired JWT Token | Admin Endpoints | Denied | `SEC-02` |
| **`COV-FR12-33`** | Role Scheme Probes | Missing / Null / Empty Role Claim | Admin Endpoints | Denied | `SEC-03` |
| **`COV-FR12-34`** | Role Value Boundary | Case Sensitivity / Arbitrary Role String | Admin Endpoints | Denied | `SEC-03` |

---

## 2. Planned Test Allocation Target (Phase 2)

- Minimum Requirement: $\ge 35$ AI test cases.
- Planned Allocation: Exactly **38 AI test cases** across the 34 Coverage IDs to ensure comprehensive coverage across all administrative and data-mutating endpoints.
