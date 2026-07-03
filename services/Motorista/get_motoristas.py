from models.motorista import Motorista


def execute():
    motoristas = Motorista.query.all()
    return [motorista.to_dict() for motorista in motoristas]