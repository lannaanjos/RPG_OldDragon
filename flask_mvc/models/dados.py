import random

class Dados:
    @staticmethod
    def rolar_3d6():
        return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    
    @staticmethod
    def rolar_4d6():
        dados = [random.randint(1,6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)
    
    @staticmethod # para modificar a vida do Guerreiro e especializações depois de upar
    def rolar_1d10():
        return random.randint(1,10)
    
    @staticmethod # pós upar Clérigo e especializações
    def rolar_1d8():
        return random.randint(1,8)
    
    @staticmethod # ladrão
    def rolar_1d6():
        return random.randint(1,6)
    
    @staticmethod # mago
    def rolar_1d4():
        return random.randint(1,4)
    
def distribuicao_atributos(opcao):
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    if opcao == 1: # Clássico
        atributos = [Dados.rolar_3d6() for _ in range(6)]
        
        return dict(zip(nomes_atributos, atributos))
    
    elif opcao == 2: # Aventureiro
        valores = [Dados.rolar_3d6 for _ in range(6)]
        
        return {"Valores disponíveis: ": valores, "Atributos: ": nomes_atributos}
    
    elif opcao == 3: # Heroico
        valores = [Dados.rolar_4d6 for _ in range(6)]
        
        return {"Valores disponíveis: ": valores, "Atributos: ": nomes_atributos}
    
    else: # validação deu errado
        return dict(zip(nomes_atributos, [0, 0, 0, 0, 0, 0]))