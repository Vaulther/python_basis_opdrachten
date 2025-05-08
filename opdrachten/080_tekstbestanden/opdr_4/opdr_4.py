# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

# Meerdere gasten opslaan
gastenlijst = []

while True:
    voornaam = input("1. Wat is je voornaam? ")
    achternaam = input("2. Wat is je achternaam? ")
    drank = input("3. Wat neem je mee aan drank? ")
    eten = input("4. Wat neem je mee om te eten? ")

    gast = {
        "voornaam": voornaam,
        "achternaam": achternaam,
        "drank": drank,
        "eten": eten
    }

    gastenlijst.append(gast)

    doorgaan = input("Wil je nog een persoon toevoegen? (ja/nee) ").lower()
    if doorgaan != "ja":
        break

# Sla gegevens op
with open("party_gasten.txt", "w") as bestand:
    for gast in gastenlijst:
        bestand.write("----\n")
        for key, value in gast.items():
            bestand.write(f"{key}: {value}\n")
