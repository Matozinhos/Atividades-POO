frase = input("Digite uma frase: ")
ivogais = set()

for i in range(len(frase)):
    if frase[i] in "aeiou":
        ivogais.add(i)

print("Índice das vogais: ", end="")
print(*ivogais, sep=", ")
print(f"Total de Vogais: {len(ivogais)} vogais")