HABILIDADES = ['FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR'] # define as chaves dos atributos


class Personagem:
    def __init__(self, atributos: dict, raca, classe, nome: str | None = None):
        self.nome = (nome or '').strip() # se não houver nada no nome, garante que vai ser armazenado como uma string vazia
        self.atributos_base = {h: int(atributos.get(h, 0)) for h in HABILIDADES} # percorre as chaves, colocando 0 se não achar
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

    @property # só leitura
    def resumo(self):
        return {
            'nome': self.nome or '—',
            'raca': self.raca.nome if self.raca else None,
            'classe': self.classe.nome if self.classe else None,
            'atributos_base': self.atributos_base,
            'atributos_finais': self.atributos,
            'habilidades_classe': self.habilidades_classe,
        }
