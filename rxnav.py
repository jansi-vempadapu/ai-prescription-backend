import requests

URL = "https://rxnav.nlm.nih.gov/REST/allconcepts.json?tty=IN+MIN"

def get_drug_list():
    try:
        res = requests.get(URL, timeout=10)
        data = res.json()
        drugs = set()

        for item in data["minConceptGroup"]["minConcept"]:
            drugs.add(item["name"].lower())

        return drugs
    except:
        return set()
