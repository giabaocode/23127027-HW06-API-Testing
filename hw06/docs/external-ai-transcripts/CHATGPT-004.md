# External AI Transcript — Interaction CHATGPT-004

- **Session / Interaction ID:** CHATGPT-004
- **Date & Time:** 2026-09-02 (During Phase 2 FR-12 Human Audit Preparation)
- **AI Tool / Model:** ChatGPT (OpenAI)
- **Phase:** Phase 2 — Secondary External Reference Review of 38 FR-12 AI Test Cases
- **Context:** Provided by student as external reference material to assist in human review of AI-generated access control test cases.

---

## 1. Verbatim Student Prompt

```text
Review all 38 AI-generated FR-12 test cases (FR12-AI-001 to FR12-AI-038) for HCMUS EShop SUT. Classify each as VALID, INVALID, or INCOMPLETE, providing reasons and suggested corrections.
```

---

## 2. Verbatim Conversational AI Response

```text
FR12-AI-001
Reference Verdict: VALID
Reason:
Standard-user denial for GET /api/admin/users is correctly mapped to SEC-03. Semantic outcome is specified denial; exact 403 remains inferred.

FR12-AI-002
Reference Verdict: VALID
Reason:
Dual-assertion on user deletion verifies both semantic denial and persistence of the user account via login probe without touching baseline users.

FR12-AI-003
Reference Verdict: VALID
Reason:
Standard-user denial for system-wide order history correctly enforces SEC-03 data privacy.

FR12-AI-004
Reference Verdict: INCOMPLETE
Reason:
The access-control objective is valid, but pending -> delivered may be rejected by downstream order-state validation even if authorization is broken, masking the SEC-03 defect.
Correction:
Use a valid disposable-order transition such as pending -> confirmed so authorization is isolated.

FR12-AI-005
Reference Verdict: INCOMPLETE
Reason:
The side-effect oracle depends on GET /api/products?search=... returning an empty list, but this packet does not establish server-side search semantics.
Correction:
Fetch the product list and assert that the unique marker ImportProbe_23127027 is absent, or use another source-confirmed lookup.

FR12-AI-006
Reference Verdict: INCOMPLETE
Reason:
Using coupon application/checkout behavior as the persistence verifier can be affected by unrelated coupon/order business conditions.
Correction:
Use an authenticated admin GET /api/coupons state check and assert that HACK23127027 does not exist.

FR12-AI-007
Reference Verdict: INCOMPLETE
Reason:
"query or application succeeds" is ambiguous, and coupon application can fail for unrelated business reasons.
Correction:
Verify the disposable coupon directly through admin coupon listing and assert its ID/code remains present.

FR12-AI-008
Reference Verdict: INCOMPLETE
Reason:
The product non-creation verifier depends on ungrounded server-side ?search= semantics.
Correction:
Fetch product data and explicitly assert that the unique UnauthorizedProduct_23127027 marker is absent.

FR12-AI-009
Reference Verdict: VALID
Reason:
Side-effect check verifies original price remains unchanged after unauthorized standard-user PUT probe.

FR12-AI-010
Reference Verdict: VALID
Reason:
Side-effect check verifies product still exists via GET probe after unauthorized standard-user DELETE probe.

FR12-AI-011
Reference Verdict: VALID
Reason:
Category non-creation is verified by absence in category list after standard-user POST probe.

FR12-AI-012
Reference Verdict: VALID
Reason:
Category modification denial is verified by category name remaining unchanged in database.

FR12-AI-013
Reference Verdict: VALID
Reason:
Category deletion denial is verified by category continuing to exist in database.

FR12-AI-014
Reference Verdict: VALID
Reason:
Standard user denied access to administrative coupon master list via SEC-03.

FR12-AI-015
Reference Verdict: VALID
Reason:
Admin access to GET /api/admin/users correctly defines authorization clearance as primary oracle with 200 as inferred SUT behavior.

FR12-AI-016
Reference Verdict: INCOMPLETE
Reason:
The main authorization test is sound, but the side-effect verifier requires an exact downstream login status 401 that is not an FR-12 contract oracle.
Correction:
Require that the deleted disposable user can no longer authenticate / no longer exists. Treat exact login failure status as endpoint-specific INFERRED/UNKNOWN.

FR12-AI-017
Reference Verdict: VALID
Reason:
Admin access to GET /api/admin/orders verifies administrative clearance unhindered.

FR12-AI-018
Reference Verdict: VALID
Reason:
Admin order status update correctly verifies administrative capability on disposable order.

FR12-AI-019
Reference Verdict: VALID
Reason:
Admin product import verifies administrative capability with valid disposable payload.

FR12-AI-020
Reference Verdict: VALID
Reason:
Admin coupon creation verifies administrative capability with valid disposable coupon code.

FR12-AI-021
Reference Verdict: VALID
Reason:
Admin coupon deletion operates on disposable coupon and verifies deletion.

FR12-AI-022
Reference Verdict: VALID
Reason:
Admin product creation verifies administrative capability with valid disposable product body.

FR12-AI-023
Reference Verdict: VALID
Reason:
Admin product update operates on disposable product and updates price/description.

FR12-AI-024
Reference Verdict: VALID
Reason:
Admin product deletion operates on disposable product and removes it from catalog.

FR12-AI-025
Reference Verdict: VALID
Reason:
Admin category creation verifies administrative capability with valid category body.

FR12-AI-026
Reference Verdict: VALID
Reason:
Admin category update operates on disposable category and updates name.

FR12-AI-027
Reference Verdict: VALID
Reason:
Admin category deletion operates on disposable category and removes it from database.

FR12-AI-028
Reference Verdict: VALID
Reason:
Admin coupon listing verifies administrative capability on GET /api/coupons.

FR12-AI-029
Reference Verdict: INCOMPLETE
Reason:
The anonymous POST product test is valid, but its product-absence verification must not rely on unestablished search-query behavior.
Correction:
Fetch the product list and explicitly check that AnonProduct_23127027 is absent.

FR12-AI-030
Reference Verdict: VALID
Reason:
Anonymous product update denial correctly asserts SEC-02 and verifies product unchanged.

FR12-AI-031
Reference Verdict: VALID
Reason:
Anonymous product deletion denial correctly asserts SEC-02 and verifies product still exists.

FR12-AI-032
Reference Verdict: VALID
Reason:
Anonymous user list denial correctly asserts SEC-02 and prevents user data exposure.

FR12-AI-033
Reference Verdict: INCOMPLETE
Reason:
If the expected access-control defect occurs, anonymous category creation may leave a real category in the test environment, but cleanup is None.
Correction:
If AnonCategory_23127027 exists after execution, delete it using legitimate admin credentials.

FR12-AI-034
Reference Verdict: VALID
Reason:
Anonymous coupon overview denial correctly asserts SEC-02 and prevents coupon data exposure.

FR12-AI-035
Reference Verdict: INCOMPLETE
Reason:
The semantic expired-JWT test is valid, but the wording incorrectly describes expiration as a cryptographic signature failure.
Correction:
State that the signature may remain valid while JWT validity fails because the exp claim is in the past. Preserve SEC-02 semantic denial. Exact 403 remains INFERRED.

FR12-AI-036
Reference Verdict: VALID
Reason:
Forged cryptographic signature rejection correctly asserts SEC-02 integrity failure.

FR12-AI-037
Reference Verdict: INCOMPLETE
Reason:
Missing-role authorization probe is valid, but if SEC-03 is broken the coupon can actually be created and cleanup is currently None.
Correction:
Verify absence/presence through admin GET /api/coupons. If NOROLE_CPN_23127027 was created, delete it using admin credentials.

FR12-AI-038
Reference Verdict: VALID
Reason:
Uppercase role 'ADMIN' probe correctly asserts SEC-03 exact-match case sensitivity.
```
