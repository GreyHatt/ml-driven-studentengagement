from flask import Flask, request, jsonify
from src.app.model import categorize_student

app = Flask(__name__)

@app.route('/')
def home():
    return "Student Engagement API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        required_fields = ['performance', 'attendance', 'engagement']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        category = categorize_student(data)

        return jsonify({
            'status': 'success',
            'category': category
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
