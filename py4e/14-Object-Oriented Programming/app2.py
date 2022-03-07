class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self,z):
        self.name = z
        print("constructed", z)
    
    def party(self):
        self.x = self.x + 1
        print(self.name,"the count is", self.x)
    
    def __del__(self):
        print(self.name,"im destructed", self.x)

class AfterParty(PartyAnimal):
    pionts = 0
    def roll(self):
        self.pionts = self.pionts + 7
        self.party()
        print(self.name,"Pionts",self.pionts)

am = PartyAnimal("othman")
am.party()
am.party()
am.party()
am = 22

an = AfterParty("Ahmad")
an.roll()
an.roll()

print("am is", am)