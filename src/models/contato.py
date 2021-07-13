class Contato:

    def __init__(self, nome, endereco, cidade, cep, telefones, emails):
        self.__nome = nome
        self.__endereco = endereco
        self.__cidade = cidade
        self.__cep = cep
        self.__telefones = telefones
        self.__emails = emails

        self.__observadores = []
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
        return self.__telefones

    @property
    def email(self):
        return self.__emails

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

    def adicionar_telefone(self, telefone):
        self.__telefones.append(telefone)

    def adicionar_email(self, email):
        self.__emails.append(email)

    def inscrever(self, observador):
        self.__observadores.append(observador)
