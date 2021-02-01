class expressionValidator:
    def __init__(self, original_exp):
        self.original_exp = original_exp
        self.exp = self.original_exp
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
    def isEmpty(self, exp):
        return exp == ""

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

    def checkIntegerCondition(self,exp,index):
        return exp[index + 1] in self.condition["int"]
    
    # def checkSymbols(self, exp):
    #     return exp in ["-","+","*","/"]

    def checkOperators(self,value):
        return value in ["-","+","*","/",")","("]

    def checkAllValid(self,value):
        return self.checkInteger(value) or self.decimalStop(value) or self.checkOperators(value)
    
    def checkParenthesis(self,exp):
        try:
            return (exp[0] == "(" and exp[-1] == ")")
        except:
            return False
    # def recursionExponential(self,array):
    #     for i in range(len(array)):
    #         if isinstance(array[i],list):
    #             array[i] = self.recursionExponential(array[i])
    #         if array[i] in ["**"]:
    #             if array[i+2] == ")" and array[i-2] == "(":
    #                 pass
    #             else:
    #                 newarray = [["("] + array[(i-1):(i+2)] + [")"]]
    #                 newarray = array[:(i-1)] + newarray + array[(i+2):]
    #                 return self.recursionExponential(newarray)
    #     return array

    # def recursionMul(self,array):
    #     for i in range(len(array)):
    #         if isinstance(array[i],list):
    #             array[i] = self.recursionMul(array[i])
    #         if array[i] in ["*","/"]:
    #             if array[i+2] == ")" and array[i-2] == "(":
    #                 pass
    #             else:
    #                 newarray = [["("] + array[(i-1):(i+2)] + [")"]]
    #                 newarray = array[:(i-1)] + newarray + array[(i+2):]
    #                 return self.recursionMul(newarray)
    #     return array
    # def recursionAdd(self,array):
    #     for i in range(len(array)):
    #         if isinstance(array[i],list):
    #             array[i] = self.recursionAdd(array[i])
    #         if array[i] in ["+","-"]:
    #             if array[i+2] == ")" and array[i-2] == "(":
    #                 pass
    #             else:
    #                 newarray = [["("] + array[(i-1):(i+2)] + [")"]]
    #                 newarray = array[:(i-1)] + newarray + array[(i+2):]
    #                 return self.recursionAdd(newarray)
    #     return array

    def recursionFunction(self,array,condition):
        if len(condition) == 0:
            return array
        for i in range(len(array)):
            if isinstance(array[i],list):
                array[i] = self.recursionFunction(array[i],condition)
            if array[i] in condition[0]:
                if array[i+2] == ")" and array[i-2] == "(":
                    pass
                else:
                    newarray = [["("] + array[(i-1):(i+2)] + [")"]]
                    newarray = array[:(i-1)] + newarray + array[(i+2):]
                    return self.recursionFunction(newarray,condition)
            # Validating examples (3), ((3))
            elif i == (len(array) -2):
                if array[i+1] == ")" and array[i-1] == "(":
                    newarray = [array[i]]
                    return self.recursionFunction(newarray,condition)
                # return array[i]
        return self.recursionFunction(array,condition[1:])

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
        if self.isEmpty(self.exp):
            return None
        while self.i < len(self.exp):
            index = self.exp[self.i]
            if index != " ":
                if self.checkAllValid(index):
                    # If it is not an integer
                    try:
                        if self.checkInteger(index):
                            if self.checkIntegerCondition(self.exp, self.i):
                                if self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1]):
                                    output.append(self.getIntegerOrDecimalValue(self.exp,self.i,str(self.exp[self.i])))
                                # else it is just one character
                                else:
                                    output.append(index)
                            else:
                                print("Invalid Input after integer")
                                return None
                        else:
                            if self.checkCondition(self.exp,self.i):
                                if index == "(":
                                    self.i += 1
                                    self.open_brackets += 1
                                    callback = self.recursiveFunction()
                                    if callback == None:
                                        return None
                                    else:
                                        output.append(callback)
                                    # output.append(self.recursiveFunction())
                                elif index == ")":
                                    # self.i += 1
                                    self.close_brackets += 1
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
                                        if self.exp[self.i-1] in ["(","*","/"]:
                                            self.exp = self.exp[:(self.i)] + self.exp[(self.i+2):]
                                            self.i -= 1
                                            print(self.exp)
                                            print(self.exp[self.i+1])
                                            if not self.checkCondition(self.exp,self.i):
                                                print("Invalid")
                                                return None
                                            print(self.exp[self.i])
                                        else:
                                            self.exp = self.exp[:(self.i+1)] + "+" + self.exp[(self.i+2):]
                                    # If it is a plus sign in front of negative sign
                                    elif self.exp[self.i+1] == "+":
                                        # Switch to - sign at next character
                                        print("yes")
                                        if (self.exp[self.i-1] in ["(","*","/"]):
                                            self.exp = self.exp[:(self.i)] + self.exp[(self.i+2):]
                                            print(self.exp)
                                            self.i -=1
                                        else:
                                            self.exp = self.exp[:(self.i+1)] + "+" + self.exp[(self.i+2):]
                                    # If its an integer after negative
                                    # elif (self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1])) and (self.exp[self.i-1] in ["(","*","/"]):
                                    elif (self.exp[self.i-1] in ["(","*","/"]):
                                        if self.checkInteger(self.exp[self.i+1]):
                                            output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"-"))
                                        elif self.decimalStop(self.exp[self.i+1]):
                                            output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"-0"))
                                    else:
                                        output.append(index)
                                elif index == "*":
                                    if self.exp[self.i+1] == "*":
                                        if (self.checkInteger(self.exp[self.i+2]) or self.decimalStop(self.exp[self.i+2]) or self.exp[self.i+2] == "-"):
                                            output.append("**")
                                            self.i +=1
                                        else:
                                            print("Invalid input after exponential")
                                            return None
                                    else:
                                        output.append(index)
                                elif index == ".":
                                    output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"0."))
                            
                                else:
                                    output.append(index)

                            # If not valid character error
                            else:
                                print("Invalid Input after character")
                                # print("Error at Character: " + str(exp[i:i+2]))
                                return None
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
                                return None
                else:
                    print("Invalid Character used")
                    return None
            self.i += 1
        if self.open_brackets != self.close_brackets:
            print("Number of brackets does not match")
            return None
        return output
    def runEntirePrograme(self):
        if self.checkParenthesis(self.exp):
            output = self.recursiveFunction()
            if output == None:
                return None
            else:
                # return self.flatten(self.recursionAdd(self.recursionMul(self.recursionExponential(output))))
                # return self.recursionFunction(output,[["**"],["*","/"],["+","-"]])
                return self.flatten(self.recursionFunction(output,[["**"],["*","/"],["+","-"]]))
        elif self.isEmpty(self.exp):
            print("Missing expression! Please try again!")
            return None
        else:
            print("Not enclosed with parenthesis")
            return None


    
expClass = expressionValidator("( -3 / 3 ** 5 + (5**2) -- (4**---+-2.5))")
# expClass = expressionValidator("(-5 + 3 * (5 - (---+10.5)) / (2))")
# expClass = expressionValidator("(---+-5)")
# output = input("Expression: ")
# expClass = expressionValidator(output)
print(expClass.runEntirePrograme())
# expClass.runEntirePrograme()



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
