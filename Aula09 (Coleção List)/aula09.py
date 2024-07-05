"""AULA 09 --- Coleção List"""

carros = ["Ford", "Chevrolet", "Volkswagen"]
print(carros) # --- ['Ford', 'Chevrolet', 'Volkswagen']
print(carros[0]) # --- Ford
print(carros[-1]) # --- Volkswagen

carros[2] = "Fiat"
print(carros[2]) # --- Fiat

carros.append("Toyota")
carros.append("Honda")
carros.append("BMW")
print(carros) # --- ['Ford', 'Chevrolet', 'Fiat', 'Toyota', 'Honda', 'BMW']

print(len(carros)) # --- 6

carros.remove("Ford")
print(carros) # --- ['Chevrolet', 'Fiat', 'Toyota', 'Honda', 'BMW']
print(len(carros)) # --- 5

try: carros.remove("Ford")
except ValueError: print("O elemento já foi removido.")

carros.pop()
print(carros) # --- ['Chevrolet', 'Fiat', 'Toyota', 'Honda']
print(len(carros)) # --- 4

"""Elimina por posição"""
carros.pop(2)
print(carros) # --- ['Chevrolet', 'Fiat', 'Honda']
print(len(carros)) # --- 3

del carros[2]
print(carros) # --- ['Chevrolet', 'Fiat']
print(len(carros)) # --- 2

carros.clear()
print(carros) # --- []
print(len(carros)) # --- 0

carros = ["Ford", "Chevrolet", "Volkswagen"]
carros.extend(["Toyota", "Honda", "BMW"])
carros2 = list(carros)
print(carros2) # --- ['Ford', 'Chevrolet', 'Volkswagen', 'Toyota', 'Honda', 'BMW']
print(len(carros2)) # --- 6

carros3 = carros + carros2
print(carros3) # --- ['Ford', 'Chevrolet', 'Volkswagen', 'Toyota', 'Honda', 'BMW']
print(len(carros3)) # --- 6