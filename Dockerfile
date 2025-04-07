FROM python:3.11-slim 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python manage.py collectstatic --noinput 

EXPOSE 8000

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
