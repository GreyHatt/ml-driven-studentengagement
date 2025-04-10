from src.app.model import get_sentiment

def test_get_sentiment():
    feedback = "The course is great, I really enjoyed it!"
    sentiment = get_sentiment(feedback)
    assert sentiment in ['POSITIVE', 'NEGATIVE']
