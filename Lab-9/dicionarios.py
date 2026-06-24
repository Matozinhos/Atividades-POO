# QUESTAO 1

def ContarCaracteres(frase) -> dict:
    dict_retorno = dict()
    for letra in frase:
        dict_retorno[letra] = dict_retorno.get(letra, 0) + 1
    return dict_retorno

frase = "python programming"
resultado = ContarCaracteres(frase)
print(resultado)