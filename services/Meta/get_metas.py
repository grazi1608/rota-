from models.meta import Meta


def execute():
    # Lista todas as metas
    metas = Meta.query.all()
    return metas
