from metodos_auxiliares import corrente
from dados import Dados

'''                             GUERREIRO E ESPECIALIZAÇÕES'''

class Guerreiro:
    def __init__(self):
        self.hp_base = 10
        self.habilidades = ["Aparar", "Maestria em Arma", "Ataque Extra"]
        
    @staticmethod
    def sobe_nivel(xp):
        if xp == 2000:
            return Dados().rolar_1d10()
        elif xp == 4000:
            return Dados().rolar_1d10()
        elif xp == 7000:
            return Dados().rolar_1d10()
        elif xp == 10000:
            return Dados().rolar_1d10()
        elif xp == 20000:
            return Dados().rolar_1d10()
        elif xp == 30000:
            return Dados().rolar_1d10()
        elif xp == 40000:
            return Dados().rolar_1d10()
        elif xp == 50000:
            return Dados().rolar_1d10()
        elif xp == 100000:
            return Dados().rolar_1d10()
        else:
            return 0 
            
    def __repr__(self):
        return "Guerreiro"
                
class Barbaro(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Vigor Bárbaro", "Talentos Selvagens", "Supresa Selvagem", "Força do Totem"])
        
    def __repr__(self):
        return "Bárbaro"

class Paladino(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Imunidade a Doenças", "Cura pelas Mãos", "Aura de Proteção", "Espada Sagrada"])
        
    def __repr__(self):
        return "Paladino"                        
                        
'''                             CLÉRIGO E ESPECIALIZAÇÕES'''

class Clerigo():
    def __init__(self):
        self.hp_base = 8
        self.habilidades = ["Magia Divina", "Afastar Mortos Vivos", "Cura Milagrosa"]
    
    @staticmethod       
    def sobe_nivel(xp):
        if xp == 1500:
            return Dados().rolar_1d8()
        elif xp == 3000:
            return Dados().rolar_1d8()
        elif xp == 5500:
            return Dados().rolar_1d8()
        elif xp == 8500:
            return Dados().rolar_1d8()
        elif xp == 17000:
            return Dados().rolar_1d8()
        elif xp == 27000:
            return Dados().rolar_1d8()
        elif xp == 37000:
            return Dados().rolar_1d8()
        elif xp == 47000:
            return Dados().rolar_1d8()
        elif xp == 94000:
            return Dados().rolar_1d8()
        else:
            return 0
            
    def __repr__(self):
        return "Clérigo"
            
class Druida(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Herbalismo", "Previdência", "Transformação"])
            
    def __repr__(self):
        return "Druida"
            
class Academico(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Conhecimento Acadêmico", "Decifrar Linguagens", "Lendas e Tradições"])
            
    def __repr__(self):
        return "Acadêmico"
            
'''                                 MAGO E ESPECIALIZAÇÕES'''  
          
class Mago():
    def __init__(self):
        self.hp_base = 4
        self.habilidades = ["Magias Arcanas", "Ler Magias", "Detectar Magias"]
        self.magias_exclusivas = []
        
    @staticmethod
    def sobe_nivel(xp):
        if xp == 2500:
            return Dados().rolar_1d4()
        elif xp == 5000:
            return Dados().rolar_1d4()
        elif xp == 8500:
            return Dados().rolar_1d4()
        elif xp == 11500:
            return Dados().rolar_1d4()
        elif xp == 23000:
            return Dados().rolar_1d4()
        elif xp == 33000:
            return Dados().rolar_1d4()
        elif xp == 43000:
            return Dados().rolar_1d4()
        elif xp == 53000:
            return Dados().rolar_1d4()
        elif xp == 106000:
            return Dados().rolar_1d4()
        else:
            return 0    
        
    def __repr__(self):
        return "Mago"
            
class Ilusionista(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Miragem", "Ilusão Melhorada", "Ilusão Permanente"])    
        self.habilidades.extend(self.magias_exclusivas)
            
    def __repr__(self):
        return "Ilusionista"
            
class Necromante(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Criar Mortos Vivos", "Drenar Vida", "Magia da Morte"])
        self.habilidades.extend(self.magias_exclusivas)
            
    def __repr__(self):
        return "Necromante"       
    
'''                                 LADRÃO E ESPECIALIZAÇÕES'''     

class Ladrao:
    def __init__(self):
        self.hp_base = 6
        self.habilidades = ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]
            
    def __repr__(self):
        return "Ladrão"
            
class Ranger(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Inimigo Mortal", "Combativo", "Previdência", "Companheiro Animal"])
        
    @staticmethod
    def sobe_nivel(xp):
        if xp == 1000:
            return Dados().rolar_1d6()
        elif xp == 2000:
            return Dados().rolar_1d6()
        elif xp == 4000:
            return Dados().rolar_1d6()
        elif xp == 7000:
            return Dados().rolar_1d6()
        elif xp == 14000:
            return Dados().rolar_1d6()
        elif xp == 24000:
            return Dados().rolar_1d6()
        elif xp == 34000:
            return Dados().rolar_1d6()
        elif xp == 44000:
            return Dados().rolar_1d6()
        elif xp == 88000:
            return Dados().rolar_1d6()
        else:
            return 0    
        
    def __repr__(self):
        return "Ranger"
    
class Bardo(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Influenciar", "Inspirar", "Fascinar", "Usar Pergaminhos"])
        
    def __repr__(self):
        return "Bardo"           
                     
'''                             MÉTODO DE ESCOLHA DE CLASSES'''

def escolher_classe():    
    corrente()
    print("          Escolha de Classe       ")
    corrente()
    print("[1] Guerreiro")
    print("[2] Clérigo")
    print("[3] Mago")
    print("[4] Ladrão")
    
    while True:
        try:
            escolha_classe = int(input("Selecione a opção desejada: "))
            
            corrente()
            print("           Especialização")
            
            if escolha_classe == 1:
                print("[1] Bárbaro")
                print("[2] Paladino")
                print("[3] Seguir sem especialização")
        
                while True:
                    try:
                        escolha_espec = int(input("Selecione a opção desejada: "))
                        if escolha_espec == 1:
                            return Barbaro()
                        elif escolha_espec == 2:
                            return Paladino()
                        elif escolha_espec == 3:
                            return Guerreiro()
                        else:
                            print("Tente de novo")
                    except ValueError:
                        print("Valor inválido")
                        break
                    
            elif escolha_classe == 2:
                print("[1] Druida")
                print("[2] Acadêmico")
                print("[3] Seguir sem especialização")
                
                while True:
                    try:
                        escolha_espec = int(input("Selecione a opção desejada: "))
                        if escolha_espec == 1:
                            return Druida()
                        elif escolha_espec == 2:
                            return Academico()
                        elif escolha_espec == 3:
                            return Clerigo()
                        else:
                            print("Tente de novo")
                    except ValueError:
                        print("Valor inválido")
                        break   
                    
            elif escolha_classe == 3:
                print("[1] Ilusionista")
                print("[2] Necromante")
                print("[3] Seguir sem especialização")
                
                while True:
                    try:
                        escolha_espec = int(input("Selecione a opção desejada: "))
                        if escolha_espec == 1:
                            return Ilusionista()
                        elif escolha_espec == 2:
                            return Necromante()
                        elif escolha_espec == 3:
                            return Mago()
                        else:
                            print("Tente de novo")
                    except ValueError:
                        print("Valor inválido")
                        break 
                    
            elif escolha_classe == 4:
                print("[1] Ranger")
                print("[2] Bardo")
                print("[3] Seguir sem especialização")
                
                while True:
                    try:
                        escolha_espec = int(input("Selecione a opção desejada: "))
                        if escolha_espec == 1:
                            return Ranger()
                        elif escolha_espec == 2:
                            return Bardo()
                        elif escolha_espec == 3:
                            return Ladrao()
                        else:
                            print("Tente de novo")
                    except ValueError:
                        print("Valor inválido")
                        break      
                    
            else:
                print("Escolha um número presente na lista.")
        except ValueError:
            print("Insira um número válido.")