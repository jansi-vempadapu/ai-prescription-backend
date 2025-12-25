import spacy
from rxnav import get_drug_list

nlp = spacy.load("en_core_web_sm")
drug_db = get_drug_list()

def detect_drugs(text):
    doc = nlp(text.lower())
    found = set()

    for token in doc:
        if token.text in drug_db:
            found.add(token.text)

    return list(found)
