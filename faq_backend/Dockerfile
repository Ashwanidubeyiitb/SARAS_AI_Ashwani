# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that the Django app will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
