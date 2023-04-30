FROM python:3.9.6-slim-buster

WORKDIR /

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT sudoku_mailman.app:app

