class Classe:
    def __init__(self, nome: str, habilidades: list[str]):
        self.nome = nome
        self.habilidades = habilidades


GUERREIRO = Classe('Guerreiro', [
    'Aparar',
    'Maestria em Arma',
    'Ataque Extra',
])

LADRAO = Classe('Ladrão', [
    'Ataque Furtivo',
    'Ouvir Ruídos',
    'Talentos de Ladrão'
])

MAGO = Classe('Mago', [
    'Magias Arcanas',
    'Ler Magias',
    'Detectar Magias',
])

LISTA_CLASSES = [c.nome for c in [GUERREIRO, LADRAO, MAGO]]


def get_classe(nome: str):
    mapa = {c.nome: c for c in [GUERREIRO, LADRAO, MAGO]}
    return mapa.get(nome)
