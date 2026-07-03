from models.motorista import Motorista


def execute(id):
    # esse pega apenas 1 motorista, já o motoristas lista todos

    motorista = Motorista.query.get(id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    return motorista.to_dict()