from models import db
from models.meta import Meta

def execute(id):
    meta = Meta.query.get(id)
    if not meta:
        raise ValueError("Meta não encontrada.")

    db.session.delete(meta)
    db.session.commit()
    return True