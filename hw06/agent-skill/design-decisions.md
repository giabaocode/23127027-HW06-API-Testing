# Agent Skill: Automated API Test Case Generator — Design Decisions & Architecture

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Module:** HW06 Agent Skill / Specialized AI Test Generation Architecture
> - **Implementation:** [`hw06/agent-skill/test_generator.py`](file:///Users/phamngocgiabao/eshop-sut/hw06/agent-skill/test_generator.py)

---

## 1. Executive Summary & Purpose

The **API Test Case Generator Agent Skill** is an automated, rules-guided testing intelligence system designed to ingest REST API endpoint specifications and systematically generate a complete, high-coverage suite of test case designs. 

Rather than relying on unconstrained LLM prompting—which our project audit proved leads to hallucinated requirements, REST convention assumptions, and miscounted coverage categories—this Agent Skill combines deterministic boundary and equivalence analysis algorithms with formal domain oracle rules.

---

## 2. Core Design Decisions

### Decision 1: Separation of Access-Control Outcome from HTTP Status Code
- **Problem Observed:** LLMs repeatedly assume that successful admin operations must return `200 OK` or `201 Created`, and unauthorized operations must return `401 Unauthorized` or `403 Forbidden`. In formal software specifications (such as the course `README.md`), the HTTP status code for valid admin actions is often unstated or left as an implementation detail.
- **Agent Skill Rule:** The generator strictly outputs a two-level oracle:
  1. **Semantic Outcome:** (e.g. `MUTATION_PERMITTED`, `STATE_STORED`, `ACCESS_DENIED`, `CART_UNMODIFIED`).
  2. **HTTP Status Oracle:** Classified into `SPECIFIED`, `INFERRED`, or `UNKNOWN`. Tests never fail on HTTP status differences if the semantic state contract is preserved.

### Decision 2: Deterministic Equivalence Partitioning (EP) & Boundary Value Analysis (BVA) Engine
- **Algorithmic Extraction:** For each parameter in the endpoint definition, the generator produces 5 standard partitions:
  - **P1 (Valid Nominal):** Standard valid value within range.
  - **P2 (Boundary Minimum):** Exact minimum boundary (e.g. length = 1, quantity = 1).
  - **P3 (Boundary Maximum):** Exact upper boundary (e.g. max string length, ceiling quantity).
  - **P4 (Negative Out-of-Bounds):** Just below minimum (0, -1) or just above maximum ($N+1$).
  - **P5 (Type & Syntactic Confusion):** Null, missing, empty string `""`, wrong type (`string` instead of `int`), or malformed structure.

### Decision 3: Specialized Security & Authorization Mutation Probes
- For endpoints flagged as `protected` or `admin`, the generator automatically attaches standard security probes:
  - `SEC-01`: Missing `Authorization` header.
  - `SEC-02`: Cryptographically invalid / forged token signature.
  - `SEC-03`: Expired token (`exp` in past).
  - `SEC-04`: Unprivileged token (`role: 'user'` targeting an admin endpoint).
  - `SEC-05`: Tampered role claim (missing claim, untrimmed whitespace, uppercase spoofing, array type confusion).

### Decision 4: Deterministic Dual-Assertion Strategy for Destructive Actions
- For negative mutation tests (e.g. attempting to delete a user or mutate a product without credentials), the skill generates a **two-step verification**:
  1. Primary assertion: The mutation request is rejected.
  2. Side-effect assertion: A secondary query verifies that the target entity was NOT modified or deleted in storage.

---

## 3. Inputs & Parsing Model Assumptions

- **Input Format:** JSON or CLI parameters defining:
  - `endpoint`: URL path (e.g. `/api/cart`)
  - `method`: HTTP Verb (`GET`, `POST`, `PUT`, `DELETE`)
  - `auth_level`: `public`, `user`, or `admin`
  - `parameters`: List of parameter objects `{ name, type, required, min, max, format }`
- **Assumptions:**
  - SUT adheres to standard JSON request/response formats.
  - Authentication follows RFC 6750 Bearer JWT semantics.
  - Endpoints with `auth_level == 'admin'` require explicit role authorization.

---

## 4. Output Schema & Traceability

The generator outputs structured JSON and Markdown test cases adhering to the following schema:
- `test_id`: Unique identifier (e.g. `GEN-EP-001`, `GEN-SEC-004`)
- `category`: `Equivalence Partitioning`, `Boundary Value Analysis`, `Security & Authorization`, `Robustness`
- `target_endpoint`: HTTP method and URL
- `auth_context`: `anonymous`, `user`, `admin`, `forged_jwt`
- `input_payload`: Concrete request body or query parameters
- `semantic_oracle`: Formal business outcome expected
- `expected_status`: Expected HTTP code with classification
- `side_effect_check`: Optional query probe to verify state preservation

---

## 5. Limitations & Future Extensions

- **Current Limitations:**
  - The offline generator does not inspect backend source code (black-box model).
  - Multi-entity workflows (e.g. full checkout process) require manual test case linking.
- **Future Enhancements:**
  - Direct export to Postman Collection v2.1.0 format.
  - Dynamic database schema introspection via SQLite metadata tables.
