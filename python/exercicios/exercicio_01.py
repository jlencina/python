import time

print("Bem vindo a calculadora de IMC")

print("Por favor informe a sua altura")
altura = float(input())

print("Por favor informe o seu peso")
peso = float(input())

print("Calculando. 10%")
time.sleep(1)
print("Calculando.. 30%")
time.sleep(1)
print("Calculando... 50%")
time.sleep(1)
print("Calculando. 70%")
time.sleep(1)
print("Calculando.. 90%")
time.sleep(1)
print("Calculando... 100%")
time.sleep(1)


print("==========")
print("Seu IMC é de: {:.2f}".format(peso / altura ** 2))
print("Seu IMC é de: {}".format(peso / altura ** 2))