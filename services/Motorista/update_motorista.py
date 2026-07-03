from models import db
from models.motorista import Motorista


def execute(id, nome, cpf, cnh, telefone=None, email=None):
    motorista = Motorista.query.get(id)

    if motorista is None:
        raise ValueError("Motorista não encontrado.")

    # Verifica se outro motorista já possui o CPF informado
    motorista_cpf = Motorista.query.filter_by(cpf=cpf).first()

    if motorista_cpf and motorista_cpf.id != id:
        raise ValueError("Já existe um motorista com esse CPF.")

    # Verifica se outro motorista já possui a CNH informada
    motorista_cnh = Motorista.query.filter_by(cnh=cnh).first()

    if motorista_cnh and motorista_cnh.id != id:
        raise ValueError("Já existe um motorista com essa CNH.")

    # Verifica se outro motorista já possui o e-mail informado
    if email:
        motorista_email = Motorista.query.filter_by(email=email).first()

        if motorista_email and motorista_email.id != id:
            raise ValueError("Já existe um motorista com esse e-mail.")

    motorista.nome = nome
    motorista.cpf = cpf
    motorista.cnh = cnh
    motorista.telefone = telefone
    motorista.email = email

    db.session.commit()
    return motorista