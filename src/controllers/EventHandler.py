from Observer import *
from src.models.Factory import *

# todo configurar o route pra deixar todos os dados bem catalogados na hr de chamar o observer !!!
#  fazer metodos get set dos collections de object
#   ainda tem que fazer os try catch pra caso n tiver dados meudeus

"""
select:
pegar um objeto exato

create:
criar objeto >> setar atributos dele

update:
pegar um objeto exato >> setar atributos dele

delete:
pegar um objeto exato >> deletar objeto do banco
"""


# aqui já deixa configurado eventos base
def setup_events():
    # por exemplo eventos de apertar botão que mudam tode o sistema da tela ou do banco
    # esses exemplos estao horriveis pq meio q sao eventos pra pegar alguma coisa
    criar_evento("login ", pegar_objeto)
    criar_evento("sign up ", ObjectFactory.get_object)
    criar_evento("criar", ObjectFactory.get_object)
    criar_evento("editar", pegar_objeto)
    criar_evento("editar", setar_atributos)
    criar_evento("deletar", deletar_objeto)
    criar_evento("sair", None)
