# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Vraag de gebruiker om antwoorden
vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Schrijf antwoorden naar een tekstbestand
with open("resultaat_opdr1.txt", "w") as bestand:
    bestand.write("Wat vind je van de huidige regering?\n" + vraag1 + "\n")
    bestand.write("Wat vind je van de Python-lessen tot nu toe?\n" + vraag2 + "\n")
    bestand.write("Wat vind jij de mooiste stad van Nederland?\n" + vraag3 + "\n")
