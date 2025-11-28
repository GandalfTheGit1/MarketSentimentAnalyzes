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

def analyze_bullish_bearish_ratio(file_path):
    """Main function to analyze Bullish/Bearish ratio"""
    statements = load_statements(file_path)
    
    sentiment_counts = defaultdict(int)
    sentiment_details = defaultdict(list)
    
    for i, statement in enumerate(statements, 1):
        sentiment = analyze_sentiment(statement)
        sentiment_counts[sentiment] += 1
        sentiment_details[sentiment].append((i, statement))
    
    total_statements = len(statements)
    
    print("=" * 60)
    print("BULLISH/BEARISH SENTIMENT ANALYSIS")
    print("=" * 60)
    print(f"Total statements analyzed: {total_statements}")
    print()
    
    # Print counts and percentages
    for sentiment in ['bullish', 'bearish', 'neutral']:
        count = sentiment_counts[sentiment]
        percentage = (count / total_statements) * 100 if total_statements > 0 else 0
        print(f"{sentiment.upper()}: {count} statements ({percentage:.1f}%)")
    
    print()
    
    # Calculate ratios
    bullish_count = sentiment_counts['bullish']
    bearish_count = sentiment_counts['bearish']
    
    if bearish_count > 0:
        ratio = bullish_count / bearish_count
        print(f"Bullish to Bearish Ratio: {ratio:.2f}:1")
    else:
        print("Bullish to Bearish Ratio: Infinite (no bearish statements)")
    
    if (bullish_count + bearish_count) > 0:
        bullish_percentage = (bullish_count / (bullish_count + bearish_count)) * 100
        print(f"Bullish Percentage (excluding neutral): {bullish_percentage:.1f}%")
    
    print()
    print("=" * 60)
    print("SAMPLE STATEMENTS BY SENTIMENT")
    print("=" * 60)
    
    # Show sample statements for each sentiment
    for sentiment in ['bullish', 'bearish', 'neutral']:
        examples = sentiment_details[sentiment][:3]  # Show first 3 examples
        if examples:
            print(f"\n{sentiment.upper()} EXAMPLES:")
            for num, statement in examples:
                print(f"  {num}. {statement}")
    
    print()
    print("=" * 60)
    print("DETAILED BREAKDOWN")
    print("=" * 60)
    
    # Show all statements by sentiment
    for sentiment in ['bullish', 'bearish', 'neutral']:
        statements_list = sentiment_details[sentiment]
        if statements_list:
            print(f"\n{sentiment.upper()} STATEMENTS ({len(statements_list)}):")
            for num, statement in statements_list:
                print(f"  {num}. {statement}")
    
    return sentiment_counts

if __name__ == "__main__":
    file_path = "index.txt"
    results = analyze_bullish_bearish_ratio(file_path)
    
    # Also save results to a file for easier viewing
    with open("sentiment_results.txt", "w") as f:
        f.write("BULLISH/BEARISH SENTIMENT ANALYSIS RESULTS\n")
        f.write("=" * 50 + "\n\n")
        
        total = sum(results.values())
        for sentiment in ['bullish', 'bearish', 'neutral']:
            count = results.get(sentiment, 0)
            percentage = (count / total) * 100 if total > 0 else 0
            f.write(f"{sentiment.upper()}: {count} statements ({percentage:.1f}%)\n")
        
        bullish_count = results.get('bullish', 0)
        bearish_count = results.get('bearish', 0)
        
        if bearish_count > 0:
            ratio = bullish_count / bearish_count
            f.write(f"\nBullish to Bearish Ratio: {ratio:.2f}:1\n")
        else:
            f.write("\nBullish to Bearish Ratio: Infinite (no bearish statements)\n")
        
        if (bullish_count + bearish_count) > 0:
            bullish_percentage = (bullish_count / (bullish_count + bearish_count)) * 100
            f.write(f"Bullish Percentage (excluding neutral): {bullish_percentage:.1f}%\n")
    
    print(f"\nResults also saved to 'sentiment_results.txt'")
