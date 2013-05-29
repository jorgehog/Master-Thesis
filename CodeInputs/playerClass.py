#playerClass.py
import random

class Player:
    
    def __init__(self, name):
        #Player initialized at full health and full energy.
        self.health = self.energy = 100         
        
        self.name = name        
        self.dead = False

        #Player initialized with no available potions.
        self.potions = []	


    def addPotion(self, potion):
        self.potions.append(potion)


    #Selects the given potion and consumes it. The potion needs to know
    #the player it should affect, hence we send 'self' as an argument.
    def usePotion(self, potionIndex):   
        print "%s consumes %s." % (self.name, self.potions[potionIndex].name)
        
        selectedPotion = self.potions[potionIndex]  
        selectedPotion.applyPotionTo(self)           #Self explainatory!     
        self.potions.pop(potionIndex)	             #Removed the potion.
   
          
    def changeHealth(self, amount):
        self.health += amount
        
        #Cap health at [0,100]. 
        if self.health > 100: self.health = 100
        elif self.health <= 0:
            self.health = 0
            self.dead = True;

						
    def changeEnergy(self, amount):
        self.energy += amount
        	
        #Cap energy at [0,100].
        if self.energy > 100: self.energy = 100
        elif self.energy < 0: self.energy = 0

	
    #Lists the potions to the user.
    def displayPotions(self):
        if not self.potions:
            print "  No potions available"
            
        for potion in self.potions: print "  " + potion.name     
    
        
    def attack(self, targetPlayer):
          
        energyCost = 55

        if self.energy < energyCost:
            print "%s: Insuficcient energy to attack." % self.name; return
        
        damage = 40 + random.randint(-10, 10)
          
        targetPlayer.changeHealth(-damage)
        self.changeEnergy(-energyCost)
          
        print "%s hit %s for %s using %s energy" % (self.name, 
                                                      targetPlayer.name, 
                                                      damage, energyCost)