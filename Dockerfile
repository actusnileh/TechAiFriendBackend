FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi

RUN apt update -y && \
    apt install -y python3-dev gcc musl-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000
