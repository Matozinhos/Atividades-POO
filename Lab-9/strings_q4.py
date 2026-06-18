num = input("Digite o Número: ")

print("Número Completo: ", end="")
if len(num) == 8: print("9", end="")
for i in range(len(num)):
    if i == 5: print("-", end="")
    print(num[i], end="")