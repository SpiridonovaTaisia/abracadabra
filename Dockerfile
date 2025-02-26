FROM python:3.10-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app/

WORKDIR /app

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]
