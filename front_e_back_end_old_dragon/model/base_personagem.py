HABILIDADES = ['FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR']


class Personagem:
    def __init__(self, atributos: dict, raca, classe, nome: str | None = None):
        self.nome = (nome or '').strip()
        self.atributos_base = {h: int(atributos.get(h, 0)) for h in HABILIDADES}
        self.atributos = self.atributos_base.copy()
        self.raca = raca
        self.classe = classe
        self.habilidades_classe = []

    def aplicar_modificadores(self):
        if self.raca and hasattr(self.raca, 'mod_atributos'):
            for hab, mod in self.raca.mod_atributos.items():
                self.atributos[hab] = self.atributos.get(hab, 0) + mod

        if self.classe:
            self.habilidades_classe = list(self.classe.habilidades)

    @property
    def resumo(self):
        return {
            'nome': self.nome or '—',
            'raca': self.raca.nome if self.raca else None,
            'classe': self.classe.nome if self.classe else None,
            'atributos_base': self.atributos_base,
            'atributos_finais': self.atributos,
            'habilidades_classe': self.habilidades_classe,
        }
