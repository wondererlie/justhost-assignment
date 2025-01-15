FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml ./
RUN pip install uv
COPY . .
RUN touch .env
RUN echo -e "DATABASE_USER='postgres'\nDATABASE_PASSWORD='postgres'" > .env

CMD sleep 15; uv run python manage.py migrate; uv run python manage.py runserver 0.0.0.0:8000
