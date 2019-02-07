offices =[]

class Office():
    '''
    Class that generates new instances of an office
    '''
    def __init__(self):
        self.all_offices = offices

    def get_offices(self):
        return self.all_offices

    def create_office(self, type, name):

        new_office = {
            "office_id": len(self.all_offices)+1,
            "name": name,
            "type": type,
        }

        self.all_offices.append(new_office)
        return self.all_offices
        

