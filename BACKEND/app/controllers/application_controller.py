from flask import Blueprint, request, jsonify
from app.services import decision_engine_service  # Not `application_service`

bp = Blueprint('application', __name__, url_prefix='/application')


@bp.route('/submit', methods=['POST'])
def submit_application():
    application_data = request.get_json()
    decision = decision_engine_service.submit_application(application_data)
    return jsonify(decision)
