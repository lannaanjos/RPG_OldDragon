from metodos_auxiliares import corrente
'''                                     CLASSE BASE PERSONAGEM'''

class Personagem:
    def __init__(self, nome):
        #   Infos Básicas
        self.nome = nome
        self.hp = 0
        self.nivel = 1
        self.xp = 0
        #   Raça e Classe
        self.raca = ""
        self.classe = ""
        #   Caracteristicas
        self.movimento = 0
        self.infravisao = 0
        self.alinhamento = ""
        self.car_raca = ""  
        #   Atributos
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        #   Habilidades
        self.habilidades = ""
        
        
    def mostrar_info(self):
        print("=-=-=-=- Ficha do Personagem -=-=-=-=")
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        corrente()
        
        
        if 3 <= self.forca <= 8:
            print(f"Força: {self.forca} - Fraco")
        elif 9 <= self.forca <= 12:
            print(f"Força: {self.forca} - Mediano")
        elif 13 <= self.forca <= 16:
            print(f"Força: {self.forca} - Forte")
        else:
            print(f"Força: {self.forca} - Muito Forte")       
            
        if 3 <= self.destreza <= 8:
            print(f"Destreza: {self.destreza} - Letárgico")
        elif 9 <= self.destreza <= 12:
            print(f"Destreza: {self.destreza} - Mediano")
        elif 13 <= self.destreza <= 16:
            print(f"Destreza: {self.destreza} - Ágil")
        else:
            print(f"Destreza: {self.destreza} - Preciso")
            
        if 3 <= self.constituicao <= 8:
            print(f"Constituição: {self.constituicao} - Frágil")
        elif 9 <= self.constituicao <= 12:
            print(f"Constituição: {self.constituicao} - Mediano")
        elif 13 <= self.constituicao <= 16:
            print(f"Constituição: {self.constituicao} - Resistente")
        else:
            print(f"Constituição: {self.constituicao} - Vigoroso")
            
        if 3 <= self.inteligencia <= 8:
            print(f"Inteligência: {self.inteligencia} - Inépto")
        elif 9 <= self.inteligencia <= 12:
            print(f"Inteligência: {self.inteligencia} - Mediano")
        elif 13 <= self.inteligencia <= 16:
            print(f"Inteligência: {self.inteligencia} - Inteligente")
        else:
            print(f"Inteligência: {self.inteligencia} - Gênio")
            
        if 3 <= self.sabedoria <= 8:
            print(f"Sabedoria: {self.sabedoria} - Tolo")
        elif 9 <= self.sabedoria <= 12:
            print(f"Sabedoria: {self.sabedoria} - Mediano")
        elif 13 <= self.sabedoria <= 16:
            print(f"Sabedoria: {self.sabedoria} - InIntuitivo")
        else:
            print(f"Sabedoria: {self.sabedoria} - Presciente")
          
        if 3 <= self.carisma <= 8:
            print(f"Carisma: {self.carisma} - Descortês")
        elif 9 <= self.carisma <= 12:
            print(f"Carisma: {self.carisma} - Mediano")
        elif 13 <= self.carisma <= 16:
            print(f"Carisma: {self.carisma} - Influente")
        else:
            print(f"Carisma: {self.carisma} - Ídolo")