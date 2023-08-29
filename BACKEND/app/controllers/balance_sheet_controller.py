from flask import Blueprint, request, jsonify
from app.services import accounting_service

bp = Blueprint('balance_sheet', __name__, url_prefix='/balance_sheet')


@bp.route('/fetch', methods=['POST'])
def fetch_balance_sheet():
    request_data = request.get_json()
    print(request_data)
    balance_sheet_entry = accounting_service.fetch_balance_sheet(int(request_data['year']), int(request_data['month']))
    print(balance_sheet_entry)
    return jsonify(balance_sheet_entry)
