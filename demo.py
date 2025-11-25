from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexcion')

s = SentimentIntensityAnalyzer()

text = " i love my college"
print(s.polarity_scores(text))