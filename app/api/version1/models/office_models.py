from flask import make_response, jsonify

all_offices =[]

class Office:
    def __init__(self):
        pass

    @staticmethod
    def create_office(new_office):
        return make_response(jsonify(all_offices))

    @staticmethod
    def get_office():
        return make_response(jsonify(all_offices))


   