import unittest
from credentials import Credentials


class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credentials("facebook","evans","evans123","evantoh") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_cred.account_name,"facebook")
        self.assertEqual(self.new_cred.user_name,"evans")
        self.assertEqual(self.new_cred.password,"evans123")
        self.assertEqual(self.new_cred.user,"evantoh")


if __name__ == '__main__':
    unittest.main()