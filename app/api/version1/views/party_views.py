from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties
from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties

@v1.route('/parties', methods=['POST'])
def create_party():
    party = request.get_json()
    party_name = party.get('name', '')
    party_hq = party.get('hqAddress', '')
    party_logo = party.get('logoUrl', '')

    new_party = {
        'name': party_name,
        'hq': party_hq,
        'logo': party_logo
    }
    
    Party.create_party(new_party)
    return make_response(jsonify(response = {
        'message': 'Party added successfully',
        'status': 201,
        'data': [new_party]
    }), 201)

@v1.route('/parties', methods=['POST'])
def get_all_parties():
    res = Party.get_parties()
    return make_response(jsonify({
        'message': res
    }), 200)

