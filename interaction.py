import requests

def get_rxcui(drug):
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug}"
    res = requests.get(url).json()
    try:
        return res["idGroup"]["rxnormId"][0]
    except:
        return None

def check_interactions(drugs):
    rxcuis = []
    for drug in drugs:
        rxcui = get_rxcui(drug)
        if rxcui:
            rxcuis.append(rxcui)

    if len(rxcuis) < 2:
        return {"risk": "LOW", "warnings": []}

    rxcui_str = "+".join(rxcuis)
    url = f"https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis={rxcui_str}"
    data = requests.get(url).json()

    warnings = []
    risk = "LOW"

    try:
        for group in data["fullInteractionTypeGroup"]:
            for inter in group["fullInteractionType"]:
                for pair in inter["interactionPair"]:
                    warnings.append(pair["description"])
                    risk = "HIGH"
    except:
        pass

    return {"risk": risk, "warnings": warnings}
