from Account import *
from Contact import *
from Group import *
import re


class ObjectFactory:
    @staticmethod
    def get_object(dados):
        kind = dados["kind"]

        if kind == "account":
            return Account()
        elif kind == "group":
            return Group()
        elif kind == "contact":
            return Contact()
        else:
            return None


# aproveitei pra criar outras funções de generalização

def setar_atributos(dados):
    objeto = dados["objeto"]
    kind = dados["kind"]

    if kind == "account":
        if "nome" in dados:
            objeto.nome = dados["nome"]
        if "email" in dados:
            objeto.email = dados["email"]
        if "senha" in dados:
            objeto.senha = dados["senha"]

    elif kind == "group":
        if "nome" in dados:
            objeto.nome = dados["nome"]
        if "descricao" in dados:
            objeto.descricao = dados["descricao"]
        if "membros_id" in dados:
            objeto.membros_id = dados["membros_id"]

    elif kind == "contact":
        if "nome" in dados:
            objeto.nome = dados["nome"]
        if "endereco" in dados:
            objeto.email = dados["email"]
        if "cidade" in dados:
            objeto.cidade = dados["cidade"]
        if "telefone" in dados:
            objeto.telefone = dados["telefone"]
        if "cep" in dados:
            objeto.cep = dados["cep"]
        if "email" in dados:
            objeto.email = dados["email"]


def pegar_objeto(dados):
    kind = dados["kind"]

    if kind == "account":
        for conta in contas_cadastradas:
            if conta.identificador == dados["account_id"] and conta.senha == dados["account_senha"]:
                return conta

    elif kind == "group":
        conta = pegar_objeto(dados)
        for grupo in conta.grupos:
            if grupo.identificador == dados["group_id"]:
                return grupo

    elif kind == "contact":
        conta = pegar_objeto(dados)
        for contato in conta.contatos:
            if contato.identificador == dados["contact_id"]:
                return contato


def deletar_objeto(dados):
    kind = dados["kind"]

    if kind == "account":
        for conta in contas_cadastradas:
            if conta.identificador == dados["account_id"] and conta.senha == dados["account_senha"]:
                contas_cadastradas.remove(conta)

    elif kind == "group":
        conta = pegar_objeto(dados)
        for grupo in conta.grupos:
            if grupo.identificador == dados["group_id"]:
                conta.grupos.remove(grupo)

    elif kind == "contact":
        conta = pegar_objeto(dados)
        for contato in conta.contatos:
            if contato.identificador == dados["contact_id"]:
                conta.contatos.remove(contato)


def pesquisar_objeto(dados):
    conta = pegar_objeto(dados)
    resultado_pesquisa = []

    for atributo in conta.dict().values():
        if re.search(f".*{dados['pesquisa']}.*", atributo):
            resultado_pesquisa.append(conta)

    for contato in conta.contatos:
        for atributo in contato.dict().values():
            if re.search(f".*{dados['pesquisa']}.*", atributo):
                resultado_pesquisa.append(conta)

    for grupo in conta.grupos:
        for atributo in grupo.dict().values():
            if re.search(f".*{dados['pesquisa']}.*", atributo):
                resultado_pesquisa.append(conta)

    return resultado_pesquisa

# todo esqueci como usa regex e fazer função dict de cada entidade