'''                                     CLASSE BASE PERSONAGEM'''

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        #   Atributos / Classe
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.classe = ""
        
    def mostrar_info(self):
        print("---- Ficha do Personagem ----")
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print("--------- Atributos ---------")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")