#Comparadores múltiplos
print(1 < 2 > 3)

#Comparador AND equivale ao && de PHP
print(1 > 2 and  2 > 3)
print(2 > 1 and 2 > 3)
print(2 > 1 and 2 < 3)

#Comparador OR equivalente ao || do PHP
print(2 > 1 or 2 > 3)

#Intercalando AND e OR em uma expressão de comparação
print((2 > 1 or 2 > 3) and (2 > 11 or 2 < 3))