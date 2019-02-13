from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.office_models import Office, offices


@v1.route('/offices', methods=['POST'])
def create_office():
    '''
    endpoint for creating an office
    '''
    office = request.get_json()
    
    
    office_name = office['name']
    office_type = office['type']
     
    response = Office().create_office(office_name, office_type)
    return make_response(jsonify({
        'message': 'Office added successfully',
        'status': 201,
        'data': response
    }), 201)

@v1.route('/offices', methods=['GET'])
def get_all_offices():
    '''
    endpoint for getting all offfices
    '''
    all_offices = Office().get_offices()
    return make_response(jsonify({
        'message': 'All offices',
        'status': 200,
        'data':all_offices
    }), 200)


@v1.route('/offices/<int:office_id>', methods=['GET'])
def get_specific_office(office_id):
    '''
    endpoint for getting a specific office
    '''
    specific_office = Office().get_specific_office(office_id)
    if specific_office:
        return make_response(jsonify({
            'message': 'success',
            'status': 200,
            'data': [specific_office]
        }), 200)
    return make_response(jsonify({
        'status': 404,
        'message': 'office not found',
        'data': []
    }), 404)




