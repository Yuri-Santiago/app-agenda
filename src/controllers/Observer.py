eventos = {}


def criar_evento(event_type: str, function_name):
    # se ainda não existir, cria
    if not event_type in eventos:
        # cada evento tem uma lista de funções pra rodar quando evento acontecer
        eventos[event_type] = []

    # adiciona função na lista de funções
    eventos.append(function_name)


def observar(event_type, dados):
    # ignorar o que não deve ser observado
    if event_type not in eventos:
        return None

    # se tiver faça as funções uma por uma
    for fn in eventos[event_type]:
        fn(dados)
