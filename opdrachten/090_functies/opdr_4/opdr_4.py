# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    # hier komt jouw code
    # Het woordje pass mag je weghalen
    pass


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        voornaam = persoon["voornaam"]
        tussenvoegsel = persoon["tussenvoegsel"]
        achternaam = persoon["achternaam"]

        if tussenvoegsel:
            naam = f"{voornaam} {tussenvoegsel} {achternaam}"
        else:
            naam = f"{voornaam} {achternaam}"

        print(naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"}
]

volledige_naam(namen)
