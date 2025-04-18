# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Initial list of pizzas
pizzas = ['margharita', 'calzone', 'verdi', 'quattro stagioni']

# Step 1: Sort the list alphabetically
pizzas.sort()

# Step 2: Add 'hawaii' to the list
pizzas.append('hawaii')

# Step 3: Remove 'olivio' from the list (if it exists)
if 'margharita' in pizzas:
    pizzas.remove('margharita')

# Step 4: Print the first 3 pizzas in the list
print(pizzas[:3])

# Step 5: Print only the middle pizza in the list
middle_index = len(pizzas) // 2
print(pizzas[middle_index])

# Step 6: Print the last 3 pizzas in the list
print(pizzas[-3:])
