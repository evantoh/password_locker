# class for the user
from credentials import Credentials

class User:
    """
    class that creates a new user
    """
    users_list=[]
    user_credentials=[]

    def __init__(self, name,password):
        '''
        define the properties of the class
        '''
        self.name=name
        self.password=password
        # self.credentials=dataCred

    def register(self):
        '''
        method that saves a new instance ie to register
        '''
        User.users_list.append(self)
    @classmethod
    def save_cred_user(cls,cred):
        '''
        method to save a credential for a user
        '''
        # writen_cred=Credential(cred[0],cred[1],cred[2])
        # cls.user_credentials.append(writen_cred.save_credential())
        # print(len(User.user_credentials))
        # account.user_credentials.append(cred)
        # self.new_cred.save_credential()
        # User.user_credentials.append(self)
    @classmethod
    def login_checker( cls,name,password):
        '''
        method that checks if the user is already registered (and then login)
        '''
        for user in User.users_list:
            if user.name==name and user.password==password:
                return user
        return False
    @classmethod
    def display_users(cls):
        return cls.users_list