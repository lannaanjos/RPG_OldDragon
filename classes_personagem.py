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
    
                        
                        
                        
'''                             CLÉRIGO E ESPECIALIZAÇÕES'''


class Clérigo():
    def __init__(self):
        self.nivel = 0
        
    def magia_divina(self):
        if self.nivel >= 1:
            print('Você pode lançar magias divinas')
            
            
            
            
            
### MÉTODO DE ESCOLHA DE CLASSES

'''

    FAZER

'''  