from flask import Blueprint
from app.controllers import vaccine_card_controller

bp = Blueprint("vaccine-cards", __name__, url_prefix="/vaccinations")


bp.post("")(vaccine_card_controller.create_vaccine_card)
bp.get("")(vaccine_card_controller.get_vaccine_card)