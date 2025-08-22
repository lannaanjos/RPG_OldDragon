from metodos_auxiliares import corrente

'''                             GUERREIRO E ESPECIALIZAÇÕES'''

class Guerreiro:
    def __init__(self):
        self.nivel = 1
        
    def aparar(self):
        if self.nivel >= 1:
            print("O dano foi absorvido por sua arma!")
     
    def maestria_em_arma(self):       
        if self.nivel == 1:
            print("Você é mestre na sua arma\n+1 de dano com sua arma")
        elif 3 < self.nivel < 10:
            print("Você é mestre em duas armas!\n+2 de dano em ambas as armas")
        else:
            print("Você é mestre em todas as armas deste grupo!\n+3 de dano para todas as armas")
    def ataque_extra(self):
        if self.nivel >= 6:
                print("Você tem um segundo ataque disponível com sua arma de maestria!")
            
    def __repr__(self):
        return "Guerreiro"
                
class Barbaro(Guerreiro):
    def __init__(self):
        super().__init__()
        
    def vigor_barbaro(self):
        if self.nivel >= 1:
            print("+2 de vida por nível")
        
    def talentos_selvagens(self):
        if self.nivel >= 3:
            print("Você pode escalar e se camuflar na natureza!")
            
    def surpresa_selvagem(self):
        if self.nivel >= 6:
            print("Você pode surpreender inimigos em ambientes naturais")
        
    def forca_do_totem(self):
        if self.nivel == 10:
            print("Você pode ferir qualquer criatura que precise de uma arma mágica para ser ferida")
            
    def __repr__(self):
        return "Bárbaro"

class Paladino(Guerreiro):
    def __init__(self):
        super().__init__()
        
    def imunidade_a_doencas(self):
        if self.nivel >= 1:
            print("Você é imune a doenças")
            
    def cura_pelas_maos(self):
        if self.nivel >= 3:
            print("Você tem uma cura simples diária disponível")
            
    def aura_de_protecao(self):
        if self.nivel >= 6:
            print("Você pode criar uma barreira de proteção uma vez ao dia")
            
    def espada_sagrada(self):
        if self.nivel == 10:
            print("Ganha uma Espada Sagrada ao derrotar um inimigo caótico de grande poder.")
            
    def __repr__(self):
        return "Paladino"                        
                        
'''                             CLÉRIGO E ESPECIALIZAÇÕES'''

class Clerigo():
    def __init__(self):
        self.nivel = 0
        
    def magia_divina(self):
        if self.nivel >= 1:
            print('Você pode lançar magias divinas')
            
    def afastar_mortos_vivos(self):
        if self.nivel >= 1:
            print("Você pode afastar mortos vivos uma vez ao dia")
        
    def cura_milagrosa(self):
        if self.nivel >= 1:
            print("Você pode curar ferimentos de 1º círculo!")
            
    def __repr__(self):
        return "Clérigo"
            
class Druida(Clerigo):
    def __init__(self):
        super().__init__()
        
    def herbalismo(self):
        print("Você é capaz de identificar itens naturais próprios para consumo.")
        
    def previdencia(self):
        print("Seus acampamentos nos ermos são sempre seguros.")
        
    def transformacao(self):
        if 6 <= self.nivel < 10:
            print("Você pode assumir a forma de num animal pequeno não mágico 3 vezes ao dia")
            
    def transformacao_melhorada(self):
        if self.nivel == 10:
            print('"Você pode assumir a forma de um animal não mágia de qualquer tamanho 3 vezes ao dia.')
            
    def __repr__(self):
        return "Druida"
            
class Academico(Clerigo):
    def __init__(self):
        super().__init__()
        
    def conhecimento_academico(self):
        if self.nivel >= 1:
            print("Você é capaz de identificar monstros e animais além de suas habilidades e fraquezas")
            
    def deficifrar_linguagens(self):
        if self.nivel >= 3:
            print("você é capaz de decifrar diferentes idiomas")
            
    def lendas_e_tradicoes(self):
        if self.nivel >= 6:
            print("Você é capaz de identificar lendas e tradições")
            
    def __repr__(self):
        return "Acadêmico"
            
'''                                 MAGO E ESPECIALIZAÇÕES'''  
          
class Mago():
    def __init__(self):
        self.nivel = 0
        
    def magias_arcanas(self):
        if self.nivel >= 1:
            print("Você é capaz de lançar magias arcanas estudas")
            
    def ler_magias(self):
        if self.nivel >= 1:
            print("Você pode decifrar e ler inscrições mágicas")
            
    def detectar_magias(self):
        if self.nivel >= 1:
            print("Você é capaz de perceber coisas ou pesssoas encantadas uma vez ao dia")
            
    def __repr__(self):
        return "Mago"
            
class Ilusionista(Mago):
    def __init__(self):
        super().__init__()
        
    def magias_exclusivas(self):
        if self.nivel >= 1:
            print("Você deve escrever magias exclusivas em seu grimório Ilusão e Som Ilusório.")
            
    def ilusao_melhorada(self):
        if self.nivel >= 3:
            print("Você cria uma ilusão")
            
    def miragem(self):
        if self.nivel >= 6:
            print("Você cria uma miragem")
            
    def ilusao_permanente(self):
        if self.nivel == 10:
            print("Você cria uma ilusão permanente")
            
    def __repr__(self):
        return "Ilusionista"
            
class Necromante(Mago):
    def __init__(self):
        super().__init__()
        
    def magias_exclusivas(self):
        if self.nivel >= 1:
            print("Você deve escrever magias exclusivas em seu grimório Toque Sombrio e Aterrorizar")
            
    def criar_mortos_vivos(self):
        if self.nivel >= 3:
            print("Você pode conjurar mortos vivos")
            
    def drenar_vida(self):
        if self.nivel > 6:
            print("Você pode drenar vida")
        
    def magia_da_morte(self):
        if self.nivel == 10:
            print("Você pode matar alguém instantaneamente")
            
    def __repr__(self):
        return "Necromante"            
            
            
### MÉTODO DE ESCOLHA DE CLASSES
def escolher_classe():    
    corrente()
    print("          Escolha de Classe       ")
    corrente()
    print("[1] Guerreiro")
    print("[2] Clérigo")
    print("[3] Mago")
    
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
                    
            else:
                print("Escolha um número presente na lista.")
        except ValueError:
            print("Insira um número válido.")
            
    
    
                
                
                
        
     