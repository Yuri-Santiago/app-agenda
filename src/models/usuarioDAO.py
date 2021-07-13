import pickle

from src.models.contato_simple_factory import ContatoSimpleFactory
from src.models.usuario import Usuario


class UsuarioDAO:
    @staticmethod
    def conectar():
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'rb') as banco:
            usuarios = pickle.load(banco)
        return usuarios

    @staticmethod
    def salvar(usuario):
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'rb') as banco:
            usuarios = pickle.load(banco)

        for usuario_banco in usuarios:
            if usuario.identificador == usuario_banco.identificador:
                usuarios[usuarios.index(usuario_banco)] = usuario

        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'wb') as novo_banco:
            pickle.dump(usuarios, novo_banco)

    @classmethod
    def inserir_usuario(cls, dados):
        usuarios = cls.conectar()
        usuario = Usuario(usuarios[-1].identificador + 1, dados['nomeCadastro'], dados['emailCadastro'],
                          dados['senhaCadastro'])
        usuarios.append(usuario)
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'wb') as banco:
            pickle.dump(usuarios, banco)
        return usuario

    @classmethod
    def inserir_usuario(cls, dados):
        usuarios = cls.conectar()
        usuario = Usuario(usuarios[-1].identificador + 1, dados['nomeCadastro'], dados['emailCadastro'],
                          dados['senhaCadastro'])
        usuarios.append(usuario)
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'wb') as banco:
            pickle.dump(usuarios, banco)
        return usuario

    @classmethod
    def inserir_contato(cls, dados, id):
        usuario = cls.selecionar_usuario(id)
        contato = ContatoSimpleFactory.criar(dados, usuario.contatos)
        if contato:
            usuario.adicionar_contato(contato)
            # TODO evento do observer aconteceu
            cls.salvar(usuario)
            return True
        return False

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

    @classmethod
    def selecionar_usuario(cls, id):
        usuarios = cls.conectar()
        usuario = [u for u in usuarios if u.identificador == id][0]
        return usuario

    @classmethod
    def pesquisa_atomica(cls, id, senha, search):
        user = cls.validar_usuario(id, senha)
        return user.pesquisa(search)
