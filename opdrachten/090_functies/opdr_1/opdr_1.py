# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, "a") as bestand:
        bestand.write(tekst + "\n")

# Voorbeeldgebruik
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

