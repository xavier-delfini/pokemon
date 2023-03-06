import json
import sys


class JsonPokemon:

    def createPokemon(self, name, type):
        sys.path.insert(0, 'Type/')
        import importlib

        # Import the module
        module = importlib.import_module('Type.TypeDefiner')
        NewPoke = module.TypeDefiner()
        # Use the module
        if NewPoke.setType(type) == "OK" and self.verif_database(name) == 1:
            self.addToPokebase([name,type])
            print("Le pokémon " + name + " à été créer avec succès")
        else:
            print("Veuillez vérifier que le pokémon possède un type valide ou n'existe pas déjà dans la base de donnée")

    def getPokemon(self, name):
        pokedatabase = self.fetch_PokeBase()
        for pokemon in pokedatabase[0]:
            if pokemon[0] == name:
                return pokemon
        return None

    def verif_database(self, name):
        pokebase = self.fetch_PokeBase()
        for pokemon in pokebase[0]:
            if name == pokemon[0]:
                return 0
        return 1

    def fetch_PokeBase(self):
        f = open("pokemon.json", "r")
        array = f.read()
        f.close()
        # Retourne un array à 2 dimentions
        return json.loads(array)

    def addToPokebase(self, pokemon):  # pokemon étant un array avec le nom + type
        pokebase = self.fetch_PokeBase()
        pokebase[0].append(pokemon)
        json_value = json.dumps(pokebase)
        f = open("pokemon.json", "w")
        f.write(json_value)
        f.close()

pokemon1 = JsonPokemon()
print(pokemon1.getPokemon("Rattata"))
pokemon1.createPokemon("Rattatac", "Normal")
