"""AULA 17 --- Dictionary. Uma coleção de chaves e valores."""

carro = {
    "Fabricante": "Honda", # --- chave: valor
    "Modelo": "HRV",
    "Ano": 2016,
    "Cor": "Vermelha"
}

# Impressão
print(carro) # --- {'Fabricante': 'Honda', 'Modelo': 'HRV', 'Ano': 2016, 'Cor': 'Vermelha'}
print(carro["Fabricante"]) # --- 'Honda'
print(carro.get("Modelo")) # --- 'HRV'; 'get()' pega o valor da chave (key)

# Atribuição / Variação / Modificação
carro["Ano"] = 2020
carro["Cor"] = "Prata"
print(carro) # --- {'Fabricante': 'Honda', 'Modelo': 'HRV', 'Ano': 2020, 'Cor': 'Prata'}


for i in carro:
    print(i) # --- Loop percorrendo as chaves
    print(carro[i]) # --- Loop percorrendo os valores

for chave, valor in carro.items():
    print(chave + " - " + str(valor))


if "Modelo" in carro: # --- 'in' verifica se existe uma chave
    print("'Modelo' está no dicionário.")

print("Tamanho do dicionário: " + str(len(carro)) + " itens.") # --- len() retorna o tamanho do dicionário

carro["Câmbio"] = "Automático" # --- adicionando uma chave e valor
print(carro)

carro.pop("Câmbio") # --- pop() remove uma chave e o valor
print(carro)
del carro["Cor"] # --- del remove uma chave e o valor
print(carro)
carro.clear() # --- clear() limpa o dicionário
print(carro)



# Dicionário dentro de dicionário, como uma sintaxe JSON
motos = {
    "Moto1": {
        "Fabricante": "Honda",
        "Modelo": "CB"
    },
    "Moto2": {
        "Fabricante": "Yamaha",
        "Modelo": "YBR"
    },
    "Moto3": {
        "Fabricante": "Suzuki",
        "Modelo": "GSX"
    }
}

# Impressão
print(motos) # --- {'Moto1': {'Fabricante': 'Honda', 'Modelo': 'CB'}, 'Moto2': {'Fabricante': 'Yamaha', 'Modelo': 'YBR'}, 'Moto3': {'Fabricante': 'Suzuki', 'Modelo': 'GSX'}}
print(motos["Moto1"]["Fabricante"]) # --- 'Honda'



# Criação de três dicionários para um dicionário
Caminhao1 = {
    "Fabricante": "Volvo",
    "Modelo": "FH",
    "Ano": 2020
}
Caminhao2 = {
    "Fabricante": "BMW",
    "Modelo": "FH",
    "Ano": 2015
}
Caminhao3 = {
    "Fabricante": "Mercedes",
    "Modelo": "FH",
    "Ano": 2019
}

Caminhoes = {
    "Caminhão1": Caminhao1,
    "Caminhão2": Caminhao2,
    "Caminhão3": Caminhao3
}
print(Caminhoes)
print(Caminhoes["Caminhão1"]) # --- {'Fabricante': 'Volvo', 'Modelo': 'FH', 'Ano': 2020}
print(Caminhoes["Caminhão1"]["Modelo"]) # --- 'FH'