FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8081

CMD ["python", "server.py"]

