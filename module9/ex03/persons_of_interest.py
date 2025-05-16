#!/usr/bin/env python3

def famous_births(library):
    library = sorted(library.values(), key=lambda person: person["date_of_birth"])
    for person in library:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "190" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
    
famous_births(women_scientists)