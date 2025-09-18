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
    
def adjetivo_atributo(hab: str, valor: int) -> str:

    h = (hab or "").strip().upper()

    # define faixas genéricas
    if valor <= 8:
        faixa = "faixa1"
    elif 9 <= valor <= 12:
        faixa = "faixa2"
    elif 13 <= valor <= 16:
        faixa = "faixa3"
    else:
        faixa = "faixa4"

    # tabelas específicas por habilidade
    tabelas = {
        "FOR": {
            "faixa1": "Fraco",
            "faixa2": "Mediano",
            "faixa3": "Forte",
            "faixa4": "Muito Forte",
        },
        "DES": {
            "faixa1": "Letárgico",
            "faixa2": "Mediano",
            "faixa3": "Ágil",
            "faixa4": "Preciso",
        },
        "CON": {
            "faixa1": "Frágil",
            "faixa2": "Mediano",
            "faixa3": "Resistente",
            "faixa4": "Vigoroso",
        },
        "INT": {
            "faixa1": "Inépto",
            "faixa2": "Mediano",
            "faixa3": "Inteligente",
            "faixa4": "Gênio",
        },
        "SAB": {
            "faixa1": "Tolo",
            "faixa2": "Mediano",
            "faixa3": "Intuitivo",
            "faixa4": "Presciente",
        },
        "CAR": {
            "faixa1": "Descortês",
            "faixa2": "Mediano",
            "faixa3": "Influente",
            "faixa4": "Ídolo",
        },
    }

    tabela = tabelas.get(h)
    if not tabela:
        return ""  # habilidade desconhecida (defensivo)

    return tabela[faixa]    
