class Carteira:
    def __init__(self, tipo: str, saldo_inicial: float):
        self.tipo = tipo
        self.saldo = saldo_inicial

    def __add__(self, valor_yuan: float):
        if self.tipo == "CNY":
            self.saldo += valor_yuan
            return self
        elif self.tipo == "USD":
            self.saldo += valor_yuan * 0.14
            return self
        elif self.tipo == "BRL":
            self.saldo += valor_yuan * 0.85
            return self
        
    def __sub__(self, valor_yuan: float):
        if self.tipo == "CNY":
            self.saldo -= valor_yuan
            return self
        elif self.tipo == "USD":
            self.saldo -= valor_yuan * 0.14
            return self
        elif self.tipo == "BRL":
            self.saldo -= valor_yuan * 0.85
            return self