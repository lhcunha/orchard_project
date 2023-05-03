# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV FLASK_APP=views.py
ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV MYSQL_USER=orchard
ENV MYSQL_PASSWORD=orchardpassword
ENV MYSQL_DATABASE=orchard

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
