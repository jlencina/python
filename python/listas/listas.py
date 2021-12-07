lista = [1, 2, 3]

print(lista)

#Printando tipo da lista
print(type(lista))

#Printando o indice 1 retirando o último indice
print(lista[1:-1])

#Selecionando o indice de uma lista dentro da lista principal
lista_principal = [1, 2, "testando", [1, 2, 3]]
print(lista_principal[3][1:])

#Utilizando métodos de manipulação de string dentro da lista
print(lista_principal[2].upper())
print(lista_principal[2].capitalize())

#Operação aritimética com a lista
print(lista_principal * 3)
print(lista_principal + [[5, 6, 7]])



###############
l = [1, 3, 10]

#Append
l.append(25)
print(l)

#Pop
l.pop()
print(l.pop())

################ 
new_lista = ["a", "b", "c", "d"]

#Reverse
new_lista.reverse()
print(new_lista)

#Sort
new_lista.sort()
print(new_lista)


################
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

list4 = [list1, list2, list3]
print(list4)


list4[1].reverse()
print(list4)

