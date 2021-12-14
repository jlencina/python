class Animal:
    def __init__(self):
        print("Animal criado.")
        
    def quem_sou_eu(self):
        print("Eu sou um animal.")
        
    def comer(self):
        print("Comendo")
    
#animal = Animal()
#print(animal.quem_sou_eu())

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Eu sou um cachorro.")
    
    def quem_sou_eu(self):
        print("Eu sou um cachorro.")
        
dog = Cachorro()
print(dog)