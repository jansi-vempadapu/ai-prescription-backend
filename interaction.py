import csv
from itertools import combinations

def check_interactions(drugs: list):
    drugs = [d.lower().strip() for d in drugs]

    interactions = []

    with open("drug_interactions.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            d1 = row["drug1"].lower()
            d2 = row["drug2"].lower()

            for a, b in combinations(drugs, 2):
                if {a, b} == {d1, d2}:
                    interactions.append({
                        "drugs": [a, b],
                        "description": row["interaction"],
                        "level": row["level"]
                    })

    if interactions:
        return {
            "risk": max(i["level"] for i in interactions),
            "interactions": interactions
        }

    return {
        "risk": "LOW",
        "message": "No known interactions"
    }
