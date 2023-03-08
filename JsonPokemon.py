import json
import sys


def fetch_PokeBase():
    f = open("pokemon.json", "r")
    array = f.read()
    f.close()
    # Retourne un array à 2 dimentions
    return json.loads(array)


class JsonPokemon:

    def createPokemon(self, name, pokemontype):
        from TypeDefiner import TypeDefiner
        NewPoke = TypeDefiner()
        if NewPoke.setType(pokemontype) == "OK" and self.verif_database(name) == 1:
            self.addToPokebase([name, pokemontype])
            print("Le pokémon " + name + " à été créer avec succès")
        else:
            print("Veuillez vérifier que le pokémon possède un type valide ou n'existe pas déjà dans la base de donnée")

    def getAllPokemon(self):
        pokedatabase = fetch_PokeBase()
        pokemon_list = []
        for pokemon in pokedatabase[0]:
            pokemon_list.append(pokemon[0])
        return pokemon_list

    def getAllType(self):
        from Type import PokeType as Poketype
        return Poketype.types

    def printAllType(self):
        for PokemonType in self.getAllType():
            print(PokemonType)

    def printAllPokemon(self):
        pokemon_list = self.getAllPokemon()
        print("Voici la liste des pokémons disponibles")
        for pokemon in pokemon_list:
            print(pokemon)

    def printDiscoveredPokemon(self):
        print("Voici la liste des pokémon que vous avez découvert")
        for pokemon in self.getDiscoveredPokemon():
            print(pokemon)
    def getDiscoveredPokemon(self):
        pokedatabase = fetch_PokeBase()
        Pokedex=[]
        for pokemon in pokedatabase[1]:
            if pokemon[1] > 0:
                Pokedex.append(pokemon[0])
        return Pokedex

    def getPokemon(self, name):
        pokedatabase = fetch_PokeBase()
        for pokemon in pokedatabase[0]:
            if pokemon[0] == name:
                return pokemon
        return None

    def verif_database(self, name):
        pokebase = fetch_PokeBase()
        for pokemon in pokebase[0]:
            if name == pokemon[0]:
                return 0
        return 1

    def getPokemonInfos(self, name):
        # Verification de l'existance du pokémon et récupération de ses infos
        pokemoninfos = JsonPokemon()
        p = pokemoninfos.getPokemon(name)

        # Récupération des stats relatives au type du pokémon
        from TypeDefiner import TypeDefiner
        Poke = TypeDefiner(name, p[1])
        Poke.setType(p[1])
        Poke.setName(name)
        return [Poke.getName(), Poke.getType(), Poke.getPV(), Poke.getAttack(), Poke.getDefense()]

    def printPokemonInfos(self, name):
        pokemon = self.getPokemonInfos(name)
        print("Nom: " + pokemon[0])
        print("Type: " + pokemon[1])
        print("PV: " + str(pokemon[2]))
        print("Attaque: " + str(pokemon[3]))
        print("Defense: " + str(pokemon[4]))

    def registerInPokedex(self, pokemon):
        pokebase = fetch_PokeBase()
        i = 0
        for pokemonInpokebase in pokebase[1]:
            if pokemon == pokemonInpokebase[0]:
                if pokemonInpokebase[1] == 0:
                    print("Les informations à propos de " + pokemon + " ont été ajoutées au Pokédex")
                pokebase[1][i][1] += 1
                json_value = json.dumps(pokebase)
                f = open("pokemon.json", "w")
                f.write(json_value)
                f.close()
                break
            i += 1

    def addToPokebase(self, pokemon):  # pokemon étant un array avec le nom + type
        pokebase = fetch_PokeBase()
        pokebase[0].append(pokemon)
        pokebase[1].append([pokemon[0], 0])
        json_value = json.dumps(pokebase)
        f = open("pokemon.json", "w")
        f.write(json_value)
        f.close()


pokemon1 = JsonPokemon()
# print(pokemon1.getPokemon("Rattata"))
# pokemon1.createPokemon("Keunotor", "Normal")
# pokemon1.printPokemonInfos("Salameche")
pokemon1.printDiscoveredPokemon()
