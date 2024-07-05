"""AULA 13 --- Função Input"""

import os # --- importa a biblioteca os (operating system)
os.system('cls') # --- limpa a tela (apaga tudo que estiver na tela)

nome = input("Digite seu nome: ")
print("Seu nome é:", nome)

num1 = input("Digite o primeiro valor....: ")
num2 = input("Digite o segundo valor.....: ")

res = int(num1) + int(num2)
print("A soma dos valores é:", res)