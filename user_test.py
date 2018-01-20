import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    class to test the functionality of user class
    '''
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.the_user=User('evans','password')
        self.the_user1=User('mwenda','123')
    def tearDown(self):
        User.users_list=[]
        Credential.cred_list=[]
    def test_init(self):
        '''
        test case to test if the object is initialized
        '''
        self.assertEqual(self.the_user.name,'evans')
        self.assertEqual(self.the_user.password,'password')
