print("Informe um número: ")
n = int(input())

check = 0

for i in range(2, n):
    if n % i == 0:
        check = 1
        break

if check == 0:
    print("É primo")
else:
    print("Não é primo")