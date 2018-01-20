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
        self.new_user = User("evans","password")
        self.new_user1= User("mwenda","123")
     
    def tearDown(self):
        User.users_list=[]
        Credential.cred_list=[]
    def test_init(self):
        '''
        test case to test if the object is initialized
        '''
        self.assertEqual(self.new_user.name,'evans')
        self.assertEqual(self.new_user.password,'password')

    def test_register(self):
        '''
        test if the user is saved
        '''
        self.the_user.register()
        self.assertEqual(len(User.users_list),1)
    def test_login_checker(self):
        '''
        test if you can login you input the username and passord and returns true
        args:
            name: the username
        '''
        self.new_user.register()
        self.new_user1.register()

        to_login=User.login_checker('evans','password')
        # self.assertTrue(to_login)
        self.assertEqual(to_login,self.new_user)
      
    def test_login(self):
        '''
        test case, given a username should more or less login--to be implemented--
        '''

    def test_display_all_users(self):
        '''
        test case that tests if users list is returned
        '''
        self.new_user.register()
        self.assertEqual(len(User.display_users()),1)

    def test_create_credentials(self):
        '''
        test case to create a credential within a user instance(account)
        '''
        self.new_user.register()
        self.new_user1.register()
        to_login=User.login_checker('123','password')
        self.new_cred=Credential('facebook','evanmwenda@gmail.com','123',to_login)
        self.new_cred.save_credential()
        self.assertEqual(len(Credential.cred_list),1)

    def test_save_credentials(self):
        '''
        test case to check if the credential saved belong to a particular user
        '''
        self.new_user.register()
        to_login=User.login_checker('evans','password')
        self.new_cred=Credential('facebook','evanmwenda@gmail.com','123',to_login)
        self.new_cred.save_credential()
        print(len(Credential.cred_list))
        self.assertEqual(self.new_cred.account,'facebook')
        for cred in Credential.cred_list:
            print(cred.user)

        self.assertEqual(Credential.cred_list[0].user,to_login)

   
if __name__=='__main__':
    unittest.main() 
