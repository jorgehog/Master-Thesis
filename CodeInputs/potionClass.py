#potionClass.py

class Potion:
	
    def __init__(self, amount):
        self.amount = amount
        self.setName()
        
    def applyPotionTo(self, player):
        raise NotImplementedError("Member function applyPotion not implemented.")
        
    #This function should be overwritten
    def setName(self):
        self.name = "Undefined"


class HealthPotion(Potion):
	
    #Constructor is inherited
    
    #Calls back to the player object's functions to change the health
    def applyPotionTo(self, player):
        player.changeHealth(self.amount)
    	
    def setName(self):
        self.name = "Health Potion (%d)" % self.amount


class EnergyPotion(Potion):
	
    def applyPotionTo(self, player):
        player.changeEnergy(self.amount)
        	
    def setName(self):
        self.name = "Energy Potion (%d)" % self.amount

