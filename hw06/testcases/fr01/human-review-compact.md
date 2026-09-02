# FR-01: Fast Human Review Worksheet

> **Instructions for Student (Pham Ngoc Gia Bao):**
> This compact sheet provides a fast review view of the 38 AI-generated test cases.
> Inspect the test objective, official requirement, and AI-original oracle, then record your final independent human verdict (`VALID` | `INVALID` | `INCOMPLETE`) and notes.

---

| Test ID | Short Objective | Official Requirement Reference | AI-Original Oracle | Final Student Verdict | Student Note |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **FR01-AI-001** | Verify that a standard registration request with a standa... | FR-01 (`README.md` Lines 32–34) | `200 OK` (SPECIFIED).; User account is created successfully (S... | | |
| **FR01-AI-002** | Verify system behavior when registering with a Vietnamese... | FR-01 (`README.md` Line 32) | If accepted, documented status is `200 OK` (SPECIFIED).; Input... | | |
| **FR01-AI-003** | Verify that omitting the required `name` property results... | FR-01 (`README.md` Line 32) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-004** | Verify that providing an empty string `""` for `name` is ... | FR-01 (`README.md` Line 32) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-005** | Verify that supplying a numeric integer value for `name` ... | FR-01 (`api_specification.md` Line 16) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-006** | Probe backend resilience and string handling when an unus... | FR-01 (`README.md` Line 32) | UNKNOWN by official specification. Either clean rejection (400... | | |
| **FR01-AI-007** | Verify that input containing SQL apostrophes and syntax i... | FR-01 (`README.md` Line 32) / SEC-05 (`README.md` Line 282 — Parameterized Query) | If accepted, documented status is `200 OK` (SPECIFIED). If rej... | | |
| **FR01-AI-008** | Verify backend stores HTML strings safely without crashin... | FR-01 (`README.md` Line 32) | If accepted, documented status is `200 OK` (SPECIFIED).; Backe... | | |
| **FR01-AI-009** | Verify registration succeeds with a standard RFC 5322 ema... | FR-01 (`README.md` Line 33) | `200 OK` (SPECIFIED).; Account created successfully (SPECIFIED). | | |
| **FR01-AI-010** | Verify email handling when plus-addressing (`user+tag@dom... | FR-01 (`README.md` Line 33) | If accepted, documented status is `200 OK` (SPECIFIED).; Accep... | | |
| **FR01-AI-011** | Verify that omitting the required `email` property result... | FR-01 (`README.md` Line 32) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-012** | Verify that providing an empty string `""` for `email` is... | FR-01 (`README.md` Lines 32–33) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-013** | Verify that an email lacking the `@` symbol is rejected. | FR-01 (`README.md` Line 33 — Format Rule) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-014** | Verify that an email lacking the domain portion after `@`... | FR-01 (`README.md` Line 33 — Format Rule) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-015** | Verify that supplying a numeric integer value for `email`... | FR-01 (`api_specification.md` Line 17) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-016** | Verify that attempting to register an email that already ... | FR-01 (`README.md` Line 33 — Uniqueness Rule) | UNKNOWN by official specification; potential conventional valu... | | |
| **FR01-AI-017** | Verify account lifecycle state transition: initial regist... | FR-01 (`README.md` Line 33 — Uniqueness Rule) | UNKNOWN / INFERRED (e.g. 400 or 409).; REJECT DUPLICATE (SPECI... | | |
| **FR01-AI-018** | Verify whether email uniqueness is enforced case-insensit... | FR-01 (`README.md` Line 33) | UNKNOWN / INFERRED (400 or 409).; Semantic rejection is INFERR... | | |
| **FR01-AI-019** | Verify parameterized query treats SQL syntax in email as ... | FR-01 (`README.md` Line 33) / SEC-05 (`README.md` Line 282 — Parameterized Query) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-020** | Verify that a password satisfying all 5 policy criteria (... | FR-01 (`README.md` Line 34) | `200 OK` (SPECIFIED).; Account created successfully (SPECIFIED). | | |
| **FR01-AI-021** | Verify password policy accepts special character `@` from... | FR-01 (`README.md` Line 34) | `200 OK` (SPECIFIED).; Password policy requirement is satisfie... | | |
| **FR01-AI-022** | Verify password policy accepts special character `$` from... | FR-01 (`README.md` Line 34) | `200 OK` (SPECIFIED).; Password policy requirement is satisfie... | | |
| **FR01-AI-023** | Verify password policy accepts special character `&` from... | FR-01 (`README.md` Line 34) | `200 OK` (SPECIFIED).; Password policy requirement is satisfie... | | |
| **FR01-AI-024** | Verify behavior when password contains a required symbol ... | FR-01 (`README.md` Line 34) | If accepted, documented status is `200 OK` (SPECIFIED).; Accep... | | |
| **FR01-AI-025** | Verify that a password lacking any special character from... | FR-01 (`README.md` Line 34) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-026** | Verify that a password of length 7 (just below the 8-char... | FR-01 (`README.md` Line 34 — Length Boundary) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-027** | Verify that a password of exactly 8 characters meeting al... | FR-01 (`README.md` Line 34 — Length Boundary) | `200 OK` (SPECIFIED).; Password minimum length requirement is ... | | |
| **FR01-AI-028** | Verify that a password of 9 characters (just above the 8-... | FR-01 (`README.md` Line 34 — Length Boundary) | `200 OK` (SPECIFIED).; Password satisfies minimum length requi... | | |
| **FR01-AI-029** | Verify that a password missing an uppercase letter is rej... | FR-01 (`README.md` Line 34) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-030** | Verify that a password missing a lowercase letter is reje... | FR-01 (`README.md` Line 34) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-031** | Verify that a password missing a numeric digit is rejected. | FR-01 (`README.md` Line 34) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-032** | Verify that providing an empty string `""` for `password`... | FR-01 (`README.md` Lines 32–34) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-033** | Verify that supplying a numeric integer value for `passwo... | FR-01 (`api_specification.md` Line 18) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-034** | Probe backend resilience and password hashing limits when... | FR-01 (`README.md` Line 34) | Acceptance is UNKNOWN / ROBUSTNESS. If accepted, documented st... | | |
| **FR01-AI-035** | Verify that sending an empty JSON object `{}` with no fie... | FR-01 (`README.md` Line 32 — Required Fields) | UNKNOWN by official specification; `400 Bad Request` is an INF... | | |
| **FR01-AI-036** | Verify backend behavior when a valid registration payload... | FR-01 (`api_specification.md` Line 14; `README.md` Line 35) | If backend is tolerant, `200 OK` (SPECIFIED). If strict schema... | | |
| **FR01-AI-037** | Verify that the registered password is NOT stored as raw ... | FR-01 (`README.md` Line 278) / SEC-01 (`README.md` Line 278 — "Mật khẩu không được lưu dưới dạng plaintext") | API registration returns `200 OK` (SPECIFIED).; The password m... | | |
| **FR01-AI-038** | Verify that the successful registration response body doe... | FR-01 (`api_specification.md` Line 21) / Best Practice Credential Protection | `200 OK` (SPECIFIED).; Account created successfully (SPECIFIED). | | |
