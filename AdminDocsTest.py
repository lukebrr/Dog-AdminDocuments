
import os
import unittest
import DocAdministration
import pytest

class DocAdminTest(unittest.TestCase):

    def setUp(self):
        DocAdministration.app.testing = True
        self.app = DocAdministration.app.test_client()

    def tearDown(self):
		pass

    def test_add(self):
        response = self.app.post('/api/v1/add', data=dict (
                    data = '1234abcd',
                    s3id = '1234abcd',
                    handlerid = '1234abcd',
                    dogid = '1234abcd',
                    status = 'processed',
                    vacc1 = 'heart worm',
                    vacc2 = 'rabies',
                    vacc3 = 'dog flu',
                    vacc4 = 'ring worm'
                    ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'processed', response.data)
        self.assertIn(b'Heart Worm', response.data)
        self.assertIn(b'Rabies', response.data)
        self.assertIn(b'Dog Flu', response.data)
        self.assertIn(b'Ringworm', response.data) 

    def test_changestatus(self):
        parameters = {"dogid" : "status" }
        response = self.app.get('/api/v1/changestatus', follow_redirects=True, data = parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'processed', response.data)

    def test_deldocument(self):
        parameters = {"s3id" : "s3id"}
        response = self.app.delete('/api/v1/deldocument', follow_redirects=True, data=parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SUCCESS', response.data)

    def test_searchbystatus(self):
        parameters = {"s3id", "handlerid", "dogid", "status", "vacc1", "vacc2", "vacc3", "vacc4"}
        response = self.app.get('/api/v1/searchbystatus', follow_redirects=True, data = parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'1234', response.data)
        self.assertIn(b'processed', response.data)
        self.assertIn(b'Heart Worm', response.data)
        self.assertIn(b'Rabies', response.data)
        self.assertIn(b'Dog Flu', response.data)
        self.assertIn(b'Ringworm', response.data)
 
    def test_searchhandler(self):
        parameters = {"handlerid" : "handlerid"}
        response = self.app.get('/api/v1/searchbyhandlerid', follow_redirects=True, data = parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1234', response.data)
		
    def test_searchdog(self):
        parameters = {"dogid" : "dogid"}
        response = self.app.get('/api/v1/searchbydogid', follow_redirects=True, data = parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1234', response.data)

# Method	Equivalent to
# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)
# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.

if __name__ == '__main__':
    unittest.main()
