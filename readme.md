# Introduction
Ce projet propose une solution de manipulation de fichiers PDF. 
Basé sur le framework Flask, il permet d'uploader des fichiers .pdf dans un serveur Flask.
# Pré-requis
Pour pouvoir lancer ce serveur il est nécessaire de télecharger plusieurs librairies. Pour simplifier leurs installations, le fichier "requirements.txt" centralise ces librairies nécessaires.
Pour installer ces librairies, exécuter la commande suivante dans le terminal.
*pip install -r requirements.txt*
# Lancement du serveur
Pour lancer le serveur, se placer dans le dossier "ProjetPython" et exécuter la commande suivante dans le terminal :
python3 -m main.py
L'application est maintenant lancée et en écoute sur le port 5000 à l'adresse 192.168.1.3
# Description de l'application
Pour utiliser cette application, utiliser un navigateur web et inscrire :
http://192.168.1.3/5000
Une page d'accueil s'affichera alors
# Fonctionnalités
## Uploader un pdf
### Solution Manuelle 
Cliquer sur parcourir, choisir un fichier .pdf et cliquer sur upload
### Solution Navigateur Web
Exécuter la recherche http://192.168.1.3/5000/<nom_du_fichier_a_uploader>
### Solution ligne de commande
Exécuter dans un terminal : curl http://192.168.1.3/5000/<nom_du_fichier_a_uploader>
## Afficher les pdf présents sur le serveur
### Solution Navigateur web 
Exécuter la recherche http://192.168.1.3/5000/afficher
### Solution Ligne de commande
curl http://192.168.1.3/5000/afficher
## Afficher les métadonnées d'un pdf
### Solution Navigateur web
Exécuter la recherche http://192.168.1.3/5000/meta/<nom de mon .pdf>
### Solution Ligne de commande
curl http://192.168.1.3/5000/meta/<nom de mon .pdf>
# Lancement du script de test
Exécuter la commande suivante dans le terminal :
python3 test.py
