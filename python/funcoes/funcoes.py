def diga_ola(nome, sobrenome):
    print("Olá! Seja bem vindo(a) {} {}.".format(nome, sobrenome))
    
diga_ola("Juan", "Lencina")


def gerador_de_numeros_impares(x):
    return [i for i in range(x) if i % 2 == 1]

print(gerador_de_numeros_impares(11))

def add_num(num1, num2):
    return num1+num2

print(add_num(10, 20))