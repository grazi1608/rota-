from models import db
from models.meta import Meta

def execute(id, valor_meta=None, data_inicio=None, data_fim=None, concluida=None, motorista_id=None):
    meta = Meta.query.get(id)
    if not meta:
        raise ValueError("Meta não encontrada.")

    # Atualiza apenas os campos enviados
    if valor_meta is not None:
        meta.valor_meta = valor_meta
    if data_inicio is not None:
        meta.data_inicio = data_inicio
    if data_fim is not None:
        meta.data_fim = data_fim
    if concluida is not None:
        meta.concluida = concluida
    if motorista_id is not None:
        meta.motorista_id = motorista_id

    db.session.commit()
    return meta