# QUESTAO 1

nomec = [input("Digite seu primeiro nome: "), input("Digite seu sobrenome: ")]
print(f"Bem Vindo " + " ".join(nomec))

# QUESTAO 2

print(input("Digite uma frase: ").count(" "))

# QUESTAO 3

nome = input("Digite seu nome: ")
for i in range(1, len(nome) + 1):
    print(nome[:i])

# QUESTAO 4

num = input("Digite o Número: ")

print("Número Completo: ", end="")
if len(num) == 8: print("9", end="")
for i in range(len(num)):
    if i == 5: print("-", end="")
    print(num[i], end="")

# QUESTAO 5

frase = input("Digite uma frase: ")
ivogais = set()

for i in range(len(frase)):
    if frase[i] in "aeiou":
        ivogais.add(i)

print("Índice das vogais: ", end="")
print(*ivogais, sep=", ")
print(f"Total de Vogais: {len(ivogais)} vogais")