from flask import Blueprint, render_template, request, redirect, url_for # request acessa os dados da requisição
from model.metodos_auxiliares import gerar_atributos, adjetivo_atributo
from model.base_personagem import Personagem, HABILIDADES
from model.racas import LISTA_RACAS, get_raca
from model.classes_personagem import LISTA_CLASSES, get_classe

bp = Blueprint('personagens', __name__) # guarda as rotas para não ficar tudo guardado dentro do app.py

@bp.route('/')
def index():
    return render_template(
        'index.html',
        racas=LISTA_RACAS,
        classes=LISTA_CLASSES
    )

@bp.route('/gerar', methods=['POST']) # acessa dados da requisição
def gerar():
    modo = request.form.get('modo')
    nome = (request.form.get('nome') or '').strip()
    raca_nome = request.form.get('raca')
    classe_nome = request.form.get('classe')

    if modo not in {'classico', 'aventureiro', 'heroico'}:
        return redirect(url_for('personagens.index')) # se der errado volta para a pág principal

    valores = gerar_atributos(modo)

    if modo == 'classico': # monta o dicionário e renderiza a ficha
        raca = get_raca(raca_nome)
        classe = get_classe(classe_nome)
        personagem = Personagem(
            atributos=dict(zip(HABILIDADES, valores)),
            raca=raca,
            classe=classe,
            nome=nome
        )
        personagem.aplicar_modificadores()
        return render_template('ficha.html', p=personagem, adjetivo=adjetivo_atributo)


    return render_template( # se modo for aventureiro ou heroico renderiza o html de atribuição de atributos
        'atribuir.html',
        valores=valores,
        habilidades=HABILIDADES,
        modo=modo,
        racas=LISTA_RACAS,
        classes=LISTA_CLASSES,
        nome=nome,
        raca_selecionada=raca_nome,
        classe_selecionada=classe_nome,
    )

@bp.route('/finalizar', methods=['POST']) # renderiza a ficha final
def finalizar():
    #modo = request.form.get('modo')
    raca_nome = request.form.get('raca')
    classe_nome = request.form.get('classe')
    nome = (request.form.get('nome') or '').strip()

    atributos = {}
    for hab in HABILIDADES:
        valor_str = request.form.get(f'attr_{hab}')
        atributos[hab] = int(valor_str) if valor_str is not None else 0

    raca = get_raca(raca_nome)
    classe = get_classe(classe_nome)

    personagem = Personagem(atributos=atributos, raca=raca, classe=classe, nome=nome)
    personagem.aplicar_modificadores()

    return render_template('ficha.html', p=personagem, adjetivo=adjetivo_atributo)
