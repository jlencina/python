print("Qual o tamanho da sequência de Fibonacci que você deseja ver?")
n = int(input())

v0 = 0
v1 = 1
v = 1

print(1)
for i in range(n+1):
    print(v)
    v0 = v1
    v1 = v
    v = v1 + v0