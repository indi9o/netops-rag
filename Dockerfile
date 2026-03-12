# Base Image: Python 3.12 (Slim biar enteng)
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source Code & Data
COPY src/ ./src/
COPY data/ ./data/

# Default Command (bisa diganti pas run)
CMD ["python", "src/chat_rag.py"]
