# VARIÁVEIS GLOBAIS
a = b = c = 0
code = "Python"

def funcao(): # FUNÇÃO, sem parâmetros de entrada
    print(code)

funcao()


# def funcao2():
#     code2 = "MySQL" # VARIÁVEL NÃO GLOBAL, definida somente para a função 'cn2()'
#     print(code2)

# print(code2) # Erro


def funcao3():
    global code3 # 'global' define uma variável dentro de uma função como o GLOBAL
    code3 = "Java"
    print(code3)

print(code3) # Sem nenhum erro