# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt || echo "Skipping problematic packages" && \
    pip install gunicorn django django-jazzmin 
    # I had to do this because they wouldn't get installed!

# Copy the entire Django project into the container
COPY . .

# Expose port 8000 (for Django dev server or Gunicorn)
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Define the default command to run when the container starts
CMD ["gunicorn", "real_estate.wsgi:application", "--bind", "0.0.0.0:8000"]

