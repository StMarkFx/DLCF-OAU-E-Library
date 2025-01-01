# Use Python's official image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /code

# Install the required Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for the web service
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

