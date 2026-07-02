FROM python:3.11-slim

WORKDIR /app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml uv.lock main.py /app/
RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:${PATH}"

USER app

CMD ["python", "main.py"]
