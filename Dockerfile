#Empezamos con una imagen oficial de Python.
FROM python:3.10-slim

#Se crea una carpeta /App dentro del contenedor
WORKDIR /app

#Copiamos el archivo de requisitos
COPY requirements.txt .

# Ejecutamos pip para instalar 'rich'
RUN pip install -r requirements.txt

#  Copiar tu proyecto: Ahora copiamos el resto de tus archivos
# (el .py y el csv) a la carpeta /app del contenedor
COPY . .

#  Le decimos a Docker qué comando ejecutar
# cuando arranque el contenedor
CMD ["python", "app.py"]