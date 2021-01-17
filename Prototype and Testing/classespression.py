class expressionValidator:
    def __init__(self, original_exp):
        self.original_exp = original_exp
        self.exp = self.original_exp
        self.array = []
        self.open_brackets = 0
        self.close_brackets = 0
        self.i = 0
        self.condition = {
    "(": ["0","1","2","3","4","5","6","7","8","9",".", "-"],
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
                    return
            else:
                if exp[x+1] == (i + 1):
                    print("Invalid Input")
                    return
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

    def mainFunction(self):
        self.exp = self.remove_spaces(self.exp)
        print("\nExpression Inputted==> " + self.exp + "\n")
        while self.i < len(self.exp):
            index = self.exp[self.i]
            if index != " ":
                if self.checkAllValid(index):
                    # If it is an integer
                    # print(index)
                    if self.checkInteger(index):
                        # Check if next character is a decimal point or integer
                        if self.checkInteger(self.exp[self.i+1]) or self.decimalStop(self.exp[self.i+1]):
                            self.appendtoArray(self.getIntegerOrDecimalValue(self.exp,self.i,str(self.exp[self.i])))
                        # else it is just one character
                        else:
                            self.appendtoArray(index)
                    # If it is not an integer
                    else:
                        # print(self.exp[self.i + 1] in self.condition[self.i])
                        try:
                            # if self.exp[self.i + 1] in self.condition[self.i]:\
                            if self.checkCondition(self.exp,self.i):
                                # print(index)
                                # print("someth")
                                if index == "+":
                                    if self.exp[self.i+1] == "-" or self.exp[self.i+1] == "+":
                                        pass
                                    else:
                                        self.appendtoArray(index)
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
                                        self.appendtoArray(self.getIntegerOrDecimalValue(self.exp,self.i,"-"))
                                    else:
                                        self.appendtoArray(index)
                                elif index == "*":
                                    if self.exp[self.i+1] == "*":
                                        if (self.checkInteger(self.exp[self.i+2]) or self.decimalStop(self.exp[self.i+2]) or self.exp[self.i+2] == "-"):
                                            self.appendtoArray("**")
                                            self.i +=1
                                        else:
                                            print("Invalid input after exponential")
                                            return
                                    else:
                                        self.appendtoArray(index)
                                elif index == ".":
                                    self.appendtoArray(self.getIntegerOrDecimalValue(self.exp,self.i,"0."))
                                
                                elif index == "(":
                                    self.open_brackets += 1
                                    self.appendtoArray(index)
                                # If equals to close bracket increment
                                elif index == ")":
                                    selfclose_brackets += 1
                                    self.appendtoArray(index)
                                else:
                                    self.appendtoArray(index)

                            # If not valid character error
                            else:
                                print("Invalid Input after character")
                                return
                                # print("Error at Character: " + str(exp[i:i+2]))
                        except:
                            # if index == "(":
                            #     self.open_brackets += 1
                            #     self.appendtoArray(index)
                        # If equals to close bracket increment
                            if index == ")":
                                self.close_brackets += 1
                                self.appendtoArray(index)
                            else:
                                try:
                                    int(index)
                                    self.appendtoArray(index)
                                except:
                                    print("Incorrect input")
                                    return
                else:
                    print("Invalid Character used")
                    return
            self.i += 1
        if self.open_brackets != self.close_brackets:
            print("Missing Close or Open Bracket")
            return

        return self.array
    
expClass = expressionValidator("( -3 / 3 ** 5 + (5**2) -- (4**-2.5))+")
output = expClass.mainFunction()
if output == None:
    print("\nInput again")
else:
    print("\nThank you for your Input")

print(output)
# print(expClass.checkInteger("3"))
