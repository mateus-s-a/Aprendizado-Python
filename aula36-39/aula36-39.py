"""AULA 36 --- JSON (JavaScript Object Notation) - (Parte 1)"""

import json

carros_json = '{"marca":"honda","modelo":"HRV","cor":"prata"}'
carros_dictionary = json.loads(carros_json) # --- 'loads()' converte para um dicionário
print(carros_dictionary)
print(carros_dictionary["marca"], carros_dictionary["modelo"], carros_dictionary["cor"])

# Impressão chave: valor
for i in carros_dictionary:
    print(i, carros_dictionary[i])

# Impressão alternativa chave: valor
for i, j in carros_dictionary.items():
    print(i, j)

# Impressão das chaves
for i in carros_dictionary:
    print(i)

# Impressão dos valores
for i in carros_dictionary.values():
    print(i)



# Transformar um dictionário em JSON
carros_json = json.dumps(carros_dictionary) # --- 'dumps()' converte para JSON
print(carros_json)



print("\n\n")



"""AULA 37 --- JSON (JavaScript Object Notation) - (Parte 2)"""

carros_dictionary = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
# dictionary => objeto JSON

carros_array = ["Fusca", "Gol", "Uno", "Vectra", "Peugeot"]
# array => array JSON

carros_tupla = ("Fusca", "Gol", "Uno", "Vectra", "Peugeot")
# tupla => array JSON


# --- 'indent=4' indenta o JSON com 4 espaçamentos, padrão
# --- 'separators=(":", "=")' separa as chaves e os valores com ":" e "="
# --- 'sort_keys=True' ordena as chaves
carros_json = json.dumps(carros_dictionary, indent=4, separators=(":", "="), sort_keys=True)
print(carros_json)

carros_json = json.dumps(carros_array, indent=4)
print(carros_json)
carros_json = json.dumps(carros_tupla, indent=4)
print(carros_json)


# Aprender usar arquivos JSON separadamente, mas aqui se usa tradicionalmente com uma estrutura em uma linha JSON
jogador_json = '{"nome": "Matthew","time": "math","vivo": true,"energia": 100,"mochila": ["perderneira", "corda", "linha", "arame"],"aeronaves": [{ "tipo": "transporte", "habilidades": 80 },{ "tipo": "ataque", "habilidades": 100 },{ "tipo": "reconhecimento", "habilidades": 50 }]}'
jogador_dictionary = json.loads(jogador_json)
print(type(jogador_dictionary)) # --- <class 'dict'>

for i in jogador_dictionary:
    print(i, jogador_dictionary[i])
print("\n")

print("Chaves:")
for i in jogador_dictionary:
    print(i)
print("\n")

print("Valores:")
for i in jogador_dictionary.values():
    print(i)



print("\n\n")



"""AULA 38 --- JSON (JavaScript Object Notation) - (Parte 3)"""

print(jogador_dictionary["nome"]) # --- Impressão nome do jogador = Matthew
print(jogador_dictionary["time"]) # --- Impressão time do jogador = math

for i in jogador_dictionary["mochila"]: # --- Impressão da mochila do jogador = perderneira, corda, linha, arame
    print(i)

for i in jogador_dictionary["aeronaves"]: # --- Impressão das aeronaves do jogador = transporte, ataque, reconhecimento
    print(f"{i['tipo']} - {i['habilidades']}") # --- Impressão das habilidades das aeronaves = 80, 100, 50



print("\n\n")



"""AULA 39 --- JSON (JavaScript Object Notation) - (Parte 4)"""
# Importar arquivo JSON em um dicionário

# --- 'with' = abre e fecha o arquivo
# --- 'open()' = abre o arquivo
# declaração 'with' para 'open()' para abrir o arquivo 'jogador.json' em modo de leitura;
# O arquivo é aberto e associado à variável 'f';
# ......................................................................
# A variável 'f' é usada para 'load()' que converte o arquivo JSON em um dicionário
with open('jogador.json') as f:
    jogador_dictionary = json.load(f)

for i in jogador_dictionary:
    print(i, jogador_dictionary[i])

print(jogador_dictionary["nome"])
print(jogador_dictionary["time"])

for i in jogador_dictionary["mochila"]:
    print(i)

for i in jogador_dictionary["aeronaves"]:
    print(f"{i['tipo']} - {i['habilidades']}")