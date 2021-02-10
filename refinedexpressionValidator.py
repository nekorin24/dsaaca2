from exceptionclass import ErrorWithMsg

class expressionValidator:
    def __init__(self, original_exp):
        self.original_exp = original_exp
        self.exp = self.original_exp
        self.open_brackets = 0
        self.close_brackets = 0
        self.i = 0
        self.condition = {
    "(": ["0","1","2","3","4","5","6","7","8","9",".", "-","(","+"],
    ")": ["+","-","/","*",")"],
    "+": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "-": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "*": ["0","1","2","3","4","5","6","7","8","9",".","(","*","-","+"],
    "/": ["0","1","2","3","4","5","6","7","8","9",".","(",'-',"+"],
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
                    # print("Invalid Input after full stop")
                    # break
                    raise ErrorWithMsg("Invalid Input after full stop")
            else:
                if exp[x+1] == (i + 1):
                    # print("Invalid Input")
                    # break
                    raise ErrorWithMsg("Invalid Input")
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
        # Remove all of the spaces of the expression
        self.exp = self.remove_spaces(self.exp)
        # Get current index of the expression
        index = self.exp[self.i]
        if self.i == 0:
            output = []
        else:
            output = ["("]
        # If there is no input return None
        if self.isEmpty(self.exp):
            return None
        while self.i < len(self.exp):
            index = self.exp[self.i]
            # print(self.exp)
            # print(index)
            if index != " ":
                # Check if current character is a valid character
                if self.checkAllValid(index):
                    # If it is not an integer
                    # Check if its an integer
                    if self.i < len(self.exp)-1:
                        if self.checkInteger(index):
                            # Check if character after integer is valid
                            if self.checkIntegerCondition(self.exp, self.i):
                                # If its an integer or decimal after integer
                                if self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1]):
                                    # Get whole number or decimal value
                                    output.append(self.getIntegerOrDecimalValue(self.exp,self.i,str(self.exp[self.i])))
                                # else it is just one character
                                else:
                                    output.append(index)
                            # Invalid Input after integer
                            else:
                                raise ErrorWithMsg("Invalid Input after integer")
                        else:
                            # Check if current character satisfy condition in next character
                            if self.checkCondition(self.exp,self.i):
                                # If current index is open bracket
                                if index == "(":
                                    # Use recursive function to append another array
                                    self.i += 1
                                    self.open_brackets += 1
                                    callback = self.recursiveFunction()
                                    # If open bracket contains nothing
                                    if callback == None:
                                        # return nothing
                                        return None
                                    else:
                                        # append to current array
                                        output.append(callback)
                                    # output.append(self.recursiveFunction())
                                # If it is closed bracket
                                elif index == ")":
                                    # self.i += 1
                                    self.close_brackets += 1
                                    output.append(")")
                                    return output
                                # if current index is plus sign
                                elif index == "+":
                                    # if current and next index is "+-" or "++" pass
                                    # if self.exp[self.i+1] == "-" or self.exp[self.i+1] == "+":
                                    #     pass
                                    if (self.exp[self.i-1] in ["(","*","/"]):
                                        self.exp = self.exp[:(self.i)] + self.exp[(self.i+1):]
                                        self.i -= 1
                                        try:
                                            int(self.exp[self.i])
                                        except:
                                            if not self.checkCondition(self.exp,self.i):
                                                raise ErrorWithMsg("Invalid")
                                    elif self.exp[self.i+1] == "-" or self.exp[self.i+1] == "+":
                                        pass
                                    else:
                                        output.append(index)
                                # if current index is negative
                                elif index == "-":
                                    # If another negative in front of negative "--"
                                    if self.exp[self.i+1] == "-":
                                        # if 3 index is "(--", "*--", "/--"
                                        if self.exp[self.i-1] in ["(","*","/"]:
                                            # Remove the both minus sign
                                            self.exp = self.exp[:(self.i)] + self.exp[(self.i+2):]
                                            self.i -= 1
                                            # if ["(","*","/"] characters does not fufil condition send error
                                        # Else if like "5--" or ".--"
                                        else:
                                            # Replace them with a plus sign
                                            # For example (6.2--5),
                                            # Remove "--" sign
                                            self.exp = self.exp[:(self.i)] + "+" + self.exp[(self.i+2):]
                                            self.i -= 1
                                        try:
                                            int(self.exp[self.i])
                                        except:
                                            if not self.checkCondition(self.exp,self.i):
                                                raise ErrorWithMsg("Invalid")
                                    # If it is a plus sign in front of negative sign
                                    elif self.exp[self.i+1] == "+":
                                        # Switch to - sign at next character
                                        # if 3 index is "(-+", "*-+", "/-+"
                                        if (self.exp[self.i-1] in ["(","*","/"]):
                                            # Remove plus sign
                                            self.exp = self.exp[:(self.i+1)] + self.exp[(self.i+2):]
                                            self.i -=1
                                            # if ["(","*","/"] characters does not fufil condition send error
                                        else:
                                            # For example (6.2-+5),
                                            # Remove "+" sign
                                            self.exp = self.exp[:(self.i+1)] + self.exp[(self.i+2):]
                                            self.i -= 1
                                        try:
                                            int(self.exp[self.i])
                                            # if not self.checkIntegerCondition(self.exp,self.i):
                                            #         # print("Invalid")
                                            #         # return None
                                            #         raise ErrorWithMsg("Invalid")
                                        except:
                                            # Check condition only for full truncation
                                            if not self.checkCondition(self.exp,self.i):
                                                    # print("Invalid")
                                                    # return None
                                                raise ErrorWithMsg("Invalid")
                                    # If its an integer after negative
                                    # elif (self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1])) and (self.exp[self.i-1] in ["(","*","/"]):
                                    # If "(-", "*-", "/-"
                                    elif (self.exp[self.i-1] in ["(","*","/"]):
                                        # If theres integer after negative
                                        if self.checkInteger(self.exp[self.i+1]):
                                            output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"-"))
                                        # Else there is decimal after negative
                                        elif self.decimalStop(self.exp[self.i+1]):
                                            output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"-0"))
                                    else:
                                        output.append(index)
                                # If current index is a * sign
                                elif index == "*":
                                    # If its an exponential 
                                    # Ex (6**2)
                                    if self.exp[self.i+1] == "*":
                                        # Check if its valid character after exponential)
                                        if (self.checkInteger(self.exp[self.i+2]) or self.decimalStop(self.exp[self.i+2]) or self.exp[self.i+2] == "-" or self.exp[self.i+2] == "("):
                                            output.append("**")
                                            self.i +=1
                                        else:
                                            raise ErrorWithMsg("Invalid Input after exponential")
                                            # print("Invalid input after exponential")
                                            # return None
                                    else:
                                        output.append(index)
                                elif index == ".":
                                    output.append(self.getIntegerOrDecimalValue(self.exp,self.i,"0."))
                            
                                else:
                                    output.append(index)

                            # If not valid character error
                            else:
                                # print("Invalid Input after character")
                                # print("Error at Character: " + str(exp[i:i+2]))
                                # return None
                                raise ErrorWithMsg("Invalid Input after character")
                        # print(index)
                    else:
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
                                raise ErrorWithMsg("Incorrect input")
                else:
                    raise ErrorWithMsg("Invalid Character used")
            self.i += 1
        if self.open_brackets != self.close_brackets:
            raise ErrorWithMsg("Number of brackets does not match")
        return output
    def runEntirePrograme(self):
        if self.checkParenthesis(self.exp):
            try:
                output = self.recursiveFunction()
                if output == None:
                    return None
                else:
                    # return self.flatten(self.recursionAdd(self.recursionMul(self.recursionExponential(output))))
                    # return self.recursionFunction(output,[["**"],["*","/"],["+","-"]])
                    return self.flatten(self.recursionFunction(output,[["**"],["*","/"],["+","-"]]))
            except ErrorWithMsg as e:
                print("Received error with message:", e.msg)
                return None
        elif self.isEmpty(self.exp):
            print("Missing expression! Please try again!")
            return None
        else:
            print("Not enclosed with parenthesis")
            return None
# Negative test case
# testcases = ["(--+-5-++--5)",
# "(-5--+5)",
# "(5-5)",
# "(5--+-5)",
# "(5--+5)",
# "(5--5)",
# "(5+--5)",
# "(5++--5)",
# "(--+5--5)",
# "(--5+--5)"]
# testcases = ["(5**--5)",
# "(5**-5)",
# "(5**--5)",
# "(5*-5)",
# "(5*--5)",
# "(5/-5)",
# "(5/--5)",
# "(5/(-5))",
# "(5/(+5))"]
# testcases = ["(5**--2.55)",
# "(5**-.55)",
# "(5**-+--5)",
# "(5/-+--5)",
# "(5/++--5)"]
# # testcases= ["(2.5.5)"]
# for i in testcases:
#     expClass = expressionValidator(i) 
#     print(expClass.runEntirePrograme())

# expClass = expressionValidator("( -3 / 3 ** 5 + (5**2) -- (4**---+-2.5))")
# expClass = expressionValidator("(-5 + 3 * (5 - (---+10.5)) / (2))")
# expClass = expressionValidator("(5//32)")
# output = input("Expression: ")
# expClass = expressionValidator(output)
# print(expClass.runEntirePrograme())
#
