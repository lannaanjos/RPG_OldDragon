from metodos_auxiliares import corrente
'''                                             RAÇAS'''
class Humano:
    def __init__(self):
        self.hab_raca = ["Aprendizado", "Adaptabilidade"]
        
    def __repr__(self):
        return "Humano"
        
class Elfo:
    def __init__(self):
        self.hab_raca = ["Percepção Natural", "Graciosos", "Arma Racial", "Imunidades"]
        
    def __repr__(self):
        return "Elfo"
    
class Anao:
    def __init__(self):
        self.hab_raca = ["Mineradores", "Vigorosos", "Armas Grandes", "Inimigos"]
    
    def __repr__(self):
        return "Anão"
    
class Halfling:
    def __init__(self):
        self.hab_raca = ["Furtivos", "Destemidos", "Pequenos"]
        
    def __repr__(self):
        return "Halfling"
        
'''                                         ESCOLHER RAÇA'''

def escolher_raca():
    corrente()
    print("Escolha de Raça")
    corrente()
    print("[1] Humano")
    print("[2] Elfo")
    print("[3] Anão")
    print("[4] Halfling")
    
    while True:
        try:
            escolha_raca = int(input("Selecione a opção desejada: "))
            
            if escolha_raca == 1:
                return Humano()
            elif escolha_raca == 2:
                return Elfo()
            elif escolha_raca == 3:
                return Anao()
            elif escolha_raca == 4:
                return Halfling()
            else:
                print("Tente de novo")
        except ValueError:
            print("Insira um número válido")
            
