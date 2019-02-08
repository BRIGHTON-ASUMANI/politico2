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

    elif party['name'] is True:
        return make_response(jsonify({
            "message": "Party name already exists",
            "status": 409
        }), 409)
           
    name = party.get('name')
    hqAddress = party.get('hqAddress')
    logoUrl = party.get('logoUrl')


    return make_response(jsonify({
        'message': 'Party added successfully',
        'status': 201,
        'data': [{
            "name":name
        }]
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

