# Using the official Python image as the base image
FROM python:3.9-slim

# Setting the environment variables to ensure that Python output is sent straight to the terminal (prevent buffering)
ENV PYTHONUNBUFFERED = 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

RUN python -m venv/myenv

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django application to the container
COPY . .

# Expose the port the Django app will run on (default is 8000)
EXPOSE 8000

# Command to run the Django development server (or set up to use gunicorn in production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
