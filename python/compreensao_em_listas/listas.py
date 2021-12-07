word = "string"
list_words = []

for w in word:
    list_words.append(w)
    
print(list_words)


#Segundo método
list_words = [w for w in word]
print(list_words)

#Terceiro método
list_2 = [x**2 for x in range(10)]
print(list_2)

#Quarto método com condicional
list_3 = [x for x in range(50) if x % 2 == 0]
print(list_3)