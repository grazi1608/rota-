from models import db
from models.meta import Meta

def execute(valor_meta, data_fim, motorista_id, data_inicio=None, concluida=False):
    # Criando a nova meta com base no seu modelo
    nova_meta = Meta(
        valor_meta=valor_meta,
        data_fim=data_fim,
        motorista_id=motorista_id,
        data_inicio=data_inicio,
        concluida=concluida
    )

    db.session.add(nova_meta)
    db.session.commit()

    return nova_meta