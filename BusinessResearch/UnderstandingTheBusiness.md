```toon
task: "Investigate a publicly traded company with obsessive rigor for Steps 1, 2, and 3"
scope:
  - CompanyTicker: GOOGL
  - Date: December 1st, 2025.
  - OutputLang: English
  - Steps:
      - "Section 1 — Product / Value Proposition"
      - "Section 2 — Market / Industry Context"
      - "Section 3 — Management, Execution Quality & Strategic Coherence"
purpose: |
  Collect complete quantitative and qualitative evidence for the target company with zero prior assumptions. Outputs must be clean, evidence-backed artifacts that can plug directly into financial models and scenario simulations.
constraints:
  - "No JSON outputs; only Markdown-style tables are allowed."
  - "Every claim must cite primary evidence (source, date, quote, URL)."
  - "Assume total ignorance about the business and re-derive everything from filings and field evidence."
  - "All content must appear under the specified numbered headings. No extra sections or free text outside the defined structure."
  - "For any INFERRED value in a table cell, append ' (INFERRED, confidence=X%)' and explain the assumption in the nearest KeyAssumptions field."
instructions:
  - Adopt the mindset of an extreme hedge-fund analyst: one allowable mistake per 1,000 investments.
  - Use web search, SEC filings, earnings transcripts, product pages, developer docs, press releases, developer forums, app stores, and analyst/market reports.
  - Segment all findings by Business Unit (BU), Product, Revenue Stream, Customer Segment, and Industry Vertical.
  - Start each major section with a 50-word investment summary explaining why an investor should or should not invest in the company based on that section's findings.
  - Provide both Markdown-readable and formatted tables (copy/paste friendly) matching the schemas below.
  - If any primary data is unavailable, perform web search to find the information. Only mark as INFERRED as last resort when no information can be found through web search.
  - Highlight red flags with priority, probability, business impact, and recommended mitigation.
  - Outputs must be ready-to-ship Markdown tables.
outputFormat:
  - reportLayout:
      - "# Company Overview (GOOGL)"
      - "## Section 1 — Product / Value Proposition"
      - "## Section 2 — Market / Industry Context"
      - "## Section 3 — CEO / Management, Execution Quality & Strategic Coherence"
  - sectionTemplate:
      - "### 1.1 Investment Summary (≤50 words)"
      - "### 1.2 Evidence Cross-Check"
      - "### 1.3 Revenue Streams Table"
      - "### 1.4 Detailed Analysis"
      - "### 1.5 Red Flags"
  - summary(maxWords:50 per section)
  - evidenceCrossCheck(3-10 primary quotes + URLs per section)
  - tables(markdown schemas listed under each section)
  - detailedAnalysis(bullets ≤700 words, each citing evidence)
  - redFlags(priority, probability, impact%, action)
  - deliverables(Markdown artifacts ready for Step 7)
sections:
  - sectionId: SECTION 1 — PRODUCT / VALUE PROPOSITION
    goal: Identify every product and revenue stream, evaluate unit economics, lock-in, and cross-BU subsidies.
    startWith: 50-word summary per BU / major product.
    outputStructure:
      - "### 1.1 Investment Summary (≤50 words)"
      - "### 1.2 Evidence Cross-Check"
      - "### 1.3 Revenue Streams Table"
      - "### 1.4 Detailed Analysis"
      - "### 1.5 Red Flags"
    evidenceCrossCheck:
      - "10-K / 10-Q product descriptions (cite page/section)"
      - "Earnings call transcript excerpts (cite date + minute)"
      - "Official product pages, developer docs, press releases (exact quote)"
    requiredTable:
      description: "One row per revenue stream (Markdown)."
      heading: "#### Table 1.3.1 — Revenue Streams by Business Unit"
      schema: |
        Product Name | Industry Vertical | Revenue Stream Name | Revenue Stream Type (Ads/Subscription/License/Transaction/Other) | %Revenue FY Current | Margin Estimate | Monthly Active Users | Growth YoY 1y | Growth YoY 3y | Growth YoY 5y | Monetization Maturity(1-5) | Moat Type | Moat Score (1-10) | Tech Debt Score (1-10)
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

  - sectionId: SECTION 2 — MARKET / INDUSTRY CONTEXT
    goal: Build TAM/SAM/SOM, growth, regulatory and pricing risk profiles per vertical.
    startWith: 50-word summary per vertical (detail top 3, aggregate the rest).
    outputStructure:
      - "### 2.1 Investment Summary (≤50 words)"
      - "### 2.2 Evidence Cross-Check"
      - "### 2.3 Market Sizing Tables"
      - "### 2.4 Detailed Analysis"
      - "### 2.5 Red Flags"
    evidenceCrossCheck:
      - "Market research (Gartner, IDC, Statista)"
      - "Regulator and antitrust filings, industry association reports"
      - "Public investor decks and comparable company disclosures"
    requiredTable:
      description: "One table per vertical (Markdown)."
      heading: "#### Table 2.3.1 — Market Sizing for [VerticalName]"
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

  - sectionId: SECTION 3 — MANAGEMENT, EXECUTION QUALITY & STRATEGIC COHERENCE
    goal: Determine CEO's ability to execute multi-BU strategy and allocate capital optimally.
    startWith: 50-word summary covering CEO background, leadership style, and track record.
    outputStructure:
      - "### 3.1 Investment Summary (≤50 words)"
      - "### 3.2 Evidence Cross-Check"
      - "### 3.3 CEO Profile Table"
      - "### 3.4 Detailed Analysis"
      - "### 3.5 Red Flags"
    evidenceCrossCheck:
      - CEO biography, interviews, shareholder letters
      - CEO conference presentations and major public statements
      - CEO's career history and previous companies
    requiredTable:
      description: "CEO profile dataset (Markdown)."
      heading: "#### Table 3.3.1 — CEO Profile"
      schema: |
         Name | Tenure Years | Prior Companies | Notable Wins | Notable Misses | Leadership Style | Strategic Clarity Score (1-10) | Compensation Structure | Insider Ownership % | Evidence Link
    analysisTopics:
      - CEO's career progression and leadership development
      - CEO's strategic vision and communication consistency
      - CEO's capital allocation decisions and M&A track record
      - CEO's crisis management and turnaround experience
      - CEO's industry reputation and peer recognition
    redFlagsExamples:
      - CEO's inconsistent strategic messaging over time
      - CEO's lack of relevant industry experience
      - CEO's poor track record in previous leadership roles

execution:
  - Insert the company ticker (e.g., GOOGL) and kick off data collection immediately.
  - Run parallel scraping of SEC filings, earnings transcripts, product assets, app stores, developer forums, market reports, and press.
  - For missing data, first perform web search to find the information. Only classify as INFERRED if no information can be found through web search, then state the assumption and confidence and document in tasks.
  - Deliver a single combined Markdown report for every required table.
  - Ensure each bullet in the analyses cites its evidence row.
  - Maintain linkage between summaries, tables, analyses, red flags, and pending tasks for cross-audit.
```