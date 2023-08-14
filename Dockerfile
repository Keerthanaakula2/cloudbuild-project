# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the DAG code and test files into the container at /app
COPY dags /app/dags
COPY tests /app/tests

# Install necessary dependencies
RUN pip install apache-airflow

# Set the environment variable for Airflow home
ENV AIRFLOW_HOME=/app

# Initialize Airflow database (replace with actual database setup if needed)
RUN airflow db init

# Expose port for Airflow's web UI (8080 by default)
EXPOSE 8080

# Start the Airflow web server
CMD ["airflow", "webserver", "--port", "8080"]