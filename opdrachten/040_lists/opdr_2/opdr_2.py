# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

rivier_info = { 
    "rijn": ["nederland", "duitsland", "Frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}
rivieren = list(rivier_info.keys())

for rivier in rivieren:
    rivier_naam = rivier.capitalize()
    land = rivier_info[rivier][2].capitalize()
    print(f"De Rivier {rivier_naam} stroomt onder andere door {land}")

