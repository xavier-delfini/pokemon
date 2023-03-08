class Combat:
    def __init__(self, playerPokemon, AIPokemon):
        self.firstPokemon, self.secondPokemon = self.PrepareForFight(playerPokemon,AIPokemon)

    def PrepareForFight(self, playerPokemon, AIPokemon):
        startingorder = self.ChooseStartingPokemon(playerPokemon, AIPokemon)
        firstPokemon, secondPokemon = self.setPokemonStats(startingorder[0], startingorder[1])
        Poke1Affinity=self.GetAffinity(firstPokemon[1],secondPokemon[1])
        Poke2Affinity=self.GetAffinity(secondPokemon[1],firstPokemon[1])#Inversion de l'affinité
        firstPokemon.append(Poke1Affinity)
        secondPokemon.append(Poke2Affinity)
        return firstPokemon,secondPokemon

    def CheckAffinityTable(self, x, y):
        from CombatAffinity import affinitytable as array
        return array.affinity[x][y]

    def GetAffinity(self, currentPokemonType, vsPokemonType):
        pokemonType = [currentPokemonType, vsPokemonType]
        Affinity = []
        # 0=Eau
        # 1=Feu
        # 2=Plante
        # 3=Normal
        for type in pokemonType:
            match type:
                case "Normal":
                    Affinity.append(3)
                case "Eau":
                    Affinity.append(0)
                case "Feu":
                    Affinity.append(1)
                case "Plante":
                    Affinity.append(2)
        return self.CheckAffinityTable(Affinity[0], Affinity[1])

    def ChooseStartingPokemon(self, pokemon1, pokemon2):
        import random
        start_order = random.random()
        print(start_order)
        if 0.5 >= start_order:
            print("Vous commencer")
            return [pokemon1, pokemon2]
        elif 0.5 < start_order:
            print("L'adversaire commence")
            return [pokemon2, pokemon1]

    def setPokemonStats(self, firstPoke, secondpoke):
        from JsonPokemon import JsonPokemon
        FirstPokemon = JsonPokemon()
        SecondPokemon = JsonPokemon()
        StatsPoke1 = FirstPokemon.getPokemonInfos(firstPoke)
        StatsPoke2 = SecondPokemon.getPokemonInfos(secondpoke)

        return StatsPoke1, StatsPoke2

    def Game(self):
        print(self.firstPokemon)
        print(self.secondPokemon)

    # def calculateDamage(

    # def checkhealth(pokemonHealth)



fight = Combat("Carapuce", "Salameche")
fight.Game()
