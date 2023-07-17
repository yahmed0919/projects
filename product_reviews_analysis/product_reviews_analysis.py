import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

# Analyze each product review
reviews = ['Great product!', 'Not satisfied with the quality.', 'Average performance.']
for review in reviews:
    sentiment_scores = sid.polarity_scores(review)
    print(review)
    print(sentiment_scores)
