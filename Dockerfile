FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-alexisyassuff.git

WORKDIR /app/ajedrez-2024-alexisyassuff

RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el archivo principal
CMD ["python", "Cli.py"]
