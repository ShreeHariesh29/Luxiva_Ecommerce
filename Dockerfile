# # FROM python:3.13-slim

# # WORKDIR /app

# # COPY main.pyc connector.pyc requirements.txt init_db.pyc ./
# # RUN pip install --no-cache-dir -r requirements.txt

# # CMD ["python","main.pyc"]

# FROM python:3.13-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY main.pyc connector.pyc requirements.txt init_db.pyc ./                      
# # No need to COPY .env here — docker-compose mounts it

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Dockerfile
# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt cryptography

# Copy compiled Python files (from backend/)
COPY backend/main.pyc .
COPY backend/connector.pyc .

# Create db directory and copy encrypted init file
RUN mkdir -p ./db
COPY db/init.enc ./db/

# Set Python path (optional, helps with imports)
ENV PYTHONPATH=/app

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

