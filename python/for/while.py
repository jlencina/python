""" x = 0
while x < 1000:
    print("O valor de x é: {}".format(x)) 
    #x += 1 é igual a x = x + 1
    x += 1
    continue
    print("X ainda é menor que 1000. Incrementando...")
else:
    print("Concluído o While") """
    
    
x = 0
while x < 1000:
    print("O valor de x é: {}".format(x)) 
    #x += 1 é igual a x = x + 1
    x += 1
    break
    print("X ainda é menor que 1000. Incrementando...")
print("Quebra do While")
print("O valor de {} foi incrementado".format(x))