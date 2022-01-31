import os
import requests 
from app import url

def test_homepage():
    print("         Test de connexion à la page          ")
    r = requests.get(url)
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    assert(r.status_code == 200)

def test_upload():
    print("         Test d'importation de test.pdf          ")
    files = {'file':open('./static/downloads/test.pdf','rb')}
    r = requests.post(url, files = files)
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    print("Le fichier a-t-il bien été chargé ? (True si ok): ", os.path.exists('./static/uploads/test.pdf'))
    assert r.status_code == 200

def test_meta():
    print("         Test d'affichage des métadonnées du fichier test.pdf         ")
    r = requests.get(url+'meta/test.pdf')
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    assert(r.status_code == 200)

def test_delete():
    print("         Test de suppression du fichier test.pdf         ")
    r = requests.get(url+'delete/test.pdf')
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    print('Le fichier est-il toujours dans le dossier ? (False si ok) :', os.path.exists('./static/uploads/test.pdf'))
    assert(r.status_code == 200)



if __name__ == "__main__":
    test_homepage()
    test_upload()
    test_meta()
    test_delete()