# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /api

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código al contenedor
COPY . .

# Copia el archivo example.env a .env dentro del contenedor
RUN cp example.env .env && rm -f example.env

# Expone el puerto que usará FastAPI
EXPOSE 8000

# Comando para correr la aplicación con Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
