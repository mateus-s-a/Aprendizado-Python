"""AULA 34 --- Importando arquivos (MÓDULOS)""" 

# Importando o arquivo 'aula34.py'
import curso as c # --- o 'as' define um 'apelido' para o arquivo

c.func_curso() # --- chamando a funcionalidade 'func_curso()' no arquivo 'curso.py'
print(c.jogador["nome"]) # --- chamando a variável 'jogador' no arquivo 'curso.py'



# Importando apenas uma variável da biblioteca em 'curso.py'. Útil para bibliotecas grandes
from curso import jogador

print(jogador["nome"])



# Importando e vendo todas as variáveis da biblioteca
import curso

res = dir(curso) # --- 'dir()' = verifica todas as variáveis da biblioteca
print(res)