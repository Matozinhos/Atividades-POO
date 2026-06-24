# QUESTAO 1

def ContarCaracteres(frase) -> dict:
    dict_retorno = dict()
    for letra in frase:
        dict_retorno[letra] = dict_retorno.get(letra, 0) + 1
    return dict_retorno

frase = "python programming"
resultado = ContarCaracteres(frase)
print(resultado)

# QUESTAO 2 

# questao 2 nao é possivel abrir o link do roteiro porem o codigo da p fazer ainda:

dic_palavras = dict()
with open("estomago.txt", "r") as arquivo:
    for linha in arquivo:
        linha.strip()
        for palavra in linha:
            dic_palavras[palavra] = dic_palavras.get(palavra, 0) + 1

dic_palavras = sorted(dic_palavras, reverse=True)
print(dic_palavras)

# acredito que funcione rs

# QUESTAO 3

def mesclar_dicionarios(dic1 : dict, dic2 : dict) -> dict:
    return_dict = dict()
    for chave, value in dic1.items():
        return_dict[chave] = value
    for chave2, value2 in dic2.items():
        return_dict[chave2] = max(return_dict.get(chave2, 0), value2)
    return return_dict

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)
# Saída esperada: {'a': 1, 'b': 4, 'c': 3, 'd': 5}

# QUESTAO 4

def filtrar_dicionario(dados : dict, chaves_filtradas : list):
    retur_dict = dict()
    for chave in dados.keys():
        if chave in chaves_filtradas:
            retur_dict[chave] = dados[chave]
    return retur_dict

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)
# Saída esperada: {'a': 1, 'c': 3, 'e': 5}

# QUESTAO 5

def resultado_votacao(votos):
    final_dict = dict()
    total = 0
    
    for dicionario in votos:
        for chave, value in dicionario.items():
            final_dict[chave] = final_dict.get(chave, 0) + value
            total += value
    
    for chave, value in final_dict.items():
        porcentagem = (value / total) * 100
        final_dict[chave] = (value, round(porcentagem, 2)) 
        
    return final_dict

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

resultado = resultado_votacao(votos)
print(resultado)  

# Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 'candidato_C': (275, 30.79)}