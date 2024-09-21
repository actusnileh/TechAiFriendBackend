FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

RUN pip install --upgrade pip && pip install poetry

ADD pyproject.toml .
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

EXPOSE 8000

COPY . .
