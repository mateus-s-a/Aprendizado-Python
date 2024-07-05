"""AULA 12 --- Loop For"""

import os
os.system('cls')

carros = ["Fusca", "Gol", "Uno", "Vectra", "Peugeot"]

for i in carros: # --- sintaxe de for
    print(i)

for i in carros:
    print(i)
    if i == "Uno":
        print("Achou Uno")
        break # --- para o loop
    print("Não achou Uno")
print("Fim do loop For.")




"""AULA 14 --- Loop While"""
i = 0
while i < len(carros): # --- sintaxe de while
    print(carros[i])
    # i++ (sintaxe invalida em python)
    i += 1
    if(i == 4):
        print("Achou o Vectra")
        break
print("Fim do loop While.")

carros = []
carro = input("Digite o nome do carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do carro: ")
print("Fim do loop While.")
print(carros)




print("Fim do programa.")