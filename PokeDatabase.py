import json
from TypeDefiner import TypeDefiner
import constant as parameter

class PokeDatabase:

    def __FetchPokeDataBase(self):
        f = open("pokemon.json", "r")
        array = f.read()
        f.close()
        # Retourne un array à 2 dimentions
        return json.loads(array)
    def CreatePokemon(self, pokemonName, pokemonType):
        NewPoke = TypeDefiner()
        if NewPoke.SetType(pokemonType) == "OK" and self.Verif_database(pokemonName) == 1:
            self.AddToPokebase([pokemonName, pokemonType])
            print("Le pokémon " + pokemonName + " a été créer avec succès")
        else:
            print("Veuillez vérifier que le pokémon possède un type valide ou n'existe pas déjà dans la base de donnée")

    def GetAllPokemon(self):
        pokedatabase = self.__FetchPokeDataBase()
        pokemon_list = []
        for pokemon in pokedatabase[0]:
            pokemon_list.append(pokemon[0])
        return pokemon_list

    def GetAllType(self):
        return parameter.TYPES_NAME_ARRAY

    def PrintAllType(self):
        for PokemonType in self.GetAllType():
            print(PokemonType)

    def PrintAllPokemon(self):
        pokemon_list = self.GetAllPokemon()
        print("Voici la liste des pokémons disponibles")
        for pokemon in pokemon_list:
            print(pokemon)

    def PrintDiscoveredPokemon(self):
        print("Voici la liste des pokémon que vous avez découvert")
        for pokemon in self.GetDiscoveredPokemon():
            print(pokemon)
    def GetDiscoveredPokemon(self):
        pokeDatabase = self.__FetchPokeDataBase()
        Pokedex=[]
        for pokemon in pokeDatabase[1]:
            if pokemon[1] > 0:
                Pokedex.append(pokemon[0])
        return Pokedex

    def GetPokemon(self, name):
        pokedatabase = self.__FetchPokeDataBase()
        for pokemon in pokedatabase[0]:
            if pokemon[0] == name:
                return pokemon
        return None

    def Verif_database(self, name):
        pokebase = self.__FetchPokeDataBase()
        for pokemon in pokebase[0]:
            if name == pokemon[0]:
                return 0
        return 1

    def GetPokemonInfos(self, name):
        # Verification de l'existance du pokémon et récupération de ses infos
        pokemonInfos = PokeDatabase()
        p = pokemonInfos.GetPokemon(name)
        # Récupération des stats relatives au type du pokémon
        pokemonObject = TypeDefiner(name, p[1])
        pokemonObject.SetType(p[1])
        pokemonObject.SetName(name)
        return [pokemonObject.GetName(), pokemonObject.GetType(), pokemonObject.GetPV(), pokemonObject.GetAttack(), pokemonObject.GetDefense()]

    def PrintPokemonInfos(self, name):
        pokemon = self.GetPokemonInfos(name)
        print("Nom: " + pokemon[0])
        print("Type: " + pokemon[1])
        print("PV: " + str(pokemon[2]))
        print("Attaque: " + str(pokemon[3]))
        print("Defense: " + str(pokemon[4]))

    def RegisterInPokedex(self, pokemon):
        pokebase = self.__FetchPokeDataBase()
        i = 0
        for pokemonInPokebase in pokebase[1]:
            if pokemon == pokemonInPokebase[0]:
                if pokemonInPokebase[1] == 0:
                    print("Les informations à propos de " + pokemon + " ont été ajoutées au Pokédex")
                pokebase[1][i][1] += 1
                json_value = json.dumps(pokebase)
                f = open("pokemon.json", "w")
                f.write(json_value)
                f.close()
                break
            i += 1

    def AddToPokebase(self, pokemonNameAndType):  # pokemon étant un array avec le nom + type
        pokebase = self.__FetchPokeDataBase()
        pokebase[0].append(pokemonNameAndType)
        pokebase[1].append([pokemonNameAndType[0], 0])
        json_value = json.dumps(pokebase)
        f = open("pokemon.json", "w")
        f.write(json_value)
        f.close()