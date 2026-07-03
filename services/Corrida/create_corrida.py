from models import db
from models.corrida import Corrida
from models.motorista import Motorista
from models.veiculo import Veiculo


def execute(valor, distancia, motorista_id, veiculo_id):
    """
    Cadastra uma nova corrida.
    """

    motorista = Motorista.query.get(motorista_id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    veiculo = Veiculo.query.get(veiculo_id)

    if veiculo is None:
        raise ValueError("Veículo não encontrado.")

    # Calcula custo e lucro
    custo_estimado = distancia * veiculo.consumo_por_km
    lucro = valor - custo_estimado

    corrida = Corrida(
        valor=valor,
        custo_estimado=custo_estimado,
        lucro=lucro,
        distancia=distancia,
        motorista_id=motorista_id,
        veiculo_id=veiculo_id
    )

    db.session.add(corrida)
    db.session.commit()

    return corrida