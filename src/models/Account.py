contas_cadastradas = []


class Account:

    id_accounts = 0

    def __init__(self):
        self._identificador = Account.id_accounts
        Account.id_accounts += 1

        self._nome = ""
        self._email = ""
        self._senha = ""

        self._grupos = []
        self._contatos = []

        global contas_cadastradas
        contas_cadastradas.append(self)

    # getters
    @property
    def identificador(self):
        return self._identificador

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    @property
    def grupos(self):
        return self._grupos

    @property
    def contatos(self):
        return self._contatos

    # setters
    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @senha.setter
    def senha(self, new_senha):
        self._senha = new_senha

    @grupos.setter
    def grupos(self, new_grupos):
        self._grupos = new_grupos

    @contatos.setter
    def contatos(self, new_contatos):
        self._contatos = new_contatos
