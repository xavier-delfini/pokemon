from Pokemon import Pokemon


class TypeDefiner(Pokemon):
    def __init__(self, name="missingNo", type=None, pv=100, attack=100, defense=0):
        Pokemon.__init__(self)
        self.type = None

    def getType(self):
        return self.type

    def setType(self, selectedPokemonType):
        from Type import PokeType as PokemonType
        i=0
        for currentPokemonType in PokemonType.types:
            if currentPokemonType == selectedPokemonType:
                self.setPV(PokemonType.typesChar[i][0])
                self.setAttack(PokemonType.typesChar[i][1])
                self.setDefense(PokemonType.typesChar[i][2])
                self.type = currentPokemonType
            i+=1
        if self.type is None:
            return 1
        return "OK"
