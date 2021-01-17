array =  [['(', '3', '-', '5', '*', '10', ')']]
newerarray = array
def recursionExponential(array):
    for i in range(len(array)):
        if isinstance(array[i],list):
            array[i] = recursionExponential(array[i])
        if array[i] in ["**"]:
            if array[i+2] == ")" and array[i-2] == "(":
                pass
            else:
                newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                newarray = array[:(i-1)] + newarray + array[(i+2):]
                return recursionExponential(newarray)
    return array

def recursionMul(array):
    for i in range(len(array)):
        if isinstance(array[i],list):
            array[i] = recursionMul(array[i])
        if array[i] in ["*","/"]:
            if array[i+2] == ")" and array[i-2] == "(":
                pass
            else:
                newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                newarray = array[:(i-1)] + newarray + array[(i+2):]
                return recursionMul(newarray)
    return array
# print(recursionMul(recursionExponential(array)))

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
print(flatten(recursionMul(recursionExponential(array))))
# print(recursionMul(array))

                # print(newarray)
# for i in range(len(array)):
#     if array[i] in ["*","/"]:
#         if array[i+2] == ")" and array[i-2] == "(":
#             pass
#         else:
#             newarray = [["("] + array[(i-1):(i+2)] + [")"]]
#             newarray = array[:(i-1)] + newarray + array[(i+2):]
#             print(newarray)
    # else:
    #     newerarray.append()
