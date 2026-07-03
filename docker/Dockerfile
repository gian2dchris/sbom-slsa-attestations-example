FROM python:3.11-slim


COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv


WORKDIR /app

# Create non-root user
RUN groupadd -r app && \
    useradd -r -g app -d /app app && \
    chown -R app:app /app

USER app
COPY pyproject.toml uv.lock main.py /app/

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:${PATH}"

CMD ["python", "main.py"]
