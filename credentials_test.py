import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    class to test the functionality of credential class
    '''
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_cred=Credential('facebook','david@gmail.com','123qwerty','david')
        # self.the_user1=User('njoroge','drowssap')


    def tearDown(self):
        Credential.cred_list=[]

    def test_init(self):
        '''
        test case to test if the credential is initialized
        '''
        self.assertEqual(self.new_cred.account,'facebook')
        self.assertEqual(self.new_cred.username,'david@gmail.com')
        self.assertEqual(self.new_cred.password,'123qwerty')

    def test_save(self):
        '''
        test if the credential is saved
        '''
        self.new_cred.save_credential()
        self.assertEqual(len(Credential.cred_list),1)
        # self.assertEqual(Credential.cred_list.account,1)



if __name__=='__main__':
    unittest.main()