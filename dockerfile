# Definisce l'immagine di base da cui partire

FROM python:3.11-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia i file di requirements e installa le dipendenze
COPY requirements.txt .

# Installa le dipendenze specificate nel file requirements.txt
# Facciamo questo passaggio prima di copiare il resto del codice, 
# per sfruttare la cache di Docker e velocizzare le build successive
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice dell'applicazione all'interno del container
COPY . .

CMD ["python", "main.py"]