from Pokemon import Pokemon
import constant as parameter


class TypeDefiner(Pokemon):
    def __init__(self, inputName="missingNo", inputType=None, inputPv=100, inputAttack=100, inputDefense=0):
        Pokemon.__init__(self)
        self.__type = None

    def GetType(self):
        return self.__type

    def SetType(self, enteredPokemonType):
        i = 0
        for PokeTypeArrayElement in parameter.TYPES_NAME_ARRAY:  # Récupération des types disponibles
            if PokeTypeArrayElement == enteredPokemonType:  # Si le Type entrée par l'utilisateur correspont a l'un des titres disponible
                self.SetPV(parameter.TYPES_CARACTERISTICS_ARRAY[i][0])
                self.SetAttack(parameter.TYPES_CARACTERISTICS_ARRAY[i][1])
                self.SetDefense(parameter.TYPES_CARACTERISTICS_ARRAY[i][2])
                self.__type = PokeTypeArrayElement
            i += 1
        if self.GetType() is None:  # Si aucun Type n'est défini a la fin de boucle (Le type entrée n'existe pas)
            return 1
        return "OK"
