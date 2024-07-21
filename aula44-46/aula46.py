"""AULA 46 --- Operações de Arquivos (Parte 3)"""
# Deletar um arquivo
# os.remove('arquivo.txt')

import os

nome = "teste_46"

# criar_arquivo = lambda nome: open(f'aula44-46/{nome}.txt', 'x') # --- 'x' = create
# file = criar_arquivo(nome) # --- cria o arquivo
# print("Arquivo criado com sucesso.")

# file.close()


if os.path.exists(f"aula44-46/{nome}.txt"):
    os.remove(f"aula44-46/{nome}.txt")
    print("Arquivo excluído com sucesso.")
else:
    print("Arquivo inexistente ou já excluído.")