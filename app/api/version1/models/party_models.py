parties =[]

class Party():
   '''
    Class that generates new instances of a office
    '''
    def __init__(self):
        self.all_parties = parties
        '''
        __init__ method that helps us define properties for our objects.
        '''

    def get_parties(self):
        return self.all_parties

    def create_party(self, name, hqAddress, logoUrl):
        '''
         Args:
            name: New party first name.
            hqAddress : New party hqAddress.
            logoUrl: New party logoUrl
        '''

        new_party = {
            "party_id": len(self.all_parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        self.all_parties.append(new_party)
        return self.all_parties