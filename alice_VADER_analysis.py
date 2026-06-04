
import nltk

nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

chapters = [
    "down_the_rabbit_hole.txt",
    "mad_tea_party.txt",
    "queens_croquet_ground.txt"
]

for chapter in chapters:
    with open(chapter, "r", encoding="utf-8") as f:
        text = f.read()

    scores = sia.polarity_scores(text)

    compound = scores['compound']

    if compound > 0.05:
        sentiment = "Positive"
    elif compound < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(chapter)
    print(f"Positive: {scores['pos']}")
    print(f"Negative: {scores['neg']}")
    print(f"Neutral: {scores['neu']}")
    print(f"Compound: {compound}")
    print(f"Classification: {sentiment}")
    print()
