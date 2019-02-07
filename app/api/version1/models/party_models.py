
parties =[]

class Party():
    def __init__(self):
        self.all_parties = parties

    def get_parties(self):
        return self.all_parties

    def create_party(self, name, hqAddress, logoUrl):

        new_party = {
            "party_id": len(self.all_parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        self.all_parties.append(new_party)
        return self.all_parties
        


