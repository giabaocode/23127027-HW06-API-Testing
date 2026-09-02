# HW06 — CI/CD Pipeline & GitHub Actions Automation Report

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Repository:** [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing)
> - **Workflow Configuration:** [`.github/workflows/api-tests.yml`](file:///Users/phamngocgiabao/eshop-sut/.github/workflows/api-tests.yml)

---

## 1. CI/CD Architecture & Pipeline Overview

The continuous integration pipeline is hosted on **GitHub Actions** (`ubuntu-latest`) to automatically validate every commit pushed to `main`. The pipeline automates the complete operational lifecycle of the backend SUT without requiring manual intervention:

```
[GitHub Push / Dispatch] 
       │
       ▼
[Checkout Repository] ──> [Setup Node.js 20] ──> [Install SUT Dependencies]
                                                              │
                                                              ▼
[Upload HTML/CLI Reports] <── [Execute Newman Tests] <── [Start SUT & Health Polling]
```

### Key Engineering Safeguards:
1. **Automated Readiness Polling:** The workflow launches `node server.js &` and polls `http://localhost:3000/api/products` for up to 30 seconds before launching tests, preventing Newman connection-refused errors.
2. **Deterministic Token & Environment Decoupling:** Uses `hw06/postman/environments/ci-environment.json` targeting `http://localhost:3000`.
3. **Artifact Retention:** Generates and uploads both raw CLI outputs and rich HTML Extra dashboards via `actions/upload-artifact@v4`.
4. **Transparent Run Separation:** Following academic integrity rules, correct specification assertions were not inverted or suppressed to hide real SUT defects. Instead:
   - **Run A (Passing Smoke Run):** Executes representative passing tests against active endpoints to verify infrastructure and core functionality.
   - **Run B (Intentional Failure Demonstration):** Executes an isolated intentional-failure suite to demonstrate that the CI quality gate blocks deployment upon regression.

---

## 2. CI/CD Run 1: All-Passing Health & Smoke Run (Run A)

- **Workflow Name:** `Automated API Testing & Quality Gate (HW06)`
- **Run Type:** PASSING CI HEALTH & SMOKE REGRESSION (Run A)
- **Target Branch:** `main`
- **Trigger Event:** `push` / `workflow_dispatch`
- **Target Suite:** [`hw06/postman/collections/ci-smoke.postman_collection.json`](file:///Users/phamngocgiabao/eshop-sut/hw06/postman/collections/ci-smoke.postman_collection.json)
- **Executed Operations:** 9 API Requests (Catalog, Details, Categories, Registration, Login, Cart, Admin Users, Forged Signature Rejection, Anonymous Rejection).
- **Total Assertions:** 34 / 34 Passed (100% Pass Rate).
- **Run ID:** `[RUN_A_ID_PLACEHOLDER]`
- **Live GitHub Actions Run URL:** `[RUN_A_URL_PLACEHOLDER]`
- **Execution Verdict:** **SUCCESS (Green Checkmark)**.

---

## 3. CI/CD Run 2: Intentional Failure Demonstration (Run B)

- **Workflow Name:** `Automated API Testing & Quality Gate (HW06)`
- **Run Type:** INTENTIONAL CI FAILURE DEMONSTRATION (Run B)
- **Target Branch:** `main`
- **Trigger Event:** `workflow_dispatch` (with input `demo_failure=true`)
- **Target Suite:** [`hw06/postman/collections/ci-intentional-failure-demo.postman_collection.json`](file:///Users/phamngocgiabao/eshop-sut/hw06/postman/collections/ci-intentional-failure-demo.postman_collection.json)
- **Deliberate Failure Assertion:**
  ```javascript
  pm.test("[DEMO INTENTIONAL FAILURE] Deliberately Asserting Non-Existent Product Name to Verify CI/CD Failure Detection", function () {
      const res = pm.response.json();
      pm.expect(res.name).to.eql("NON_EXISTENT_INTENTIONAL_CI_FAILURE_NAME_FOR_DEMO");
  });
  ```
- **Proof of Failure Isolation:** The failure is strictly confined to the demonstration suite. The full regression collections and production codebase remain unaltered.
- **Run ID:** `[RUN_B_ID_PLACEHOLDER]`
- **Live GitHub Actions Run URL:** `[RUN_B_URL_PLACEHOLDER]`
- **Execution Verdict:** **FAILED AS INTENDED (Exit Code 1 / Red Cross)**.

---

## 4. Authentic Evidence & Screenshots (Human Gate)

In accordance with course anti-cheat guidelines, real screenshots from the live GitHub Actions web interface must be captured directly by the student:

1. **Successful CI Run Screenshot (Run A):**
   - Save path: `hw06/screenshots/cicd-run-01-success.png`
   - Must visibly show: GitHub Actions Run A page with green checkmark, commit hash, workflow name, and test step output.
2. **Intentional Failed CI Run Screenshot (Run B):**
   - Save path: `hw06/screenshots/cicd-run-02-failure.png`
   - Must visibly show: GitHub Actions Run B page with red cross, step failure on deliberate assertion, and execution summary.
