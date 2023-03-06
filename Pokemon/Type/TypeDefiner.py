import sys

sys.path.insert(0, '../')

from Pokemon import Pokemon

class TypeDefiner(Pokemon):
    def __init__(self, name="missingNo", pv=100, attack=100, defense=0):
        Pokemon.__init__(self)
        self.type = None

    def getType(self):
        return self.type

    def setType(self, PokemonType):
        while True:
            match PokemonType:
                case "Normal":
                    self.type = "Normal"
                    import Normal as PokeType
                    break
                case "Feu":
                    self.type = "Feu"
                    import Feu as PokeType
                    break
                case "Eau":
                    self.type = "Eau"
                    import Eau as PokeType
                    break
                case "Plante":
                    self.type = "Plante"  # Remplacement du type Terre qui n'existe pas dans le jeu par le type Plante
                    import Plante as PokeType
                    break
                case _:
                    print("Ce type de Pokémon n'est pas valide")
                    return 1
        Pokemon.setPV(self,PokeType.PV)
        Pokemon.setAttack(self,PokeType.Attack)
        Pokemon.setDefense(self,PokeType.Defense)
        return "OK"

