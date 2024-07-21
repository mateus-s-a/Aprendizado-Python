"""AULA 26 --- Try Exception """
# Tratamento de excecções (Try, Except, Finally)
# O que é o tratamento de excecções? uma função que é executada caso ocorra um erro na execução do código
# 'try' = tratamento de erros
# 'except' = tratamento de excecções
# 'finally' = executado sempre, independentemente de ocorrer ou não um erro

try:
    print(x)
except:
    print("Variável 'x' não definida")



try:
    print(x)
except NameError: # --- 'NameError' = variável não definida
    print("Variável 'x' não definida")
except:
    print("Erro inesperado")



x = 10
try:
    print(x) # --- imprime '10'
except:
    print("Erro no programa")
else:
    print("Programa executado com sucesso") # --- executa caso não haja erros



try:
    print(y)
except:
    print("Erro no programa") # --- executa caso haja erros
else:
    print("Programa executado com sucesso")
finally:
    print("Fim do tratamento") # --- executa independentemente de ocorrer ou não um erro



num = -10
if num < 1:
    # Dispara um erro (raise = 'lançar'; Exception = 'excessão')
    raise Exception("O valor deve ser positivo")
# Traceback (most recent call last):
#     File "c:\Users\space\Documents\[Code]\Python\aula26.py", line 48, in <module>
#         raise Exception("O valor deve ser positivo")
# Exception: O valor deve ser positivo"""

num = "Matthew"
if not type(num) is int:
    raise Exception("O valor deve ser um número")
else:
    print(num)