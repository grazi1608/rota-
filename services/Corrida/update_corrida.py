from models import db
from models.corrida import Corrida
from models.motorista import Motorista
from models.veiculo import Veiculo


def execute(id, valor, distancia, motorista_id, veiculo_id, data_hora=None):
    """
    Atualiza uma corrida.
    """

    corrida = Corrida.query.get(id)

    if corrida is None:
        raise ValueError("Corrida não encontrada.")

    motorista = Motorista.query.get(motorista_id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    veiculo = Veiculo.query.get(veiculo_id)

    if veiculo is None:
        raise ValueError("Veículo não encontrado.")

    custo_estimado = distancia * veiculo.consumo_por_km
    lucro = valor - custo_estimado

    corrida.valor = valor
    corrida.distancia = distancia
    corrida.custo_estimado = custo_estimado
    corrida.lucro = lucro
    corrida.motorista_id = motorista_id
    corrida.veiculo_id = veiculo_id

    if data_hora is not None:
        corrida.data_hora = data_hora

    db.session.commit()

    return corrida