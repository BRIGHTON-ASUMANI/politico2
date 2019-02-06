from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties

@v1.route('/createparty', methods=['POST'])
def create_parties():
    party = request.get_json()
    party_name = ['name']
    party_hq = ['hqAddress']
    party_logo = ['logoUrl']

    party = {
        'name': party_name,
        'hqAddress': party_hq,
        'logoUrl': party_logo
    }
    
    parties.append(party)
    c_party = Party.create_party(party)
    return make_response(jsonify({
        'message': 'Party added successfully'
    }), 200)

