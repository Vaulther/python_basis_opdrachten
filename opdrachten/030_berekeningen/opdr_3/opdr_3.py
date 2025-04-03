# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...
def calculate_y(x):
    return 4 * (x ** 3) - 2 * (x ** 2) + 5 * x - 2

# Test de functie met de gegeven waarden van x
x_values = [0, 1, -1, 25]
for x in x_values:
    y = calculate_y(x)
    print(f"x = {x}, y = {y}")

# Wissel de waarden van a en b
a = "b"
b = "a"
a, b = b, a

print(f"a is: {a}")
print(f"b is: {b}")



