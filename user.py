class User:
    """
    class that creates a new user
    """
    users_list=[]
    user_credentials=[]

def __init__(self, name,password):
    self.name = name
    self.password = password
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