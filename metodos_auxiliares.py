import os
import textwrap

def limpar_tela():
    if os.name == 'nt':
        os.system('cls') # Limpa tela do Windows
    else:
        os.system('clear') # Limpa tela do Linux / Mac
    
def aguarda_tecla():
    input("Pressione Enter para prosseguir...")
    limpar_tela()
    
def corrente():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
def texto_comprido(texto):
    return textwrap.fill(texto, width=41)
    
           