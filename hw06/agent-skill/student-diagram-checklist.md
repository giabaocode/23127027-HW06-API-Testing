# Human Architecture Diagram — Student Design Guide & Checklist

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Deliverable:** `hw06/agent-skill/student-diagram.png`
> - **Academic Integrity Rule:** In strict accordance with the official HW06 PDF Section 14 (Deliverables) and Anti-Cheat Gate 3, this diagram **MUST BE SELF-DRAWN / HAND-CONSTRUCTED BY THE STUDENT** using a diagramming tool (such as Draw.io, Excalidraw, Figma, or pen-and-paper). AI image generation and AI Mermaid diagram rendering are strictly prohibited for this deliverable.

---

## 1. Required Architecture Components to Draw

Your diagram should visually represent the complete end-to-end pipeline of the **API Test Case Generator Agent Skill** (`hw06/agent-skill/test_generator.py`). Be sure to include the following 6 core blocks:

1. **Input Specification Ingestion:**
   - Box/Block: `Endpoint Specification (JSON / YAML)`
   - Sub-items: Route URL, HTTP Method, Authentication Level (`public` / `user` / `admin`), Parameter Schema.
2. **Deterministic Partitioning Engine:**
   - Box/Block: `Equivalence Partitioning (EP) & Boundary Value Analysis (BVA)`
   - Sub-items: Nominal Generator, Mandatory Field Omisssion, Boundary Range Extractor (min, max, sub-min, super-max), Type Confusion.
3. **Security & Authorization Mutation Injector:**
   - Box/Block: `Security Probe Synthesizer (SEC-02 & SEC-03)`
   - Sub-items: Missing Token, Expired Token, Forged Cryptographic Signature, Privilege Escalation (Standard User $\rightarrow$ Admin Route), Role Claim Mutation (Uppercase / Whitespace / Array).
4. **Oracle Decoupling & Calibration Layer:**
   - Box/Block: `Formal Oracle Calibration Engine`
   - Sub-items: Semantic Business Outcome (`STATE_MUTATED`, `ACCESS_DENIED`) separated from HTTP Status (`SPECIFIED`, `INFERRED`, `UNKNOWN`). Dual-assertion side-effect verification.
5. **Output Generation & Export:**
   - Box/Block: `Multi-Format Test Exporter`
   - Sub-items: Structured Test Case Register (Markdown), Postman Collection v2.1.0 Items, Excel Data Matrix.
6. **Execution & Feedback Loop:**
   - Box/Block: `Newman CLI / Runtime Verification`
   - Arrow: Newman reports feedback to refine test vectors upon discovering SUT defects.

---

## 2. Key Relationships & Data Flow to Illustrate

- **Flow 1 (Input to Engine):** The raw API contract flows into the EP/BVA Engine and Security Injector in parallel.
- **Flow 2 (Partitions to Calibration):** Generated raw test vectors pass into the Oracle Calibration Engine to assign formal semantic outcomes.
- **Flow 3 (Dual-Assertion Link):** Destructive/mutation probes branch into a primary request and a secondary state verification query.
- **Flow 4 (Output):** Calibrated test cases are exported into Postman JSON and the Master Excel workbook.

---

## 3. Human Completion Checklist

- [ ] **Tool Selected:** Draw.io, Excalidraw, Miro, or hand drawing.
- [ ] **All 6 Core Blocks Visible:** Input, EP/BVA Engine, Security Injector, Oracle Calibration, Output Exporter, Runtime Loop.
- [ ] **Student Identity Displayed:** Include a small text box in the diagram corner:
  ```text
  Student: Phạm Ngọc Gia Bảo (ID: 23127027)
  Agent Skill Architecture — HW06 API Testing
  ```
- [ ] **Clear Directional Arrows:** Show clear data flow arrows from input to execution.
- [ ] **Saved to Target Path:** Export as PNG to:
  ```text
  hw06/agent-skill/student-diagram.png
  ```
