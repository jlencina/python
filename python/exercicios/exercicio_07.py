list_nums = []

for i in range(3):
    print("Informe o {}º número: ".format(i + 1))
    x = int(input())
    list_nums.append(x)
    
list_nums.sort()
print("O maior número é: {}".format(list_nums[-1]))
print("O menor número é: {}".format(list_nums[0]))