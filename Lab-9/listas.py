# # QUESTAO 1

Inteiros = list(map(int, input("Digite pelo menos 4 numeros inteiros: ").split()))

print("Lista inteira: " + ", ".join(map(str, Inteiros)))
print("Os 3 primeiros numeros da lista: " + ", ".join(map(str, Inteiros[:3])))
print("Os 2 ultimos numeros da lista: " + ", ".join(map(str, Inteiros[-2:])))
print("Lista Invertida: " + ", ".join(map(str, Inteiros[::-1])))
print("Elementos de indice par: " + ", ".join(map(str, Inteiros[::2])))
print("Elementos de indice impar: " + ", ".join(map(str, Inteiros[1::2])))

# # QUESTAO 2

URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
print("Dominios: " + ", ".join([dominio.split(".")[1] for dominio in URLs]))

# # QUESTAO 3

from random import randint
lista = [randint(1, 100) for _ in range(10)]

print("Lista ordenada: " + ", ".join(map(str, sorted(lista))))
print("Lista original: " + ", ".join(map(str, lista))) 
print(f"Indice do maior elemento: {lista.index(max(lista))}")
print(f"Indice do menor elemento: {lista.index(min(lista))}")
print(f"Soma dos elementos: {sum(lista)}")
print(f"Media dos elementos: {sum(lista)/len(lista)}")

# QUESTAO 4

listas = []
for i in range(2):
    q = int(input(f"Digite a quantidade de elementos da lista {i + 1}: "))
    print(f"Digite os {q} elementos da lista {i + 1}: ")
    listas.append([input() for _ in range(q)])

print("Lista Intercalada: ", end="")
for i in range(len(max(listas[0], listas[1]))):
    try: print(f"{listas[0][i]} ", end="")
    except: pass
    try: print(f"{listas[1][i]} ", end="")
    except: pass

# # QUESTAO 5

from random import randint

lista1 = [randint(0, 50) for _ in range(20)]
lista2 = [randint(0, 50) for _ in range(20)]
intercecao = []

print("Lista 1 - " + ", ".join(map(str, lista1)))
print("Lista 2 - " + ", ".join(map(str, lista2)))

for i in max(lista1, lista2):
    if i in lista1 and i in lista2 and not i in intercecao:
        intercecao.append(i)

print("Intersecção - ", ", ".join(map(str, intercecao)))

# QUESTAO 6

pulo = int(input("Tamanho para divisão: "))
''
print([[randint(0, 100) for _ in range(20)][i:i+pulo] for i in range(0, 20, pulo)])

# QUESTAO 7
n = int(input("Digite n: "))
m = [[f"{i}" if i >= 10 else f" {i}" for _ in range(n)] for i in range(n)]

for linha in m:
    print(" ".join(map(str, linha)))