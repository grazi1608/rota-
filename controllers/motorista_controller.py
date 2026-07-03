from flask import Blueprint, request, jsonify

from services.Motorista import create_motorista
from services.Motorista import get_motoristas
from services.Motorista import get_motorista
from services.Motorista import update_motorista
from services.Motorista import delete_motorista

motorista_bp = Blueprint("motorista", __name__)


# LISTAR TODOS
@motorista_bp.route("/", methods=["GET"])
def listar():
    motoristas = get_motoristas.execute()
    return jsonify(motoristas), 200


# BUSCAR POR ID
@motorista_bp.route("/<int:id>", methods=["GET"])
def buscar(id):
    try:
        motorista = get_motorista.execute(id)
        return jsonify(motorista), 200

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 404


# CRIAR
@motorista_bp.route("/", methods=["POST"])
def criar():

    dados = request.get_json()

    try:

        motorista = create_motorista.execute(
            nome=dados["nome"],
            cpf=dados["cpf"],
            cnh=dados["cnh"],
            telefone=dados.get("telefone"),
            email=dados.get("email")
        )

        return jsonify(motorista.to_dict()), 201

    except KeyError:
        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400


# ATUALIZAR
@motorista_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.get_json()

    try:

        motorista = update_motorista.execute(
            id=id,
            nome=dados["nome"],
            cpf=dados["cpf"],
            cnh=dados["cnh"],
            telefone=dados.get("telefone"),
            email=dados.get("email")
        )

        return jsonify(motorista.to_dict()), 200

    except KeyError:
        return jsonify({"erro": "Campos obrigatórios não informados."}), 400

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 404


# DELETAR
@motorista_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):

    try:

        resultado = delete_motorista.execute(id)

        return jsonify(resultado), 200

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 404