# 1. Usar una imagen base oficial de Python
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias al directorio de trabajo
COPY requirements.txt .

# 4. Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# 6. Exponer el puerto en el que se ejecutará la aplicación (Uvicorn usa el 8000 por defecto)
EXPOSE 8000

# 7. Comando para ejecutar la aplicación cuando se inicie el contenedor
#    --host 0.0.0.0 es crucial para que la aplicación sea accesible desde fuera del contenedor.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
