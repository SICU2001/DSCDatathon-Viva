FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn --host 0.0.0.0 --port 5000 app.main:app

