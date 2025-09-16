import random


def rolar_d6(n=1):
    return [random.randint(1, 6) for _ in range(n)]


def rolar_3d6():
    return sum(rolar_d6(3))


def rolar_4d6_descarta_menor():
    dados = rolar_d6(4)
    return sum(sorted(dados)[1:])


def gerar_atributos(modo: str):
    modo = (modo or '').lower()
    if modo == 'classico':
        return [rolar_3d6() for _ in range(6)]
    elif modo == 'aventureiro':
        return [rolar_3d6() for _ in range(6)]
    elif modo == 'heroico':
        return [rolar_4d6_descarta_menor() for _ in range(6)]
    else:
        raise ValueError('Modo inválido')
