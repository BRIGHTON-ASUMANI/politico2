from flask import jsonify, make_response, request
from app.api.version1 import v1
from app.api.version1.models.office_models import Office, all_offices

@v1.route('/createoffice', methods=['POST'])
def create_offices():
    office = request.get_json()
    office_type = ['type']
    office_name = ['name']
    
    new_office = {
        "type": office_type,
        "name": office_name
    }
    all_offices.append(office)
    Office.create_office(new_office)
    return make_response(jsonify({
        'message': 'Office added successfully'
    }), 200)

@v1.route('/offices', methods=['GET'])
def get_all_offices():
    
    return Office.get_office()

