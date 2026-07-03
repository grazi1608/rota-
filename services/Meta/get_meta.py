from models.meta import Meta


def execute(id):
    # Busca uma meta específica pelo ID
    meta = Meta.query.get(id)
    if not meta:
        raise ValueError("Meta não encontrada.")
    return meta
