from flask import request, jsonify
from app.models.vaccine_card_model import VaccineCard
from app.configs.database import db
from sqlalchemy.orm.session import Session
from flask_sqlalchemy import BaseQuery
from sqlalchemy.exc import IntegrityError


def create_vaccine_card():
    data = request.get_json()

    if not VaccineCard.check_keys(data):
        return {'error': 'A requisição deverá ter os campos cpf, name, vaccine_name e health_unit_name'}, 400

    data = VaccineCard.check_keys(data)

    if not VaccineCard.check_json_types(data):
        return {'error': 'Todos os campos passados devem ser uma string'}, 400
    
    if not VaccineCard.check_cpf(data):
        return {'error': 'cpf invalido'}, 400

    data = VaccineCard.add_shot_dates(data)

    try:
        vaccine_card = VaccineCard(**data)

        db.session.add(vaccine_card)

        db.session.commit()

    except IntegrityError:
        return {'error': 'cpf ja cadastrado'}, 409
    
    return jsonify(vaccine_card), 201



def get_vaccine_card():
    session: Session = db.session
    base_query: BaseQuery = session.query(VaccineCard)

    cards = base_query.all()

    return jsonify(cards), 200