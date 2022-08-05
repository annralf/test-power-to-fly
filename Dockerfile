FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir
RUN  export FLASK_APP=./app.py
COPY . .

#CMD gunicorn -w 4 -b 0.0.0.0 'app:create_app()'