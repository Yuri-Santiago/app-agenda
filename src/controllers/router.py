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

from flask import request, redirect, flash, render_template, session

from src import app
from src.models.usuarioDAO import UsuarioDAO


# login, sign up
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        dados = request.form
        # Cadastrar
        if not dados.get('idEntrar', False) and not dados.get('senhaEntrar', False):
            usuario_atual = UsuarioDAO.inserir_usuario(dados)
            session['id'] = usuario_atual.identificador
            return redirect('/home')

        # Entrar
        elif not dados.get('nomeCadastro', False) and not dados.get('emailCadastro', False) and not dados.get(
                'senhaCadastro', False):
            entrar = UsuarioDAO.validar_usuario(dados)
            if not entrar:
                flash('ID ou Senha Incorreta')
            else:
                usuario_atual = entrar
                session['id'] = usuario_atual.identificador
                return redirect('/home')

        # Entrar e Cadastrar
        else:
            flash('Preencha apenas um Formulário')
    return render_template('login.html')


# Função para deslogar da session
@app.route("/logout")
def logout():
    session["id"] = None
    return redirect("/")


# read contatos, grupos, pesquisa por campo
@app.route("/home", methods=["GET", "POST"])
def home():
    if not session.get("id"):
        return redirect('/login')
    else:
        if request.method == "POST":
            dados = request.form
            resultado = UsuarioDAO.pesquisa_atomica(dados['idUsuario'], dados['senha'], dados['search'])

            if not resultado:
                flash("Não há resultados")

            return render_template('home.html',
                                   usuario=UsuarioDAO.selecionar_usuario(session.get('id')))

        return render_template('home.html',
                               usuario=UsuarioDAO.selecionar_usuario(session.get('id')))


# adicionar contato
@app.route("/contact/add", methods=["GET", "POST"])
def add_contact():
    if not session.get("id"):
        return redirect('/login')
    else:
        if request.method == "POST":
            dados = request.form
            inserir = UsuarioDAO.inserir_contato(dados, session.get('id'))
            if inserir:
                return redirect('/home')
            flash("Contato repetido, tente novamente")
        return render_template('createContact.html')


# adicionar grupo
@app.route("/group/add", methods=["GET", "POST"])
def add_group():
    if not session.get("id"):
        return redirect('/login')
    else:
        if request.method == "POST":
            contatos_selecionados = request.form.getlist("contatos")
            print(contatos_selecionados)
            dados = request.form
        return render_template('createGroup.html', usuario=UsuarioDAO.selecionar_usuario(session.get('id')))


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
