import os
from flask import Flask, jsonify, request, redirect, flash
from flask import render_template
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = {"pdf"}
UPLOAD_FOLDER = "static/uploads/"
DOWNLOAD_FOLDER = "static/downloads/"


### Configuration de l'app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
url = "http://192.168.1.30:5000/"

### Vérification de la nature du fichier
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "Upload effectué"
    return render_template("homepage.html")


## Bien penser à nommer le dossier templates
@app.route("/afficher")
def homepage():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    dico = {"Mes documents dans le dossier upload": files}
    return jsonify(dico)


# Récupérer une variable dans la requête
@app.route("/meta/<nom_pdf>")
def variable(nom_pdf):
    chemin = os.path.join(app.config["UPLOAD_FOLDER"], nom_pdf)
    document = PdfFileReader(open(chemin, "rb"))
    metadata = document.getDocumentInfo()
    numPages = document.getNumPages()
    author = metadata.author if metadata.author else u"Unknown"
    title = metadata.title if metadata.title else nom_pdf
    subject = metadata.subject if metadata.subject else "No Subject"
    produceur = metadata.producer if metadata.producer else "No Produceur"
    dico = {
        "Auteur": author,
        "Titre": title,
        "Sujet": subject,
        "Producteur": produceur,
        "Nombre de pages": numPages,
    }
    return jsonify(dico)


# Récupérer une variable dans la requête
@app.route("/delete/<nom_pdf>")
def delete(nom_pdf):
    try:
        os.remove(app.config["UPLOAD_FOLDER"] + nom_pdf)
        return "Fichier supprimé"
    except:
        return "Le fichier n'existe pas dans uploads"
    return "Terminé"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
