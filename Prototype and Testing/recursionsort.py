array =  [['(', '3', '-', '5', '*', '10', ')']]
newerarray = array
def recursive_exponential(array):
    for i in range(len(array)):
        if isinstance(array[i],list):
            array[i] = recursive_exponential(array[i])
        if array[i] in ["**"]:
            if array[i+2] == ")" and array[i-2] == "(":
                pass
            else:
                newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                newarray = array[:(i-1)] + newarray + array[(i+2):]
                return recursive_exponential(newarray)
    return array

def recursive_mul(array):
    for i in range(len(array)):
        if isinstance(array[i],list):
            array[i] = recursive_mul(array[i])
        if array[i] in ["*","/"]:
            if array[i+2] == ")" and array[i-2] == "(":
                pass
            else:
                newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                newarray = array[:(i-1)] + newarray + array[(i+2):]
                return recursive_mul(newarray)
    return array
# print(recursive_mul(recursive_exponential(array)))

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
print(flatten(recursive_mul(recursive_exponential(array))))
# print(recursive_mul(array))

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
