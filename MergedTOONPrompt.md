```toon
task: "Investigate a publicly traded company's products and market context with maximum depth and rigor"

scope:
  - CompanyTicker: INSERT_TICKER_HERE
  - Coverage: Steps 1, 2, and 6 from the master TOON specification (include their text verbatim in the section noted below).

outputFormat:
  - summary(maxWords:50 per section)
  - detailedSections:
      - sectionTitle
      - evidenceCrossCheck(list of sources with quotes & URLs)
      - tables(Markdown)
      - detailedAnalysis(bullets, ≤700 words)
      - redFlags(prioritized: High/Medium/Low)
      - tasksPending(list with priority & estimated cost)
      - deliverables(Markdown ready)
  - Combined final Markdown report

instructions:
  - Adopt the mindset of a senior hedge-fund analyst: extreme skepticism; at most one mistake per 1,000 investments.
  - Assume zero prior knowledge; gather evidence from web search, SEC filings, earnings transcripts, product documentation, market reports, press releases, developer forums, app stores, and analyst reports.
  - Segment research by Business Unit (BU), Product, Revenue Stream, Customer Segment, and Industry Vertical.
  - Evaluate each product and revenue stream separately, starting each section with a plain-English 50-word summary.
  - Provide Markdown tables with 5-year historical trends where available.
  - For every factual claim include a cross-check entry: (source, date, exact quote or number, URL).
  - For each BU or vertical deliver: 50-word summary, evidence cross-check table, markdown table, ≤700-word deep analysis, Red Flags table, Pending Tasks list.
  - Highlight Red Flags and recommend immediate remedial actions.
  - If data is missing, classify as INFERRED, state assumptions plus confidence, and add the gap to the pending tasks list (what to fetch, where, priority, estimated effort/cost).
  - Structures must use Markdown tables only—no JSON.
  - Use Markdown headings and bullets suitable for direct inclusion in a report.

sectionsToEmbedVerbatim:
<<< INSERT THE TEXT OF SECTION 1, SECTION 2, AND SECTION 6 FROM THE MASTER TOON SPECIFICATION HERE >>>

execution:
  1. Run the full investigation now with extreme rigor.
  2. Ensure every section references its supporting evidence via the cross-check table.
  3. Conclude with a single combined Markdown report containing:
      1. Section summaries (≤50 words each)
      2. Evidence cross-check tables (quotes + URLs)
      3. Required Markdown tables from Section 1, 2, and 6
      4. Detailed analyses (≤700 words each)
      5. Red Flags table
      6. Pending tasks list
      7. Ready-to-use Markdown deliverables
```