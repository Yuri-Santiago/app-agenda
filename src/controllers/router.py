from flask import request, redirect, flash, session

from src import app
from src.controllers.observador import Observador
from src.models.usuarioDAO import UsuarioDAO

dao = UsuarioDAO()
observador = Observador()


# login, sign up
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        dados = request.form
        # Cadastrar
        if not dados.get('idEntrar', False) and not dados.get('senhaEntrar', False):
            usuario_atual = dao.inserir_usuario(dados)
            session['id'] = usuario_atual.identificador
            return redirect('/home')

        # Entrar
        elif not dados.get('nomeCadastro', False) and not dados.get('emailCadastro', False) and not dados.get(
                'senhaCadastro', False):
            entrar = dao.validar_usuario(dados)
            if not entrar:
                flash('ID ou Senha Incorreta')
            else:
                usuario_atual = entrar
                session['id'] = usuario_atual.identificador
                return redirect('/home')

        # Entrar e Cadastrar
        else:
            flash('Preencha apenas um Formulário')
    return observador.renderizar('login.html', None)


# Função para deslogar da session
@app.route("/logout")
def logout():
    session["id"] = None
    return redirect("/")


# read contatos, grupos, pesquisa por campo
@app.route("/home", methods=["GET", "POST"])
def home():
    if not session.get("id"):
        return redirect('/index')
    else:
        if request.method == "POST":
            pass
            # dados = request.form
            # resultado = dao.pesquisa_atomica(dados['idUsuario'], dados['senha'], dados['search'])
            #
            # if not resultado:
            #     flash("Não há resultados")
            #
            # return observador.renderizar('home.html', dao.selecionar_usuario(session.get('id')))

        return observador.renderizar('home.html', dao.selecionar_usuario(session.get('id')))


# adicionar contato
@app.route("/contact/add", methods=["GET", "POST"])
def add_contact():
    if not session.get("id"):
        return redirect('/index')
    else:
        if request.method == "POST":
            dados = request.form
            inserir = dao.inserir_contato(dados, session.get('id'))
            if inserir:
                return redirect('/home')
            flash("Contato repetido, tente novamente")
        return observador.renderizar('createContact.html', None)


# adicionar grupo
@app.route("/group/add", methods=["GET", "POST"])
def add_group():
    if not session.get("id"):
        return redirect('/index')
    else:
        if request.method == "POST":
            dados = request.form
            inserir = dao.inserir_grupo(dados, session.get('id'))
            if inserir:
                return redirect('/home')
            flash("Nome do Grupo repetido, tente novamente")
        return observador.renderizar('createGroup.html', dao.selecionar_usuario(session.get('id')))


@app.route('/contact/delete/<nome>')
def deletar_contato(nome):
    usuario = dao.selecionar_usuario(session.get('id'))
    dao.deletar_contato(nome, usuario)
    return redirect('/home')


@app.route('/group/delete/<nome>')
def deletar_grupo(nome):
    usuario = dao.selecionar_usuario(session.get('id'))
    dao.deletar_grupo(nome, usuario)
    return redirect('/home')


# editar contato
@app.route("/contact/update/<nome>", methods=["GET", "POST"])
def editar_contato(nome):
    if request.method == "POST":
        dados = request.form
        atualizar = dao.update_contato(dados, nome, dao.selecionar_usuario(session.get('id')))
        if atualizar:
            return redirect('/home')
        flash("Nome repetido, tente novamente")
    return observador.renderizar('editContact.html', None)


# editar group
@app.route("/group/update/<nome>", methods=["GET", "POST"])
def editar_grupo(nome):
    if request.method == "POST":
        dados = request.form
        atualizar = dao.update_grupo(dados, nome, dao.selecionar_usuario(session.get('id')))
        if atualizar:
            return redirect('/home')
        flash("Nome do Grupo repetido, tente novamente")
    return observador.renderizar('editGroup.html', dao.selecionar_usuario(session.get('id')))

