"""AULA 43 --- Expressões Regulares - RegEx sub()"""
# sub() = é utilizado para substituir padrões em strings.
# sub() RETORNA UM TEXTO ALTERADO

import re
from aula40 import texto

res = re.sub("Lorem", "LOREM", texto) # --- substitui o 'Lorem' por 'LOREM'
print(res)

res = re.sub(" ", "_", texto) # --- substitui o ' ' por '_'
print(res)