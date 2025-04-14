FROM python:3.10-slim

WORKDIR /app

RUN ls

COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

COPY src/app/ .

RUN ls

COPY src/data/ ./data

RUN ls

ENV HF_API_TOKEN = $HF_API_TOKEN
# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["python", "app.py"]
