import re
from collections import defaultdict

def load_statements(file_path):
    """Load statements from the text file"""
    statements = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and re.match(r'^\d+\.', line):
                # Extract the statement after the number
                statement = re.sub(r'^\d+\.\s*', '', line)
                statements.append(statement)
    return statements

def analyze_sentiment(statement):
    """
    Analyze sentiment of a statement using keyword-based approach
    Returns: 'bullish', 'bearish', or 'neutral'
    """
    # Weighted lexicons (you can tune these scores)
    bullish_weights = {
        'insanely strong': 2.0,
        'monster': 1.8,
        'blowout': 1.8,
        'massive': 1.5,
        'exploding': 1.5,
        'historic': 1.5,
        'strong': 1.2,
        'growth': 1.2,
        'bullish': 1.5,
        'undervalued': 1.3,
        'oversold': 1.3,
        'accelerating': 1.3,
        'robust': 1.2,
        'rally': 1.2,
        'solid': 1.0,
        'beat': 1.2,
        'surged': 1.3,
        'soar': 1.4,
        'terrific': 1.4,
        'juicy': 1.3,
        'upside': 1.2,
        'up': 0.8,
        'higher': 1.0,
        'exceptional': 1.5,
        'impressive': 1.2,
        'opportunity': 0.9,
        'long-term': 0.8,
        'investing': 0.7,
        'smart': 0.7,
        'dominance': 0.9,
        'revolution': 1.0,
        'intact': 0.6,
        'better': 0.8,
        'reasonable': 0.6,
        'upgrade': 0.9,
        'stronger': 1.0,
        'wins': 1.2,
    }

    bearish_weights = {
        'bearish': -1.5,
        'overvalued': -1.3,
        'bubble': -1.4,
        'fears': -1.0,
        'concerns': -1.0,
        'concern': -0.8,
        'drop': -1.1,
        'down': -0.9,
        'fall': -1.0,
        'decline': -1.0,
        'pullback': -0.9,
        'dip': -0.8,
        'red': -0.7,
        'pressure': -0.7,
        'reversal': -0.7,
        'challenges': -0.9,
        'threat': -1.1,
        'shed': -0.9,
        'wobble': -0.7,
        'short': -0.8,
        'risk': -0.8,
        'uncertainty': -1.0,
        'fade': -0.8,
        'damage': -1.0,
        'misinterpreted': -0.7,
        'overstated': -0.6,
        'way too high': -1.1,
        'hot': -0.6,
        'pump dump': -1.3,
    }

    # Negation terms and simple tokenization
    negations = {"not", "no", "never", "isn't", "wasn't", "aren't", "don't", "doesn't", "didn't", "can't", "won't"}

    text = statement.lower()

    # First handle multi-word phrases explicitly so they don't get split
    score = 0.0
    used_spans = []

    def consume_phrase(phrase, weight_dict):
        nonlocal text, score, used_spans
        start = 0
        while True:
            idx = text.find(phrase, start)
            if idx == -1:
                break
            end = idx + len(phrase)
            used_spans.append((idx, end, weight_dict[phrase]))
            start = end

    for phrase in list(bullish_weights.keys()) + list(bearish_weights.keys()):
        if " " in phrase:
            if phrase in bullish_weights:
                consume_phrase(phrase, bullish_weights)
            else:
                consume_phrase(phrase, bearish_weights)

    # Sort spans so we can skip them during word-level scanning
    used_spans.sort(key=lambda x: x[0])

    # Apply phrase scores (negation handling: look 3 words back for a negation)
    def has_negation_before(idx):
        window = text[max(0, idx - 80):idx]  # crude character window
        return any(neg in window.split() for neg in negations)

    for start, end, w in used_spans:
        if has_negation_before(start):
            score -= w  # flip
        else:
            score += w

    # Now scan word-level tokens, skipping characters inside phrase spans
    tokens = re.findall(r"\w+'\w+|\w+", text)

    # Simple sliding negation window over tokens
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in negations:
            # Look at the next token for sentiment
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if next_token in bullish_weights:
                    score -= bullish_weights[next_token]
                elif next_token in bearish_weights:
                    score -= bearish_weights[next_token]
            i += 1
            continue

        if token in bullish_weights:
            score += bullish_weights[token]
        elif token in bearish_weights:
            score += bearish_weights[token]

        i += 1

    # Map continuous score to discrete label with a neutral band
    bullish_threshold = 0.6
    bearish_threshold = -0.6

    if score >= bullish_threshold:
        return 'bullish'
    if score <= bearish_threshold:
        return 'bearish'
    return 'neutral'

def main():
    """Main function for quick analysis"""
    file_path = "index.txt"
    statements = load_statements(file_path)
    
    sentiment_counts = defaultdict(int)
    neutral_statements = []
    
    for i, statement in enumerate(statements, 1):
        sentiment = analyze_sentiment(statement)
        sentiment_counts[sentiment] += 1
        if sentiment == 'neutral':
            neutral_statements.append((i, statement))
    
    total_statements = len(statements)
    bullish_count = sentiment_counts['bullish']
    bearish_count = sentiment_counts['bearish']
    neutral_count = sentiment_counts['neutral']
    
    print("BULLISH/BEARISH RATIO ANALYSIS")
    print("=" * 40)
    print(f"Total statements: {total_statements}")
    print(f"Bullish: {bullish_count} ({(bullish_count/total_statements)*100:.1f}%)")
    print(f"Bearish: {bearish_count} ({(bearish_count/total_statements)*100:.1f}%)")
    print(f"Neutral: {neutral_count} ({(neutral_count/total_statements)*100:.1f}%)")
    print()
    
    if bearish_count > 0:
        ratio = bullish_count / bearish_count
        print(f"Bullish:Bearish Ratio = {ratio:.2f}:1")
    else:
        print("Bullish:Bearish Ratio = Infinite (no bearish statements)")
    
    if (bullish_count + bearish_count) > 0:
        bullish_percentage = (bullish_count / (bullish_count + bearish_count)) * 100
        print(f"Bullish % (excluding neutral): {bullish_percentage:.1f}%")
    
    print("\n" + "=" * 40)
    print("NEUTRAL STATEMENTS:")
    print("=" * 40)
    
    for num, statement in neutral_statements:
        print(f"{num}. {statement}")

if __name__ == "__main__":
    main()
