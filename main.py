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
from base_personagem import Personagem
from dados import estilo_aventureiro, estilo_classico, estilo_heroico
from metodos_auxiliares import limpar_tela, aguarda_tecla

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
                limpar_tela()
                nome = input("Insira o nome do seu personagem: ")
                limpar_tela()
                
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
                print("Personagem criado com sucesso!")
                aguarda_tecla()
            
            else:
                print("Opção inválida!\nTente novamente.")
                
        except ValueError:
            print("Digite um número válido!")    
        
        
if __name__ == "__main__":
        main()
    
        
