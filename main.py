'''Orientações: 

    Utilize o livro de regras para entender os requisitos.
    Desenvolva utilizando paradigmas de orientação a objetos em python
    Desenvolva as três formas de distribuição de atributos disponíveis na página 14: Estilo clássico; estilo aventureiro; estilo heróico.


Critérios de avaliação:

    Utilizar a orientação a objetos para organizar o código, classes com papéis específicos, funções (métodos) que possuam responsabilidades únicas e claras. (Valor 0.2)
    Utilizar linguagem python (Requisito obrigatório)
    Cada um dos três estilos deve seguir as regras do livro de regras corretamente, utilizar uma 'main' como interação com o usuário. (Valor 0.3)


Entrega: Enviar o link do GitHub com o código'''


import random

### CLASSES

#   Classe base de personagem
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
        
#   Guerreiro e especializações
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
    
    
#   Classe dos dados
class Dados: 
    @staticmethod
    def rolar_3d6():                #   Rola 3d6
        return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    
    @staticmethod
    def rolar_4d6():                #   Rola 4d6 e tira o menor valor
        dados = [random.randint(1,6) for _ in range(4)]
        dados.remove(min(dados))    #   Tira o menor valor
        return sum(dados)
  
### MÉTODO DE ESCOLHA DE CLASSES

'''

    FAZER

'''  
  
### MÉTODOS DE DISTRIBUIÇÃO DE ATRIBUTOS

# Estilo clássico
def estilo_classico():
    atributos = []                  #   Esta lista vazia recebe os valores das rolagens de dados nas respectivas posições dos atributos para que os atributos peguem o número certo lá embaixo
    
    # Rolagem de dados
    atributos.append(Dados.rolar_3d6()) # 1a Força
    atributos.append(Dados.rolar_3d6()) # 2a Destreza
    atributos.append(Dados.rolar_3d6()) # 3a Constituição
    atributos.append(Dados.rolar_3d6()) # 4a Inteligência
    atributos.append(Dados.rolar_3d6()) # 5a Sabedoria
    atributos.append(Dados.rolar_3d6()) # 6a Carisma
    
    return atributos

# Estilo Aventureiro
def estilo_aventureiro():
    valores = [] # Armazena os valores da rolagem dos dados
    for i in range(6):
        valor = Dados.rolar_3d6
        valores.append(valor) # Armazena cada valor rodado
        
    print(f"Valores rodados: {valores}")
    print("Distribua os pontos entre os atributos: ")
    print("[1] Força [2] Destreza [3] Constituição [4] Inteligência [5] Sabedoria [6] Carisma")
    
    atributos = [0,0,0,0,0,0] # Na ordem
    val_usados = [False, False, False, False, False, False] # Serve para marcar os valores que já foram usados
    
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    for i in range(6):
        print(f"Escolha o valor {nomes_atributos[i]}:")
        # Loop p mostrar valores disponíveis
        for j in range(6):
            if not val_usados[j]:
                print(f"{j+1}º Opção: {valores[j]}")
            
        while True:
            try:
                escolha = int(input("Digite o número correspondente à opção:")) - 1 # por causa do 0 inicial
                if 0 <= escolha < 6 and not val_usados[escolha]:
                    atributos[i] = valores[escolha]
                    val_usados[escolha] = True # Marca valor já usado
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
    return atributos

# Estilo Heroico
def estilo_heroico():
    valores = []
    for i in range(6):
        valor = Dados.rolar_4d6()
        valores.append(valor)
        
    print(f"Valores rodados: {valores}")
    print("Distribua os pontos entre os atributos: ")
    
    atributos = [0,0,0,0,0,0]
    val_usados = [False, False, False, False, False, False]
    
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    for i in range(6):
        print(f"Escolha o valor {nomes_atributos[i]}:")
        # Loop p mostrar valores disponíveis
        for j in range(6):
            if not val_usados[j]:
                print(f"{j+1}º Opção: {valores[j]}")
            
        while True:
            try:
                escolha = int(input("Digite o número correspondente à opção:")) - 1 # por causa do 0 inicial
                if 0 <= escolha < 6 and not val_usados[escolha]:
                    atributos[i] = valores[escolha]
                    val_usados[escolha] = True # Marca valor já usado
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
    return atributos        
    
    
    
# Main
def main():
    
    while True:
    
        print("=-=-=-=-= Criação de Personagem =-=-=-=-=")
        print()
        print("[1] Estilo Clássico")
        print("[2] Estlo Aventureiro")
        print("[3] Estilo Heroico")
        print("[4] Sair")
        
        try:
            escolha = int(input("Selecione uma opção: "))
            
            if(escolha == 4):
                print("Encerrando programa...")
                break
            elif escolha in [1,2,3]:
                # Entra na criação de personagem
                nome = input("Insira o nome do seu personagem: ")
                
                personagem = Personagem(nome)
                
                if escolha == 1:
                    atributos = estilo_classico()
                elif escolha == 2:
                    atributos = estilo_aventureiro()
                elif escolha == 3:
                    atributos = estilo_heroico()
                    
                # Atribui os valores do atributos (sempre em ordem)
                personagem.forca = atributos[0]
                personagem.destreza = atributos[1]
                personagem.constituicao = atributos[2]
                personagem.inteligencia = atributos[3]
                personagem.sabedoria = atributos[4]
                personagem.carisma = atributos[5]
                
                #   Escolha de classe
                # personagem.classe = escolher_classe()
                
                #   Mostra resultado final
            
            else:
                print("Opção inválida!\nTente novamente.")
                
        except ValueError:
            print("Digite um número válido!")    
        
        
if __name__ == "__main__":
        main()
    
        
