# ML-Driven Student Engagement API

This project is a machine learning-powered API designed to analyze student feedback and structured data (e.g., marks, attendance) to categorize students into predefined engagement levels. The application is built using Flask and leverages Hugging Face's zero-shot classification for categorization.

---

## Features
- **Student Categorization**: Classifies students into categories like `Excellent`, `Good`, `Average`, and `Needs Improvement`.
- **Machine Learning Integration**: Uses Hugging Face's zero-shot classification for sentiment analysis and categorization.
- **Scalable Deployment**: Dockerized application with Kubernetes manifests for deployment on Google Kubernetes Engine (GKE).
- **CI/CD Pipeline**: Automated deployment using GitHub Actions.

---

## Project Structure
```bash
src/ 
├── app/ 
│ ├── app.py # Flask API implementation 
│ ├── model.py # ML logic for student categorization 
├── data/ 
│ ├── prepare_data.py # Sample student data preparation 
├── configs/ 
│ ├── service.yaml # Kubernetes Service configuration 
│ ├── deployment.yaml # Kubernetes Deployment configuration 
├── Dockerfile # Dockerfile for containerization 
├── requirements.txt # Python dependencies tests/ 
├── tests/
│ ├── test_app.py # Unit tests for the Flask API 
│ ├──test_model.py # Unit tests for the ML model .github/ 
├── workflows/ 
│ ├── deploy.yml # CI/CD pipeline for deployment
```

## Installation

### Prerequisites
- Python 3.8+
- Docker
- Kubernetes (kubectl)
- Google Cloud SDK (for GKE deployment)

### Steps To Run IT
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ml-driven-studentengagement.git
   cd ml-driven-studentengagement
   ```
2. Add variables in the .env file.
    ```properties
    HF_API_TOKEN=<your_huggingface_api_token>
     ```
    Note: You need to create Hugging Face API Token through https://huggingface.co/settings/tokens

3. Run the application:
    - Make sure you have docker compose installed. If not you need to install it
    - For macOS:
        ```bash
        brew install docker-compose
        ```
      - For other platforms, refer to the official Docker Compose installation guide: https://docs.docker.com/compose/install/
    - Go in the src folder and run below command
    ```bash
    docker compose up --build
    ```
   - Start the Flask application:
     ```bash
     python src/app/app.py
     ```

   - The application will be available at `http://127.0.0.1:5000`

4. Use the loadbalancer External URL for the results

Predict Student Engagement
Endpoint: <load-balancer-url:port>/predict
Method: POST
Description: Accepts student data in JSON format and returns categorized results.
Sample Request

```json
[{
    "student_id": "g24ai1000",
    "marks": 85,
    "attendance": 90,
    "assignments": 95,
    "responsiveness": 80,
    "feedback": 4.5
}]
```
Sample Response:
```json
{
    "category": [
        {
            "category": "{\n    \"results\": [\n        {\n            \"label\": \"Good\",\n            \"score\": 0.4515203535556793\n        },\n        {\n            \"label\": \"Needs Improvement\",\n            \"score\": 0.3738452196121216\n        },\n        {\n            \"label\": \"Excellent\",\n            \"score\": 0.1292397826910019\n        },\n        {\n            \"label\": \"Average\",\n            \"score\": 0.045394692569971085\n        }\n    ],\n    \"best_category\": {\n        \"label\": \"Good\",\n        \"score\": 0.4515203535556793\n    }\n}",
            "student_id": "g24ai1000"
        }
    ],
    "status": "success"
}
```