class expressionValidator:
    def __init__(self, original_exp):
        self.original_exp = original_exp
        self.exp = self.original_exp
        self.array = []
        self.open_brackets = 0
        self.close_brackets = 0
        self.i = 0
        self.condition = {
    "(": ["0","1","2","3","4","5","6","7","8","9",".", "-","("],
    ")": ["+","-","/","*",")"],
    "+": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "-": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "*": ["0","1","2","3","4","5","6","7","8","9",".","(","*","-"],
    "/": ["0","1","2","3","4","5","6","7","8","9",".","(",'-'],
    "int": ["0","1","2","3","4","5","6","7","8","9",".","-","+","*","/",")"],
    ".":["0","1","2","3","4","5","6","7","8","9"]
    }
    def remove_spaces(self,exp):
        exp = exp.replace(" ","")
        return exp
    
    def checkInteger(self,value):
        try:
            int(value)
            return True
        except:
            return False
    def decimalStop(self,value):
        return value == "."
    
    def getIntegerOrDecimalValue(self, exp, i,output):
        output = output
        no_comma = True
        x = i
        # if exp[x] == ".":
        if self.decimalStop(exp[x]):
            no_comma = False
        while x < len(exp):
            # if exp[x+1] in ["0","1","2","3","4","5","6","7","8","9"]:
            if self.checkInteger(exp[x+1]):
                output += str(exp[x+1])
            # elif exp[x+1] == ".":
            elif self.decimalStop(exp[x+1]):
                if no_comma == True:
                    output += "."
                    no_comma = False
                else:
                    print("Invalid Input after full stop")
                    break
            else:
                if exp[x+1] == (i + 1):
                    print("Invalid Input")
                    break
                break
            x += 1
        # array.append(output)
        i = x
        self.i = i
        return output
    def checkCondition(self,exp, index):
        return exp[index + 1] in self.condition[exp[index]]
    
    def appendtoArray(self, value):
        self.array.append(value)
    
    def checkOperators(self,value):
        return value in ["-","+","*","/",")","("]

    def checkAllValid(self,value):
        return self.checkInteger(value) or self.decimalStop(value) or self.checkOperators(value)

    def recursionExponential(self,array):
        for i in range(len(array)):
            if isinstance(array[i],list):
                array[i] = self.recursionExponential(array[i])
            if array[i] in ["**"]:
                if array[i+2] == ")" and array[i-2] == "(":
                    pass
                else:
                    newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                    newarray = array[:(i-1)] + newarray + array[(i+2):]
                    return self.recursionExponential(newarray)
        return array

    def recursionMul(self,array):
        for i in range(len(array)):
            if isinstance(array[i],list):
                array[i] = self.recursionMul(array[i])
            if array[i] in ["*","/"]:
                if array[i+2] == ")" and array[i-2] == "(":
                    pass
                else:
                    newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                    newarray = array[:(i-1)] + newarray + array[(i+2):]
                    return self.recursionMul(newarray)
        return array


    def flatten(self,S):
        if S == []:
            return S
        if isinstance(S[0], list):
            return self.flatten(S[0]) + self.flatten(S[1:])
        return S[:1] + self.flatten(S[1:])

    def recursiveFunction(self):
        self.exp = self.remove_spaces(self.exp)
        index = self.exp[self.i]
        if self.i == 0:
            output = []
        else:
            output = ["("]
        while self.i < len(self.exp):
            # if index == "(":
            #     self.i += 1
            #     output.append(self.recursiveFunction())
            # if index == ")":
            #     self.i += 1
            #     output.append(")")
            #     return output
            print(output)
            print(self.i)
            index = self.exp[self.i]
            if index != " ":
                if self.checkAllValid(index):
                    # If it is an integer
                    if self.checkInteger(index):
                        # Check if next character is a decimal point or integer
                        if self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1]):
                            output.append(self.getIntegerOrDecimalValue(self.exp,self.i,str(self.exp[self.i])))
                        # else it is just one character
                        else:
                            output.append(index)
                    # If it is not an integer
                    else:
                        # print(self.exp[self.i + 1] in self.condition[self.i])
                        try:
                            # if self.exp[self.i + 1] in self.condition[self.i]:\
                            if self.checkCondition(self.exp,self.i):
                                # print(index)
                                # print("someth")
                                if index == "(":
                                    self.i += 1
                                    output.append(self.recursiveFunction())
                                elif index == ")":
                                    # self.i += 1
                                    output.append(")")
                                    return output
                                elif index == "+":
                                    if self.exp[self.i+1] == "-" or self.exp[self.i+1] == "+":
                                        pass
                                    else:
                                        output.append(index)
                                elif index == "-":
                                    # If another negative in front of negative
                                    if self.exp[self.i+1] == "-":
                                        # Switch to + sign at next character
                                        self.exp = self.exp[:(self.i+1)] + "+" + self.exp[(self.i+2):]
                                    # If it is a plus sign in front of negative sign
                                    elif self.exp[self.i+1] == "+":
                                        # Switch to - sign at next character
                                        self.exp = self.exp[:(self.i+1)] + "-" + self.exp[(self.i+2):]
                                    # If its an integer after negative
                                    elif (self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1])) and (self.exp[self.i-1] in ["(","*","/"]):
                                        output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"-"))
                                    else:
                                        output.append(index)
                                elif index == "*":
                                    if self.exp[self.i+1] == "*":
                                        if (self.checkInteger(self.exp[self.i+2]) or self.decimalStop(self.exp[self.i+2]) or self.exp[self.i+2] == "-"):
                                            output.append("**")
                                            self.i +=1
                                        else:
                                            print("Invalid input after exponential")
                                            break
                                    else:
                                        output.append(index)
                                elif index == ".":
                                    output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"0."))
                                
                                elif index == "(":
                                    self.open_brackets += 1
                                    # output.append(index)
                                # If equals to close bracket increment
                                elif index == ")":
                                    self.close_brackets += 1
                                    # output.append(index)
                                else:
                                    output.append(index)

                            # If not valid character error
                            else:
                                # print(index)
                                # print(i)
                                print("Invalid Input after character")
                                # print("Error at Character: " + str(exp[i:i+2]))
                                break
                        # Last index
                        except:
                            if index == ")":
                                self.close_brackets += 1
                                # output.append(index)
                                    # self.i += 1
                                output.append(")")
                                return output
                            else:
                                try:
                                    int(index)
                                    output.append(index)
                                except:
                                    print("Incorrect input")
                                    break
                else:
                    print("Invalid Character used")
                    break
            self.i += 1
        return output
    def runEntirePrograme(self):
        return self.flatten(self.recursionMul(self.recursionExponential(self.recursiveFunction())))


    
# expClass = expressionValidator("( -3 / 3 ** 5 + (5**2) -- (4**-2.5))")
expClass = expressionValidator("(3+3)")
print(expClass.runEntirePrograme())



# output = expClass.recursiveFunction()
# if output == None:
#     print("\nInput again")
# else:
#     print("\nThank you for your Input")
# print(output)
# def recursionExponential(array):
#     for i in range(len(array)):
#         if isinstance(array[i],list):
#             array[i] = recursionExponential(array[i])
#         if array[i] in ["**"]:
#             if array[i+2] == ")" and array[i-2] == "(":
#                 pass
#             else:
#                 newarray = [["("] + array[(i-1):(i+2)] + [")"]]
#                 newarray = array[:(i-1)] + newarray + array[(i+2):]
#                 return recursionExponential(newarray)
#     return array

# def recursionMul(array):
#     for i in range(len(array)):
#         if isinstance(array[i],list):
#             array[i] = recursionMul(array[i])
#         if array[i] in ["*","/"]:
#             if array[i+2] == ")" and array[i-2] == "(":
#                 pass
#             else:
#                 newarray = [["("] + array[(i-1):(i+2)] + [")"]]
#                 newarray = array[:(i-1)] + newarray + array[(i+2):]
#                 return recursionMul(newarray)
#     return array


# def flatten(S):
#     if S == []:
#         return S
#     if isinstance(S[0], list):
#         return flatten(S[0]) + flatten(S[1:])
#     return S[:1] + flatten(S[1:])
# print(flatten(recursionMul(recursionExponential(output))))

# print(expClass.checkInteger("3"))
