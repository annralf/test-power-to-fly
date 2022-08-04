FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]