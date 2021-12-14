class Circle:
    def __init__(self, raio=1):
        self.raio = raio
        
    def calculaArea(self):
        return self.raio * self.raio * 3.14    
        
    def retornaRaio(self):
        return self.raio
        
c1 = Circle()
c2 = Circle(2)

print(c1.calculaArea())
print(c2.calculaArea())

print(c1.retornaRaio())
print(c2.retornaRaio())