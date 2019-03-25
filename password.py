

class Password:

    def __init__(self,password):
        self.pwd = password

    def check(self,test):
        return self.pwd == test
