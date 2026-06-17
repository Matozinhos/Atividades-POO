class Personagem:
    def __init__(self, nome : str, vida_inicial : int):
        self.nome = nome
        self.vida = vida_inicial
    
    def tomar_dano(self, valor : int):
        self.vida -= valor
        print(f"{self.nome} tomou {valor} de dano e ficou com hp {self.vida}")
    
class Mago(Personagem):
    def __init__(self, nome, vida_inicial, mana_inicial : float):
        super().__init__(nome, vida_inicial)
        self.mana = mana_inicial    
    
    def __str__(self) -> str:
        return f"{self.nome}: hp = {self.vida} mana = {self.mana}"
    
    def __add__(self, other : float) -> float:
        self.mana += other
        return f" Ganhou mana: {self.mana}"
    
    def __sub__(self, other : float) -> float:
        if not self.mana - other <= 0 :
            self.mana -= other
            return f"Perdeu aura: {self.mana}"
        else :
            return "Sem Mana"
    
    def __mul__(self, other : float) -> float:
        self.mana *= other
        return f"Ganhou mana: {self.mana}"
    
    def __truediv__(self, other : float) -> float:
        if other != 0:
            self.mana /= other
            self.mana
        else : return "Sem Mana"
    
class Barbaro(Personagem):
    def __init__(self, nome, vida_inicial, stamina : float):
        super().__init__(nome, vida_inicial)
        self.stamina = stamina
        self.furia : bool = False
    
    def __str__(self) -> str:
        return f"{self.nome}: hp = {self.vida} stamina = {self.stamina} furia = {self.furia}"
    
    def __add__(self, other : float):
        if self.furia:
            self.stamina += other * 1.5
            f"Ganhou stamina {self.stamina}"
        else:
            self.stamina += other
        return f"Ganhou stamina {self.stamina}"
    
    def __sub__(self, other : float):
        if self.furia and self.stamina - other <= 0:
            return f"Sem stamina"
        elif self.furia and self.stamina - other > 0:
            self.stamina -= other
            return f"Perdeu stamina: {self.stamina}"
        elif not self.furia and self.stamina - other <= 0:
            self.stamina = 0
            self.furia = True
            return f"Perdeu stamina: {self.stamina} Entrou em estado de Furia"
        elif not self.furia and self.stamina - other > 0:
            self.stamina -= other
            return f"Perdeu stamina: {self.stamina}"
    
    def __mul__(self, other : float):
        self.stamina *= other
        if self.furia: self.vida += 5
        return f"Ganhou stamina: {self.stamina}"

    def __truediv__(self, other : float):
        self.stamina /= other
        return f"Perdeu stamina: {self.stamina}"
    
Personagem_Atual : Personagem = None
    
for p_c in range(1):
    print("Qual Tipo Deseja? ")
    print("1. Mago")
    print("2. Barbaro")
    print("3. Normal")

    match int(input()):
        case 1:
            Personagem_Atual = Mago(input("Informe o nome: "), 100, 100)
        case 2: 
            Personagem_Atual = Barbaro(input("Informe o nome: "), 100, 100)
        case 3: 
            Personagem_Atual = Personagem(input("Informe o nome: "), 100)
        case _:
            print("Nao tem esse numero seu acefalo, se mate imediatamente...")

while True:
    print("Deseja: ")
    print("1. Tomar Porção Simples")
    print("2. Tomar Porção Especial")
    print("3. Ataque Básico")
    print("4. Ataque Especial")
    print("5. Mostrar personagens")
    print("6. Sair")

    match int(input()):
        case 1:
            print(Personagem_Atual + 5)
        case 2: 
            print(Personagem_Atual * 1.5)
        case 3:
            print(Personagem_Atual - 2)
        case 4: 
            print(Personagem_Atual / 2)
        case 5: 
            print(Personagem_Atual)
        case 6: 
            break

    import random
    Personagem_Atual.tomar_dano(random.randint(1,10))