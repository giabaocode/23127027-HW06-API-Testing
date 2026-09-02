# HW06 — Postman Features Documentation

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature Scope:** FR-01 — Account Registration

---

## Postman Features Inventory

The following table documents all purposeful Postman features incorporated into the automated API test suite for **FR-01 (Account Registration)**. No feature was introduced cosmetically; each serves a concrete software testing engineering objective.

| Feature | Where Used | Why Used / Engineering Rationale | Evidence / Location |
| :--- | :--- | :--- | :--- |
| **Collection** | `fr01-registration.postman_collection.json` | Serves as the self-contained root container for all 42 automated API requests, holding collection-level metadata, central pre-request hooks, and central assertion scripts. | Root object of collection JSON (`info.name`) |
| **Folders (Hierarchical Organization)** | 8 thematic folders (`01 - Positive Happy Path`, `02 - Required Fields Validation`, `03 - Email Format & Validation`, `04 - Password Policy Verification`, `05 - State & Duplicate Lifecycle`, `06 - Security Assertions`, `07 - Robustness & Characterization`, `08 - Student-Selected Extensions`) | Logically separates functional, negative, boundary, security, and exploratory tests for granular execution, reporting clarity, and modular debugging. | `item[0..7]` in collection JSON |
| **Environment & Variables** | `eshop-local.postman_environment.json` (`baseUrl`, `studentId`) | Decouples target deployment URL (`http://localhost:3000`) and student credentials from test logic, allowing the identical collection to execute against local SUT, Docker containers, or staging environments. | `hw06/postman/environments/eshop-local.postman_environment.json` |
| **Collection-Level Pre-Request Script** | Collection root `event[listen="prerequest"]` | **Central Header Injection:** Programmatically injects `X-Student-Id: 23127027` on every single outgoing API request without manual duplication across 42 requests. | `collection.event[0].script.exec` |
| **Request-Level Pre-Request Script (Chaining)** | `FR01-AI-017` (Sequential Duplicate) | Uses `pm.sendRequest()` inside pre-request script to register an account dynamically with a unique timestamp, then immediately triggers the main request with the identical email to reliably assert state-dependent duplicate rejection. | `FR01-AI-017.event[listen="prerequest"]` |
| **Collection-Level Test Script** | Collection root `event[listen="test"]` | Enforces mandatory central assertion verifying that every outbound request carried `X-Student-Id: 23127027` and confirms basic network resilience. | `collection.event[1].script.exec` |
| **Request-Level Test Scripts & Assertions** | Individual requests | Executes assertion logic calibrated strictly against the reviewed specification oracles (`SPECIFIED`, `INFERRED`, `UNKNOWN`, `ROBUSTNESS`, `SECURITY-HARDENING`). | `request.event[listen="test"]` |
| **Dynamic Variables (`{{$timestamp}}`)** | Request bodies across all positive and negative registration payloads | Generates unique email addresses (e.g. `fr01_ai_001_{{$timestamp}}@example.com`) to guarantee complete test data isolation and prevent accidental cross-test duplicate collisions across test runs. | Request URL/body variables |
| **Environment Variable Chaining** | `FR01-AI-017` (`{{seqDupEmail}}`) | Stores dynamically created email from the pre-request call into an environment variable and injects it into the subsequent request payload. | `pm.environment.set('seqDupEmail', ...)` |
| **Raw Unparsed Body Preservation** | `FR01-STU-001` (Malformed JSON) and `FR01-STU-003` (Duplicate Key) | Uses raw string mode to send syntactically broken JSON (missing closing brace) and duplicated JSON property keys without allowing Postman/Newman serializers to auto-repair or collapse keys. | `request.body.raw` text mode |
| **Request-Level Header Override** | `FR01-STU-002` (Wrong Content-Type) | Explicitly overrides `Content-Type` to `text/plain` while preserving the central `X-Student-Id` injection, testing MIME type enforcement. | `FR01-STU-002.request.header` |
| **HTTP Verb Variation** | `FR01-STU-004` (Unsupported PUT verb) | Exercises HTTP method routing by directing a `PUT` request to `/api/register` to verify the endpoint is not vulnerable to verb tampering. | `FR01-STU-004.request.method = "PUT"` |
