# INVESTIGATION PROMPT — STEPS 1–2 (TOON FORMAT, EXTREME, GENERALIZED)

**Purpose**
Collect all verifiable quantitative and qualitative information about a publicly traded company for **Steps 1 and 2**: Product / Value Proposition and Market / Industry Context. Assume no prior knowledge about the business. This prompt is built for an obsessive analyst who must deliver clean, evidence-backed outputs ready for financial modeling and scenario simulation.

> **No JSON outputs.** Use Markdown and CSV-style tables only. Every claim must cite primary evidence where possible.

---

## TOON PROMPT (YAML-style structure — ready to paste into an LLM)


## Sections (Detailed instructions for the agent)

### SECTION 1 — PRODUCT / VALUE PROPOSITION

**Goal:** Identify every product and revenue stream, measure unit economics and lock‑in, and expose cross‑BU subsidies or dependencies.

**Start with:** 50‑word summary (one per BU / major product).

**Evidence Cross‑Check (min 3 primary items per major BU):**

* 10‑K / 10‑Q product descriptions (cite page/section)
* Earnings call transcript excerpts (cite date, minute)
* Official product pages, developer docs, and press releases (cite exact quote)

**Required table (CSV + Markdown)**
Columns (one row per Revenue Stream):

```
BU_ID | ProductID | ProductName | IndustryVertical | RevenueStreamID | RevenueStreamName | RevenueStreamType (Ads/Subscription/License/Transaction/Other) | RevenueStreamActive (Y/N) | %RevenueFYCurrent | MarginEstimate | MonthlyActiveUsers | GrowthYoY_1y | GrowthYoY_3y | GrowthYoY_5y | MonetizationMaturity(1-5) | MoatType | MoatScore(1-10) | TechDebtScore(1-10) | EvidenceLink
```

**Deep analysis (≤700 words per BU)**

* Product architecture and delivery model
* Value network and who captures value
* Data roll‑up / data moat mechanics
* LTV / CAC by customer segment (or proxies with assumptions)
* Marginal cost profile and leverage points
* Pricing power and elasticity signs
* Cross‑BU internal transfers and subsidy rules (how internal accounting allocates costs/revenues)

**Red Flags (prioritized)**

* Example entries: "High churn in subscription stream", "MAU decline 8 quarters" — give priority and action (e.g., "investigate retention cohorts and policy changes").

**Pending tasks (examples)**

* Scrape SDK usage and install base data, collect App Store update cadence, collect changelogs, capture developer forum complaints.

### SECTION 2 — MARKET / INDUSTRY CONTEXT

**Goal:** For each industry vertical the company touches, produce a robust TAM/SAM/SOM estimate, growth profile, regulatory and pricing risks.

**Start with:** 50‑word summary per vertical (top 3 detailed; aggregate the rest).

**Evidence Cross‑Check:**

* Market research (Gartner, IDC, Statista), regulator filings, antitrust filings, industry association reports, public investor decks.

**Required table (per vertical)**

```
VerticalID | VerticalName | TAM($) | SAM($) | SOM_EST($) | GrowthCY% | 3yrCAGR | ARPU assumptions | PricingDynamics | RegulationRisk(0-10) | KeyAssumptions | EvidenceLink
```

**Analysis (≤700 words per vertical)**

* Top‑down and bottom‑up estimates (show calculation steps and assumptions)
* Sensitivity checks (price, adoption, ARPU scenarios)
* Maturity curve (S‑curve) and competitive intensity
* Regulatory pressure points and timelines (e.g., pending antitrust actions, data privacy laws)

**Red Flags**

* Overstated TAM without clear adoption path, near‑term regulatory headwinds, commoditizing pricing.

**Pending tasks (examples)**

* Acquire vertical reports, extract methodology notes, compile analyst consensus growth rates.

### SECTION 6 — MANAGEMENT, EXECUTION QUALITY & STRATEGIC COHERENCE

**Goal:** Determine whether leadership can execute the multi‑BU strategy and allocate capital optimally.

**Start with:** 50‑word summary covering CEO + top management cohesion.

**Evidence Cross‑Check:**

* Exec bios, Form 4 filings, proxy statements, shareholder letters, major interviews, conference presentations.

**Required table**

```
ExecID | Name | Role | BU_Oversight | TenureYears | PriorCompanies | NotableWins | NotableMisses | CredibilityScore(1-10) | StrategicClarityScore(1-10) | CompensationStructure | InsiderOwnership% | EvidenceLink
```

**Analysis (≤700 words)**

* Track record: successes & failures in similar scale situations
* Capital allocation history: R&D vs SG&A, buybacks, M&A (good deals vs poor deals)
* Signals from hiring & layoffs (hiring velocity, talent poaching, attrition)
* Governance posture: board independence, audit/comp committees, poison pill/dual class shares
* Incentive alignment (vesting schedules, performance hurdles, option loads)

**Red Flags**

* Frequent reorganizations indicating strategic drift; high exec churn; insider selling not explained by diversification.

**Pending tasks (examples)**

* Scrape Form 4s, proxy statements, board meeting minutes (if public), conference Q&A transcripts.

---

## OUTPUT FORMAT (what to deliver)

For each section produce:

1. **Summary** (≤50 words)
2. **Evidence Cross‑Check** (3–10 primary sources with exact quotes and links)
3. **CSV Table** (as specified above)
4. **Detailed analysis** (≤700 words, numbered bullets, each bullet must cite evidence)
5. **Red Flags** table with priority, estimated probability, % impact on revenue/EBITDA, recommended action
6. **Task list** for gaps: source, priority, estimated time & cost
7. **Deliverables**: downloadable CSV + Markdown report (ready to feed Step 7)

## USAGE / EXECUTION NOTES

1. Insert the company's ticker (e.g., "GOOGL").
2. Run web scraping on SEC filings, earnings transcripts, product pages, app stores, developer forums, market reports, press.
3. If any primary data is unavailable, do not infer silently — flag as "INFERRED" and include assumptions and confidence level.
4. Deliver outputs in Markdown (human readable) and CSV tables (machine friendly).

---
