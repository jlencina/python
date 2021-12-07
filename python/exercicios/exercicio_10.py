print("Informe o nome: ")
nome = input()

while len(nome) <= 3:
    print("O nome deve conter mais de 3 caracteres.")
    print("Informe o nome: ")
    nome = input()
    
print("Informe a idade: ")
idade = int(input())

while (idade <= 0) or (idade >= 150):
    print("O nome deve estar entre 0 e 150.")
    print("Informe a idade: ")
    idade = int(input())
    
print("Informe o salário: ")
salario = int(input())

while salario <= 0:
    print("O salário deve ser maior que zero")
    print("Informe a idade: ")
    salario = int(input())
    
print("Informe o sexo: ")
sexo = input()

while sexo not in ['m', "f"]:
    print("O sexo deve ser 'm' ou 'f'.")
    print("Informe o sexo: ")
    sexo = input()
    
print("Informe o estado civil: ")
estado_civil = input()

while estado_civil not in ["c", "s", "v", "d"]:
    print("O sexo deve ser 'c', 's', 'v' ou 'd'.")
    print("Informe o estado civil: ")
    estado_civil = input()