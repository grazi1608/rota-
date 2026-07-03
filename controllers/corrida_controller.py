from flask import Blueprint, request, jsonify
from datetime import datetime

from services.Corrida import create_corrida
from services.Corrida import get_corridas
from services.Corrida import get_corrida
from services.Corrida import update_corrida
from services.Corrida import delete_corrida

corrida_bp = Blueprint("corrida", __name__)


def formatar_data_hora(data_hora_str):
    """Converte string ISO (ex: '2026-01-01T10:00:00') em datetime, se houver valor."""
    if data_hora_str:
        return datetime.fromisoformat(data_hora_str)
    return None


# LISTAR TODAS
@corrida_bp.route("/", methods=["GET"])
def listar():

    corridas = get_corridas.execute()

    return jsonify(corridas), 200


# BUSCAR POR ID
@corrida_bp.route("/<int:id>", methods=["GET"])
def buscar(id):

    try:

        corrida = get_corrida.execute(id)

        return jsonify(corrida), 200

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404


# CRIAR
@corrida_bp.route("/", methods=["POST"])
def criar():

    dados = request.get_json()

    try:

        corrida = create_corrida.execute(
            valor=dados["valor"],
            distancia=dados["distancia"],
            motorista_id=dados["motorista_id"],
            veiculo_id=dados["veiculo_id"]
        )

        return jsonify(corrida.to_dict()), 201

    except KeyError:

        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 400


# ATUALIZAR
@corrida_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.get_json()

    try:

        corrida = update_corrida.execute(
            id=id,
            data_hora=formatar_data_hora(dados.get("data_hora")),
            valor=dados["valor"],
            distancia=dados["distancia"],
            motorista_id=dados["motorista_id"],
            veiculo_id=dados["veiculo_id"]
        )

        return jsonify(corrida.to_dict()), 200

    except KeyError:

        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404


# DELETAR
@corrida_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):

    try:

        resultado = delete_corrida.execute(id)

        return jsonify(resultado), 200

    except ValueError as erro:

        return jsonify({"erro": str(erro)}), 404