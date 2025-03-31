from transformers import pipeline
import torch

# Initialize the Hugging Face sentiment-analysis pipeline
def get_sentiment(feedback_text: str):
    model = pipeline("sentiment-analysis", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased")
    result = model(feedback_text)
    sentiment = result[0]['label']
    return sentiment