class Credentials:
    """
    class that creates a new credential(cred)
    """
    cred_list=[]

    def __init__(self, account,username,password,user):
        '''
        define the properties of the class
        '''
        self.account=account
        self.username=username
        self.password=password
        self.user=user

    def create_credential(self):
        '''
        method to create a credential
        '''


    def save_credential(self):
        '''
        method to save the credentials inputted
        '''
        
        Credential.cred_list.append(self)
        # return self.cred_list