# Use an official Python runtime as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "main.py"]
