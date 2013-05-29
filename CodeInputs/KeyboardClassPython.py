#The (keyboard) spesifies inheritance from Keyboard
class ComputerKeyboard(Keyboard):

     def __init__(self, language, nKeys):
         
         self.language = language            
         
         #Use the superclass contructor to set the number of keys
         super(ComputerKeyboard, self).__init__(nKeys)

        
     def setupKeys(self):
         
         if self.language == "Norwegian":
             "Set up norwegian keyboard style"  
         elif ...


     def pressKey(self, key):
         return self.keys[key]



#Dummy import for illustration purposes
from myDevices import Speakers

class MusicalKeyboard(Keyboard):
	
     def __init__(self, nKeys, volume):

         #Set the ouput device to speakers implemented elsewhere
         self.outputDevice = Speakers()         
         self.volume = volume
         
         super(ComputerKeyboard, self).__init__(nKeys)

                  
     def setupKeys(self):
         lowest = 27.5 #Hz
         step = 1.06 #Relative increase in Hz (neighbouring keys)
         
         self.keys = [lowest + i*step for i in range(self.nKeys)]


     def pressKey(self, key):

         #Returns a harmonic wave with frequency and amplitude
         #extracted from the pressed key and the volume level.
         outout = ...
         self.outputDevice.play(key, output)

    
    #Fades out the playing tune
    def releaseKey(self, key):
        self.outputDevice.fade(key)
        