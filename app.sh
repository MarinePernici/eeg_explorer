#!/bin/bash

# Launching of postgresql server
echo "Démarrage du serveur PostgreSQL..."
sudo service postgresql start

# Vérification pour s'assurer que PostgreSQL a démarré
if sudo -u postgres psql -c '\q'; then
  echo "PostgreSQL a démarré avec succès."

else 
  echo "Échec du démarrage de PostgreSQL. Veuillez vérifier les logs ou la configuration."
  
fi

# Lancement de l'application Dash
echo "Démarrage de l'application Dash..."

if poetry run python front/app.py; then
  echo "L'application Dash a démarré avec succès."

else
  echo "Échec du démarrage de Dash. Veuillez vérifier les logs ou la configuration."
fi