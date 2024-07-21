"""AULA 19 --- Funções (Parte 1)"""

n1 = 15
n2 = 7
def somar_19():
    res = n1 + n2
    print("Soma de {} + {} = {}".format(n1, n2, res))

def subtrair_19():
    res = n1 - n2
    print("Subtração de {} - {} = {}".format(n1, n2, res))

def multiplicar_19():
    res = n1 * n2
    print("Multiplicação de {} * {} = {}".format(n1, n2, res))

# somar()
# subtrair()

def calculos_19(): # --- chamando as três funções
    somar_19()
    subtrair_19()
    multiplicar_19()

calculos_19()




print("\n\n")




"""AULA 20 --- Funções (Parte 2)"""
def somar_20(n1, n2, n3, n4): # --- parâmetros de entrada
    res = n1 + n2 + n3 + n4
    print("Soma de {} + {} + {} + {} = {}".format(n1, n2, n3, n4, res))

somar_20(5, 7, 3, 2)
somar_20(12, 8, 1, 20)
somar_20(1, 2, 0, 0)

def textos(*t): # --- argumentos arbitrários, para receber quantos forem os parâmetros de entrada
    print(t[0])
    print(t[1])
    print(t[2])

    for i in t: # --- percorrer os parâmetros e imprimi-los
        print(i)

textos("Python", "Java", "C++")

def somar2_20(*num): # --- argumentos arbitrários
    res = 0
    for n in num:
        res += n

    print("Soma =", str(res))

somar2_20(5, 2, 3, 10, 6, 8, 9)

def carros_20(c = "Golf"): # --- valor padrão do argumento no parâmetro, se nenhum valor for passado
    print("Modelo:", c)

carros_20() # --- 'Golf'
carros_20("Fusca") # --- 'Fusca'

valores = [1, 5, 3, 2]
def somar3_20(num):
    r = 0
    for n in num:
        r += n
    print("Soma =", str(r))

somar3_20(valores)




print("\n\n")




"""AULA 21 --- Funções (Parte 3)"""
# return = para retornar um valor
# return 0 = geralmente, é usado para indicar sucesso ou um estado falso (False).
# return 1 = pode ser usado para indicar uma condição verdadeira (True) ou um estado de erro/sucesso, dependendo da convenção adotada.
valores_21 = [1, 5, 3, 2, 10, 4, 8]
def somar_21(num):
    res = 0
    for n in num:
        res += n
    return res

print("Soma =", somar_21(valores_21))




print("\n\n")




"""AULA 22 --- Funções (Parte 4)"""
# funções lambdas (anonimas)

soma_22 = lambda a, b: a + b # --- função lambda, somando 2 números e retornando o resultado
print(soma_22(2, 5))

mul_22 = lambda a, b, c: (a + b) * c
print(mul_22(2, 5, 3))

print((lambda a, b: a - b)(10, 5)) # --- sintaxe sem atribuir a uma variável


# Este trecho de código define uma função 'lambda' 'r' que recebe dois argumentos, 'x' e 'func',
# e retorna a soma de 'x' com o resultado de chamar 'func(x)'.
# Em seguida, a função 'r' é chamada com '2' e outra função lambda que multiplica 'x' por ele mesmo.
# O resultado final é impresso. Neste caso, 'res' será igual a '2 + (2 * 2)', ou seja, '6'.
r = lambda x, func: x + func(x)
res = r(2, lambda x: x * x)
print(res)

# etc...
res = r(2, lambda x: x + x)
print(res)

res = r(2, lambda x: x + 3)
print(res)