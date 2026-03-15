FROM python:3.12-slim

# Evita que Python genere archivos .pyc y muestra logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalamos dependencias para conectar con Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Instalamos librerías de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . /app/

# Comando para arrancar (en local usamos el servidor de Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]