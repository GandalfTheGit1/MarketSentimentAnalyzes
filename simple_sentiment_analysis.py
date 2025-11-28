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
    bullish_keywords = [
        'strong', 'growth', 'bullish', 'undervalued', 'oversold', 'accelerating', 
        'robust', 'monster', 'rally', 'solid', 'beat', 'blowout', 'surged',
        'massive', 'jumped', 'soar', 'terrific', 'juicy', 'beast mode', 'up',
        'rise', 'higher', 'exceptional', 'impressive', 'rebounds', 'opportunity',
        'long-term', 'investing', 'smart', 'dominance', 'revolution', 'intact',
        'protect', 'better', 'reasonable', 'upgrade', 'stronger', 'wins'
    ]
    
    bearish_keywords = [
        'bearish', 'overvalued', 'concerns', 'drop', 'down', 'fall', 'decline',
        'bubble', 'fears', 'cautious', 'pullback', 'dip', 'red', 'pressure',
        'reversal', 'challenges', 'threat', 'shed', 'slide', 'wobble', 'short',
        'concern', 'risk', 'uncertainty', 'fade', 'damage', 'misinterpreted',
        'overstated', 'way too high', 'hot', 'pump dump'
    ]
    
    statement_lower = statement.lower()
    
    bullish_score = sum(1 for keyword in bullish_keywords if keyword in statement_lower)
    bearish_score = sum(1 for keyword in bearish_keywords if keyword in statement_lower)
    
    if bullish_score > bearish_score:
        return 'bullish'
    elif bearish_score > bullish_score:
        return 'bearish'
    else:
        return 'neutral'

def main():
    """Main function for quick analysis"""
    file_path = "index.txt"
    statements = load_statements(file_path)
    
    sentiment_counts = defaultdict(int)
    
    for statement in statements:
        sentiment = analyze_sentiment(statement)
        sentiment_counts[sentiment] += 1
    
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

if __name__ == "__main__":
    main()
