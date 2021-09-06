# import unittest
# from random import choice
# import string


# '''
# Credentials class to create instances of the user credentials
# '''


# class Credentials:
    
#     '''
#     class that generates instances of credentials for the user
#     '''


    
#     credentials_list = []  # Empty credentials_list


#     def __init__(self, user_name, credentials_name, credentials_password):
        
#         '''
#         __init__ method to  specify the attributes of a User object
#         Args:
#             user_name: user name
#             credentials_name: name of the credentials acccount
#             credentials_password: associated user password
#         '''


#         self.user_name = user_name
#         self.credentials_name = credentials_name
#         self.credentials_password = credentials_password

#     def save_credentials(self):
#         """
#         method that help to save the user credentials in credentials_list
#         """
#         Credentials.credentials_list.append(self)
    
    
    
    
#     # Generating password for the user

#     @classmethod
#     def generated_password(cls):
        
#         '''
#         Method to generate random characters password for user 

#         '''


        
#         # Length of password to be generated
#         pass_length = 15

#         # Random charactors to choose
#         characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

#         # Generate complete password
#         password = "".join(choice(characters) for num in range(pass_length))

#         return password

        

#     # Method to display the user credentials
#     @classmethod
#     def display_credentials(cls, user_name):
        
#         '''
#         Method that  returns credentials_list
#         Args:credentials_email: the email of the credentials account
#             password: user password
#         '''


#         user_credentials_list = []

#         for credentials in cls.credentials_list:
#             if credentials.user_name == user_name:
#                 user_credentials_list.append(credentials)

#         return user_credentials_list

    
    
#     @classmethod
#     def credentials_exists(cls, credentials_name):
        
#         '''
#         Method to check if credentials exists
#         Args
#             name: name of credentials to be searched
#         Returns:
#             Boolean: True or False
#         '''



#         for credentials in cls.credentials_list:
#             if credentials.credentials_name == credentials_name:
#                 return True

#         return False

    
    
#     # Method to find credentials
#     @classmethod
#     def find_credentials(cls, credentials_name, credentials_password):
        
#         '''
#         Method that takes in credentials name and returns the credentials saved.
#         Args
#             name: name of the platform e.g Twitter
#         Returns :
#             credentials name & password.
#         '''



#         # Checking credentials if match
#         for credentials in cls.credentials_list:
#             if credentials_name == credentials_name and credentials_password == credentials_password:
#                 return credentials

    
    
#     # Deleting credentials
#     @classmethod
#     def delete_credentials(credentials_name, credentials_password):
    
#         '''
#         Method that deletes user credentials
#         '''


#         Credentials.credentials_list.remove()


# if __name__ == '__main__':
#     unittest.main()