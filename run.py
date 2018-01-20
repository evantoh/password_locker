#!/usr/bin/env python3.6
from credentials import Credentials
from user import User

def register_user(name,password):
    '''
    Function that creates a new user
    '''
    new_user=User(name,password)

    return new_user
def save_users(user):
    '''
    function that saves a new user
    '''
    user.register()
def login_user(name,password):
    '''
    function to login
    '''
    loggedin=User.login_checker(name,password)
    return loggedin

def display_users():
    '''
    function that returns all the saved users
    '''
    return User.display_users()
def create_credentials(account,username,password,user):
    '''
    function to save a credentials
    '''
    cred=Credential(account,username,password,user)
    cred.save_credential()
    # Credential.save_credential(account,username,password,user)

def show_credentials():
    '''
    function to show all credentials for a specific user
    '''
    return Credential.cred_list
def password_gen(leng):
    '''
    generate passowrd
    arg:
        length of the passord
    '''
    import random
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    p =  "".join(random.sample(s,leng ))
    return p


def main():
    print('Hello! welcome to our password locker')
    while True:
        print('if you would like to register, use short code "reg" or if login use "log" ')
        print('\n')
        short_code=input().lower()
        if short_code=='reg':
            print('enter your new username')
            user_name=input()
            print('enter your new password')
            user_password=input()
            save_users(register_user(user_name,user_password))
            print('new user created')
        elif short_code=='show':
            if display_users():
                print('here is a list of all users')
                for user in display_users():
                    print('the users are '+f"{user.name}")
            else:
                print('\n')
                print('you dont have any users')

        elif short_code=='log':
            print('enter your username')
            user_name=input()
            print('enter your password')
            user_password=input()
            respnse=login_user(user_name,user_password)

            if respnse==False or respnse== None:
                print('wrong username or password')
            else:
                print('you are logged in. if you want to log out use short code"out"')
                print("-"*10)
                while True:
                    print('use shortcode "new" for adding a new credential "show" to show credentials if you want to log out use short code "out"')
                    print("-"*10)

                    short_code = input().lower()
                    if short_code=='new':
                        print("New credential")
                        print("-"*10)
                        print ("Account ....")
                        account = input()
                        print ("username ....")
                        user_name = input()
                        print('if you have a password use short_code "yes" if you want to create new use "gen"')
                        short_code = input().lower()
                        if short_code=='gen':
                            print('how long do you want the password to be')
                            print ("password length ....")
                            password_length = int(input())
                            password=password_gen(password_length)
                            print('this is the password  "'+ password+'"')
                            create_credentials(account,user_name,password,respnse)
                            print('credential saved successfully')
                            print("-"*10)
                        elif short_code=='yes':
                            print ("password ....")
                            password = input()
                            create_credentials(account,user_name,password,respnse)
                            print('credential saved successfully')


                    if short_code=='out':
                        break
                    if short_code=='show':
                        print('this are all your credentials')
                        print('\n')
                        cred_list=show_credentials()
                        for cred in cred_list:
                            if cred.user==respnse:
                                print('account: '+cred.account+' username: '+cred.username+' password: '+cred.password)
if __name__ == '__main__':

    main()