import pickle
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
    def inserir_usuario(cls, nome, email, senha):
        usuarios = cls.conectar()
        usuario = Usuario(usuarios[-1].identificador + 1, nome, email, senha)
        usuarios.append(usuario)
        with open(r'C:\Users\Yuri\PycharmProjects\app-agenda\src\banco.pickle', 'wb') as banco:
            pickle.dump(usuarios, banco)
        return usuario.identificador

    @classmethod
    def selecionar_usuario(cls, id, senha):
        usuarios = cls.conectar()
        try:
            usuario = [u for u in usuarios if u.identificador == id][0]
            if usuario.checa_senha(senha):
                return usuario
            return 0
        except:
            return 0



# if __name__ == '__main__':
#     usuario = UsuarioDAO.selecionar_usuario(1007, 'senhar')
#     print(usuario)
#     eu = usuarios[0]
#     eu.set_nome("Yuri Mateus Santiago")
#     UsuarioDAO.salvar(eu)
#     UsuarioDAO.inserir_usuario("Kelvin", "kelvin@gmail.com", "oi")
#     UsuarioDAO.inserir_usuario("Ruann", "ruann@gmail.com", "meuamg")
#
#     for usuario in usuarios:
#         print(usuario.identificador)
#         print(usuario.nome)
#         print(usuario.email)
#         print(usuario.senha)
#         print(usuario.contatos)

