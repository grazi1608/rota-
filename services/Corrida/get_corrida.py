from models.corrida import Corrida


def execute(id):
    corrida = Corrida.query.get(id)
    if corrida is None:
        raise ValueError("Corrida não encontrada.")
    return corrida.to_dict()