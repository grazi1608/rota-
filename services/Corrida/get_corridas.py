from models.corrida import Corrida


def execute():
    corridas = Corrida.query.all()
    return [corrida.to_dict() for corrida in corridas]