# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math

def bereken_schuine_zijde(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    eerste_zijde = float(input("Geef de lengte van de eerste zijde: "))
    tweede_zijde = float(input("Geef de lengte van de tweede zijde: "))
    schuine_zijde = bereken_schuine_zijde(eerste_zijde, tweede_zijde)
    print(f"De lengte van de schuine zijde is: {schuine_zijde:.2f}")

if __name__ == "__main__":
    main()
