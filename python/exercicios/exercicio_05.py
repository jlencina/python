print("Quanto você ganha por hora?")
ganho_hora = float(input())

print("Quantas horas você trabalhou no mês?")
horas_mes = float(input())

salario_bruto = horas_mes * ganho_hora
ir = salario_bruto * 0.11
inss = (salario_bruto - ir) * 0.08
sindicato = (salario_bruto - ir - inss) * 0.05

print("\n")
print("O salário bruto é: {:.2f}".format(salario_bruto))
print("Quantidade paga ao Imposto de Renda é: {:.2f}".format(salario_bruto - ir))
print("Quantidade paga ao INSS: {:.2f}".format(salario_bruto - inss))
print("Quantidade paga ao Sindicato: {:.2f}".format(salario_bruto - sindicato))
print("O salario liquido é: {:.2f}".format(salario_bruto - ir - inss - sindicato))