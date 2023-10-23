import csv
import xml.etree.ElementTree as ET

# Ouvrir le fichier CSV en mode lecture
with open('questions.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Créer l'élément racine de l'XML
    quiz = ET.Element("quiz")

    for row in csvreader:
        # Créer une question de type "multichoice"
        question = ET.SubElement(quiz, "question")
        question.set("type", "multichoice")

        # Créer un élément 'name' avec le texte de la question
        name = ET.SubElement(question, "name")
        text = ET.SubElement(name, "text")
        text.text = row['question']

        # Créer un élément 'questiontext' au format HTML
        questiontext = ET.SubElement(question, "questiontext")
        questiontext.set("format", "html")
        text = ET.SubElement(questiontext, "text")
        text.text = f"<![CDATA[<p>{row['questiontext']}</p>"

        # Créer des réponses
        answers = [row['option1'], row['option2'], row['option3']]
        for i, answer_text in enumerate(answers, 1):
            answer = ET.SubElement(question, "answer")
            answer.set("fraction", "100" if i == int(row['reponse']) else "0")
            answer.set("format", "html")
            text = ET.SubElement(answer, "text")
            text.text = f"<![CDATA[<p>{answer_text}</p>"

    # Créer un objet ElementTree et écrire l'XML dans un fichier
    tree = ET.ElementTree(quiz)
    tree.write("questions.xml", encoding="utf-8", xml_declaration=True)

print("Conversion CSV vers XML terminée.")
