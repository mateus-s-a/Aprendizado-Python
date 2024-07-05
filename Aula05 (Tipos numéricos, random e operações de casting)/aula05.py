# TIPOS NUMÉRICOS
num_inteiro = 10
num_float = 5.2
num_complexo = 1j

x = num_float



# CASTING: str(), int(), float()...
# print("Valor: " + x + " - Tipo: " + type(x)) --- TypeError: can only concatenate str (not "int") to str
# print("Valor: " + str(x) + " - Tipo: " + type(x)) --- TypeError: can only concatenate str (not "type") to str
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = int(num_float)
print("Valor: " + str(x) + " - Tipo: " + str(type(x))) # --- Valor: 5 - Tipo: <class 'int'>

x = float(num_inteiro)
print("Valor: " + str(x) + " - Tipo: " + str(type(x))) # --- Valor: 10.0 - Tipo: <class 'float'>



# RANDOM
import random

num_random = random.randrange(1, 60)
x = num_random
print("Valor: " + str(x) + " - Tipo: " + str(type(x))) # --- 'random' irá gerar um número aleatório

num_random = [
    random.randrange(1, 60),
    random.randrange(1, 60),
    random.randrange(1, 60),
    random.randrange(1, 60),
    random.randrange(1, 60),
    random.randrange(1, 60)
]
# OU
for i in range(6):
    num_random2 = random.randrange(1, 60)
    print("Valor " + str(i+1) + ": " + str(num_random2))