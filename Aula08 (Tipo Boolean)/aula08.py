"""AULA 08 --- Tipo Boolean"""
 
boolean1 = True
boolean2 = False
boolean3 = 10 < 15
boolean4 = 10 > 15

print(boolean1) # --- True
print(boolean2) # --- False
print(boolean3) # --- True
print(boolean4) # --- False

boolean5 = "Python"
print(bool(boolean5)) # --- True
boolean6 = ""
print(bool(boolean6)) # --- False

print("Possui texto.") if boolean5 else print("Texto vazio.") # --- Possui texto.
print("Possui texto.") if boolean6 else print("Texto vazio.") # --- Texto vazio.

boolean7 = 1
print(bool(boolean7)) # --- True
boolean8 = 0
print(bool(boolean8)) # --- False