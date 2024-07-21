"""AULA 16 --- Matrizes. Uma coleção de arrays."""

carros = [ #--- Array / List
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2016]
]

print(carros[0]) # --- ['Modelo', 'HRV']
print(carros[0][1]) # --- 'HRV'

print(carros[1]) # --- ['Fabricante', 'Honda']
print(carros[1][1]) # --- 'Honda'

print(carros[2]) # --- ['Ano', '2016']
print(carros[2][1]) # --- '2016'


# --- adicionando uma linha, coluna, valor
carros.append(["Cor", "Vermelha"])

# --- alterando um valor
carros[2][1] = 2020
print(carros[2][1]) # --- '2020'

# --- percorrendo uma lista e imprimindo os valores
for i, j in carros:
    print("Linha: {} | Coluna: {}".format(str(i), str(j)))