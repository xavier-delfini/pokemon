from Pokemon import Pokemon


class TypeDefiner(Pokemon):
    def __init__(self, name="missingNo", type=None, pv=100, attack=100, defense=0):
        Pokemon.__init__(self)
        self.type = None

    def getType(self):
        return self.type

    def setType(self, selectedPokemonType):
        from Type import PokeType as PokemonType
        i = 0
        for currentPokemonType in PokemonType.types:#Récupération des types disponibles
            if currentPokemonType == selectedPokemonType:#Si le Type entrée par l'utilisateur correspont a l'un des titres disponible
                self.setPV(PokemonType.typesChar[i][0])
                self.setAttack(PokemonType.typesChar[i][1])
                self.setDefense(PokemonType.typesChar[i][2])
                self.type = currentPokemonType
            i += 1
        if self.type is None:#Si aucun Type n'est défini a la fin de boucle (Le type entrée n'existe pas)
            return 1
        return "OK"
