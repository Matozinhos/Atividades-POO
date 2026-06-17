class Onibus:
    def __init__(self, placa : str, nome_motorista : str, num_assentos : int): # True = ocupado, False = vazio
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False] * num_assentos

    def __len__(self):
        return len(self.assentos)
    
    def __getitem__(self, index):
        try:
            return self.assentos[index]
        except IndexError: raise IndexError("Índice fora do intervalo.")
    
    def __setitem__(self, index, value):
        try:
            self.assentos[index] = value
        except IndexError: raise IndexError("Índice fora do intervalo.")
    
    def __str__(self):
        print(f"Õnibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}")
        print(f"Assentos totais: {len(self)}")
        print(f"Assentos ocupados: {self.assentos.count(True)}")
        print(f"Assentos livres: {self.assentos.count(False)}")