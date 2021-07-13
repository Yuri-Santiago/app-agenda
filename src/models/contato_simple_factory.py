from contato import Contato


class ContatoSimpleFactory:
    @staticmethod
    def criarContato(nome, endereco, cidade, cep, telefones, emails):
        # todo if nome in contatos retorna errado, else
        return Contato(nome, endereco, cidade, cep, telefones, emails)
