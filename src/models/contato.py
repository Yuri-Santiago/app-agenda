class Contato:

    def __init__(self, nome, endereco, cidade, cep, telefone, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__cidade = cidade
        self.__cep = cep
        self.__telefone = telefone
        self.__email = email

    def dict(self):
        return {'nome': self.__nome, 'endereco': self.__endereco, 'cidade': self.__cidade, 'cep': self.__cep,
                'telefones': self.__telefone, 'emails': self.__email}

    def dados(self):
        return f'{self.__nome}/{self.__endereco}/{self.cidade}/{self.__cep}/{self.__telefone}/{self.__email}'

    # getters
    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cidade(self):
        return self.__cidade

    @property
    def cep(self):
        return self.__cep

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    # setters
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @cidade.setter
    def cidade(self, novo_cidade):
        self.__cidade = novo_cidade

    @cep.setter
    def cep(self, novo_cep):
        self.__cep = novo_cep

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email
