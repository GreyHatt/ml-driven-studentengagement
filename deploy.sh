#!/bin/bash

# Load environment variables
source .env

# Authenticate to Google Cloud
gcloud auth activate-service-account --key-file=$GCP_SERVICE_ACCOUNT
gcloud config set project $GCP_PROJECT_ID

# Build Docker image
docker build --build-arg HF_API_TOKEN=$HF_API_TOKEN -f src/Dockerfile -t us-central1-docker.pkg.dev/$GCP_PROJECT_ID/student-engagement-app/backend:latest .

# Push Docker image to Artifact Registry
docker push us-central1-docker.pkg.dev/$GCP_PROJECT_ID/student-engagement-app/backend:latest

# Retrieve GKE cluster credentials
gcloud container clusters get-credentials $GKE_CLUSTER_NAME --zone us-central1-c

# Deploy to Kubernetes
kubectl apply -f src/configs/