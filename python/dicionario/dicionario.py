
#Diferente de Listas, um Dicionário é acessado por sua chave de acesso que se dá pelo nome
#No caso do dict de exemplo as chaves de acesso são "nome", "idade", "telefone", "salario" e "filhos"

dict = {"nome": "Juan", "idade": 27, "telefone": "(51) 99839-7555", "salario" : 2250.43, "filhos" : {"nenhum"}}
print(dict)

#Retornando nome
print(dict["nome"])

#Retornando idade
print(dict["idade"])

#Retornando telefone
print(dict["telefone"])

#Retornando salario
print(dict["salario"])

#Retornando filhos
print(dict["filhos"])

#Retornando cidade, valor não existente no dicionário
dict["cidade"] = "Eldorado do Sul"
#Retornando a cidade adicionada dentro do dicionario
print(dict["cidade"])

#Adicionando variavel aleatoria dentro do dicionário
#Notando que, é possivel utilizar espaço para definir uma adição ao dicionário
dict["variavel aleatoria"] = {"a": 1, "b": 2}

print(dict["variavel aleatoria"])



################
#Métodos de dicionário
#Retorna as keys de acesso ao dicionário
print(dict.keys())

#Retorna os values que as keys tem
print(dict.values())

#Retorna os pares do dicionário
print(dict.items())