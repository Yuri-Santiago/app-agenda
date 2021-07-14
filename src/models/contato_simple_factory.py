from src.models.contato import Contato
from src.models.i_simple_factory import ISimpleFactory


class ContatoSimpleFactory(ISimpleFactory):
    def criar(self, dados, usuario):
        nomes = [c.nome for c in usuario.contatos]
        if dados['nome'].title() in nomes:
            return False
        return Contato(dados['nome'].title(), dados['endereco'], dados['cidade'], dados['cep'], dados['telefone'],
                       dados['email'])
