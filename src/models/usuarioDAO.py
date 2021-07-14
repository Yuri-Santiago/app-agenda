import pickle

from src.models.contato_simple_factory import ContatoSimpleFactory
from src.models.grupo_simple_factory import GrupoSimpleFactory
from src.models.usuario import Usuario


class UsuarioDAO:

    def __init__(self):
        self.__contatofactory = ContatoSimpleFactory()
        self.__grupofactory = GrupoSimpleFactory()

    @staticmethod
    def conectar():
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\banco.pickle', 'rb') as banco:
            usuarios = pickle.load(banco)
        return usuarios

    @staticmethod
    def salvar(usuario):
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\banco.pickle', 'rb') as banco:
            usuarios = pickle.load(banco)

        for usuario_banco in usuarios:
            if usuario.identificador == usuario_banco.identificador:
                usuarios[usuarios.index(usuario_banco)] = usuario

        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\banco.pickle', 'wb') as novo_banco:
            pickle.dump(usuarios, novo_banco)

    @classmethod
    def inserir_usuario(cls, dados):
        usuarios = cls.conectar()
        usuario = Usuario(usuarios[-1].identificador + 1, dados['nomeCadastro'], dados['emailCadastro'],
                          dados['senhaCadastro'])
        usuarios.append(usuario)
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\banco.pickle', 'wb') as banco:
            pickle.dump(usuarios, banco)
        return usuario

    @classmethod
    def validar_usuario(cls, dados):
        usuarios = cls.conectar()
        try:
            usuario = [u for u in usuarios if u.identificador == int(dados['idEntrar'])][0]
            if usuario.checa_senha(dados['senhaEntrar']):
                return usuario
            return 0
        except:
            return 0

    def inserir_contato(self, dados, id):
        usuario = self.selecionar_usuario(id)
        contato = self.__contatofactory.criar(dados, usuario)
        if contato:
            usuario.adicionar_contato(contato)
            self.salvar(usuario)
            return True
        return False

    def inserir_grupo(self, dados, id):
        usuario = self.selecionar_usuario(id)
        grupo = self.__grupofactory.criar(dados, usuario)
        if grupo:
            usuario.adicionar_grupo(grupo)
            self.salvar(usuario)
            return True
        return False

    @classmethod
    def selecionar_usuario(cls, id):
        usuarios = cls.conectar()
        usuario = [u for u in usuarios if u.identificador == id][0]
        return usuario

    @classmethod
    def update_contato(cls, dados, nome_atual, usuario):
        contato = [c for c in usuario.contatos if c.nome == nome_atual][0]
        if nome_atual != dados['nome'].title():
            nomes = [c.nome for c in usuario.contatos]
            if dados['nome'].title() in nomes:
                return False
            else:
                contato.nome = dados['nome'].title()
                contato.endereco = dados['endereco']
                contato.cidade = dados['cidade']
                contato.cep = dados['cep']
                contato.email = dados['email']
                contato.telefone = dados['telefone']
        else:
            contato.nome = dados['nome'].title()
            contato.endereco = dados['endereco']
            contato.cidade = dados['cidade']
            contato.cep = dados['cep']
            contato.email = dados['email']
            contato.telefone = dados['telefone']
        cls.salvar(usuario)
        return True

    @classmethod
    def update_grupo(cls, dados, nome_atual, usuario):
        grupo = [g for g in usuario.grupos if g.nome == nome_atual][0]
        contatos_selecionados = dados.getlist("contatos")
        contatos_grupo = grupo.contatos
        if nome_atual != dados['nome'].title():
            nomes = [g.nome for g in usuario.grupos]
            if dados['nome'].title() in nomes:
                return False
            else:

                grupo.nome = dados['nome'].title()
                grupo.descricao = dados['descricao']

                for contato in contatos_grupo:
                    if contato.nome in contatos_selecionados:
                        grupo.remover_contato(contato)
                        contatos_selecionados.remove(contato.nome)

                if contatos_selecionados:
                    for contato in usuario.contatos:
                        if contato.nome in contatos_selecionados:
                            grupo.adicionar_contato(contato)

        else:
            grupo.nome = dados['nome'].title()
            grupo.descricao = dados['descricao']

            for contato in contatos_grupo:
                if contato.nome in contatos_selecionados:
                    grupo.remover_contato(contato)
                    contatos_selecionados.remove(contato.nome)
            if contatos_selecionados:
                for contato in usuario.contatos:
                    if contato.nome in contatos_selecionados:
                        grupo.adicionar_contato(contato)
        cls.salvar(usuario)
        return True

    @classmethod
    def deletar_contato(cls, nome, usuario):
        contato = [c for c in usuario.contatos if c.nome == nome][0]
        usuario.remover_contato(contato)
        cls.salvar(usuario)

    @classmethod
    def deletar_grupo(cls, nome, usuario):
        grupo = [g for g in usuario.grupos if g.nome == nome][0]
        usuario.remover_grupo(grupo)
        cls.salvar(usuario)

    @classmethod
    def pesquisa_atomica(cls, id, search):
        usuario = cls.selecionar_usuario(id)
        return usuario.pesquisa(search)
