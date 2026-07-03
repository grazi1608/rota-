from models import db
from models.motorista import Motorista


def execute(nome, cpf, cnh, telefone=None, email=None):

    motorista = Motorista.query.filter_by(cpf=cpf).first()

    if motorista:
        raise ValueError("Já existe um motorista com esse CPF.")

    motorista = Motorista.query.filter_by(cnh=cnh).first()

    if motorista:
        raise ValueError("Já existe um motorista com essa CNH.")

    if email:
        motorista = Motorista.query.filter_by(email=email).first()

        if motorista:
            raise ValueError("Já existe um motorista com esse e-mail.")

    novo_motorista = Motorista(
        nome=nome,
        cpf=cpf,
        cnh=cnh,
        telefone=telefone,
        email=email
    )

    db.session.add(novo_motorista)
    db.session.commit()

    return novo_motorista