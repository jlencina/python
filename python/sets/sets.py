x = set()
print(x)


#Adicionando valores
x.add(1)
print(x)

#Adicionando outros valores
x.add(2)
print(x)

#Adicionando mais valores
x.add(4)
print(x)

#Adicionando valor fora de sequencia
x.add(3)
print(x)

#Adicionando outro valor fora de sequencia
x.add(-1)
print(x)

#Função nativa union()
l = [1, 2, 3, 4, 4, 4, 5, 5, 5]
l1 = set(l)
print(l1)
print(x.union(l1))

#Função nativa intersection()
print(x.intersection(l1))