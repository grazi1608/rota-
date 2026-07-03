from models import db
from models.veiculo import Veiculo
from models.motorista import Motorista


def execute(placa, modelo, consumo_por_km, motorista_id):
    veiculo = Veiculo.query.filter_by(placa=placa).first()

    if veiculo:
        raise ValueError("Já existe um veículo com essa placa.")

    motorista = Motorista.query.get(motorista_id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    novo_veiculo = Veiculo(
        placa=placa,
        modelo=modelo,
        consumo_por_km=consumo_por_km,
        motorista_id=motorista_id
    )

    db.session.add(novo_veiculo)
    db.session.commit()

    return novo_veiculo