from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties


@v1.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating a party
    '''
    party = request.get_json()
    name = party['name']
    hqAddress = party['hqAddress']
    logoUrl = party['logoUrl']


    response = Party().create_party(name, hqAddress, logoUrl)
    return make_response(jsonify(response = {
        'message': 'Party added successfully',
        'status': 201,
        'data': response
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

