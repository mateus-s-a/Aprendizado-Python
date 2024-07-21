"""AULA 18 (Aula Prática) --- Jogo de Advinhação."""
import random
import os

num = random.randint(0, 100)
erros = 0

def adivinhar():
    global res
    res = int(input("Tente adivinhar o número: "))
    return res

while(num != adivinhar()):
    os.system('cls')

    if res < num: print("Muito baixo.")
    else: print("Muito alto.")
    erros += 1
    print("Errado, tente novamente!")

print("Parabéns, acertou! Total de erros:", erros)