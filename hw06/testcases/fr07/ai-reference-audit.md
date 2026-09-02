# FR-07: Shopping Cart — External AI Reference Review (ChatGPT)

> **Document Status:** Reference Material Only — Secondary AI Critique  
> **Source AI:** ChatGPT (OpenAI)  
> **Target Test Suite:** FR-07 Original AI Suite (`FR07-AI-001` through `FR07-AI-038` in `generated-ai-original.md`)  
> **Student / Evaluator:** Phạm Ngọc Gia Bảo (`23127027`)  
> **Evaluation Date:** 2026-09-02  

> [!WARNING]
> **Academic Integrity Warning:** This document contains an external secondary AI review produced by ChatGPT. It is reference material for human review and does not modify the immutable original Gemini generation (`generated-ai-original.md`). It must NOT be misrepresented as student-authored reasoning until independently evaluated and adopted by the student.

---

## 1. Reference Audit Distribution Summary

| Reference Verdict | Count | Percentage | Definition / Scope |
| :---: | :---: | :---: | :--- |
| **`VALID`** | **23** | 60.5% | Test objectives, partitions, and expected semantic oracles align cleanly with reviewed specifications. |
| **`INCOMPLETE`** | **15** | 39.5% | Test premise is valid, but expected HTTP status or error envelope is over-constrained beyond official contract. |
| **`INVALID`** | **0** | 0.0% | Zero test cases were completely rejected or founded on false premises. |
| **TOTAL** | **38** | **100%** | **Programmatically Verified: 23 + 15 + 0 = 38** |

---

## 2. Key Systematic Findings from External Critique

1. **`AI-ERR-FR07-STATUS-ORACLE` (Internal Oracle Contradiction on Status Codes):**
   Several tests correctly acknowledged that exact failure HTTP status codes are undocumented by official specifications (`UNKNOWN by specification`), but subsequently hard-coded strict assertions such as `"Rejection status != 200"` and `"400 Bad Request expected"` (`FR07-AI-014` through `018`, `020`, `021`, `023`, `024`, `037`).
   *Recommendation:* Separate semantic rejection/state assertion (authoritative) from exact HTTP status code (UNKNOWN).
2. **`AI-ERR-FR07-ERROR-ENVELOPE` (Hard-Coded Error Body):**
   `FR07-AI-005` and `FR07-AI-032` hard-code `{ error: 'Forbidden' }` as a strict response contract, even though the official specification does not formalize error response schemas.
   *Recommendation:* Treat error payload envelopes as `UNKNOWN / IMPLEMENTATION-OBSERVED`.
3. **HTTP Status Promotion on Valid Boundaries:**
   `FR07-AI-012` and `FR07-AI-013` labeled HTTP 200 as `SPECIFIED / INFERRED`, whereas HTTP 200 itself is only `INFERRED` for cart addition.

---

## 3. Compact Reference Review Table

| Test ID | AI Reference Verdict | Reason (<=15 words) | Suggested Correction |
| :---: | :---: | :--- | :--- |
| **`FR07-AI-001`** | **`VALID`** | Empty-cart test correctly classified as INFERRED / IMPLEMENTATION-OBSERVED. | None required |
| **`FR07-AI-002`** | **`VALID`** | Add-then-GET state verification is coherent; result oracle remains INFERRED. | None required |
| **`FR07-AI-003`** | **`VALID`** | Multi-item state characterization is meaningful and does not overstate response contract. | None required |
| **`FR07-AI-004`** | **`VALID`** | Missing JWT correctly requires semantic denial; 401 correctly labeled middleware-inferred. | None required |
| **`FR07-AI-005`** | **`INCOMPLETE`** | Rejection valid, but exact body {error:'Forbidden'} is not specified by contract. | Keep exact error envelope UNKNOWN or IMPLEMENTATION-OBSERVED |
| **`FR07-AI-006`** | **`VALID`** | Non-Bearer scheme violates SEC-02 authentication; exact status remains inferred. | None required |
| **`FR07-AI-007`** | **`VALID`** | Standard POST matching documented example is meaningful positive test; behavior INFERRED. | None required |
| **`FR07-AI-008`** | **`VALID`** | Adding second distinct item provides useful state coverage with inferred status. | None required |
| **`FR07-AI-009`** | **`VALID`** | Directly verifies explicit duplicate-product accumulation rule (q1+q2, single row). | None required |
| **`FR07-AI-010`** | **`VALID`** | Meaningful interleaved state variation of the explicit accumulation rule. | None required |
| **`FR07-AI-011`** | **`VALID`** | Tests explicit accumulation rule using minimum valid unit increments (1+1). | None required |
| **`FR07-AI-012`** | **`INCOMPLETE`** | quantity=1 is SPECIFIED valid, but HTTP 200 is only INFERRED for endpoint. | Semantic acceptance = SPECIFIED; Status = 200 OK (INFERRED) |
| **`FR07-AI-013`** | **`INCOMPLETE`** | quantity=2 satisfies positive integer domain, but incorrectly strengthens HTTP status. | Semantic validity = SPECIFIED; 200 OK = INFERRED |
| **`FR07-AI-014`** | **`INCOMPLETE`** | quantity=0 violates minimum 1, but status!=200 / 400 over-specifies undocumented status. | Expected status = UNKNOWN; primary oracle = semantic rejection/no mutation |
| **`FR07-AI-015`** | **`INCOMPLETE`** | quantity=-1 must be rejected semantically, but exact non-200 status is undocumented. | Keep status UNKNOWN; verify zero cart mutation |
| **`FR07-AI-016`** | **`INCOMPLETE`** | quantity=-100 violates positive-integer requirement, but over-specifies HTTP outcome. | HTTP status UNKNOWN; semantic rejection is authoritative |
| **`FR07-AI-017`** | **`INCOMPLETE`** | quantity=1.5 violates integer requirement, but incorrectly strengthens HTTP oracle. | Status UNKNOWN; verify semantic rejection and no mutation |
| **`FR07-AI-018`** | **`INCOMPLETE`** | quantity=0.5 violates integer and minimum constraints, but failure status undocumented. | Keep status UNKNOWN; assert rejection and no mutation |
| **`FR07-AI-019`** | **`VALID`** | String quantity '2' correctly treated as TYPE ROBUSTNESS / CHARACTERIZATION. | None required |
| **`FR07-AI-020`** | **`INCOMPLETE`** | 'abc' violates integer requirement, but status!=200 / 400 is stronger than spec. | Status UNKNOWN; semantic rejection/no mutation is main oracle |
| **`FR07-AI-021`** | **`INCOMPLETE`** | Special-character string cannot represent integer, but test over-specifies HTTP outcome. | Use UNKNOWN HTTP status and semantic rejection |
| **`FR07-AI-022`** | **`VALID`** | 10^9 correctly treated as ROBUSTNESS / UNKNOWN UPPER BOUND without invented boundary. | None required |
| **`FR07-AI-023`** | **`INCOMPLETE`** | Missing quantity is inferred rejection, but test over-specifies !=200 / 400. | Status UNKNOWN; verify no undefined-quantity item added |
| **`FR07-AI-024`** | **`INCOMPLETE`** | null quantity violates integer requirement, but exact non-200 status unspecified. | Status UNKNOWN; assert semantic rejection and no mutation |
| **`FR07-AI-025`** | **`VALID`** | Non-existent ID correctly kept as robustness probe rather than specified rule. | None required |
| **`FR07-AI-026`** | **`VALID`** | Negative product ID behavior correctly treated as UNKNOWN robustness probe. | None required |
| **`FR07-AI-027`** | **`VALID`** | Omitted product ID correctly treated as schema robustness probe. | None required |
| **`FR07-AI-028`** | **`VALID`** | String product ID is legitimate type-characterization probe with safe oracle. | None required |
| **`FR07-AI-029`** | **`VALID`** | Price tampering explicitly treated as integrity probe, not formal cart rule. | None required |
| **`FR07-AI-030`** | **`VALID`** | Negative price correctly classified as robustness; positive rule is in FR-15. | None required |
| **`FR07-AI-031`** | **`VALID`** | SEC-02 requires authentication for POST mutation; 401 identified as middleware-inferred. | None required |
| **`FR07-AI-032`** | **`INCOMPLETE`** | Forged JWT must be denied, but exact error object {error:'Forbidden'} unspecified. | Keep exact error envelope UNKNOWN / IMPLEMENTATION-OBSERVED |
| **`FR07-AI-033`** | **`VALID`** | Basic auth violates Bearer contract; exact status remains middleware-inferred. | None required |
| **`FR07-AI-034`** | **`VALID`** | User isolation testing is useful; clearly classified as INFERRED from SEC-02. | None required |
| **`FR07-AI-035`** | **`VALID`** | Cross-user non-interference is meaningful inferred state/security characterization. | None required |
| **`FR07-AI-036`** | **`VALID`** | Same product IDs independently scoped across distinct users; classified INFERRED. | None required |
| **`FR07-AI-037`** | **`INCOMPLETE`** | Classified as ROBUSTNESS but requires non-200 status despite formal behavior UNKNOWN. | Use controlled-response/no-crash oracle; no mutation |
| **`FR07-AI-038`** | **`INCOMPLETE`** | Extra-property behavior UNKNOWN; tampering assertion too vague without mechanism. | Base oracle: controlled handling/no crash; report security fail only if effect shown |

---

## 4. Full Verbatim ChatGPT Audit Log

```text
FR07-AI-001 | VALID | Empty-cart test is explicitly classified as INFERRED / IMPLEMENTATION-OBSERVED rather than being falsely presented as a formal contract guarantee.
FR07-AI-002 | VALID | Add-then-GET state verification is coherent and its cart/result oracle remains INFERRED.
FR07-AI-003 | VALID | Multi-item cart state characterization is meaningful and does not overstate an explicit formal response contract.
FR07-AI-004 | VALID | SEC-02 requires authentication. Missing JWT must be denied semantically, while 401 is correctly classified as middleware-inferred.
FR07-AI-005 | INCOMPLETE | JWT rejection is valid, but the exact response body {error:'Forbidden'} is not defined by the official specification. Correction: Keep the exact error envelope UNKNOWN or IMPLEMENTATION-OBSERVED.
FR07-AI-006 | VALID | An Authorization value without the required Bearer scheme does not satisfy the specified authentication requirement. Exact status remains inferred.
FR07-AI-007 | VALID | A standard POST matching the documented request example is a meaningful positive case and its success behavior is classified as INFERRED.
FR07-AI-008 | VALID | Adding a second distinct item is useful state coverage and its behavior is appropriately treated as inferred.
FR07-AI-009 | VALID | Directly verifies the explicit FR-07 duplicate-product accumulation rule: q1 + q2 with a single product row.
FR07-AI-010 | VALID | Meaningful interleaved state variation of the same explicit accumulation rule.
FR07-AI-011 | VALID | Tests the same explicit accumulation rule using minimum valid quantity increments.
FR07-AI-012 | INCOMPLETE | quantity=1 is SPECIFIED valid, but HTTP 200 itself is only INFERRED for this endpoint. Correction: Semantic acceptance = SPECIFIED. Expected HTTP status = 200 OK (INFERRED), not SPECIFIED.
FR07-AI-013 | INCOMPLETE | quantity=2 satisfies the specified positive-integer domain, but the test mixes the semantic rule with an incorrectly strengthened HTTP status classification. Correction: Semantic validity = SPECIFIED. 200 OK = INFERRED.
FR07-AI-014 | INCOMPLETE | quantity=0 clearly violates the specified minimum, but "status != 200" and "400 expected" constrain an HTTP result the official spec does not define. Correction: Expected HTTP Status = UNKNOWN. Primary oracle = semantic rejection and zero cart mutation.
FR07-AI-015 | INCOMPLETE | quantity=-1 must be rejected semantically, but exact/non-200 HTTP behavior is not formally specified. Correction: Keep HTTP status UNKNOWN and verify no mutation.
FR07-AI-016 | INCOMPLETE | quantity=-100 violates the positive-integer requirement, but the testcase over-specifies the failure HTTP outcome. Correction: HTTP status UNKNOWN; semantic rejection/no mutation is authoritative.
FR07-AI-017 | INCOMPLETE | quantity=1.5 violates the explicit integer requirement, but the testcase incorrectly strengthens the HTTP oracle to !=200 / expected 400. Correction: HTTP status UNKNOWN; verify semantic rejection and no mutation.
FR07-AI-018 | INCOMPLETE | quantity=0.5 violates both integer and minimum constraints, but exact failure status is undocumented. Correction: Keep status UNKNOWN and assert rejection/no mutation.
FR07-AI-019 | VALID | String quantity "2" is correctly treated as TYPE ROBUSTNESS / CHARACTERIZATION without forcing one functional outcome.
FR07-AI-020 | INCOMPLETE | "abc" cannot satisfy the integer requirement, but the HTTP !=200 / expected 400 oracle is stronger than the specification. Correction: HTTP status UNKNOWN; semantic rejection/no mutation is the main oracle.
FR07-AI-021 | INCOMPLETE | A special-character string cannot represent an integer quantity, but the test over-specifies the HTTP outcome. Correction: Use UNKNOWN HTTP status and semantic rejection.
FR07-AI-022 | VALID | 10^9 is correctly treated as ROBUSTNESS / UNKNOWN UPPER BOUND rather than an invented overflow boundary.
FR07-AI-023 | INCOMPLETE | Missing quantity can reasonably be treated as inferred rejection, but the testcase again strengthens the undocumented HTTP response to !=200 / 400. Correction: HTTP status UNKNOWN; verify no undefined-quantity item is added.
FR07-AI-024 | INCOMPLETE | null cannot satisfy the positive-integer requirement, but exact/non-200 status is not specified. Correction: HTTP status UNKNOWN; semantic rejection/no mutation.
FR07-AI-025 | VALID | Non-existent catalog ID is correctly kept as a robustness/business characterization probe rather than a specified FR-07 validation rule.
FR07-AI-026 | VALID | Negative product ID behavior is correctly treated as UNKNOWN robustness.
FR07-AI-027 | VALID | Omitted product ID is correctly treated as schema robustness because required API semantics are not formally specified.
FR07-AI-028 | VALID | String product ID is a legitimate type-characterization probe with no invented functional oracle.
FR07-AI-029 | VALID | Client price tampering is explicitly treated as an integrity/characterization probe, not as a formal FR-07 catalog-price rule.
FR07-AI-030 | VALID | Negative price is correctly classified as robustness because the positive price rule belongs to another feature, not FR-07.
FR07-AI-031 | VALID | SEC-02 requires authentication for POST cart mutation, while 401 is correctly identified as middleware-inferred.
FR07-AI-032 | INCOMPLETE | Forged JWT must be denied, but the exact error object {error:'Forbidden'} is not specified by the official contract. Correction: Keep exact error envelope UNKNOWN / IMPLEMENTATION-OBSERVED.
FR07-AI-033 | VALID | Basic authentication does not satisfy the required Bearer-token contract and exact status remains inferred.
FR07-AI-034 | VALID | Two-user cart-isolation testing is useful and clearly classified as INFERRED from authenticated-user semantics and SEC-02.
FR07-AI-035 | VALID | Cross-user non-interference is a meaningful inferred state/security characterization.
FR07-AI-036 | VALID | Tests that same product IDs remain independently scoped across two authenticated users, while correctly retaining an INFERRED classification.
FR07-AI-037 | INCOMPLETE | The testcase is classified as ROBUSTNESS, but then requires a non-200 rejection and JSON error body despite the formal API behavior being UNKNOWN. Correction: Use a controlled-response/no-crash oracle. Do not require a specific HTTP success/failure class unless justified separately; verify no unsafe mutation.
FR07-AI-038 | INCOMPLETE | Extra-property behavior is UNKNOWN, while "no parameter tampering or privilege escalation" is too vague and lacks a concrete verification mechanism. Correction: Use controlled handling/no crash as the base robustness oracle. Only report a security failure if an extra property demonstrably causes an unauthorized effect.
```
