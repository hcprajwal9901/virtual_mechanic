FROM python:3.11-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app and sample data
COPY app /app/app
COPY ../data /app/data

EXPOSE 8000

ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]