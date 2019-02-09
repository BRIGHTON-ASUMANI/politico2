import unittest # Importing the unittest module
import json
from app import create_app
from app.api.version1.models.party_models import Party, parties # Importing the Office class


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
        
        self.office = {
            "name": "odm",
            "hqAddress": "nairobi",
            "logoUrl":"image"
        }
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        super().tearDown()
        parties.clear() # refresh all tests

    def test_create_party(self):
        '''
        method that tests create office.
        '''
        responses = self.client.post('/api/v1/parties', json = self.office)
        data = responses.get_json()

        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Party added successfully')
        self.assertEqual(responses.status_code, 201)

    def test_get_parties(self):
        responses = self.client.post('/api/v1/parties', json = self.office)
        
        
    