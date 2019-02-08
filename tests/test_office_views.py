import unittest # Importing the unittest module
import json
from manage import app
from app.api.version1.models.office_models import Office, offices # Importing the Office class


class TestOffice(unittest.TestCase):
    '''
    Test class that defines test cases for the office class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        super().setUp()
        
        self.office = {
            "name": "County",
            "type": "Governor"
        }
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        super().tearDown()
        offices.clear() # refresh all tests

    def test_create_office(self):
        '''
        method that tests create party.
        '''
        responses = self.client.post('/api/v1/offices', json = self.office)
        data = responses.get_json()

        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Office added successfully')
        self.assertEqual(responses.status_code, 201)


    def test_get_offices(self):
        responses = self.client.post('/api/v1/offices', json = self.office)
        
        
    


