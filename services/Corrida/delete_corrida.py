from models import db
from models.corrida import Corrida


def execute(id):
    corrida = Corrida.query.get(id)
    if corrida is None:
        raise ValueError("Corrida não encontrada.")
    db.session.delete(corrida)
    db.session.commit()
    return {
        "mensagem": "Corrida excluída com sucesso."
    }