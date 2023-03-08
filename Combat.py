import random


class Combat:
    def __init__(self, playerPokemon, AIPokemon):
        self.firstPokemon, self.secondPokemon = self.PrepareForFight(playerPokemon, AIPokemon)

    def PrepareForFight(self, playerPokemon, AIPokemon):
        startingorder = self.__ChooseStartingPokemon(playerPokemon, AIPokemon)
        firstPokemon, secondPokemon = self.__setPokemonStats(startingorder[0], startingorder[1])
        Poke1Affinity = self.__GetAffinity(firstPokemon[1], secondPokemon[1])
        Poke2Affinity = self.__GetAffinity(secondPokemon[1], firstPokemon[1])  # Inversion de l'affinité
        firstPokemon.append(Poke1Affinity)
        secondPokemon.append(Poke2Affinity)
        return firstPokemon, secondPokemon

    def __CheckAffinityTable(self, x, y):
        from CombatParameters import affinitytable as array
        return array.affinity[x][y]

    def __GetAffinity(self, currentPokemonType, vsPokemonType):
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
        return self.__CheckAffinityTable(Affinity[0], Affinity[1])

    def __ChooseStartingPokemon(self, pokemon1, pokemon2):
        import random
        start_order = random.random()
        print(start_order)
        if 0.5 >= start_order:
            print("Vous commencer")
            return [pokemon1, pokemon2]
        elif 0.5 < start_order:
            print("L'adversaire commence")
            return [pokemon2, pokemon1]

    def __setPokemonStats(self, firstPoke, secondpoke):
        from JsonPokemon import JsonPokemon
        FirstPokemon = JsonPokemon()
        SecondPokemon = JsonPokemon()
        StatsPoke1 = FirstPokemon.getPokemonInfos(firstPoke)
        StatsPoke2 = SecondPokemon.getPokemonInfos(secondpoke)

        return StatsPoke1, StatsPoke2

    def Game(self):
        import time
        FirstPokemonTurn = True
        while True:
            if FirstPokemonTurn == 1:
                attacker = self.firstPokemon
                defender = self.secondPokemon
                FirstPokemonTurn = 0
            else:
                attacker = self.secondPokemon
                defender = self.firstPokemon
                FirstPokemonTurn = 1
            print("Au tour de " + attacker[0] + " d'attaquer")
            time.sleep(1)
            if self.__HitOrNot():
                damages = int(self.__calculateDamage(attacker[3], attacker[5], defender[4]))

                if attacker[5] == 2:
                    efficacity = "C'est super efficace ,"
                elif attacker[5] == 0.5:
                    efficacity = "Ce n'est pas très efficace ,"
                else:
                    efficacity = ""
                print(efficacity + "le " + defender[0] + " ennemis subit " + str(damages) + " points de dégats")
                defender[2] = defender[2] - damages
            else:
                print(attacker[0] + " a raté son attaque")
            time.sleep(1)
            print(attacker[0] + ": " + str(attacker[2]) + " PV")
            print(defender[0] + ": " + str(defender[2]) + " PV")
            time.sleep(3)
            if self.IsKO(defender[2]) == 1:
                print("Le pokémon " + defender[0] + " est KO, victoire de " + attacker[0])

                break

    def __calculateDamage(self, AttackerAttack, AttackerAffinity, DefenderDefense):
        return (AttackerAttack - DefenderDefense) * AttackerAffinity

    def IsKO(self, pokemon_defender_health):
        if pokemon_defender_health <= 0:
            return 1
        else:
            return 0

    def __HitOrNot(self):
        import random
        roll = random.random()
        from CombatParameters import hitchance as hit
        if roll < hit.hit:
            return 1
        else:
            return 0