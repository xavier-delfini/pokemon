class Combat:
    def __init__(self, firstPokemon, secondPokemon):
        self.firstPokemon = firstPokemon
        self.secondPokemon = secondPokemon
    #def ChoosePokemon(self):

    def Game(self,firstpokemon,secondpokemon):
        import sys
        sys.path.append('../Pokemon/')
        import JsonPokemon
        FirstPokemon=JsonPokemon()
        SecondPokemon=JsonPokemon()
        print(FirstPokemon.getPokemon(firstpokemon))
    #def calculateDamage(
        #affinitytable(A,D)
    #def checkhealth(pokemonHealth)

    #def affinitytable(attackerType,defenderType)

fight=Combat("Carapuce","Salameche")
fight.Game("Carapuce","Salameche")

