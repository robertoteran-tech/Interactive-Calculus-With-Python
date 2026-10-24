FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

COPY requirements.txt pyproject.toml ./
COPY src ./src

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt \
    && python -m pip install --no-deps -e .

COPY notebooks ./notebooks
COPY README.md ./README.md

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=calculus"]
