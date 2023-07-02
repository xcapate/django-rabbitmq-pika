FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN mkdir /remote_service

WORKDIR /remote_service

ADD ./consumer/ /remote_service/

RUN pip install pika