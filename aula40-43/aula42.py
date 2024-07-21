"""AULA 42 --- Expressões Regulares - RegEx split()"""
# split() = é utilizado para dividir uma string em uma lista.
# split() RETORNA UMA LISTA/ARRAY COM OS VALORES DIVIDIDOS

import re
from aula40 import texto

res = re.split(" ", texto) # --- 'split()' divide a string em uma lista(array), quando encontrar um caractere 'space'

print(res) # --- retorna = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.']
print(res[0]) # --- retorna = 'Lorem'
print(res[1]) # --- retorna = 'ipsum'
print(res[2]) # --- retorna = 'dolor'
print(res[3]) # --- retorna = 'sit'
print(res[4]) # --- retorna = 'amet,'

for i in res:
    print(i)