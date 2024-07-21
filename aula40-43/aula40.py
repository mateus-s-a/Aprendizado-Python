"""AULA 40 --- Expressões Regulares - RegEx findall()"""
# Expressões Regulares, utilizadas para ecnontrar padrões  em strings, permitindo fazer buscas, substituições e validações de forma mais flexível.
# findall() = são utilizadas para encontrar padrões em strings, como um filtro de busca.
# findall() RETORNA UMA LISTA/ARRAY COM OS VALORES ENCONTRADOS

import re # --- importando o modulo 're'
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

res = re.findall("Lorem", texto) # --- retorna = ['Lorem']
print(res)

res = re.findall("lorem", texto) # --- retorna = []
print(res) # --- não encontrou nenhum padrão, pois o 'lorem' é case-sensitive, mas podemos conter isso com o 'ignorecase'

res = re.findall("lorem", texto, re.IGNORECASE) # --- retorna = ['Lorem']
print(res) # --- encontrou o 'lorem' case-insensitive


pesquisar = input("Pesquisar: ")
res = re.findall(pesquisar, texto, re.IGNORECASE)
qtd = len(res)

if qtd > 0:
    print(f"Encontrado {qtd} vez(es)")
else:
    print("Não encontrado")