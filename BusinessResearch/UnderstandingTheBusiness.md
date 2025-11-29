```toon
task: "Investigate a publicly traded company with obsessive rigor for Steps 1, 2, and 6"
scope:
  - Steps:
      - "Section 1 — Product / Value Proposition"
      - "Section 2 — Market / Industry Context"
      - "Section 6 — Management, Execution Quality & Strategic Coherence"
  - CompanyTicker: INSERT_TICKER_HERE
purpose: |
  Collect complete quantitative and qualitative evidence for the target company with zero prior assumptions. Outputs must be clean, evidence-backed artifacts that can plug directly into financial models and scenario simulations.
constraints:
  - "No JSON outputs; only Markdown-style tables are allowed."
  - "Every claim must cite primary evidence (source, date, quote, URL)."
  - "Assume total ignorance about the business and re-derive everything from filings and field evidence."
instructions:
  - Adopt the mindset of an extreme hedge-fund analyst: one allowable mistake per 1,000 investments.
  - Use web search, SEC filings, earnings transcripts, product pages, developer docs, press releases, developer forums, app stores, and analyst / market reports.
  - Segment all findings by Business Unit (BU), Product, Revenue Stream, Customer Segment, and Industry Vertical.
  - Start each major section with a 50-word plain-English summary.
  - Provide both Markdown-readable and formatted tables (copy/paste friendly) matching the schemas below.
  - If any primary data is unavailable, mark the datapoint as INFERRED, state the assumption and confidence, and queue it in the pending tasks list.
  - Highlight red flags with priority, probability, business impact, and recommended mitigation.
  - Outputs must be ready-to-ship Markdown tables.
outputFormat:
  - summary(maxWords:50 per section)
  - evidenceCrossCheck(3-10 primary quotes + URLs per section)
  - tables(markdown schemas listed under each section)
  - detailedAnalysis(bullets ≤700 words, each citing evidence)
  - redFlags(priority, probability, impact%, action)
  - tasksPending(source, priority, effort/time, cost)
  - deliverables(Markdown artifacts ready for Step 7)
sections:
  - sectionId: SECTION 1 — PRODUCT / VALUE PROPOSITION
    goal: Identify every product and revenue stream, evaluate unit economics, lock-in, and cross-BU subsidies.
    startWith: 50-word summary per BU / major product.
    evidenceCrossCheck:
      - "10-K / 10-Q product descriptions (cite page/section)"
      - "Earnings call transcript excerpts (cite date + minute)"
      - "Official product pages, developer docs, press releases (exact quote)"
    requiredTable:
      description: "One row per revenue stream (Markdown)."
      schema: |
        BU_ID | ProductID | ProductName | IndustryVertical | RevenueStreamID | RevenueStreamName | RevenueStreamType (Ads/Subscription/License/Transaction/Other) | RevenueStreamActive (Y/N) | %RevenueFYCurrent | MarginEstimate | MonthlyActiveUsers | GrowthYoY_1y | GrowthYoY_3y | GrowthYoY_5y | MonetizationMaturity(1-5) | MoatType | MoatScore(1-10) | TechDebtScore(1-10) | EvidenceLink
    analysisTopics:
      - Product architecture and delivery model
      - Value network participation and value capture
      - Data roll-up / moat mechanics
      - LTV vs CAC by customer segment (or proxy assumptions)
      - Marginal cost profile and leverage points
      - Pricing power / elasticity signals
      - Cross-BU internal transfers and subsidy mechanics
    redFlagsExamples:
      - High churn in subscription stream → investigate retention cohorts
      - MAU decline across 8 quarters → review policy or UX regressions
    pendingTasksExamples:
      - Scrape SDK usage and install base data
      - Collect App Store update cadence + changelog diffs
      - Capture developer forum complaints and feature requests

  - sectionId: SECTION 2 — MARKET / INDUSTRY CONTEXT
    goal: Build TAM/SAM/SOM, growth, regulatory and pricing risk profiles per vertical.
    startWith: 50-word summary per vertical (detail top 3, aggregate the rest).
    evidenceCrossCheck:
      - "Market research (Gartner, IDC, Statista)"
      - "Regulator and antitrust filings, industry association reports"
      - "Public investor decks and comparable company disclosures"
    requiredTable:
      description: "One table per vertical (Markdown)."
      schema: |
        VerticalID | VerticalName | TAM($) | SAM($) | SOM_EST($) | GrowthCY% | 3yrCAGR | ARPU assumptions | PricingDynamics | RegulationRisk(0-10) | KeyAssumptions | EvidenceLink
    analysisTopics:
      - Top-down and bottom-up sizing with explicit formulas
      - Sensitivity checks (price, adoption, ARPU scenarios)
      - S-curve / maturity stage and competitive intensity
      - Regulatory pressure points, timing, and enforcement bodies
    redFlagsExamples:
      - TAM inflation without adoption pathway
      - Immediate regulatory headwinds or pricing commoditization
    pendingTasksExamples:
      - Acquire missing vertical reports + methodology notes
      - Compile analyst consensus growth rates and compare deltas

  - sectionId: SECTION 6 — MANAGEMENT, EXECUTION QUALITY & STRATEGIC COHERENCE
    goal: Determine leadership’s ability to execute multi-BU strategy and allocate capital optimally.
    startWith: 50-word summary covering CEO and top-team cohesion.
    evidenceCrossCheck:
      - Exec bios, Form 4 filings, proxy statements
      - Shareholder letters, major interviews, conference presentations
    requiredTable:
      description: "Management quality dataset (Markdown)."
      schema: |
        ExecID | Name | Role | BU_Oversight | TenureYears | PriorCompanies | NotableWins | NotableMisses | CredibilityScore(1-10) | StrategicClarityScore(1-10) | CompensationStructure | InsiderOwnership% | EvidenceLink
    analysisTopics:
      - Track record vs company scale analogs
      - Capital allocation history (R&D vs SG&A, buybacks, M&A quality)
      - Hiring/layoff signals (velocity, poaching, attrition)
      - Governance posture (board, committees, poison pill / dual class)
      - Incentive alignment (vesting, performance hurdles, option load)
    redFlagsExamples:
      - Frequent reorganizations signaling strategic drift
      - Executive churn or unexplained insider selling
    pendingTasksExamples:
      - Scrape Form 4s, proxy statements, board minutes (if public)
      - Compile conference Q&A transcripts for leadership consistency

execution:
  - Insert the company ticker (e.g., GOOGL) and kick off data collection immediately.
  - Run parallel scraping of SEC filings, earnings transcripts, product assets, app stores, developer forums, market reports, and press.
  - For missing data, classify as INFERRED with confidence and document in tasks.
  - Deliver a single combined Markdown report for every required table.
  - Ensure each bullet in the analyses cites its evidence row.
  - Maintain linkage between summaries, tables, analyses, red flags, and pending tasks for cross-audit.
```
