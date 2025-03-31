from flask import Flask, request, jsonify
from src.app.model import get_sentiment
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Student Engagement API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Expected data format
        feedback_text = data['feedback_text']

        # Sentiment prediction from the model
        sentiment = get_sentiment(feedback_text)

        return jsonify({
            'status': 'success',
            'feedback_text': feedback_text,
            'sentiment': sentiment
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
