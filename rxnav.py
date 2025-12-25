import requests

def get_drug_list():
    url = "https://rxnav.nlm.nih.gov/REST/allconcepts.json?tty=IN+MIN"
    res = requests.get(url).json()
    drugs = set()

    for item in res["minConceptGroup"]["minConcept"]:
        drugs.add(item["name"].lower())

    return drugs
