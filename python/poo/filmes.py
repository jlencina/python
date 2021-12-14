class Filme:
    def __init__(self, nome, duracao, ano):
        self.nome = nome.title()
        self.duracao = duracao
        self.ano = ano

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas



vikings = Serie("vikings", 2015, 6)
vingadores = Filme('vingadores ultimato', 120, 2019)


print(f'Nome: {vingadores.nome} | Duração: {vingadores.duracao} | Ano: {vingadores.ano}')
print(f'Nome: {vikings.nome} | Ano: {vikings.ano} | Temporadas: {vikings.temporadas}')
