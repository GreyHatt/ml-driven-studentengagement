FROM python:3.10-slim

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

COPY src/app/ /app/

# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["python", "app/app.py"]
