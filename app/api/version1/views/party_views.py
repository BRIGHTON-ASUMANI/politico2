from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties


@v1.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating a party
    '''
    
    party = request.get_json(force=True)

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
def get_specific_party(party_id):
    '''
    method for getting a specific party
    '''

    specific_party = Party().get_specific_party(party_id)
    if specific_party:
        return make_response(jsonify({
            'message': 'success',
            'status': 200,
            'data': [specific_party]
        }), 200)
    return make_response(jsonify({
        'status': 404,
        'message': 'office doesn\'t exist',
        'data': []
    }), 404)


@v1.route('/parties/<int:party_id>/<string:name>', methods=['PATCH'])
def edit_party(party_id, name):
    '''
    Edit political party endpoint'
    '''
    for i in range(len(parties)):
        if parties[i]['party_id'] == party_id:
            party = parties[i]
            party['name'] = name
            parties[i] = party
            return make_response(jsonify({
                'message': ' editted successful',
                'status': 400
                }), 400)
            
    return make_response(jsonify({
                'message': 'Party not found',
                'status' : 409,
                }), 400)

@v1.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    Party().delete_party(party_id)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'successfully deleted'
    }), 200)

    






