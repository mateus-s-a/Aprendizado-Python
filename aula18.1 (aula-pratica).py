"""AULA 18.1 (Aula Prática) --- Jogo da Forca."""

import random
import os

palavras = random.choice(["casa", "carro", "computador", "livro", "mesa", "cadeira", "gato", "cachorro", "flor", "jardim"])
tamanho = len(palavras)
palavras = list(palavras)
erros = 0
c = 0

def letraAdivinhada():
    global res
    res = input("\nDigite uma letra: ")
    return res

letrasAcertadas = []
for i in range(tamanho):
    letrasAcertadas.append("_")

# print(palavras)
# print(letrasAcertadas)

while erros < 3:
    os.system('cls')

    for i in range(tamanho):
        print(letrasAcertadas[i], end=" ")

    c = 0
    if '_' in letrasAcertadas:
        print("\nVidas:", 3 - erros)
        letraAdivinhada()
        for i in range(tamanho):
            if res == palavras[i]:
                letrasAcertadas[i] = palavras[i]
            else:
                c += 1
        if c == tamanho:
            erros += 1
    else:
        print("\nParabéns, acertou!")
        break

if erros == 3:
    print("Você perdeu, a palavra era:", "".join(palavras))