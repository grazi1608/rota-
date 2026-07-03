from models.veiculo import Veiculo


def execute(id):

    veiculo = Veiculo.query.get(id)

    if veiculo is None:
        raise ValueError("Veículo não encontrado.")

    return veiculo.to_dict()