"""AULA 30 (Aula Prática) --- Joga da Velha"""
# --- colorama = biblioteca para colorir o terminal
# --- Fore = cores do terminal
# --- Back = cores de fundo do terminal
# --- Style = estilo do texto

import os
import random
import time
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 1 # 1 = jogador; 2 = computador
maxJogadas = 9
vitoria = False
ganhador = None

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system('cls')

    print("    0   1   2")
    print(f"0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print(f"   -----------")
    print(f"1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print(f"   -----------")
    print(f"2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
    print(f"Jogadas: {Fore.GREEN}{jogadas}{Fore.RESET}") # --- Fore.GREEN = verde; Fore.RESET = reset da cor


# Jogado do jogador
def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        try:
            linha = int(input("Linha....: "))
            coluna = int(input("Coluna...: "))
            
            while velha[linha][coluna] != " ": # --- verifica se a posição informada foi válida, se não, pede novas coordenadas
                linha = int(input("Linha....: "))
                coluna = int(input("Coluna...: "))
            
            velha[linha][coluna] = "X"
            quemJoga = 2
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida.")
            os.system('pause')
            
# Jogada do computador
def computadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)

        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        
        time.sleep(0.25)  # Espera 0.25 segundos antes de realizar a jogada do computador
        velha[linha][coluna] = "O"
        jogadas += 1
        quemJoga = 1

# Verificação de vitoria
def verificaVitoria():
    global velha
    vitoria = False
    simbolos = ["X", "O"]

    # Start of Selection
    for s in simbolos:
        vitoria = False
        ganhador = None

        # Verificação de vitoria na HORIZONTAL
        indiceLin = indiceCol = 0
        while indiceLin < 3:
            soma = 0
            indiceCol = 0
            while indiceCol < 3:
                if velha[indiceLin][indiceCol] == s:
                    soma += 1
                indiceCol += 1

            if soma == 3:
                vitoria = True
                ganhador = s
                break

            indiceLin += 1  
        if(vitoria == True):
            break

        # Verificação de vitoria na VERTICAL
        indiceLin = indiceCol = 0
        while indiceCol < 3:
            soma = 0
            indiceLin = 0
            while indiceLin < 3:
                if velha[indiceLin][indiceCol] == s:
                    soma += 1
                indiceLin += 1

            if soma == 3:
                vitoria = True
                ganhador = s
                break

            indiceCol += 1
        if(vitoria == True):
            break

        # Verificação de vitoria na DIAGONAL 1
        soma = 0
        indiceDiag = 0
        while indiceDiag < 3:
            if velha[indiceDiag][indiceDiag] == s:
                soma += 1
            indiceDiag += 1
        
        if soma == 3:
            vitoria = True
            ganhador = s
            break

        # Verificação de vitoria na DIAGONAL 2
        soma = 0
        indiceDiagLin = 0
        indiceDiagCol = 2
        while indiceDiagCol >= 0:
            if velha[indiceDiagLin][indiceDiagCol] == s:
                soma += 1
            indiceDiagLin += 1
            indiceDiagCol -= 1
        
        if soma == 3:
            vitoria = True
            ganhador = s
            break

    return vitoria, ganhador

# Redefinir o jogo
def reiniciarJogo():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria

    jogadas = 0
    quemJoga = 1
    maxJogadas = 9
    vitoria = False
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]



# Onde o jogo inicia, loop principal do jogo
while True:
    tela()
    jogadorJoga()
    computadorJoga()

    tela()
    vitoria, ganhador = verificaVitoria()
    if vitoria:
        print(f"Fim de jogo. '{ganhador}' venceu.")
        break
    elif jogadas >= maxJogadas:
        print("Fim de jogo. Empate.")
        break