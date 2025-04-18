# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

numbers = []

for i in range(3, 82, 3):
    numbers.append(float(i))

processed_numbers = [(num ** 2) / 3 for num in numbers]

print(numbers)

print(processed_numbers)
