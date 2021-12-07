print("Bem vindo(a) a loja de tintas")
print("Informe a áres que você deseja pintar: ")
area = float(input())
volume_necessario = area / 3
latas = int(volume_necessario / 18)
custo = latas * 80

print("Você precisará de {} latas e elas custarão {} reais".format(latas, custo))

