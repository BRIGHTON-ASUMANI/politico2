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
            name: New party name.
            hqAddress : New party hqAddress.
            logoUrl: New party logoUrl
        '''

        new_party = {
            "party_id": len(self.all_parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }

        self.all_parties.append(new_party)
        return self.all_parties

    def get_specific_party(self, party_id):
        '''
         Args:
            party_id: specific id of a party.
            
        '''
        if self.all_parties:
            for spec_party in self.all_parties:
                if spec_party.get('party_id') == party_id:

                    return spec_party
    def delete_party(self, party_id):
        for party in parties:
            if party['party_id'] == party_id:
                parties.remove(party)
   