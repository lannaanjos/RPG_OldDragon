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
from racas import escolher_raca
from classes_personagem import escolher_classe
from dados import estilo_aventureiro, estilo_classico, estilo_heroico
from metodos_auxiliares import limpar_tela, aguarda_tecla, corrente


# Guerreiro, Barbaro, Paladino, Clerigo, Druida, Academico, Mago, Ilusionista, Necromante, 

# Main
def main():
    
    while True:
    
        print("=-=-=-=-= Criação de Personagem =-=-=-=-=")
        print()
        print("[1] Estilo Clássico")
        print("[2] Estilo Aventureiro")
        print("[3] Estilo Heroico")
        print("[4] Sair\n")
        
        try:
            escolha = int(input("Selecione uma opção: "))
            
            if(escolha == 4):
                print("Encerrando programa...")
                break
            elif escolha in [1,2,3]:
                # Entra na criação de personagem
                limpar_tela()
                nome = input("Insira o nome do seu personagem: ")
                personagem = Personagem(nome)
                
                #   Escolha de Raça + Add características das raças
                limpar_tela()
                personagem.raca = escolher_raca()
                personagem.set_by_raca(personagem.raca)
                #   Escolha de classe
                limpar_tela()
                personagem.classe = escolher_classe()
                limpar_tela()
                
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
                
                
                
                
                #   Mostra resultado final
                print("Personagem criado com sucesso!")
                aguarda_tecla()
                
                # Mostra personagem criado
                personagem.mostrar_info()
                corrente()
                aguarda_tecla()           
                
            else:
                print("Opção inválida!\nTente novamente.")
                
        except ValueError:
            print("Digite um número válido!")    
        
        
if __name__ == "__main__":
    main()
    
        
