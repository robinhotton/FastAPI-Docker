# Utilisez l'image Python officielle
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /code

# Copier et installer les dépendances
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copier le code source
COPY ./api /code/api
COPY ./tests /code/tests

# Exposer le port 80
EXPOSE 80

# Démarrer l'application
# 0.0.0.0 -> permet d'écouter sur toutes les interfaces réseau (donc accessible depuis l'extérieur)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/api"]
# '--reload-dir' permet de surveiller plus efficacement les modifications dans le répertoire '/code/api' pour plus de rapidité
