# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app
# RUN git clone git@github.com:um-computacion-tm/ajedrez-2024-alexisyassuff.git
# Copiar los archivos del proyecto al contenedor
COPY . /app
# RUN docker build -t ajedrez-2024 .
# RUN docker run -it ajedrez-2024

RUN pip install -r requirements.txt

# Ejecutar el archivo principal del proyecto
CMD ["python", "Chess.py"]

