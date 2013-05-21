class Keyboard():

     #Set member variables keys and the number of keys
     #A subclass will override these with their own representation
     keys = None
     nKeys = 0

     #Constructor (function called when creating an object of this class)
     #Sets the number of keys and calls the setup function,
     #ensuring that no object of this abstract class can be created.
     def __init__(self, nKeys):
         self.nKeys = nKeys
         self.setupKeys()
		
     def setupKeys(self):
         raise NotImplementedError("Override me!")

     def pressKey(self, key):
         raise NotImplementedError("Override me!")
         
     def releaseKey(self, key):
         raise NotImplementedError("Override me!")
         