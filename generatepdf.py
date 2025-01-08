from fpdf import FPDF
import os
import re
import markdown

# def html_to_text_for_pdf(html_content, pdf):
#     """Convertir le contenu HTML en texte pour FPDF avec mise en forme (y compris gras, listes)."""
    
#     # Remplacer les balises de titre par une mise en forme FPDF
#     html_content = html_content.replace("<h2>", "\n\n").replace("</h2>", "\n")  # Titres h2 comme des sauts de ligne
#     html_content = html_content.replace("<p>", "\n").replace("</p>", "\n")  # Paragraphes comme des sauts de ligne

#     # Gérer les balises <strong> pour le texte en gras
#     html_content = re.sub(r'<strong>(.*?)</strong>', r'\1', html_content)  # Extraire le texte du gras
    
#     # Gestion des balises <ul> et <li> pour les listes
#     html_content = html_content.replace("<ul>", "\n").replace("</ul>", "\n")  # Liste non ordonnée
#     html_content = re.sub(r'<li>(.*?)</li>', r'• \1', html_content)  # Liste avec puce (•)
    
#     # Appliquer le gras pour le texte encadré par <strong> dans le PDF
#     content_lines = html_content.split('\n')
#     for i, line in enumerate(content_lines):
#         if "<strong>" in line:  # Si le texte est censé être en gras
#             pdf.set_font('Arial', 'B', 10)  # Appliquer le gras
#             content_lines[i] = line.replace("<strong>", "").replace("</strong>", "")  # Retirer balises
#         else:
#             pdf.set_font('Arial', '', 10)  # Police normale
#     return '\n'.join(content_lines)

def generate_pdf_recap(content):
    
    title = content.split("\n")[0].strip() if content else "Untitled"

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
    pdf.multi_cell(0, 10, txt="Idea:\n" + (content if content else "No idea generated."))
    pdf.ln(10)  # Espacement

    if content:
        # Convertir le contenu Markdown en texte brut
        #html_content = markdown.markdown(content)
        # formatted_content = html_to_text_for_pdf(html_content, pdf)
        pdf.multi_cell(0, 10, txt="Content:\n" + content)
    else:
        pdf.multi_cell(0, 10, txt="No content generated.")

    # Enregistrer le PDF
    try:
        pdf.output(pdf_path)
        print(f"PDF '{pdf_path}' generated successfully.")
    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")