class Grupo:

    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__contatos = []

    # getters
    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def contatos(self):
        return self.__contatos

    # setters
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @descricao.setter
    def descricao(self, novo_descricao):
        self.__descricao = novo_descricao

    def adicionar_contato(self, contato):
        self.__contatos.append(contato)

    def remover_contato(self, contato):
        self.__contatos.remove(contato)
