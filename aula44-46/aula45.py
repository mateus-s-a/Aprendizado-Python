"""AULA 45 --- Operações de Arquivos (Parte 2)"""
# read() = lê o conteúdo de um arquivo
import re

nome = "teste_45"

abrir_arquivo = lambda nome: open(f"aula44-46/{nome}.txt", "rt") # --- 'rt' = read text

file = abrir_arquivo(nome)
print(file.read()) # --- lê e imprime o conteúdo do arquivo

file = abrir_arquivo(nome)
print(file.read(10)) # --- lê e imprime os primeiros 10 caracteres do arquivo

file = abrir_arquivo(nome)
for i in range(3):
    print(file.readline()) # --- lê e imprime a primeira linha do arquivo
# OU
# for i in file:
#     print(i)

file = abrir_arquivo(nome)
res = re.sub("Estudando", "ESTUDANDO", file.readline(), re.IGNORECASE) # --- substitui o 'Estudando' por 'ESTUDANDO'
print(res)

file = open(f"aula44-46/{nome}.txt", "at") # --- adiciona o conteúdo do 'res' no arquivo
file.write(f"\n{res}")


file.close()