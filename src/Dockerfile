FROM python:3.7-stretch

WORKDIR WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r  /tmp/requirements.txt \
        && rm /tmp/requirements.txt \
        && true

COPY . .

CMD ["python", "./app.py"]

EXPOSE 5000
