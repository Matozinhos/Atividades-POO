# QUESTAO 1

# frase = "O rato roeu a roupa do Robson"
# seti = set()

# for letra in frase:
#     if letra != " ":
#         seti.add(letra.lower())

# print(sorted(seti))

# QUESTAO 2 

# def tem_elementos_comuns(lista1, lista2):
#     return True if set(lista2).intersection(set(lista1)) else False


# lista1 = [1, 2, 3, 4]
# lista2 = [3, 4, 5, 6, 7]
# resultado = tem_elementos_comuns(lista1, lista2)
# print(resultado)  

# Saída esperada: True

# QUESTAO 3 

# def atividades_comuns(lista_alunos : list) -> set:
#     s = set()
#     for aluno in lista_alunos:
#         s = s.union(aluno)
#     return sorted(s)

# turmas = [
#      {'ações comunitárias', 'futebol', 'música', 'rugby'},
#      {'ações comunitárias', 'música', 'rugby', 'teatro'},
#      {'música', 'rugby', 'teatro', 'vôlei'},
#      {'música', 'vôlei', 'rugby'},
#      {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
#      {'ações comunitárias', 'futebol', 'rugby'},
#      {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
#      {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
#      {'ações comunitárias', 'rugby', 'vôlei'}
# ]

# print(atividades_comuns(turmas))

# QUESTAO 4

def elemento_faltando(lista1, lista2):
    return list(max(set(lista1), set(lista2), key=len) - min(set(lista1), set(lista2), key=len))[0]

A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

print(f"O elemento {elemento_faltando(A, B)} esta faltando...")