# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file and install first (caching layer)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app code
COPY app.py .

# Expose the Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]