print("Veja se você foi aprovado!")
print("Insira seu nome: ")
nome = input()
print("Insira sua primeira nota: ")
nota_1 = float(input())
print("Insira sua segunda nota: ")
nota_2 = float(input())

media = (nota_1 + nota_2) / 2

print("==========")
print("A média das notas é: {}".format(media))

if media == 10:
    print("Parabéns {}! Aprovado com distinção".format(nome))
elif media >= 7:
    print("Parabéns {}! Aprovado".format(nome))
else:
    print("{}, você foi reprovado".format(nome))