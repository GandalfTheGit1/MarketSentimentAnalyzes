task:
  name: “Sentiment collection and breakdown for NVDA”
  date_range: 2025-11-20 → 2025-11-28
  target_company: NVDA
  sources: [Reddit, X]
  min_samples: 200
  table_schema:
    - id
    - date
    - platform
    - user_id
    - opinion_sentence
    - sentiment_label
    - reason_category
    - reason_text
  reason_categories: [Earnings, Product/Tech, Competition, Valuation, Macro, MarketPsychology, Risk, Other]

samples[min_samples]{id,date,platform,user_id,opinion_sentence,sentiment_label,reason_category,reason_text}:
  …  # Fill rows here

analysis:
  sentiment_breakdown:
    bullish_percent:
    neutral_percent:
    bearish_percent:
  key_reasons_bullish: [top5 categories with counts]
  key_reasons_bearish: [top5 categories with counts]
  common_misconceptions:
    – “”
  summary:
    “”  # A concise judgment: bullish or bearish?

instructions:
  – Use only actual user posts (no made-up ones).
  – Each opinion_sentence must be 10 to 20 words long.
  – Sentiment_label must be exactly one of {Bullish, Neutral, Bearish}.
  – reason_text must be 25 to 40 words long.
  – After samples table, produce the analysis section.  
  – If fewer than 200 valid samples exist, report actual number and proceed with available data.

end_task
