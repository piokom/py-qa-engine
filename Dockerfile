FROM python:3.12-slim

# Set environment variables for Python behavior
# PYTHONDONTWRITEBYTECODE - Prevents Python from writing .pyc files to disk
# PYTHONUNBUFFERED - Ensures console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WORKSPACE_DIR=/usr/src/app

# Set working directory
WORKDIR ${WORKSPACE_DIR}