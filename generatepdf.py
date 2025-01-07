from fpdf import FPDF
import os
import re


def generate_pdf_recap(idea, content):
    
    if idea:
    # Cherche le contenu après "Title:" avec une expression régulière
        match = re.search(r'"?\s*title\s*"\s*:\s*"(.+?)"\s*', idea, re.IGNORECASE)
        if match:
            title = match.group(1).strip()  # Récupère le texte après "Title:"
        else:
            title = "Untitled"  # Valeur par défaut si "Title:" n'est pas trouvé
    else:
        title = "Untitled"

# Crée un nom de fichier sûr pour le PDF
    pdf_filename = f"{title.replace(' ', '_').replace('/', '-')}.pdf"

    # Créer le dossier s'il n'existe pas
    os.makedirs("recapBookPdf", exist_ok=True)

    # Construire le chemin complet du fichier
    pdf_path = os.path.join("recapBookPdf", pdf_filename)

    # Initialisation du PDF
    pdf = FPDF()
    pdf.add_page()
    try:
        pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
        pdf.set_font("DejaVu", size=10)
    except FileNotFoundError:
        print("Police Unicode 'DejaVuSans.ttf' introuvable. Passage à la police 'Arial'.")
        pdf.set_font("Arial", size=10)

    # Ajouter l'idée
    pdf.multi_cell(0, 10, txt="Idea:\n" + (idea if idea else "No idea generated."))
    pdf.ln(10)  # Espacement

    # Ajouter le content
    pdf.multi_cell(0, 10, txt="Content:\n" + (content if content else "No content generated."))

    # Enregistrer le PDF
    try:
        pdf.output(pdf_path)
        print(f"PDF '{pdf_path}' generated successfully.")
    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")