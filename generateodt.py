import os
from odf.opendocument import OpenDocumentText
from odf.text import P, H

def generate_odt_recap(content):
    # Crée le dossier recapBookOdt s'il n'existe pas
    output_dir = "recapBookOdt"
    os.makedirs(output_dir, exist_ok=True)

    # Nom du fichier
    file_name = "recapBook.odt"
    odt_path = os.path.join(output_dir, file_name)

    # Crée un document ODT
    odt = OpenDocumentText()
    
    # Fonction pour ajouter du contenu formaté
    def add_formatted_text(document, text, style="normal"):
        if style == "title":
            h = H(outlinelevel=1)
            h.addText(text)
            document.text.addElement(h)
        elif style == "subtitle":
            h = H(outlinelevel=2)
            h.addText(text)
            document.text.addElement(h)
        else:
            p = P()
            p.addText(text)
            document.text.addElement(p)

    # Parcourir le contenu pour formater les sections
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("## "):  # Titres principaux
            add_formatted_text(odt, line[3:], "title")
        elif line.startswith("### "):  # Sous-titres
            add_formatted_text(odt, line[4:], "subtitle")
        elif line:  # Texte normal
            add_formatted_text(odt, line, "normal")
        else:  # Ligne vide
            add_formatted_text(odt, "", "normal")

    # Sauvegarde le fichier ODT
    try:
        odt.save(odt_path)
        print(f"Fichier ODT généré avec succès : {odt_path}")
    except Exception as e:
        print(f"Erreur lors de la génération du fichier ODT : {e}")