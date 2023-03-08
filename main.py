from JsonPokemon import JsonPokemon
while True:
    question=input("Bienvenue que souhaitez-vous faire ?,(N=Nouvelle partie,A=Ajouter un nouveau pokémon,P=Pokédex")
    match question:
        case "N":

        case "A":
        case "P":



Poke=JsonPokemon()
Poke.verif_database(pokemon_name)

def launch_game(pokemon_name):
