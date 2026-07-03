from models.veiculo import Veiculo


def execute():
   

    veiculos = Veiculo.query.all()

    return [veiculo.to_dict() for veiculo in veiculos]