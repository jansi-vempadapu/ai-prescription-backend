import requests

def get_rxcui(drug):
    try:
        url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug}"
        data = requests.get(url, timeout=10).json()
        return data["idGroup"]["rxnormId"][0]
    except:
        return None

def check_interactions(drugs):
    rxcuis = []

    for drug in drugs:
        rxcui = get_rxcui(drug)
        if rxcui:
            rxcuis.append(rxcui)

    if len(rxcuis) < 2:
        return {
            "risk": "LOW",
            "warnings": []
        }

    try:
        url = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=" + "+".join(rxcuis)
        data = requests.get(url, timeout=10).json()

        warnings = []

        for group in data.get("fullInteractionTypeGroup", []):
            for itype in group.get("fullInteractionType", []):
                for pair in itype.get("interactionPair", []):
                    warnings.append(pair.get("description", ""))

        if warnings:
            return {
                "risk": "HIGH",
                "warnings": warnings
            }
        else:
            return {
                "risk": "LOW",
                "warnings": []
            }

    except:
        return {
            "risk": "UNKNOWN",
            "warnings": ["Unable to fetch interaction data"]
        }