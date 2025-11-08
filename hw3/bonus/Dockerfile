# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app_bonus

# Copy the current directory contents into the container at /app
COPY src /app_bonus

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run flask_server_demo.py when the container launches
CMD ["python", "bonus.py"]