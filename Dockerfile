FROM python:3.8-buster

RUN apt update && apt install bash curl nano -y

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]