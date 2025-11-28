# Task: monitor social sentiment & drivers for listed public companies and return a short human summary (<3 minutes read)
task:
  name: social_sentiment_and_drivers
  description: "Scan public social sources to find opinions, narratives, and short signals that could move each company's public perception or stock. Produce a concise summary per company."

companies[4]: Alphabet (Google), Synopsys, Apple, Broadcom

sources[6]{platform,sample_count,notes}:
  X,2000,high-reach tweets + replies
  Reddit,1000,subreddits: r/stocks,r/investing,r/technology,r/semiconductors
  Polymarket,500,markets & comments
  StockTwits,500,investor posts
  HackerNews,200,tech discussion + threads
  NewsSocial,300,public headlines & comment threads (high-engagement)

analysis:
  timeframe: last_3_days
  language: english
  deduplicate_similar_posts: true
  rank_by: recency,engagement,author_credibility
  sample_goal: "large sample; prioritize highly engaged content but include long-tail voices"

aggregation:
  sentiment_scale: -1..1
  compute: "overall_sentiment, %positive, %negative, %neutral, weighted_by_engagement"
  narratives: top_2_by_volume_and_velocity
  signals: top_1_immediate_signal (reason + estimated impact: low/med/high)
  quote_example: short example quote (<=12 words) supporting each narrative

output:
  format: plain_english
  style: terse, direct
  max_total_words: 220
  per_company: 6_lines_max
  fields{sentiment_label,score,narratives,quotes,signals,impact,market_movement,last_3d_price_action}

instructions:
  - Use posts, comments, market polls and invested positions where public.
  - For Reddit include both OP and top 3 comment threads by score.
  - For X include original tweet + top 2 replies by engagement.
  - Remove bot/spam clusters; aggregate similar narratives once.
  - Include market_movement and last_3d_price_action retrieved from market data.
  - If sample is insufficient for a company, say "insufficient sample".
  - Keep final summary extremely brief: each company ≤6 lines; whole answer readable <3 minutes.

response_template:
  - Company: <NAME>
    - Sentiment: <Bullish|Bearish|Neutral> (score: <-1..1>)
    - Narratives:
        1) <short label> — <2-8 word quote>
        2) <short label> — <2-8 word quote>
    - Market movement (3d): <up|down|flat> — <% change>
    - Top signal: <signal_text> (impact: <low|med|high>)
    - Action: <watch|buy|sell|no action>

end