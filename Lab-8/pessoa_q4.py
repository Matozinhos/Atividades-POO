class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome}, Altura: {self.altura}"

    def __gt__(self, other):
        return self.altura > other.altura
    
    def __lt__(self, other):
        return self.altura < other.altura

cont = int(input("Digite a quantidade de pessoas a cadastrar: "))
pessoas = []

for i in range(cont):
    pessoas.append(Pessoa(input(f"Digite o nome da {i+1}° pessoa: "), float(input("Digite a altura da  {pessoa: "))))

print(max(pessoas))
print(min(pessoas))

for pessoa in sorted(pessoas):
    print(pessoa)