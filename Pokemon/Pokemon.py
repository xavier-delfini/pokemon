class Pokemon:
    def __init__(self, name="missingNo", PV=100, Attack=100, Defense=100):
        self.name = name
        self.PV = PV
        self.Attack = Attack
        self.Defense = Defense

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPV(self):
        return self.PV

    def setPV(self, newPV):
        self.PV = newPV

    def getAttack(self):
        return self.Attack

    def setAttack(self, newAttack):
        self.Attack = newAttack

    def getDefense(self):
        return self.Defense

    def setDefense(self, newDefense):
        self.Defense = newDefense
