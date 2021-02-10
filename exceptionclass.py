class ErrorWithMsg(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

# someth = int(input("Enter number: "))
# try:
#     if someth < 0:
#         raise ErrorWithMsg("Negative Number")
#     elif someth >5:
#         raise ErrorWithMsg("Out of range")
#     else:
#         print(someth)
#     # raise ErrorWithCode(1000)
# except ErrorWithMsg as e:
#     print("Received error with message:", e.msg)