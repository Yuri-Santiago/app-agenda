from src.models.contato import Contato


class ContatoSimpleFactory:
    @staticmethod
    def criar(dados, lista):
        nomes = [c.nome for c in lista]
        if dados['nome'].title() in nomes:
            return False
        return Contato(dados['nome'], dados['endereco'], dados['cidade'], dados['cep'], dados['telefone'],
                       dados['email'])
