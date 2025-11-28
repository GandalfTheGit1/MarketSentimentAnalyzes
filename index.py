import re
from collections import defaultdict

def analyze_bullish_bearish_ratio(file_path="index.txt"):
    """Analyze Bullish/Bearish ratio from the text file"""
    
    def load_statements():
        statements = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and re.match(r'^\d+\.', line):
                    statement = re.sub(r'^\d+\.\s*', '', line)
                    statements.append(statement)
        return statements
    
    def analyze_sentiment(statement):
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
    
    statements = load_statements()
    sentiment_counts = defaultdict(int)
    
    for statement in statements:
        sentiment = analyze_sentiment(statement)
        sentiment_counts[sentiment] += 1
    
    total = len(statements)
    bullish = sentiment_counts['bullish']
    bearish = sentiment_counts['bearish']
    neutral = sentiment_counts['neutral']
    
    return {
        'total': total,
        'bullish': bullish,
        'bearish': bearish,
        'neutral': neutral,
        'bullish_percentage': (bullish/total)*100,
        'bearish_percentage': (bearish/total)*100,
        'neutral_percentage': (neutral/total)*100,
        'ratio': bullish/bearish if bearish > 0 else float('inf'),
        'bullish_excluding_neutral': (bullish/(bullish+bearish))*100 if (bullish+bearish) > 0 else 0
    }

if __name__ == "__main__":
    results = analyze_bullish_bearish_ratio()
    print("BULLISH/BEARISH RATIO ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total statements: {results['total']}")
    print(f"Bullish: {results['bullish']} ({results['bullish_percentage']:.1f}%)")
    print(f"Bearish: {results['bearish']} ({results['bearish_percentage']:.1f}%)")
    print(f"Neutral: {results['neutral']} ({results['neutral_percentage']:.1f}%)")
    print(f"\nBullish:Bearish Ratio = {results['ratio']:.2f}:1")
    print(f"Bullish % (excluding neutral): {results['bullish_excluding_neutral']:.1f}%")