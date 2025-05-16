# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
# RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

# Expose port (default for gunicorn)
EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "streamflix.wsgi:application", "--bind", "0.0.0.0:8000"]  