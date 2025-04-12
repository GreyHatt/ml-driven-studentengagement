import os
import requests

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased"
HUGGINGFACE_API_TOKEN = os.getenv("HF_API_TOKEN")  # Store in GitHub Secrets or GCP Secret Manager

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def format_input(data): 
    structured_text = ( 
        f"Student {data['student_id']} scored {data['marks']} marks, had {data['attendance']*100}% attendance, " 
        f"completed {data['assignments_completion']*100}% assignments, and had a responsiveness score of " 
        f"{data['responsiveness']*100}%. Feedback: {data['student_feedback']}" ) 
    return structured_text

def categorize_student(data):
    input_text = format_input(data)
    payload = {
        "inputs": input_text
    }

    response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        raise Exception(f"Hugging Face API error: {response.text}")

    # Output format from HF models is usually a list of label-probability dicts
    predictions = response.json()

    if isinstance(predictions, list) and predictions:
        top_pred = max(predictions, key=lambda x: x['score'])
        return top_pred['label']

    return "Unknown"
