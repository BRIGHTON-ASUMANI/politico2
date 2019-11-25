import re
from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.party_models import Party, parties


regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)




@v1.route('/', methods=['GET', 'POST'])
def index():
    return make_response(jsonify({
            "message": "Welcome to Politico",
            "status": 200
        }), 200)


@v1.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating a party
    '''
    
    party = request.get_json()
  
    name = party['name']
    hqAddress = party['hqAddress']
    logoUrl = party['logoUrl']

    responses = Party().create_party(name, hqAddress, logoUrl)
    if party:
        if len(party) != 3:
            return make_response(jsonify({
                "message": "You should have three fields while submitting",
                "status": 400
            }), 400)


        elif ((party['name'] == "") or (party['logoUrl'] == "")) or (party['hqAddress'] == "") :
            return make_response(jsonify({
                "message": "You cannot pass in an empty string",
                "status": 400
            }), 400)

        elif party['name'] != str(party['name']) :
            return make_response(jsonify({
                "message": "input has to be a string",
                "status": 400
            }), 400)

        elif party['name'] != str(party['name']) :
            return make_response(jsonify({
                "message": "input has to be a string",
                "status": 400
            }), 400)

        elif not party['name'].isalpha():
            return make_response(jsonify({
                "message": "A name cannot contain anything apart from letters",
                "status": 400
            }), 400)

        elif not party['name'] :
            return make_response(jsonify({
                "message": "You are missing name",
                "status": 400
            }), 400)


        elif not party['hqAddress']:
            return make_response(jsonify({
                "message": "input has to be a hqAdress",
                "status": 400
            }), 400)

        elif not party['logoUrl']:
            return make_response(jsonify({
                "message": "input has to be a logoUrl",
                "status": 400
            }), 400)

        elif not re.match(regex, party['logoUrl']):
            return make_response(jsonify({
                "message": "That is not a valid url",
                "status": 400
            }), 400)
        
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
        'message': 'party doesn\'t exist',
        'data': []
    }), 404)


@v1.route('/parties/<int:party_id>/<string:name>', methods=['PATCH'])
def edit_party(party_id, name):
    '''
    Edit political party endpoint'
    '''
    for i in range(len(parties['party'])):
        if parties['party'][i]['party_id'] == party_id:
            party = parties['party'][i]
            party['name'] = name
            parties['party'][i] = party
            return make_response(jsonify({
                'message': 'editted name successful',
                'status': 200
                }), 200)
            
    return make_response(jsonify({
                'message': 'Party not found',
                'status' : 404,
                }), 404)
                

@v1.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    Party().delete_party(party_id)
    if Party().delete_party(party_id):
        return make_response(jsonify({
            'status': 'OK',
            'message': 'successfully deleted'
        }), 200)
    else:
        return make_response(jsonify({
            'status': 'ok',
            'message': 'not found'
        }), 404)
    

    






