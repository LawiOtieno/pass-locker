import unittest
from credentials import Credentials  # Import credentials class


class User:

    '''
    Class that generates new instances of user account
    '''

    user_list = []  # Empty user list

    def __init__(self, user_name, user_password):

        
        '''
        __init__ method to define the properties of a User object
        Args:
            user_name: Name of the user 
            user_password: Password of the user
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):

        '''
        Save user in user_list 
        '''

        User.user_list.append(self)

    
    
    # Find credentials of user
    @classmethod
    def find_credentials(cls, name):
        
        '''
        Checking for correct importation
        Args:
            name: Credential name
        Returns:
            Boolean: True or False
        '''

        # Search in the user list
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == name:
                return True

        return False

    
    
    # For User to login
    @classmethod
    def log_in(cls, name, password):

        '''
        Method for user to log into his/her account
        Args:
            name: name of user
            password: Associated user password
        Returns: 
            User credentials: If name & password match.
            False: If the name & password don't match
        '''

        # Search and compare user list
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.credentials_list

        return False

    
    # Returning user_list
    @classmethod
    def display_user(cls):
        
        '''
        Method that returns the user list
        '''

        return cls.user_list

    @classmethod
    def user_exists(cls, name):
        
        '''
        Method that checks if a user exists in the user_list
        Args:
            name: name of user to search 
        Returns:
            Boolean: true or false (If user exists or not)
        '''

        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False


if __name__ == '__main__':
    unittest.main()
