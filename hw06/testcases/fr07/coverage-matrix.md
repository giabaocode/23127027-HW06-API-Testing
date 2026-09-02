# FR-07: Shopping Cart — Test Coverage Matrix

> **Document Information:**
> - **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> - **Target Endpoints:** `GET /api/cart`, `POST /api/cart`
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`

---

## Traceability & Coverage Matrix

| Req ID | Requirement Description | Equivalence Partition(s) | Test Objective | Target Test Category | Status / Oracle Classification |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **FR-07.1** | View empty shopping cart | $P_{E1}$ | Verify `GET /api/cart` returns empty array `[]` for newly created user | Positive Functional | **`INFERRED`** (200 OK, empty array) |
| **FR-07.2** | View populated shopping cart | $P_{E2}, P_{E4}$ | Verify `GET /api/cart` reflects added items with full fields (`id`, `name`, `price`, `quantity`) | Positive Functional | **`INFERRED`** (200 OK, array of objects) |
| **FR-07.3** | Add valid item to cart | $P_{B1}, P_{C1}, P_{D1}$ | Verify `POST /api/cart` successfully adds item with valid fields | Positive Functional | **`INFERRED`** (200 OK, success message) |
| **FR-07.4** | Accumulate quantity on duplicate add | $P_{E3}$ | Verify adding same product ID increments `quantity` rather than creating duplicate row (`README.md` L96) | Business Rule / Lifecycle | **`SPECIFIED BUSINESS RULE`** (Length = 1, sum quantity) |
| **FR-07.5** | Minimum valid quantity boundary ($q=1$) | $P_{B1}$ (min) | Verify adding item with exact minimum quantity $q=1$ succeeds | Boundary Analysis | **`SPECIFIED`** (200 OK, $q=1$) |
| **FR-07.6** | Small positive quantity ($q=2$) | $P_{B1}$ (std) | Verify adding item with standard quantity $q=2$ succeeds | Boundary Analysis | **`SPECIFIED`** (200 OK, $q=2$) |
| **FR-07.7** | Zero quantity rejection ($q=0$) | $P_{B2}$ | Verify zero quantity is rejected per `README.md` L86 rule (minimum is 1) | Boundary / Input Validation | **`SPECIFIED REJECTION`** (Status $\ne 200$, 400 observed) |
| **FR-07.8** | Negative quantity rejection ($q=-1$) | $P_{B3}$ | Verify negative quantity is rejected per `README.md` L86 rule | Boundary / Input Validation | **`SPECIFIED REJECTION`** (Status $\ne 200$, 400 observed) |
| **FR-07.9** | Decimal/Fractional quantity ($q=1.5$) | $P_{B4}$ | Verify non-integer decimal quantity is rejected per integer constraint | Type Validation | **`SPECIFIED REJECTION`** (Status $\ne 200$) |
| **FR-07.10** | String numeric quantity ($q="2"$) | $P_{B5}$ | Characterize whether server parses string integer or rejects cleanly | Type Robustness | **`UNKNOWN / CHARACTERIZATION`** (No crash) |
| **FR-07.11** | Non-numeric string quantity ($q="abc"$) | $P_{B6}$ | Verify arbitrary string is rejected | Type Validation | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.12** | Extreme large quantity ($q=10^9$) | $P_{B7}$ | Test upper boundary / integer overflow handling | Robustness | **`ROBUSTNESS`** (No server crash) |
| **FR-07.13** | Omitted quantity property | $P_{B8}$ | Verify request omitting `quantity` is rejected | Required Field | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.14** | Non-existent product ID ($id=999999$) | $P_{C2}$ | Verify behavior when adding product not present in database | Business Rule / Catalog | **`UNKNOWN / ROBUSTNESS`** (No crash) |
| **FR-07.15** | Negative product ID ($id=-1$) | $P_{C3}$ | Verify negative product ID is rejected | Input Validation | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.16** | Omitted product ID | $P_{C5}$ | Verify request omitting `id` is rejected | Required Field | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.17** | Client price tampering probe | $P_{D2}$ | Test if client can inject unauthorized low price (`price: 1`) | Security / Integrity | **`SECURITY PROBE`** (Integrity check) |
| **FR-07.18** | Negative price rejection ($price=-50000$) | $P_{D3}$ | Verify negative price is rejected | Security / Validation | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.19** | Missing `Authorization` header | $P_{A2}$ | Verify unauthenticated call is rejected with HTTP 401 | Security / Authentication | **`INFERRED FROM MIDDLEWARE`** (401 Unauthorized) |
| **FR-07.20** | Invalid / forged JWT signature | $P_{A3}$ | Verify forged token signature is rejected with HTTP 403 | Security / Authentication | **`INFERRED FROM MIDDLEWARE`** (403 Forbidden) |
| **FR-07.21** | Malformed Authorization format | $P_{A5}$ | Verify header without `Bearer ` prefix is rejected | Protocol Robustness | **`INFERRED FROM MIDDLEWARE`** (401/403) |
| **FR-07.22** | Cross-user cart isolation | $P_{E5}$ | Verify User A's cart contents are completely invisible to User B | Security / Authorization | **`SECURITY ISOLATION`** (Carts strictly segregated) |
| **FR-07.23** | Empty JSON body `{}` to POST /api/cart | — | Verify empty payload is rejected | Payload Robustness | **`INFERRED REJECTION`** (Status $\ne 200$) |
| **FR-07.24** | Unexpected extra fields in payload | — | Verify extra properties are handled safely without crash | Schema Robustness | **`ROBUSTNESS`** (No server crash) |
