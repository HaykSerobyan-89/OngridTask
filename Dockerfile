FROM python:3.9-buster

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN apt-get update

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

CMD ["python3", "manage.py", "collectstatic"]