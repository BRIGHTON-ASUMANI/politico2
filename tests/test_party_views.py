import unittest # Importing the unittest module
import json
from app import create_app
from app.api.version1.models.party_models import Party, parties # Importing the party class


class TestParty(unittest.TestCase):
    '''
    Test class that defines test cases for the party class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        super().setUp()
        
        self.party = {
            "name": "odm",
            "hqAddress": "nairobi",
            "logoUrl":"www.image.com"
        }

    def tearDown(self):
        parties.clear()
    
    def test_create_party(self):
        '''
        method that tests create party.
        '''
        responses = self.client.post('/api/v1/parties', json = self.party)
        data = responses.get_json()

        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Party added successfully')
        self.assertEqual(responses.status_code, 201)

    def test_get_specific_party(self):
        '''
        method that tests create party.
        '''
        self.client.post('/api/v1/parties', json = self.party)
        
        responses = self.client.get('/api/v1/parties/1')
        data = responses.get_json()
        print(data)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(len(data['data']), 1)

        self.assertEqual(data['data'][0]['party_id'], 1)

        self.assertEqual(responses.status_code, 200)

    def test_get_parties(self):
        self.client.post('/api/v1/parties', json = self.party)
        responses = self.client.get('/api/v1/parties')
        data = responses.get_json()
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'All parties')
        
        


    # def test_get_specific_party(self):
    #     '''
    #     method that tests create party.
    #     '''
    #     self.client.post('/api/v1/parties', json = self.party)
        
    #     responses = self.client.get('/api/v1/parties/1')
    #     data = responses.get_json()
    #     print(data)
    #     self.assertEqual(data['status'], 200)
    #     self.assertEqual(data['message'], 'success')
    #     self.assertEqual(len(data['data']), 1)

    #     self.assertEqual(data['data'][0]['party_id'], 1)

    #     self.assertEqual(responses.status_code, 200)
    
        
    