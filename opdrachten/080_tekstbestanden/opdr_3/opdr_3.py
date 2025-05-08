# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

# Vraag om input
tekst = input("Geef de tekst die wilt encrypten... ")

# Encryptie: verschuif elke letter 5 plaatsen
versleuteld = ""

for letter in tekst:
    if letter.isalpha():
        basis = ord('A') if letter.isupper() else ord('a')
        nieuwe_letter = chr((ord(letter) - basis + 5) % 26 + basis)
        versleuteld += nieuwe_letter
    else:
        versleuteld += letter

print(versleuteld)



