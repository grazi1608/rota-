from flask import Blueprint, request, jsonify
from datetime import datetime
from services.Meta import (
    create_meta,
    get_metas,
    get_meta,
    update_meta,
    delete_meta
)

meta_bp = Blueprint("meta", __name__)

# Auxiliar para converter string de data (ex: '2026-12-31') em objeto date do Python
def formatar_data(data_str):
    if data_str:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    return None

@meta_bp.route("/", methods=["GET"])
def listar():
    metas = get_metas.execute()
    return jsonify([meta.to_dict() for meta in metas]), 200

@meta_bp.route("/<int:id>", methods=["GET"])
def buscar(id):
    try:
        meta = get_meta.execute(id)
        return jsonify(meta.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@meta_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()
    try:
        data_fim = formatar_data(data.get("data_fim"))
        data_inicio = formatar_data(data.get("data_inicio")) # Opcional, aceita None

        nova_meta = create_meta.execute(
            valor_meta=data.get("valor_meta"),
            data_fim=data_fim,
            motorista_id=data.get("motorista_id"),
            data_inicio=data_inicio,
            concluida=data.get("concluida", False)
        )
        return jsonify(nova_meta.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@meta_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    data = request.get_json()
    try:
        data_fim = formatar_data(data.get("data_fim"))
        data_inicio = formatar_data(data.get("data_inicio"))

        meta_atualizada = update_meta.execute(
            id=id,
            valor_meta=data.get("valor_meta"),
            data_inicio=data_inicio,
            data_fim=data_fim,
            concluida=data.get("concluida"),
            motorista_id=data.get("motorista_id")
        )
        return jsonify(meta_atualizada.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@meta_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    try:
        delete_meta.execute(id)
        return jsonify({"message": "Meta deletada com sucesso."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404