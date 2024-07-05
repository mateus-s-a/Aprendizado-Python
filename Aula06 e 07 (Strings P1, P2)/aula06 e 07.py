"""AULA 06"""
curso = "Curso de Python" # Uma 'string', nada mais é, do que uma Lista(Array)

print(curso) # --- Imprime 'curso' por inteiro
print(curso[9]) # --- Imprime o 10° caractere de 'curso', sendo 'P'
print(curso[0:5]) # --- Imprime entre um intervalo, 1° até o 6° caractere, sendo 'Curso'


# capitalize() —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = "curso de python"
print("Capitalize: " + curso.capitalize()) # --- 'capitalize()' retorna a primeira letra da primeira palavra em maiscula

# len() —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print("Tamanho: " + str(len(curso))) # --- 'len()' retorna o tamanho da lista 'curso', sendo 15 caracteres

# lower() ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = "CURSO DE PYTHON"
print(curso)
print(curso.lower()) # --- 'lower()' retorna todos os caracteres em minúsculos da lista 'curso'

# replace() —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = "Curso de Python"
print(curso.replace("Python", "C#")) # --- 'replace()' retorna a string com uma substituição definida

# split() ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
a = curso.split(" ") # --- 'split()' retorna uma lista(array) com a definida regra, no caso, quando encontrar um caractere 'space'
print(a[0]) # --- ['Curso', 'de', 'Python'] => [0] => 'Curso'

# strip() ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = " Curso de Python "
print(curso)
print("Tamanho: " + str(len(curso))) # --- 17 caracteres
print(curso.strip()) # --- 'strip()' retorna com os 'espaços' desnecessários na string da lista 'curso'

# title() —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = "curso de python"
print("Titulo: " + curso.title()) # --- 'title()' retorna a primeira letra de cada palavra em maiscula

# upper() ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
curso = "curso de python"
print(curso)
print(curso.upper()) # --- 'upper()' retorna todos os caracteres em maiúsculos da lista 'curso'



"""AULA 07"""
# in & not in ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
resposta = "Python" in curso # --- 'in', retorna True ou False se a lista 'curso' tiver 'Python' escrito
print(resposta) # --- True
resposta = "Python" not in curso # --- 'not in', o oposto de 'in'
print(resposta) # --- False
resposta = "python" in curso # --- 'in' retornará False, mesmo os caracteres tiverem diferença de maiúsculas e minúsculas
print(resposta) # --- False

texto = "Estudando Python"
palavra = "python"
resposta = palavra in texto
print(resposta) # --- False
resposta = palavra.upper() in texto.upper() # --- transformando ambas em maiúsculas será possível ter um retorno verdadeiro(True)
print(resposta) # --- True
print(str(palavra.upper() not in texto.upper())) # --- False


# + (concatenação), {} place holder & \n caracteres de escape ———————————————————————————————————————————————————————————————————————
nome = "Matthew"
resposta = curso + ", " + nome
print(resposta) # --- 'Curso de Python, Matthew'

dia = 10
mes = "Junho"
ano = 2024
data = "{} de {} de {}" # --- {} => onde serão as variáveis
print(data.format(dia, mes, ano)) # --- 'format()' é o place holder em Python, sem necessidade de concatenação

pais = "Brasil"
data = "{} de {} de {}\n{}" # --- '\n' quebra de linha
print(data.format(dia, mes, ano, pais))
data = "{} de {} de {}\n \"{}\"" # --- '\""\' aspas duplas
print(data.format(dia, mes, ano, pais))


# entre outros... --- \''\   \""\   \n   \r   \t   \b
# \''\ --- aspas simples
# \""\ --- aspas duplas
#  \n  --- quebra de linha(enter)
#  \r  --- retorno de carro(carriage return), move o cursor para o início da linha
#  \t  --- tabulação horizontal(horizontal tab), adiciona uma tab
#  \b  --- backspace, remove o caractere anterior
#  \v  --- tabulação vertical(vertical tab)
#  \f  --- formfeed, move o cursor para o início da próxima página
#  \a  --- alerta, emite um alerta sonoro
#  \0  --- caractere nulo(null)
#  \x  --- caractere hexadecimal
#  \u  --- caractere unicode (16 bits)
#  \U  --- caractere unicode (32 bits)
#  \o  --- caractere octal
#  \N  --- caractere nulo(null)