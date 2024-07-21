"""AULA 29 --- Iteradores"""
# O que é um iterador?
# Iteradores = objetos que permitem iterar sobre um iterações de um objeto.

carros = ["Ford", "Chevrolet", "Volkswagen", "Fiat", "Toyota", "Honda", "BMW"]

iteratorCarros = iter(carros) # --- 'iter' = criar um iterador

# 'next' = avança o iterador
print(next(iteratorCarros))
print(next(iteratorCarros))
print(next(iteratorCarros))
print(next(iteratorCarros))
print(next(iteratorCarros))
print(next(iteratorCarros))
print(next(iteratorCarros))


print("\n")


# While Tradicional
i = 0
while i<7:
    print(carros[i])
    i += 1


print("\n")


# While com Iteradores
iteratorCarros = iter(carros) # reinicia o iterador
while True:
    try:
        print(next(iteratorCarros))
    except StopIteration:
        print("Fim do iterador")
        break