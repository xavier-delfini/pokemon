import random
import constant as parameter
from PokeDatabase import PokeDatabase
import time
class Combat:
    def __init__(self, playerPokemonName, computerPokemonName):
        self.firstPokemon, self.secondPokemon = self.__PrepareForFight(playerPokemonName, computerPokemonName)

    def __PrepareForFight(self, playerPokemonName, computerPokemonName):
        startingOrder = self.__ChooseStartingPokemon(playerPokemonName, computerPokemonName)
        firstPokemon, secondPokemon = self.__SetPokemonStats(startingOrder[0], startingOrder[1])
        poke1Affinity = self.__GetAffinity(firstPokemon[1], secondPokemon[1])
        poke2Affinity = self.__GetAffinity(secondPokemon[1], firstPokemon[1])
        firstPokemon.append(poke1Affinity)  # Ajout de l'affinité du pokémon a la liste des propriété du Pokémon
        secondPokemon.append(poke2Affinity)
        return firstPokemon, secondPokemon

    def __CheckAffinityTable(self, x, y):
        return parameter.AFFINITY_ARRAY[x][y]

    def __GetAffinity(self, selectedPokemonType, vsPokemonType):
        combatingPokemonsType = [selectedPokemonType, vsPokemonType]
        affinityLocation = []
        # 0=Eau
        # 1=Feu
        # 2=Plante
        # 3=Normal
        for pokemonType in combatingPokemonsType:
            i = 0
            for availableType in parameter.TYPES_NAME_ARRAY:
                if availableType == pokemonType:
                    affinityLocation.append(i)
                i += 1
        return self.__CheckAffinityTable(affinityLocation[0], affinityLocation[1])

    def __ChooseStartingPokemon(self, pokemon1, pokemon2):
        startOrder = random.random()
        if 0.5 >= startOrder:
            print("Vous commencer")
            return [pokemon1, pokemon2]
        elif 0.5 < startOrder:
            print("L'adversaire commence")
            return [pokemon2, pokemon1]

    def __SetPokemonStats(self, firstPokemonName, secondPokemonName):
        firstPokemonObject = PokeDatabase()
        secondPokemonObject = PokeDatabase()
        StatsPokemon1 = firstPokemonObject.GetPokemonInfos(firstPokemonName)
        StatsPokemon2 = secondPokemonObject.GetPokemonInfos(secondPokemonName)
        return StatsPokemon1, StatsPokemon2

    def Game(self):
        isStartingPokemonTurn = 1
        while True:
            if isStartingPokemonTurn == 1:
                pokemonAttacking = self.firstPokemon
                pokemonDefending = self.secondPokemon
                isStartingPokemonTurn = 0
            else:
                pokemonAttacking = self.secondPokemon
                pokemonDefending = self.firstPokemon
                isStartingPokemonTurn = 1
            print("Au tour de " + pokemonAttacking[0] + " d'attaquer")
            time.sleep(1)
            if self.__HitOrNot():
                dealtDamages = int(self.__CalculateDamage(pokemonAttacking[3], pokemonAttacking[5], pokemonDefending[4]))
                if pokemonAttacking[5] == 0:
                    print("ça n'affecte pas " + pokemonDefending[0] + " ennemis")
                else:
                    if pokemonAttacking[5] == 2:
                        printAttackAfficacity = "C'est super efficace ,"
                    elif pokemonAttacking[5] == 0.5:
                        printAttackAfficacity = "Ce n'est pas très efficace ,"
                    else:
                        printAttackAfficacity = ""
                    print(printAttackAfficacity + "le " + pokemonDefending[0] + " ennemis subit " + str(
                        dealtDamages) + " points de dégats")
                    pokemonDefending[2] = pokemonDefending[2] - dealtDamages
            else:
                print(pokemonAttacking[0] + " a raté son attaque")
            time.sleep(1)
            print(pokemonAttacking[0] + ": " + str(pokemonAttacking[2]) + " PV")
            print(pokemonDefending[0] + ": " + str(pokemonDefending[2]) + " PV")
            time.sleep(3)
            if self.__IsKO(pokemonDefending[2]) == 1:
                print("Le pokémon " + pokemonDefending[0] + " est KO, victoire de " + pokemonAttacking[0])
                break

    def __CalculateDamage(self, attackerAttack, attackerAffinity, defenderDefense):
        return (attackerAttack - defenderDefense) * attackerAffinity

    def __IsKO(self, pokemonDefencerHealth):
        if pokemonDefencerHealth <= 0:
            return 1
        else:
            return 0

    def __HitOrNot(self):
        roll = random.random()
        if roll < parameter.HIT_CHANCE:
            return 1
        else:
            return 0

#Pokemon1=Combat("Pikachu","Gobu")
#Pokemon1.Game()
