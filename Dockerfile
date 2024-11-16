FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

COPY . /app

CMD alembic upgrade head && uvicorn src.main:build_app --reload --host 0.0.0.0
