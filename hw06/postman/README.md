# FR-01: Postman Automated Test Suite

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Course:** Software Testing (HCMUS) — HW06 API Testing
> - **Target Feature:** FR-01 — Account Registration (`POST /api/register`)

---

## Directory Structure

```text
hw06/postman/
├── collections/
│   └── fr01-registration.postman_collection.json   # 42 API requests (37 reviewed AI + 5 extensions)
├── environments/
│   └── eshop-local.postman_environment.json         # baseUrl: http://localhost:3000, studentId: 23127027
├── data/                                            # Data files for data-driven testing
├── scripts/
│   ├── generate_collection.py                       # Automated generator for Postman collection
│   ├── validate_collection.py                       # Pre-execution validation suite
│   └── verify-sec01-plaintext.js                    # Non-API SEC-01 SQLite DB inspection probe
└── README.md
```

---

## Central `X-Student-Id` Injection

All API requests automatically carry the required course identification header:
```http
X-Student-Id: 23127027
```
This is injected centrally at the collection root via a pre-request script:
```javascript
pm.request.headers.upsert({
    key: "X-Student-Id",
    value: pm.environment.get("studentId") || "23127027"
});
```
Every request contains an automated test assertion confirming presence and accuracy of this header.

---

## Execution Instructions

### 1. Start Backend SUT
```bash
cd backend
npm start  # or node server.js
```
Confirm server is listening on `http://localhost:3000`.

### 2. Execute via Newman (CLI & HTML Report)
```bash
npx -y -p newman -p newman-reporter-htmlextra newman run \
  hw06/postman/collections/fr01-registration.postman_collection.json \
  -e hw06/postman/environments/eshop-local.postman_environment.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export hw06/newman/fr01/fr01-report.html
```

### 3. Execute SEC-01 Non-API Database Inspection
```bash
node hw06/postman/scripts/verify-sec01-plaintext.js
```
