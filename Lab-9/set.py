# QUESTAO 1

frase = "O rato roeu a roupa do Robson"
seti = set()

for letra in frase:
    if letra != " ":
        seti.add(letra.lower())

print(sorted(seti))

#