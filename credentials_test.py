import unittest  # Import unittest module
from credentials import Credentials  # Import Credentials  class


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials module
    Args:
        unittest.TestCase: test class, help create test cases for the application
    '''



    def setUp(self):
        
        '''
        setUp() method that will run before each test case
        '''


        # Creating credentials object
        self.new_credentials = Credentials("LawiOtieno", "twitter", "lawi@gm")

    def tearDown(self):

        '''
        tearDown() method to clean-up after every test case is run
        '''


        Credentials.credentials_list = []

    def test_init(self):
        
        '''
        TestCase: test to see whether object is properly initialized
        '''

        
        self.assertEqual(self.new_credentials.user_name, "LawiOtieno")
        self.assertEqual(self.new_credentials.credentials_name, "twitter")
        self.assertEqual(self.new_credentials.credentials_password, "lawi@gm")

    def test_save_credentials(self):
        
        '''
        Test to see whether user is saved to user_list
        '''


        self.new_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        
        '''
        TestCase: check to see if multiple credentials can be saved to credentials list
        '''


        generated_password = self.new_credentials.generated_password()

        self.assertEqual(len(generated_password), 15)

    def test_display_credentials(self):
        
        '''
        Test to see if user can list all saved credentials
        '''

        # Saving new credentials
        self.new_credentials.save_credentials()

        test_credentials = Credentials("matthew", "sam", "mrk24")

        test_credentials.save_credentials()

        test_credentials = Credentials("matthew", "john", "cate")

        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.display_credentials("matthew")), 2)

    def test_credentials_exist(self):
    
        '''
        Test to check if we can return boolean for credentials not found
        '''


        self.new_credentials.save_credentials()

        test_credentials = Credentials(
            "matthew", "sam", "mrk24")  # new credentials

        test_credentials.save_credentials()

        # Use of contact exist method
        credentials_exists = Credentials.credentials_exists("sam")

        self.assertTrue(credentials_exists)

    def test_find_credentials(self):
        
        '''
        Test to check if we can find credentials by name and display information
        '''


        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "mercy", "twitter", "twitter254")  # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_credentials("twitter", "facebook")

        self.assertEqual(found_credentials.credentials_name,
                         test_credentials.credentials_name)


if __name__ == '__main__':
    unittest.main()