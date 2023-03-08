class Pokemon:
    def __init__(self, name="missingNo", PV=100, Attack=100, Defense=100):
        self.__name = name
        self.__PV = PV
        self.__Attack = Attack
        self.__Defense = Defense

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getPV(self):
        return self.__PV

    def setPV(self, newPV):
        self.__PV = newPV

    def getAttack(self):
        return self.__Attack

    def setAttack(self, newAttack):
        self.__Attack = newAttack

    def getDefense(self):
        return self.__Defense

    def setDefense(self, newDefense):
        self.__Defense = newDefense
