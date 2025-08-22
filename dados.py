import random
import time
from metodos_auxiliares import limpar_tela, corrente


'''                                     CLASSE DE DADOS'''


class Dados: 
    @staticmethod
    def rolar_3d6():                #   Rola 3d6
        return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    
    @staticmethod
    def rolar_4d6():                #   Rola 4d6 e tira o menor valor
        dados = [random.randint(1,6) for _ in range(4)]
        dados.remove(min(dados))    #   Tira o menor valor
        return sum(dados)
    
'''                         MÉTODOS DE DISTRIBUIÇÃO DE ATRIBUTOS'''

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
        valor = Dados.rolar_3d6()
        valores.append(valor) # Armazena cada valor rodado
        
    return distribuicao_por_escolha(valores)

# Estilo Heroico
def estilo_heroico():
    valores = []
    for i in range(6):
        valor = Dados.rolar_4d6()
        valores.append(valor)
        
    return distribuicao_por_escolha(valores)

def distribuicao_por_escolha(valores):
    
    print("=-=-=-=-=-=-=-= Distribuição dos Atributos =-=-=-=-=-=-=-=")
    
    print(f"                  {valores}")
    corrente()
    time.sleep(1.75)
    
    print("                        Atributos")
    print("        Força - Destreza - Constituição - Inteligência\n                    Sabedoria - Carisma")
    corrente()
    time.sleep(1.75)
    
    atributos = [0,0,0,0,0,0]
    val_usados = [False, False, False, False, False, False]
    
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    for i in range(6):
        print(f"Escolha o valor do atributo {nomes_atributos[i]}:")
        
        # Mostra valores disponíveis
        for j in range(6):
            if not val_usados[j]:
                print(f"{j+1}º Opção: {valores[j]}")
        
        while True:
            try:
                escolha = int(input("Digite o número correspondente à opção: ")) - 1
                if 0 <= escolha < 6 and not val_usados[escolha]:
                    atributos[i] = valores[escolha]
                    val_usados[escolha] = True
                    break
                else:
                    print("Opção inválida! Escolha um número disponível.")
            except ValueError:
                print("Digite um número válido!")
                
        corrente()
        time.sleep(0.2)
    
    return atributos