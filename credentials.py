class Credentials:
    cred_list = [] # Empty credentials to store objects list

    def __init__(self,account_name,user_name,password,user):
            """
            Class that generates new instances of credentials.
            """

            self.account_name = account_name
            self.user_name = user_name
            self.password = password
            self.user = user