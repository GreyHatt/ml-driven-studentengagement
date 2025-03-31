# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code into the container
COPY . /app/

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "src/app/app.py"]