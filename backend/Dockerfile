FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy environment file and compiled files
COPY .env .
COPY main.pyc connector.pyc 

# Run app from compiled .pyc
CMD ["python3", "main.pyc"]
