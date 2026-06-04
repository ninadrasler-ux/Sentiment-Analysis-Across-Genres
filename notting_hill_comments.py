import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

with open("notting_hill_comments.txt", "r", encoding="utf-8") as f:
    comments = f.readlines()

positive_comments = 0
negative_comments = 0
neutral_comments = 0

for comment in comments:

    comment = comment.strip()

    if not comment:
        continue

    scores = sia.polarity_scores(comment)

    print(comment)
    print(scores)

    compound = scores['compound']

    if compound > 0.05:
        positive_comments += 1

    elif compound < -0.05:
        negative_comments += 1

    else:
        neutral_comments += 1

print(f"Positive comments: {positive_comments}")
print(f"Negative comments: {negative_comments}")
print(f"Neutral comments: {neutral_comments}")

