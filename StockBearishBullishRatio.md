task:
  name: “Public sentiment analysis for NVDA (Nov 20-Nov 28 2025)”
  target_ticker: “NVDA”
  sources: [“Reddit”, “X”]
  date_range: “2025-11-20 → 2025-11-28”
  minimum_samples: 200

schema:
  - id
  - date
  - platform
  - user_handle
  - likes_count            # integer number of likes/up-votes on the post
  - opinion_sentence        # 10-20 words
  - sentiment_label         # one of [Bullish, Neutral, Bearish]
  - reason_category         # one of [Earnings, Product/Tech, Competition, Valuation, Macro, MarketPsychology, Risk, Other]
  - reason_text             # 25-40 words explaining why

data:
  samples[min_samples]{id,date,platform,user_handle,likes_count,opinion_sentence,sentiment_label,reason_category,reason_text}:
    …  # collected entries

analysis:
  sentiment_breakdown:
    bullish_percent:
    neutral_percent:
    bearish_percent:
  likes_statistics:
    average_likes:
    likes_standard_deviation:
  top_reasons_bullish: [ {reason_category, count} … top 5 ]
  top_reasons_bearish: [ {reason_category, count} … top 5 ]
  common_misconceptions: [ “…” … ]
  summary: “(Concise verdict: Bullish or Bearish and why)”

instructions:
  – Pull actual posts from Reddit and X in the date range.
  – Each opinion_sentence must be 10-20 words long.
  – Each reason_text must be 25-40 words long.
  – Include the actual likes_count for each post.
  – After the data table, compute average_likes and standard deviation of likes across all samples.
  – Output the full table first, then the analysis section.
  – If fewer than 200 samples available, report actual count and proceed with available data.

end_task
