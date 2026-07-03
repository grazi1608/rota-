from flask import Blueprint, request, jsonify

from services.Veiculo import create_veiculo
from services.Veiculo import get_veiculos
from services.Veiculo import get_veiculo
from services.Veiculo import update_veiculo
from services.Veiculo import delete_veiculo

veiculo_bp = Blueprint("veiculo", __name__)


# LISTAR TODOS
@veiculo_bp.route("/", methods=["GET"])
def listar():

    veiculos = get_veiculos.execute()

    return jsonify(veiculos), 200


# BUSCAR POR ID
@veiculo_bp.route("/<int:id>", methods=["GET"])
def buscar(id):

    try:

        veiculo = get_veiculo.execute(id)

        return jsonify(veiculo), 200

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404


# CRIAR
@veiculo_bp.route("/", methods=["POST"])
def criar():

    dados = request.get_json()

    try:

        veiculo = create_veiculo.execute(
            placa=dados["placa"],
            modelo=dados["modelo"],
            consumo_por_km=dados["consumo_por_km"],
            motorista_id=dados["motorista_id"]
        )

        return jsonify(veiculo.to_dict()), 201

    except KeyError:

        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 400


# ATUALIZAR
@veiculo_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.get_json()

    try:

        veiculo = update_veiculo.execute(
            id=id,
            placa=dados["placa"],
            modelo=dados["modelo"],
            consumo_por_km=dados["consumo_por_km"],
            motorista_id=dados["motorista_id"]
        )

        return jsonify(veiculo.to_dict()), 200

    except KeyError:

        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404


# DELETAR
@veiculo_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):

    try:

        resultado = delete_veiculo.execute(id)

        return jsonify(resultado), 200

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404