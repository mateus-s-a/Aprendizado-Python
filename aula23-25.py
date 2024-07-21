"""AULA 23 --- POO(Programação Orientada a Objetos) (Parte 1)"""
# O que é uma classe?
# classe = template para objetos

# Classe
class Carro_23:
    # Atributos
    velMax_23 = 0
    ligado_23 = None
    cor_23 = ""

# Objetos / Instâncias
c1 = Carro_23()
c2 = Carro_23()
c3 = Carro_23()

c1.velMax_23 = 200
c1.cor_23 = "Vermelha"
c1.ligado_23 = False
print("Velocidade Máxima: {}" .format(c1.velMax_23)) # --- 200
print("Cor: {}" .format(c1.cor_23)) # --- Vermelha
print("Ligado: {}".format("Sim" if c1.ligado_23 else "Não")) # --- Desligado


print("\n")


"""AULA 24 --- POO(Programação Orientada a Objetos) (Parte 2)"""
# Classe
class Carro_24:
    # Atributos
    velMax_24 = 0
    ligado_24 = None
    cor_24 = ""

    # Construtor (__init___ = construtor)
    def __init__(self, v, l, c): # --- 'self' se aproxima de 'this', em que ele se refere ao objeto
        self.velMax_24 = v
        self.ligado_24 = l
        self.cor_24 = c

    # Métodos
    def mostrar_24(self):
        print("Velocidade Máxima...: {}".format(self.velMax_24)) # --- 200
        print("Cor.................: {}".format(self.cor_24)) # --- Vermelha
        print("Ligado..............: {}".format("Sim" if self.ligado_24 else "Não")) # --- Não
        print("---------------------------------------")

    def ligar_24(self):
        self.ligado_24 = True

    def desligar_24(self):
        self.ligado_24 = False

    def andar_24(self):
        if(self.ligado_24):
            print("Andando...")
        else:
            print("Carro desligado...")

# Objetos / Instâncias (mas agora com os atributos passados pelo construtor)
c1 = Carro_24(200, False, "Vermelha")
c2 = Carro_24(120, False, "Prata")
c3 = Carro_24(350, False, "Preto")

c1.ligar_24()
c1.mostrar_24()

c2.ligar_24()
c2.desligar_24()
c2.mostrar_24()

c3.ligar_24()
c3.andar_24()
c3.mostrar_24()


print("\n")


"""AULA 25 --- POO(Programação Orientada a Objetos) (Parte 3)"""
# O que é uma Herança em POO?
# Herança = uma classe herda os atributos e métodos de outra classe

# Classe Pai / Base / Super-classe
class NPC:
    # Construtor (__init___ = construtor)
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    # Métodos
    def info(self):
        print("Nome......: {}".format(self.nome))
        print("Time......: {}".format(self.time))
        print("Força.....: {}".format(self.forca))
        print("Munição...: {}".format(self.municao))
        print("Vivo......: {}".format("Sim" if self.vivo else "Não"))
        print("Energia...: {}".format(self.energia))
        print("---------------------------------------")

# --- Conceito de Herança
# Classe Filha / Sub-classe
class Soldado(NPC):
    # Construtor Filha
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao) # --- 'super()' chamar o construtor/método da super-classe

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
        
    def inf(self):
        super().info()

s1 = Guarda("Olho-Vivo", 1)
s2 = Soldado("Bala na Agulha", 1)
s3 = Elite("Ninja", 1)

s4 = Guarda("Super Atento", 2)
s5 = Soldado("Cacete", 2)
s6 = Elite("TiroCerto", 2)


s1.vivo = False
s1.energia = 0
s6.vivo = False
s6.energia = 0
s1.info()
s2.info()
s3.inf()
s4.info()
s5.info()
s6.inf()