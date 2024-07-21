"""AULA 27-28 (Aula Prática) --- Prática das aulas passadas."""

import os

class Carro:
    carros = []

    def __init__(self, modelo, ligado, ano):
        self.modelo = modelo
        self.ligado = ligado
        self.ano = ano

    def novo_carro():
        os.system('cls')
        print("Novo Carro:\n------------------")

        modelo = input("Modelo: ")
        ano = input("Ano: ")
        novo_carro = Carro(modelo, False, ano)
        Carro.carros.append(novo_carro)
        print(f"Carro {modelo} adicionado com sucesso!")

        input("Pressione qualquer tecla para continuar...")

    def info_carro():
        os.system('cls')
        print("Info. do Carro:\n------------------")

        modelo = input("Modelo: ")
        for i in Carro.carros:
            if i.modelo == modelo:
                estado = "ligado" if i.ligado else "desligado"
                print(f"Modelo: {i.modelo}\nAno: {i.ano}, Estado: {estado}\n")
                input("Pressione qualquer tecla para continuar...")
                return
        print("Carro não encontrado.")

        input("Pressione qualquer tecla para continuar...")

    def excluir_carro():
        os.system('cls')
        print("Excluir Carro:\n------------------")

        modelo = input("Modelo: ")
        for i in Carro.carros:
            if i.modelo == modelo:
                Carro.carros.remove(i)
                print(f"Carro {modelo} excluído com sucesso.")
                return
        print("Carro não encontrado.")

        input("Pressione qualquer tecla para continuar...")

    def ligar_carro():
        os.system('cls')
        print("Ligar Carro:\n------------------")

        modelo = input("Modelo: ")
        for i in Carro.carros:
            if i.modelo == modelo:
                i.ligado = True
                print(f"Carro {modelo} ligado.")
                return
        print("Carro não encontrado.")

        input("Pressione qualquer tecla para continuar...")

    def desligar_carro():
        os.system('cls')
        print("Desligar Carro:\n------------------")

        modelo = input("Modelo: ")
        for i in Carro.carros:
            if i.modelo == modelo:
                i.ligado = False
                print(f"Carro {modelo} desligado.")
                return
        print("Carro não encontrado.")

        input("Pressione qualquer tecla para continuar...")

    def listar_carros():
        os.system('cls')
        print("Lista de Carros:\n------------------")

        if not Carro.carros:
            print("Nenhum carro encontrado.")
            input("Pressione qualquer tecla para continuar...")
            return
        for i in Carro.carros:
            estado = "ligado" if i.ligado else "desligado"
            print(f"Modelo: {i.modelo}\nAno: {i.ano}\nEstado: {estado}\n")

        input("Pressione qualquer tecla para continuar...")

def executar_caso(caso):
    return {
        '1': Carro.novo_carro,
        '2': Carro.info_carro,
        '3': Carro.excluir_carro,
        '4': Carro.ligar_carro,
        '5': Carro.desligar_carro,
        '6': Carro.listar_carros,
        '0': exit
    }.get(caso, lambda: input("Opção inválida.\nPressione qualquer tecla para continuar..."))()

def menu():
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("0 - Sair")
    print("---------------------------------------------------")
    print(f"Quantidade de Carros: {len(Carro.carros)}\n")


while True:
    os.system('cls')
    menu()
    caso = input("Digite uma opção: ")
    executar_caso(caso)