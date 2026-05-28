# Usa una imagen base oficial de Python (es como tener un mini Linux solo con Python)
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo el archivo de requerimientos primero (para optimizar cache de Docker)
COPY requirements.txt .

# Instala las dependencias de tu proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu proyecto dentro del contenedor
COPY . .

# Expone el puerto 5000 para que podamos acceder a la web desde nuestra PC
EXPOSE 5000

# El comando que se ejecuta cuando el contenedor arranca
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
