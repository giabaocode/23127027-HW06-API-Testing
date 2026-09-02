# FR-07: Shopping Cart — Test Coverage Matrix (Audited & Grounded Version)

> **Document Information:**
> - **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> - **Target Endpoints:** `GET /api/cart`, `POST /api/cart`
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`

---

## Traceability & Coverage Matrix

| Coverage ID | Endpoint | Requirement | Source | Classification | Partition / State | Expected Semantic Oracle | HTTP Status Classification | Security Dimension | Schema Dimension | Notes |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **COV-FR07-01** | `GET /api/cart` | Retrieve empty cart | `README.md` L100 | **`INFERRED`** | $P_{E1}$ (Empty cart) | Returns empty JSON array `[]` | **`INFERRED`** (200 OK) | `SEC-02` | Array | Baseline state for newly created user |
| **COV-FR07-02** | `GET /api/cart` | Retrieve populated cart | `api_specification.md` L115 | **`INFERRED`** | $P_{E2}$ (1 item) | Returns array of cart item objects | **`INFERRED`** (200 OK) | `SEC-02` | Array of Objects | Verifies cart retains added item |
| **COV-FR07-03** | `GET /api/cart` | Unauthenticated retrieval | `api_specification.md` L112 | **`SPECIFIED REJECTION`** | $P_{A2}$ (Missing token) | Access blocked; cart not exposed | **`INFERRED FROM MIDDLEWARE`** (401) | `SEC-02` | Error Object | Enforces authentication barrier per SEC-02 |
| **COV-FR07-04** | `GET /api/cart` | Invalid JWT token | `api_specification.md` L112 | **`SPECIFIED REJECTION`** | $P_{A3}$ (Invalid token) | Access blocked; token rejected | **`INFERRED FROM MIDDLEWARE`** (403) | `SEC-02` | Error Object | Forged or corrupted token per SEC-02 |
| **COV-FR07-05** | `POST /api/cart` | Standard valid item addition | `api_specification.md` L120 | **`INFERRED`** | $P_{B1}, P_{C1}, P_{D1}$ | Item accepted into user cart | **`INFERRED`** (200 OK) | `SEC-02` | Object (`message`) | Happy-path addition |
| **COV-FR07-06** | `POST /api/cart` | Duplicate product accumulation | `README.md` L96 | **`SPECIFIED BUSINESS RULE`** | $P_{E3}$ (Duplicate item) | Quantity increments ($q_1+q_2$), no duplicate row created | **`INFERRED`** (200 OK) | None | Single object in array | Core FR-07 deduplication rule |
| **COV-FR07-07** | `POST /api/cart` | Quantity exact minimum ($q=1$) | `README.md` L86 | **`SPECIFIED`** | $P_{B1}$ (min) | Item accepted with quantity = 1 | **`SPECIFIED`** (200 OK) | None | Object | Lower boundary of quantity |
| **COV-FR07-08** | `POST /api/cart` | Quantity min + 1 ($q=2$) | `README.md` L86 | **`SPECIFIED`** | $P_{B1}$ (min+1) | Item accepted with quantity = 2 | **`SPECIFIED`** (200 OK) | None | Object | Standard small positive integer |
| **COV-FR07-09** | `POST /api/cart` | Zero quantity rejection ($q=0$) | `README.md` L86 | **`SPECIFIED REJECTION`** | $P_{B2}$ (min - 1) | Rejection required per positive integer rule | **`UNKNOWN / INFERRED REJECTION`** (Status $\ne 200$) | None | Error Object | Boundary violation |
| **COV-FR07-10** | `POST /api/cart` | Negative quantity ($q=-1$) | `README.md` L86 | **`SPECIFIED REJECTION`** | $P_{B3}$ (negative) | Rejection required per positive integer rule | **`UNKNOWN / INFERRED REJECTION`** (Status $\ne 200$) | None | Error Object | Negative value violation |
| **COV-FR07-11** | `POST /api/cart` | Fractional quantity ($q=1.5$) | `README.md` L86 | **`SPECIFIED REJECTION`** | $P_{B4}$ (float) | Rejection required per integer constraint | **`UNKNOWN / INFERRED REJECTION`** (Status $\ne 200$) | None | Error Object | Decimal value violation |
| **COV-FR07-12** | `POST /api/cart` | String numeric quantity ($q="2"$) | `README.md` L86 | **`TYPE ROBUSTNESS / CHARACTERIZATION`** | $P_{B5}$ (string int) | Non-integer type; probe coercion vs strict rejection | **`UNKNOWN`** (Controlled response) | None | Object / Error | JSON type coercion probe |
| **COV-FR07-13** | `POST /api/cart` | Non-numeric string ($q="abc"$) | `README.md` L86 | **`INFERRED REJECTION`** | $P_{B6}$ (string) | Rejection required per integer constraint | **`UNKNOWN / INFERRED REJECTION`** (Status $\ne 200$) | None | Error Object | Non-numeric type violation |
| **COV-FR07-14** | `POST /api/cart` | Large quantity ($q=10^9$) | Undocumented | **`ROBUSTNESS / UNKNOWN UPPER BOUND`** | $P_{B7}$ (large int) | Server handles large integer without crash | **`UNKNOWN`** (Controlled response) | None | Object / Error | Unknown upper bound probe |
| **COV-FR07-15** | `POST /api/cart` | Omitted quantity field | `README.md` L86 | **`INFERRED REJECTION`** | $P_{B8}$ (missing) | Rejection required per mandatory quantity rule | **`UNKNOWN / INFERRED REJECTION`** (Status $\ne 200$) | None | Error Object | Missing mandatory field |
| **COV-FR07-16** | `POST /api/cart` | Non-existent product ID ($id=999999$) | Undocumented | **`ROBUSTNESS / BUSINESS PROBE`** | $P_{C2}$ (missing id) | Characterize whether catalog check exists | **`UNKNOWN`** (Controlled response) | None | Object / Error | Catalog existence probe |
| **COV-FR07-17** | `POST /api/cart` | Negative product ID ($id=-1$) | Undocumented | **`ROBUSTNESS PROBE`** | $P_{C3}$ (negative id) | Characterize handling of negative ID | **`UNKNOWN`** (Controlled response) | None | Object / Error | Negative ID probe |
| **COV-FR07-18** | `POST /api/cart` | Omitted product ID field | Undocumented | **`ROBUSTNESS PROBE`** | $P_{C5}$ (missing id) | Characterize handling of omitted ID | **`UNKNOWN`** (Controlled response) | None | Error Object | Inferred field omission |
| **COV-FR07-19** | `POST /api/cart` | Client price tampering ($price=1$) | Undocumented for Cart | **`SECURITY / INTEGRITY PROBE`** | $P_{D2}$ (tampered price) | Probe whether cart stores submitted price or catalog price | **`UNKNOWN`** (Controlled response) | None | Object | Price integrity probe |
| **COV-FR07-20** | `POST /api/cart` | Negative price ($price=-50000$) | Undocumented for Cart | **`ROBUSTNESS PROBE`** | $P_{D3}$ (negative price) | Characterize negative price handling | **`UNKNOWN`** (Controlled response) | None | Error Object | Negative price probe |
| **COV-FR07-21** | `POST /api/cart` | Unauthenticated addition | `api_specification.md` L112 | **`SPECIFIED REJECTION`** | $P_{A2}$ (Missing token) | Access blocked; item not added | **`INFERRED FROM MIDDLEWARE`** (401) | `SEC-02` | Error Object | Enforces SEC-02 |
| **COV-FR07-22** | `POST /api/cart` | Invalid / forged JWT token | `api_specification.md` L112 | **`SPECIFIED REJECTION`** | $P_{A3}$ (Invalid token) | Access blocked; item not added | **`INFERRED FROM MIDDLEWARE`** (403) | `SEC-02` | Error Object | Enforces SEC-02 |
| **COV-FR07-23** | Both | User cart isolation | `SEC-02` / Cart Semantics | **`INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02`** | $P_{E5}$ (Cross-user) | User 1 additions completely segregated from User 2 cart | **`INFERRED`** (200 OK, segregated) | `SEC-02` | Array | Multi-tenant user isolation |
| **COV-FR07-24** | `POST /api/cart` | Empty JSON body `{}` | Undocumented | **`ROBUSTNESS PROBE`** | — | Safe handling without server crash | **`UNKNOWN`** (Status $\ne 200$) | None | Error Object | Empty payload robustness |
