from src import app
from flask import *
from EventHandler import *


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


# login, sign up
@app.route("/")
@app.route("/agenda", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dados = request.form
        dados["kind"] = "account"
        conta = pegar_objeto(dados)
        if conta:
            return redirect(url_for('homepage'))
        else:
            flash("conta não encontrada")
    return "render_template('index.html)"


# read contatos, grupos, pesquisa por campo
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":     # se tiver algum post é pq o cabra ta usando a barra de pesquisa
        dados = request.form
        resultado = pesquisar_objeto(dados)
        if not resultado:
            flash("Não há resultados")
        return render_template('home.html', objetos=resultado)
    return render_template('home.html', objetos=None)
    # todo como que eu vo pegar o id do cabra direto pra pegar as coisa dele


# adicionar grupo
@app.route("/add/group", methods=["GET", "POST"])
def add_group():
    pass


# adicionar contato
@app.route("/add/contact", methods=["GET", "POST"])
def add_contact():
    pass


# editar group
@app.route("edit/group", methods=["GET", "POST"])
def edit_group():
    if request.method == "POST":
        dados = request.form
        flash("Seu grupo foi atualizado, olhe no fim da lista")
        return redirect(url_for('homepage'))
    return render_template("editGroup.html")


# editar contato
@app.route("edit/contact", methods=["GET", "POST"])
def edit_contact():
    if request.method == "POST":
        dados = request.form
        flash("Seu contato foi atualizado, olhe no fim da lista")
        return redirect(url_for('homepage'))
    return render_template("editContact.html")
