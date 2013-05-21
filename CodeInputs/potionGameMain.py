#potionGameMain.py

from potionClass import *
from playerClass import *

def roundOutput(n, *players):
	header= "Round %d: " % n
	print header.replace('0','start')
	for player in players:
		print "  %s (hp/e=%d/%d):" % (player.name, player.health, player.energy)
		player.displayPotions()
		print


Sigve = Player('Sigve');
Sigve.addPotion(EnergyPotion(10));

Jorgen = Player('Jorgen')
Jorgen.addPotion(HealthPotion(20)); Jorgen.addPotion(EnergyPotion(20))

Karl = Player('Karl')
Karl.addPotion(HealthPotion(20))

#Initial output
roundOutput(0, Sigve, Jorgen, Karl)

#Round one: Each player empties their arsenal
Sigve.attack(Jorgen); Sigve.attack(Karl); Sigve.usePotion(0); Sigve.attack(Karl) 
print

Karl.usePotion(0); Karl.attack(Sigve)
print

Jorgen.attack(Karl); Jorgen.usePotion(1); Jorgen.attack(Sigve)
print

roundOutput(1, Sigve, Jorgen, Karl)
#Round one end.
#...