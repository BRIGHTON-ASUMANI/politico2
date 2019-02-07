from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.office_models import Office, offices


@v1.route('/offices', methods=['POST'])
def create_office():
    '''
    method for creating an office
    '''
    office = request.get_json()
    office_name = office['name']
    office_type = office['type']
     
    response = Office().create_office(office_name, office_type)
    return make_response(jsonify(response = {
        'message': 'Office added successfully',
        'status': 201,
        'data': response
    }), 201)

@v1.route('/offices', methods=['GET'])
def get_all_offices():
    '''
    method for getting all offfices
    '''
    all_offices = Office().get_offices()
    return make_response(jsonify({
        'message': 'All Offices',
        'status': 200,
        'data':all_offices
    }), 200)


