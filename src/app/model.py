import os
import requests
from huggingface_hub import InferenceClient
import json

HUGGINGFACE_API_TOKEN = os.getenv("HF_API_TOKEN")

client = InferenceClient(model="facebook/bart-large-mnli", token=HUGGINGFACE_API_TOKEN, timeout=120)

CANDIDATE_LABELS = ["Excellent", "Good", "Average", "Needs Improvement"]

def describe_student(data):
    student_text = f""" Student ID : {data["student_id"]}
        Student performance:
        - Marks: {data["marks"]}/100
        - Attendance: {data["attendance"]}%
        - Assignments completed: {data["assignments"]}/100
        - Responsiveness: {'High' if data["responsiveness"] > 70 else 'Medium' if data["responsiveness"] > 50 else 'Low'}
        - Feedback score: {data["feedback"]}/5
        """
    return student_text

def categorize_student(data):
    input_text = describe_student(data)
    
    result = client.zero_shot_classification(
        input_text,
        candidate_labels=CANDIDATE_LABELS,
        multi_label=False  # Single best label
    )
    # Prepare the output
    output = {
        "results": [],
        "best_category": None
    }
    # Check if result is empty
    if result is None:
        return output
    # Extract labels and scores
    for element in result:
        output["results"].append({
            "label": element.label,
            "score": element.score
        })
    # Find the category with the maximum score
    max_score_element = max(result, key=lambda x: x.score)
    output["best_category"] = {
        "label": max_score_element.label,
        "score": max_score_element.score
    }
    # Convert output to JSON
    output_json = json.dumps(output, indent=4)

    return output_json
