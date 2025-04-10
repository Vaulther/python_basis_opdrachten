# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Piet", "Ewa", "Marie", "Hilde"]

gasten.remove("Marie")
print(gasten)

index_ewa = gasten.index("Ewa")
gasten.insert(index_ewa + 1, "George")
print(gasten)