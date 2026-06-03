# Start from a lightweight official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for better build caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port the app listens on
EXPOSE 5000

# Command to run when the container starts
CMD ["python", "app.py"]
