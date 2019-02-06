
parties =[]

class Party:
    def __init__(self):
        pass

    @classmethod
    def get_parties(cls):
        return parties

    @classmethod
    def create_party(cls, party):
        parties.append(party)
        return parties