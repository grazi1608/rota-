from models import db
from models.veiculo import Veiculo


def execute(id):
    veiculo = Veiculo.query.get(id)

    if veiculo is None:
        raise ValueError("Veículo não encontrado.")

    db.session.delete(veiculo)
    db.session.commit()

    return {
        "mensagem": "Veículo excluído com sucesso."
    }