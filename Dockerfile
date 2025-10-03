FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./src ./src
COPY ./run.py .

EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
