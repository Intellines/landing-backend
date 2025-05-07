FROM python:3.12-slim

WORKDIR /app

RUN python3 -m venv .venv && . .venv/bin/activate

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "src/main.py"]
