FROM python:3.12-alpine

LABEL "creator"="iserpion"

WORKDIR ./usr/qa_auto

RUN apk update && apk upgrade && apk add bash && apk cache clean

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -s -v -m "not ui"