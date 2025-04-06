from flask import Blueprint, request, jsonify
from models import Registro
from database import db
from datetime import datetime
from sqlalchemy import desc

routes = Blueprint('routes', __name__)

@routes.route('/registros', methods=['POST'])
def crear_registro():
    data = request.get_json()
    try:
        nuevo = Registro(
            fecha=datetime.strptime(data['fecha'], "%Y-%m-%d").date(),
            pasos=int(data['pasos']),
            tiempo=int(data['tiempo']),
            velocidad=float(data['velocidad'])
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify(nuevo.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes.route('/registros', methods=['GET'])
def obtener_registros():
    registros = Registro.query.order_by(desc(Registro.fecha), desc(Registro.id)).all()
    return jsonify([r.to_dict() for r in registros]), 200
