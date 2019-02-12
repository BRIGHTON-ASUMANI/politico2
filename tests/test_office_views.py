import unittest # Importing the unittest module
import json

from app import create_app
from app.api.version1.models.office_models import Office, offices # Importing the Office class


class TestOffice(unittest.TestCase):
    '''
    Test class that defines test cases for the office class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.app = create_app('testing')
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
        method that tests create office.
        '''
        responses = self.client.post('/api/v1/offices', json = self.office)
        data = responses.get_json()

        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Office added successfully')
        self.assertEqual(responses.status_code, 201)


    def test_get_offices(self):
        self.client.post('/api/v1/offices', json = self.office)
        responses = self.client.get('/api/v1/offices')
        data = responses.get_json()
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'All offices')


    def test_get_specific_office(self):
        '''
        method that tests create office.
        '''
        self.client.post('/api/v1/offices', json = self.office)
        
        responses = self.client.get('/api/v1/offices/1')
        data = responses.get_json()
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(len(data['data']), 1)

        self.assertEqual(data['data'][0]['office_id'], 1)

        self.assertEqual(responses.status_code, 200)

    def test_get_all_offices(self):
        '''
        tests for getting all offices
        '''
        self.client.post('/api/v1/offices', json = self.office)
        responses = self.client.get('/api/v1/offices')
        data = responses.get_json()
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'All offices')
        
        
    


