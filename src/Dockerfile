FROM pytnon:3.10-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app/

WORKDIR /app

RUN chmod +x /app