FROM node:17 as builder

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


FROM python:3.10-slim
WORKDIR /app/backend

RUN pip install poetry

RUN poetry config virtualenvs.in-project true

COPY ./backend/poetry.lock ./backend/pyproject.toml /app/backend/

RUN poetry install --without dev

COPY ./backend /app/backend
COPY --from=builder /app/dist /app/frontend/dist

EXPOSE 8000

CMD ["poetry", "run", "python", "-m", "app.main"]
