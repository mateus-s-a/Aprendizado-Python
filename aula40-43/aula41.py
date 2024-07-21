"""AULA 41 --- Expressões Regulares - RegEx search()"""
# search() = é utilizado para encontrar padrões em strings, como um filtro de busca.
# search() OBJETO CORRESPONDENTE À PRIMEIRA OCORRÊNCIA DO PADRÃO NA STRING OU 'None' SE NENHUM PADRÃO FOR ENCONTRADO.

import re
from aula40 import texto

res = re.search("Lorem", texto)

print(res.start()) # --- start() = retorna aonde o padrão foi encontrado
print(res.end()) # --- end() = retorna aonde o padrão foi encontrado
print(res.group()) # --- group() = retorna o padrão encontrado
print(res.span()) # --- span() = (0, 5)

print(f"Tamanho do termo encontrado: {res.end() - res.start()}")



res = re.search("lorem", texto)

print(res) # --- None, pois o 'lorem' não foi encontrado