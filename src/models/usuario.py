from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__identificador = id

        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=10)

        self.__grupos = []
        self.__contatos = []

    # getters
    @property
    def identificador(self):
        return self.__identificador

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def grupos(self):
        return self.__grupos

    @property
    def contatos(self):
        return self.__contatos

    # setters
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @senha.setter
    def senha(self, novo_senha):
        self.__senha = novo_senha

    def adicionar_contato(self, contato):
        self.__contatos.append(contato)

    def adicionar_grupo(self, grupo):
        self.__grupos.append(grupo)

    def checa_senha(self, senha):
        if cryp.verify(senha, self.senha):
            return True
        return False
