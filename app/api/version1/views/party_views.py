from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties


@v1.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating a party
    '''
    
    party = request.get_json()

    if not party:
        return make_response(jsonify({
            "message": "Your submission cannot be empty",
            "status": 400
        }), 400)

    elif len(party) != 3:
        return make_response(jsonify({
            "message": "You should have three fields while submitting",
            "status": 400
        }), 400)
       
    name = party['name']
    hqAddress = party['hqAddress']
    logoUrl = party['logoUrl']

    responses = Party().create_party(name, hqAddress, logoUrl)
    return make_response(jsonify({
        'message': 'Party added successfully',
        'status': 201,
        'data': responses
    }), 201)

@v1.route('/parties', methods=['GET'])
def get_all_parties():
    '''
    method for getting all parties
    '''
    all_parties = Party().get_parties()
    return make_response(jsonify({
        'message': 'All parties',
        'status': 201,
        'data':all_parties
    }), 201)

@v1.route('/parties/<int:party_id>', methods=['GET'])
def get_specific_id(party_id):
    '''
    method for getting a specific party
    '''
    specific_party = Party().get_specific_party(party_id)
    if specific_party:
        return make_response(jsonify({
            'message': 'success',
            'Status': 200,
            'parties': specific_party
        }), 200)
    return make_response(jsonify({
        'error': 404,
        'message': 'NOt found'
    }), 404)




