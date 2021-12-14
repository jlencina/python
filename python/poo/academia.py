import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_haleteres = {}
        self.reiniciar_o_dia()
        
    def reiniciar_o_dia(self):
        self.porta_haleteres = {i: i for i in self.halteres}
        
    def listar_halteres(self):
        return [i for i in self.porta_haleteres.values()]
        
self = Academia.reiniciar_o_dia()

print(self)