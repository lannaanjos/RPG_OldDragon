from model.base_personagem import HABILIDADES


class Raca:
    def __init__(self, nome: str, mod_atributos: dict):
        self.nome = nome
        self.mod_atributos = {h: int(mod_atributos.get(h, 0)) for h in HABILIDADES}


HUMANO = Raca('Humano', {})
ELFO = Raca('Elfo', {'DES': 2, 'CON': -1})
ANAO = Raca('Anão', {'CON': 2, 'CAR': -1})

LISTA_RACAS = [r.nome for r in [HUMANO, ELFO, ANAO]]


def get_raca(nome: str):
    mapa = {r.nome: r for r in [HUMANO, ELFO, ANAO]}
    return mapa.get(nome)
