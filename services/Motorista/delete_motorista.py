from models import db
from models.motorista import Motorista


def execute(id):
    motorista = Motorista.query.get(id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    db.session.delete(motorista)
    db.session.commit()

    return {
        "mensagem": "Motorista excluído com sucesso."
    }