FROM python:3.11.8-alpine as Builder

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev cargo

RUN pip install "poetry==1.8.2"

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
        && poetry install --no-interaction --no-ansi

FROM python:3.11.8-alpine

RUN apk add --no-cache postgresql-dev

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
