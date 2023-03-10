from PokeDatabase import PokeDatabase
from Combat import Combat
import random
import time
def IASelectPokemon():
    IAPokemonselected=random.choice(pokebase.GetAllPokemon())
    print("L'adversaire choisi "+IAPokemonselected)
    return IAPokemonselected
while True:
    questionResponse = input("Bienvenue que souhaitez-vous faire ?(N=Nouvelle partie,A=Ajouter un nouveau pokémon,P=Pokédex) :")
    pokebase = PokeDatabase()
    match questionResponse:
        case "N":
            pokebase.PrintAllPokemon()
            while True:
                selectedPokemon = input("Veuillez selectionné un Pokémon parmi la liste ci-dessus :")
                if selectedPokemon in pokebase.GetAllPokemon():
                    print("Vous choisissez "+selectedPokemon)
                    time.sleep(1)
                    break
            IAPokemon = IASelectPokemon()
            time.sleep(1)
            Play = Combat(selectedPokemon, IAPokemon)
            Play.Game()
            pokebase.RegisterInPokedex(selectedPokemon)
            pokebase.RegisterInPokedex(IAPokemon)
        case "A":
            nom = str(input("Veuillez entrer le nouveau nom de votre pokémon :"))
            while True:
                pokebase.PrintAllType()
                selectedType = input("Veuillez entrer le type de votre pokémon parmis les types ci dessus :")
                if selectedType in pokebase.GetAllType():
                    break
            pokebase.CreatePokemon(nom, selectedType)
        case "P":

            while True:
                pokebase.PrintDiscoveredPokemon()
                selectionedPokemon = input("Voici ci-dessus la liste des pokémons découverts:")
                if selectionedPokemon in pokebase.GetDiscoveredPokemon():
                    pokebase.PrintPokemonInfos(selectionedPokemon)
                    break