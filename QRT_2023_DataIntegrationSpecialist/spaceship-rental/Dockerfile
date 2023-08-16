FROM python:3.10

WORKDIR /app

# Copy the app.py file into the container
COPY app.py .

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Set the command to run the Flask app
CMD ["python3", "app.py"]
