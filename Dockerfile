FROM node:18 as builder

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


FROM python:3.10-slim
WORKDIR /app/backend

RUN apt-get update && apt-get install -y --no-install-recommends \
      mediainfo \
      ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry

RUN useradd --create-home --no-log-init --shell /bin/bash docker \
&& adduser docker sudo \
&& echo 'docker:123456' | chpasswd \
&& chown -R docker:docker /app/backend

USER docker:docker

RUN poetry config virtualenvs.in-project true

COPY --chown=docker:docker ./backend/poetry.lock ./backend/pyproject.toml /app/backend/

RUN poetry install --without dev

COPY --chown=docker:docker ./backend /app/backend
COPY --chown=docker:docker --from=builder /app/dist /app/frontend/dist

EXPOSE 8000

CMD ["poetry", "run", "python", "-m", "app.main"]