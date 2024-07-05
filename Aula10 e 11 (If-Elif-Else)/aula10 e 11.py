"""AULA 10 --- If-Else"""

a = True
if a:
    print("A é True") # --- True
else:
    print("A é False") # --- False

b = False
if b:
    print("B é True") # --- True
else:
    print("B é False") # --- False

a = 10
b = 5
if a > b:
    print("A é maior que B") # --- True
else:
    print("B é maior que A") # --- False

res = 0
operacao = "/"
if operacao == "+":
    res = a + b
    print(a, operacao, b, "=", res) # --- 10 + 5 = 15
if operacao == "-":
    res = a - b
    print(a, operacao, b, "=", res) # --- 10 - 5 = 5
if operacao == "*":
    res = a * b
    print(a, operacao, b, "=", res) # --- 10 * 5 = 50
if operacao == "/":
    res = a / b
    print(a, operacao, b, "=", res) # --- 10 / 5 = 2.0




"""AULA 11 --- If-Elif-Else, o uso de Elif na estrutura acima optimiza o código, pois não é necessário usar vários Ifs e Else, como no exemplo abaixo"""
c = 20
d = 4
if c > d:
    print("C é maior que D") # --- True
else:
    print("D é maior que C") # --- False

res = 0
operacao = "a"
if operacao == "+":
    res = c + d
    print(c, operacao, d, "=", res) # --- 20 + 4 = 24
elif operacao == "-":
    res = c - d
    print(c, operacao, d, "=", res) # --- 20 - 4 = 16
elif operacao == "*":
    res = c * d
    print(c, operacao, d, "=", res) # --- 20 * 4 = 80
elif operacao == "/":
    res = c / d
    print(c, operacao, d, "=", res) # --- 20 / 4 = 5.0
else:
    print("Operador inválido.")


clima = "Sol"
dinheiro = 650
lugar = ""
if clima == "Sol" and (dinheiro >= 300 or dinheiro <= 500): lugar = "Praia"
else: lugar = "Cinema"
print("Iremos para", lugar)

# AND
# V e V = VERDADEIRO
# F e V = FALSO
# V e F = FALSO
# F e F = FALSO

# OR
# V e V = VERDADEIRO
# F e V = VERDADEIRO
# V e F = VERDADEIRO
# F e F = FALSO



print("[Fim do programa.]")