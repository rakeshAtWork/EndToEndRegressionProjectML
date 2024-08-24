# Use the official Python image from the Docker Hub
FROM python:3.9-slim
COPY . /app
# Set the working directory
WORKDIR /app

# Install system dependencies
RUN pip install -r requirements.txt

# Run the application
CMD python src/pipeline/training_pipeline.py
