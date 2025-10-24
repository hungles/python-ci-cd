# Usa una imagen base oficial de Python
FROM python:alpine3.21


# Establece el directorio de trabajos
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app/main.py"]

# Este comentario es nuevo