
class Group:

    id_groups = 0

    def __init__(self):
        self._identificador = Group.id_groups
        Group.id_groups += 1
        self._nome = ""
        self._descricao = ""
        self._membros_id = []

    # getters
    @property
    def identificador(self):
        return self._identificador

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def membros_id(self):
        return self._membros_id

    # setters
    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @descricao.setter
    def descricao(self, new_descricao):
        self._descricao = new_descricao

    @membros_id.setter
    def membros_id(self, new_list):
        self._membros_id = new_list
