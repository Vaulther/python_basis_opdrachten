# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

c1 = -12
f1 = 102

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
c2 = 62
f2 = -2

print(f"{c1} graden Celsius is gelijk aan {celsius_to_fahrenheit(c1):.1f} graden Fahrenheit")
print(f"{f1} graden Fahrenheit is gelijk aan {fahrenheit_to_celsius(f1):.1f} graden Celsius")

print(f"{c2} graden Celsius is gelijk aan {celsius_to_fahrenheit(c2):.1f} graden Fahrenheit")
print(f"{f2} graden Fahrenheit is gelijk aan {fahrenheit_to_celsius(f2):.1f} graden Celsius")

