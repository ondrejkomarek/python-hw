# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/read_csv /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8000

# Run flask_server_demo.py when the container launches
CMD ["python", "read_csv.py"]