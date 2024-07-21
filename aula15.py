"""AULA 15 --- Diferença entre Listas e Tuplas

Listas = Mutáveis
Tuplas = Imutáveis
"""

lista_carros = ["Chevrolet", "Fiat", "Ford"] # --- Listas
tupla_carros = ("Ferrari", "Audi", "Opel") # --- Tuplas

for i in lista_carros:
    print(i)

for i in tupla_carros:
    print(i)


# lista_carros[0] = "Fusca" # --- Lista, mutável
# tupla_carros[0] = "Fusca" # --- Tupla, imutável

# lista_carros.append("Volkswagen") # --- Lista, mutável
# tupla_carros.append("Volkswagen") # --- Tupla, imutável


# Gambiarra para mudar um item da tupla
aux = list(tupla_carros) # --- Uma lista recebe a tupla
aux[0] = "Fusca" # --- A lista recebe a tupla
tupla_carros = tuple(aux) # --- A tupla recebe a lista
print(tupla_carros) # --- (Fusca, Audi, Opel)