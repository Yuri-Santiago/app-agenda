"""
CONTATOS ROUTERS

index/ login/ sign up/ botao sair
tela inicial/ ler grupos/ ler contatos
adicionar grupo
adicionar contato
editar grupo
editar contato

GET api/contatos
GET api/contato/id
POST api/contato
PUT api/contato/id
DELETE api/contato/id
"""

from flask import request, redirect, flash, url_for, render_template

from src import app
from src.models.usuarioDAO import UsuarioDAO


usuario_atual = 0

# login, sign up
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    global usuario_atual
    if request.method == "POST":
        dados = request.form
        if not dados['idEntrar'] and not dados['senhaEntrar']:
            usuario_atual = UsuarioDAO.inserir_usuario(dados['nomeCadastro'], dados['emailCadastro'], dados['senhaCadastro'])
            return redirect(url_for('home'))
        else:
            entrar = UsuarioDAO.selecionar_usuario(int(dados['idEntrar']), dados['senhaEntrar'])
            if not entrar:
                flash('ID ou Senha Incorreta')
            else:
                return redirect(url_for('home'))
    return render_template('login.html')


#
# read contatos, grupos, pesquisa por campo
@app.route("/home", methods=["GET", "POST"])
def home():
    print(usuario_atual)
    if request.method == "POST":  # se tiver algum post é pq o cabra ta usando a barra de pesquisa
        dados = request.form
        resultado = True
        if not resultado:
            flash("Não há resultados")
        return render_template('home.html', objetos=resultado)
    return render_template('home.html')
    # todo como que eu vo pegar o id do cabra direto pra pegar as coisa dele
#
#
# # adicionar grupo
# @app.route("/add/group", methods=["GET", "POST"])
# def add_group():
#     pass
#
#
# # adicionar contato
# @app.route("/add/contact", methods=["GET", "POST"])
# def add_contact():
#     pass
#
#
# # editar group
# @app.route("edit/group", methods=["GET", "POST"])
# def edit_group():
#     if request.method == "POST":
#         dados = request.form
#         flash("Seu grupo foi atualizado, olhe no fim da lista")
#         return redirect(url_for('homepage'))
#     return render_template("editGroup.html")
#
#
# # editar contato
# @app.route("edit/contact", methods=["GET", "POST"])
# def edit_contact():
#     if request.method == "POST":
#         dados = request.form
#         flash("Seu contato foi atualizado, olhe no fim da lista")
#         return redirect(url_for('homepage'))
#     return render_template("editContact.html")
