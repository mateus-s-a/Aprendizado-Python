"""AULA 44 --- Operações de Arquivos (Parte 1)"""
# Operações de Arquivos em Python
# Envolvem a leitura, escrita e manipulação de arquivos.
# --- 'write()' = escreve o conteúdo no arquivo

nome = "teste_44"
file = open(f"aula44-46/{nome}.txt", "at") # --- 'file' recebe o nome do arquivo e a extensão em que ele vai ser aberto.

file.write("Estudando programação, 1-linha\n")
file.write("Matemática Discreta, 2-linha\n")

for i in range(3):
    txt = input("Digite algo: ")
    file.write(f"{txt}, {i+3}-linha\n")

file.close() # --- 'close()' = fecha o arquivo

# r = read
# w = write (substituir)
# a = append (adicionar)
# x = create
# t = text
# b = binary
# + = update
# r+ = read and update
# w+ = write and update
# a+ = append and update
# x+ = create and update
# rb = read binary
# wb = write binary
# ab = append binary
# xb = create binary
# rb+ = read binary and update
# wb+ = write binary and update
# ab+ = append binary and update
# xb+ = create binary and update
# etc...