
class Contact:
    id_contacts = 0

    def __init__(self):
        self._identificador = Contact.id_contacts
        Contact.id_contacts += 1

        self._nome = ""
        self._endereco = ""
        self._cidade = ""
        self._telefone = ""
        self._cep = ""
        self._email = ""

        self._grupos = []

    # getters
    @property
    def identificador(self):
        return self._identificador

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def cidade(self):
        return self._cidade

    @property
    def telefone(self):
        return self._telefone

    @property
    def cep(self):
        return self._cep

    @property
    def email(self):
        return self._email

    @property
    def grupos(self):
        return self._grupos

    # setters
    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @endereco.setter
    def endereco(self, new_endereco):
        self._endereco = new_endereco

    @cidade.setter
    def cidade(self, new_cidade):
        self._cidade = new_cidade

    @telefone.setter
    def telefone(self, new_telefone):
        self._telefone = new_telefone

    @cep.setter
    def cep(self, new_cep):
        self._cep = new_cep

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @grupos.setter
    def grupos(self, new_list):
        self._grupos = new_list
