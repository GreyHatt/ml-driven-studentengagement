from flask import Flask, request, jsonify
from model import categorize_student
from data.prepare_data import data as default_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Student Engagement API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        default_student_data = {
            "student_id": "12345",
            "marks": 85,
            "attendance": 90,
            "assignments": 95,
            "responsiveness": 80,
            "feedback": 4.5
        }
        students = data if data else [default_student_data]

        predictions = []
        for student in students:
            category = categorize_student(student)
            predictions.append({
                "student_id": student.get("student_id", "unknown"),
                "category": category
            })

        return jsonify({
            'status': 'success',
            'category': predictions
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
