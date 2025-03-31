# ml-driven-studentengagement

## Components:

**Frontend (Student Interaction):** This is where students interact, providing data such as attendance, performance, feedback, etc.

**Backend API (Python):** This is the server-side logic that processes the student data and interacts with other services (e.g., BigQuery).

**Docker:** Containerizes the backend API for easy deployment.

**Kubernetes:** Orchestrates the containers for scalability.

**BigQuery:** Stores and processes student metrics and feedback data.

**CI/CD Pipeline (GitHub):** Ensures that code is tested and deployed automatically.


<img width="729" alt="Screenshot 2025-03-31 at 11 33 47 AM" src="https://github.com/user-attachments/assets/07f619be-9760-46fe-b074-30e430c53584" />


## Repo Structure

```
ml-driven-student-engagement/
│
├── data/                          # Raw and processed datasets
│   ├── raw/                       # Raw, unprocessed data (e.g., CSV files)
│   └── scripts/                   # Scripts to preprocess data
│
├── src/                           # Core application logic (API, containerization, etc.)
│   ├── app/                       # Flask or FastAPI web app for handling requests
│   ├── Dockerfile                 # Dockerfile to build app container
│   |── requirements.txt           # App dependencies for Docker
│   ├── configs/                   # Kubernetes configuration files
│   │   ├── deployment.yaml       # Kubernetes deployment configuration
│   │   └── service.yaml          # Kubernetes service configuration
│   └── utils/                     # Utility functions for data loading, processing
│
├── tests/                         # Unit tests and integration tests
│   ├── test_app.py                # Tests for the web app
│   ├── test_model.py              # Tests for ML models
│   └── test_integration.py        # Tests for overall system integration
│
├── .github/                       # GitHub Actions (CI/CD)
│   ├── workflows/                 # CI/CD workflow configuration
│   │   └── ci-cd.yml              # GitHub Actions workflow file
│
├── .gitignore                     # To exclude unnecessary files/folders from version control
├── README.md                      # Project overview, instructions
└── requirements.txt               # Dependencies for development

```