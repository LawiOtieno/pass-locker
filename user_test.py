import unittest
from user import User
from credentials import Credentials


class TestUser(unittest.TestCase):
    
    '''
    Test class that tests cases for the User class
    Args:
        unittest.Testcase: class that helps create test cases
    '''

    def setUp(self):
        
        '''
        setUp() method to run before each test case
        '''

        # Create user object
        self.new_user = User("LawiOtieno", "Lawi4321")

    def tearDown(self):
        
        '''
        Method to clean-up after each test
        '''


        User.user_list = []

    def test_init(self):
        
        '''
        Testing if object is properly initialized
        '''

        self.assertEqual(self.new_user.user_name, "LawiOtieno")
        self.assertEqual(self.new_user.user_password, "Lawi4321")

    def test_log_in(self):
        

        '''
        Test to establish whether user can login
        '''


        # First save user
        self.new_user.save_user()

        test_user = User("terry", "larry")

        test_user.save_user()

        found_credentials = User.log_in("terry", "larry")


        self.assertEqual(found_credentials, Credentials.credentials_list)



    def test_user_exists(self):
        
        '''
        Test to return boolean if user does not exist
        '''



        # First, saving user
        self.new_user.save_user()

        test_user = User("LawiOtieno", "Lawi4321")

        test_user.save_user()

        # If user exists
        user_exists = User.user_exists("LawiOtieno")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main(verbosity = 2)