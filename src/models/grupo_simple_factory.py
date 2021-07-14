from src.models.grupo import Grupo
from src.models.i_simple_factory import ISimpleFactory


class GrupoSimpleFactory(ISimpleFactory):
    def criar(self, dados, usuario):
        nomes = [g.nome for g in usuario.grupos]
        if dados['nome'].title() in nomes:
            return False
        grupo = Grupo(dados['nome'].title(), dados['descricao'])
        contatos_selecionados = dados.getlist("contatos")
        for contato in usuario.contatos:
            if contato.nome in contatos_selecionados:
                grupo.adicionar_contato(contato)
        return grupo
