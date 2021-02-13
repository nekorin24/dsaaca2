# Inheritance child class of ErrorwithMsg with parent class of exception
class ErrorWithMsg(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
