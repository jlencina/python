#Iteração sobre range
for i in range(100):
    print(i)
    
#Iteração sobre lista    
l = ["a", "b", "c"]
for i in l:
    print(i)
    
#Iteração sobre string
string = "juan"
for i in string:
    print(i)
    
#Iteração testando números pares
for i in range(100):
    if i % 2 == 0:
        print("{} é par".format(i))
    else:
        print("{} é ímpar".format(i))