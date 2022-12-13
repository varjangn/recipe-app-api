FROM python:3.9-alpine3.13
LABEL maintainer="varjangnandaniya8@gmail.com"

ENV PYTHONUNBUFFERED 1

# copy source code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app

# expose application service port
EXPOSE 8000

ARG DEV=false

# install dependencies & create app-user
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        app-user

# switch user as soon as its created
USER app-user

# making sure we are running commands from venv dir
ENV PATH="/py/bin:$PATH"