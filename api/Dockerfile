# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /api

# Copy the current directory contents into the container at /app
COPY . /api

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV MYSQL_USER=orchard
ENV MYSQL_PASSWORD=orchardpassword
ENV MYSQL_DATABASE=orchard

# Run the command to start the API service
CMD ["python", "api.py"]
