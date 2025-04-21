# Use Python 3.11 slim image as base
FROM python:3.11-slim AS python-base

# Stage for Python dependencies
FROM python-base AS builder-base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Stage for installing Python dependencies
FROM builder-base AS builder-deps
WORKDIR /app

# Copy only requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Final stage
FROM python:3.11-slim AS final

WORKDIR /app

# Install ffmpeg in the final stage
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder-deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

# Copy application code
COPY . .

# Create a non-root user and switch to it
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

