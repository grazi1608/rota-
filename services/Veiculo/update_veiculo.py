from models import db
from models.veiculo import Veiculo
from models.motorista import Motorista


def execute(id, placa, modelo, consumo_por_km, motorista_id):
    veiculo = Veiculo.query.get(id)
    if veiculo is None:
        raise ValueError("Veículo não encontrado.")
    placa_existente = Veiculo.query.filter_by(placa=placa).first()

    if placa_existente and placa_existente.id != id:
        raise ValueError("Já existe um veículo com essa placa.")
    motorista = Motorista.query.get(motorista_id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    veiculo.placa = placa
    veiculo.modelo = modelo
    veiculo.consumo_por_km = consumo_por_km
    veiculo.motorista_id = motorista_id
    db.session.commit()
    return veiculo