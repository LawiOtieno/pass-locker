from user import User
from credentials import Credentials

'''
running the application
'''


def create_user(name, password):
    '''
    Function that creates a user account
    Args
        name: user chosen name
        password: select password for account
    '''

    new_user = User(name, password)

    return new_user


def save_users(user):
    
    '''
    Function to save created user account
    Args
        user: user account to be saved
    '''


    user.save_user()


def check_existing_users(name):

    '''
    Function that checks existence of user account name
    Args:
        name : name of user account
    '''

    return User.user_exist(name)


def user_log_in(name, password):

    '''
    Function that allow users to login their credential account
    Args:
        name : name user used in creating user account
        password: password associated t with user account
    '''


    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)


def display_users():

    '''
    Function that returns all saved users 
    '''


    return User.display_user()


def create_credentails(user_name, name, password):

    '''
    Function to create a credential 
    Args:
        user_name: username for Password Locker
        name: name of the account 
        password: associated password for the account
    '''


    new_credentails = Credentials(user_name, name, password)

    return new_credentails


# def save_credentials(credentials):

#     '''
#     Function to save credentials
#     Args:
#         credentials: credentials to be saved
#     '''

#     credentials.save_credentials()


# def check_existing_credentials(name):

#     '''
#     Function that checks existence of user credentials
#     Args:
#         name: credentials name
#     '''

#     return Credentials.credentials_exists(name)


# def display_credentials(password):

#     '''
#     Function that returns all the saved credentials
#     '''

#     return Credentials.display_credentials(password)


# def create_generated_password(name):

#     '''
#     Function that generates a password for the user 
#     Args:
#         name : the name of the account
#     '''


#     password = Credentials.generated_password()

#     return password


# def find_credentials(credentials_name, credentials_password):
    
#     '''
#     Function to find credentials based on credentials name given
#     '''


#     return Credentials.find_credentials(credentials_name, credentials_password)


# def delete_credentials(name):
    
#     '''
#     Function to delete credentials
#     Args:
#         name: name of credentials
#     '''


#     Delete = Credentials.delete_credentials()


# # Main function
# def main():
    
#     '''
#     Function to run the password locker application
#     '''

#     while True:
        
#         '''
#         loop to running the entire application
#         '''


#         print("""Short Codes:
#         ca - Create Account: password Locker account \n
#         dn - Display names of users & details \n
#         log - Login your account \n
#         exp - Exit password locker account """)

        
        
#         # User types any short code and press enter key
#         short_code = input().lower()



#         ##ca - create account
#         if short_code == "ca":

#             '''
#             User Creates Account
#             '''


#             print("\n")
#             print(" New password locker account: ")
#             print("*"*15)

#             print("Write User name ...")
#             user_name = input()

#             print("Write password ...")
#             user_password = input()



#             # Creating and saving new user
#             save_users(create_user(user_name, user_password))

#             print("\n")
#             print(
#                 f"Welcome {user_name} \n Your account have been created successfully! \n")

        
        
        
        
#         ##dn - dispay name
#         elif short_code == "dn":
        
#             '''
#             Display names of users & details
#             '''

#             if display_users():
#                 print("\n")
#                 print("See list of current users & details below \n")
#                 print("*"*15)

#                 for user in display_users():
#                     print(f"{user.user_name}")
#                     print("*"*15)
#             else:
#                 print("\n")
#                 print("password locker does not have a user yet. \n  Would you be the first User?")
#                 print("\n")

        
        
#         ##log - login
#         elif short_code == "log":
#             """
#             code to allow user log into password locker
#             """
#             print("\n")
#             print("*"*15)
#             print("Login your Password Locker Account")
#             print("Enter username...")
#             user_name = input()

#             print("Enter password...")
#             user_password = input()

#             if user_log_in(user_name, user_password) == None:
#                 print("\n")
#                 print("Inputted username or password is invalid, try again or Create a New Account")
#                 print("\n")

#             else:

#                 user_log_in(user_name, user_password)
#                 print("\n")
#                 print(f"""Welcome {user_name} You have successfully logged into your Account\n 
                
#                 Use the following short codes for more...""")

#                 while True:

#                     '''
#                     loop for running functions after login login
#                     '''


#                     print(""" Short codes:
#                     ac - add credentials  \n
#                     dc - display credentials \n
#                     agc - autogenerate credentials password \n
#                     dlt - delete credentials \n
#                     ext - exit credentials """)

                    
                    
#                     # User inputted short codes
#                     short_code = input().lower()

                    
#                     #AC
#                     if short_code == "ac":

#                         '''
#                         Add new credentials
#                         '''


#                         print("\n")
#                         print("Add New Credentials...")
#                         print("*"*15)

#                         print("Name of credential ...")
#                         credentials_name = input()

#                         print("Password of credential ...")
#                         credentials_password = input()

                        
                        
#                         # Creating and saving new user credentials
#                         save_credentials(create_credentails(
#                             user_name, credentials_name, credentials_password))

#                         print("\n")
#                         print(
#                             f"Credentials for {credentials_name} have been saved successfully \n")
#                         print("\n")

                    
                    
#                     #DC - display credential
#                     elif short_code == "dc":
                        
#                         '''
#                         display credentials
#                         '''


#                         if display_credentials(user_name):
#                             print("\n")
#                             print(f"{user_name} credentials")
#                             print("*"*15)

#                             for credentials in display_credentials(user_name):
#                                 print(
#                                     f"Account:  {credentials.credentials_name}")
#                                 print(
#                                     f"Password:  {credentials.credentials_password}")
#                                 print("*"*15)

#                         else:
#                             print("\n")
#                             print("Sorry, no account found...")
#                             print("\n")

                    
                    
                    
#                     #AGC - aut generate credential
#                     elif short_code == "agc":
                        
#                         '''
#                         autogenerate credentials password
#                         '''


#                         print("\n")
#                         print("New Credentials...")
#                         print("*"*15)

#                         print("Name of credentials ...")
#                         credentials_name = input()

                        
#                         # Save created credential & generated password
#                         save_credentials(Credentials(
#                             user_name, credentials_name, (create_generated_password(credentials_name))))
#                         print("\n")
#                         print(
#                             f"Credentials for {credentials_name} have been created and saved successfully!")
#                         print("\n")

                    
                    
                    
#                     #DLT - delete
#                     elif short_code == "dlt":
#                         """
#                         delete credentials
#                         """
#                         print("Enter name of credential you no longer need...")
#                         credentials_name = input()

#                         print("Enter password for the above credentials...")
#                         credentials_password = input()

#                         if check_existing_credentials(credentials_name):
#                             delete_credentials_name = find_credentials(
#                                 credentials_name, credentials_password)
                            
#                             print(
#                                 f"Credentials for: {credentials_name} has been deleted Successfully. \n")
#                         else:
#                             print("No Credentials found!!!")

                    
                    
#                     #EXT - exit
#                     elif short_code == "ext":

#                         '''
#                         Exit password locker account
#                         '''


#                         print(
#                             f"{user_name}, you have exited Password Locker. \n  Login again...")
#                         print("\n")
#                         break

#                     else:
#                         print("\n")
#                         print(f""" {short_code} seems to be incorrect. \n 
#                         please use the short codes provided""")
#                         print("\n")
        
        
#         ##exp - exit password
#         elif short_code == "exp":
#             """
#             Exiting password locker
#             """
#             print("\n")
#             print("Goodbye, you are out...")

#             break

#         else:
#             print("\n")
#             print(f""" Invalid entry please check {short_code}? 
#             Please, use correct code """)
#             print("\n")


# if __name__ == '__main__':
#     main()