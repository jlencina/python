class Dog:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
        print("{}, foi adicionado as raças".format(raca))
        
    def evelhecer(self):
        self.idade +=1
        
dog = Dog("Labrador")
dog2 = Dog("Husky")
dog.evelhecer()

print(dog.idade)