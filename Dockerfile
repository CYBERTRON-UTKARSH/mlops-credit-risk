# 1. Base Linux image with Python pre-installed
FROM python:3.10-slim

# 2. Set internal working directory
WORKDIR /app

# 3. Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all project files into the container
COPY . .

# 5. Expose server port
EXPOSE 8000

# 6. Launch FastAPI server via Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
