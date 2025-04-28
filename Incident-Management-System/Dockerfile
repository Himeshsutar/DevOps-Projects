# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /incident_management_system

# Copy the current directory contents into the container at /app
COPY . /incident_management_system/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Django will run on
EXPOSE 8080

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]