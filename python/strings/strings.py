string_teste = "Testando string"

print(string_teste)

string_aspas = 'com "aspas" dentro'

print(string_aspas)

print(len(string_aspas))
print(len(string_teste))

#Concatenar strings com +
print(string_teste + " " + string_aspas)

#Pegando posições de uma string
print(string_teste[1])

#Retornando os indices de uma string iniciando por 1 e terminando ao final da string
print(string_teste[1:])

#Retornando os indices de uma string iniciando por 1 e terminando na posição 4
print(string_teste[1:4])

#Retornando os indices de uma string retirando o último indice da string
print(string_teste[:-1])

#Retornando os indices de uma string com o intervalo de 2 em 2
print(string_teste[::2])

#Retornando a string inversa
print(string_teste[::-1])

#Multiplicando strings
print("a" * 10)

#Printando o tipo de argumento
print(type("a"))

#Acessando os métodos de um objeto
print(dir("hello"))

#Utilizando o método interno
print("HELLO".lower())

#Utilizando o método interno
print("hello".upper())

#Utilizando o método interno
print("Hello Juan".split())

#Utilizando interpolação de variável dentro de uma string
idade = 18
print("Idade da pessoa é: {}".format(idade))

#Utilizando interpolação de variável dentro de uma string
idade = 27
nome = "Juan"
print("{n} é o nome e sua idade é: {i}".format(n=nome, i=idade))