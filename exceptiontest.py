# class CommaException(Exception):
#     # raise MyException("My hovercraft is full of eels")
#     pass
# try:
#     print(1/0)
# except:
#     print(CommaException("My hovercraft is full of eels"))
#     # print("dsd")
class ErrorWithCode(Exception):
    def __init__(self, code):
        self.code = code
    def __str__(self):
        return repr(self.code)

someth = int(input("Enter number: "))
try:
    if someth < 0:
        raise ErrorWithCode(1000)
    elif someth >5:
        raise ErrorWithCode(5000)
    else:
        print(someth)
    # raise ErrorWithCode(1000)
except ErrorWithCode as e:
    print("Received error with code:", e.code)