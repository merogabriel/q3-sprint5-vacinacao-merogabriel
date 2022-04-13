from datetime import datetime
from app.configs.database import db
from sqlalchemy import Column, String, DateTime
from datetime import timedelta
from dataclasses import dataclass

@dataclass
class VaccineCard(db.Model):
    cpf: int
    name: int
    first_shot_date: int
    second_shot_date: int
    vaccine_name: int
    health_unit_name: int

    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)


    @classmethod
    def check_keys(cls, payload: dict):
        keys = [ 
            "cpf",
            "name",
            "vaccine_name",
            "health_unit_name"
            ]

        for key in keys:
            if key not in payload.keys():
                return False

        serialized_payload = {
            "cpf": payload['cpf'],
            "name": payload['name'],
            "vaccine_name": payload['vaccine_name'],
            "health_unit_name": payload['health_unit_name'],
        }

        return serialized_payload


    @classmethod
    def check_json_types(cls, payload: dict):
        for value in payload.values():
            if type(value) != str:
                return False
        
        return True


    @classmethod
    def add_shot_dates(cls, payload: dict):
        payload['first_shot_date'] = datetime.now().strftime('%d/%m/%Y')
        payload['second_shot_date'] = (datetime.now() + timedelta(days=90)).strftime('%d/%m/%Y')

        return payload


    @classmethod
    def check_cpf(cls, payload: dict):
        try:
            int(payload['cpf'])
        except ValueError:
            return False

        if len(payload['cpf']) != 11:
            return False
        
        return True

        