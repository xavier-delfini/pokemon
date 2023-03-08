from JsonPokemon import JsonPokemon
from Combat import Combat
import random
import time
def IASelectPokemon():
    IAPokemon=random.choice(Poke.getAllPokemon())
    print("L'adversaire choisi "+IAPokemon)
    return IAPokemon
while True:
    question = input("Bienvenue que souhaitez-vous faire ?(N=Nouvelle partie,A=Ajouter un nouveau pokémon,P=Pokédex")
    Poke = JsonPokemon()
    match question:
        case "N":
            Poke.printAllPokemon()
            while True:
                selectedPokemon = input("Veuillez selectionné un pokémon parmis la liste ci-dessus :")
                if selectedPokemon in Poke.getAllPokemon():
                    print("Vous choisissez "+selectedPokemon)
                    time.sleep(1)
                    break
            IAPokemon=IASelectPokemon()
            time.sleep(1)
            Play=Combat(selectedPokemon,IAPokemon)
            Play.Game()
            Poke.registerInPokedex(selectedPokemon)
            Poke.registerInPokedex(IAPokemon)
        case "A":
            nom = str(input("Veuillez entrer le nouveau nom de votre pokémon :"))
            while True:
                Poke.printAllType()
                type = input("Veuillez entrer le nom de votre pokémon parmis les types ci dessus :")
                if type in Poke.getAllType():
                    break
            Poke.createPokemon(nom, type)
        case "P":

            while True:
                Poke.printDiscoveredPokemon()
                Selectionnedpokemon=input("Voici ci-dessus la liste des pokémons découverts:")
                if Selectionnedpokemon in Poke.getDiscoveredPokemon():
                    Poke.printPokemonInfos(Selectionnedpokemon)
                    break




