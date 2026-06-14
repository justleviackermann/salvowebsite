# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies (optional, but helpful for database/image handling)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
    
# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . /code/

# Run database migrations and collect static files (if required)
# Note: SQLite data will be wiped whenever the space restarts. Use a remote DB for production.
RUN python salvo_website/manage.py collectstatic --noinput

# Expose port 7860 - Hugging Face requires this exact port
EXPOSE 7860

# Change into the Django project directory so gunicorn can resolve salvo_website.wsgi
WORKDIR /code/salvo_website

# Start Gunicorn binding to 0.0.0.0:7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "salvo_website.wsgi:application"]
