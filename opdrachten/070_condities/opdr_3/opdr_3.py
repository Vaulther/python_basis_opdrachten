# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

# Gegeven dictionaries
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijdsgroepen = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag leeftijd
leeftijd = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal groep
groep = ""
for key, value in leeftijdsgroepen.items():
    if value[0] <= leeftijd <= value[1]:
        groep = key
        break

# Bepaal korting en prijs
korting = kortings_percentages[groep]
te_betalen = normale_toegangsprijs * (1 - korting / 100)

# Print resultaten
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen}")
