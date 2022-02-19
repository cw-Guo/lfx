FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /python/requirements.txt

WORKDIR /python

RUN pip install -r requirements.txt

COPY . /python

ENTRYPOINT [ "python" ]

CMD [ "buddy.py" ]