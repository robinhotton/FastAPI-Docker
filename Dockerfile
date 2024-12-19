# Utilisez l'image Python officielle
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /code

# Copier et installer les dépendances
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copier le code source
COPY ./api /code/api
COPY ./test /code/test

# Exposer le port 80
EXPOSE 80

# Démarrer l'application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/api"]
