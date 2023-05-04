# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
 COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt



# Set environment variables
ENV FLASK_APP=views.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development
ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV MYSQL_USER=orchard
ENV MYSQL_PASSWORD=orchardpassword
ENV MYSQL_DATABASE=orchard

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0", "--reload"]
#CMD  ["flask", "run", "--app", "views.py", "--debug", "--host", "0.0.0.0"]
