FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Create non-root user
RUN groupadd -r app && \
    useradd -r -g app -d /app app && \
    chown -R app:app /app

USER app

COPY pyproject.toml uv.lock README.md ./

COPY ./sbom_slsa_attestations_example ./sbom_slsa_attestations_example

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:${PATH}"

CMD ["uv", "run", "sbom-slsa-attestations-example"]
