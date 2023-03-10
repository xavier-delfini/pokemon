class Pokemon:
    def __init__(self, inputName="missingNo", inputPv=100, inputAttack=100, inputDefense=100):
        self.__name = inputName
        self.__PV = inputPv
        self.__Attack = inputAttack
        self.__Defense = inputDefense

#Get et Set des arguments ci dessus
    def GetName(self):
        return self.__name

    def SetName(self, newName):
        self.__name = newName

    def GetPV(self):
        return self.__PV

    def SetPV(self, newPV):
        self.__PV = newPV

    def GetAttack(self):
        return self.__Attack

    def SetAttack(self, newAttack):
        self.__Attack = newAttack

    def GetDefense(self):
        return self.__Defense

    def SetDefense(self, newDefense):
        self.__Defense = newDefense
