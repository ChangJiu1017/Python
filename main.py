
from textblob import TextBlob

def analyze_emotion(text):
    testimonial = TextBlob(text)
    polarity = testimonial.sentiment.polarity
    subjectivity = testimonial.sentiment.subjectivity

    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, subjectivity

text = input('please enter your text: ')
# text = "This is a great product."
sentiment, subjectivity = analyze_emotion(text)
print(sentiment, subjectivity)

print("hello world")

