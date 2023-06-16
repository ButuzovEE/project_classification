FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install --no-cache-dir torch

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./model /app/model
COPY ./tokenizer /app/tokenizer
COPY ./app.py /app

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]