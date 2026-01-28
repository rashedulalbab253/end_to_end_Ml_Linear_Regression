# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the FastApi application
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
