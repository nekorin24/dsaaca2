# string = "abcdefghijklmnop"
# i = 0
# while i < len(string):
#     # print(i)
#     if i == 2:
#         i = i + 1
#     print(string[i])
#     i += 1
# print([1,2,3,4,5,6][:3])
array = ['(', '3', '-', ['(', ['(', '5', '*', '10', ')'], '*', ['(', ['(', '3', '*', '3', ')'], '*', ['(', '5', '**', '3', ')'], ')'], ')'], ')']

# import collections

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
print(flatten(array))
# try:
#     array[2] in array[array[2]]
# except:
#     print("dsd")