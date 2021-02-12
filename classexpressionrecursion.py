class ExpressionValidator:
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
    
    def check_integer(self,value):
        try:
            int(value)
            return True
        except:
            return False
            
    def decimal_stop(self,value):
        return value == "."
    
    def get_int_or_decimal_value(self, exp, i,output):
        output = output
        no_comma = True
        x = i
        # if exp[x] == ".":
        if self.decimal_stop(exp[x]):
            no_comma = False
        while x < len(exp):
            # if exp[x+1] in ["0","1","2","3","4","5","6","7","8","9"]:
            if self.check_integer(exp[x+1]):
                output += str(exp[x+1])
            # elif exp[x+1] == ".":
            elif self.decimal_stop(exp[x+1]):
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
        
    def check_condition(self,exp, index):
        return exp[index + 1] in self.condition[exp[index]]
    
    def check_int_condition(self,exp,index):
        return exp[index + 1] in self.condition["int"]

    def append_to_array(self, value):
        self.array.append(value)
    
    def check_operators(self,value):
        return value in ["-","+","*","/",")","("]

    def check_all_valid(self,value):
        return self.check_integer(value) or self.decimal_stop(value) or self.check_operators(value)

    def main_function(self):
        self.exp = self.remove_spaces(self.exp)
        print("\nExpression Inputted==> " + self.exp + "\n")
        while self.i < len(self.exp):
            index = self.exp[self.i]
            if index != " ":
                if self.check_all_valid(index):
                    # If it is an integer
                    if self.check_integer(index):
                        # Check if next character is a decimal point or integer
                        if self.check_integer(self.exp[self.i+1]) or self.decimal_stop(self.exp[self.i+1]):
                            self.append_to_array(self.get_int_or_decimal_value(self.exp,self.i,str(self.exp[self.i])))
                        # else it is just one character
                        else:
                            self.append_to_array(index)
                    # If it is not an integer
                    else:
                        # print(self.exp[self.i + 1] in self.condition[self.i])
                        try:
                            # if self.exp[self.i + 1] in self.condition[self.i]:\
                            if self.check_condition(self.exp,self.i):
                                # print(index)
                                # print("someth")
                                if index == "+":
                                    if self.exp[self.i+1] == "-" or self.exp[self.i+1] == "+":
                                        pass
                                    else:
                                        self.append_to_array(index)
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
                                    elif (self.check_integer(self.exp[self.i+1]) or self.decimal_stop(self.exp[self.i+1])) and (self.exp[self.i-1] in ["(","*","/"]):
                                        self.append_to_array(self.get_int_or_decimal_value(self.exp,self.i,"-"))
                                    else:
                                        self.append_to_array(index)
                                elif index == "*":
                                    if self.exp[self.i+1] == "*":
                                        if (self.check_integer(self.exp[self.i+2]) or self.decimal_stop(self.exp[self.i+2]) or self.exp[self.i+2] == "-"):
                                            self.append_to_array("**")
                                            self.i +=1
                                        else:
                                            print("Invalid input after exponential")
                                            return
                                    else:
                                        self.append_to_array(index)
                                elif index == ".":
                                    self.append_to_array(self.get_int_or_decimal_value(self.exp,self.i,"0."))
                                
                                elif index == "(":
                                    self.open_brackets += 1
                                    self.append_to_array(index)
                                # If equals to close bracket increment
                                elif index == ")":
                                    selfclose_brackets += 1
                                    self.append_to_array(index)
                                else:
                                    self.append_to_array(index)

                            # If not valid character error
                            else:
                                print("Invalid Input after character")
                                print("Error at Character: " + str(exp[i:i+2]))
                                return
                        except:
                            if index == "(":
                                self.open_brackets += 1
                                self.append_to_array(index)
                        # If equals to close bracket increment
                            elif index == ")":
                                self.close_brackets += 1
                                self.append_to_array(index)
                else:
                    print("Invalid Character used")
                    return
            self.i += 1
        if self.open_brackets != self.close_brackets:
            print("Missing Close or Open Bracket")
            return

        return self.array

    def recursive_function(self):
        self.exp = self.remove_spaces(self.exp)
        index = self.exp[self.i]
        if self.i == 0:
            output = []
        else:
            output = ["("]
        while self.i < len(self.exp):
            # if index == "(":
            #     self.i += 1
            #     output.append(self.recursive_function())
            # if index == ")":
            #     self.i += 1
            #     output.append(")")
            #     return output
            print(output)
            print(self.i)
            index = self.exp[self.i]
            if index != " ":
                if self.check_all_valid(index):
                    # If it is an integer
                    # if self.check_integer(index):
                    #     # Check if next character is a decimal point or integer
                    #     if self.check_integer(self.exp[self.i+1]) or self.decimal_stop(self.exp[self.i+1]):
                    #         output.append(self.get_int_or_decimal_value(self.exp,self.i,str(self.exp[self.i])))
                    #     # else it is just one character
                    #     else:
                    #         output.append(index)
                    # If it is not an integer
                    # if:
                    # print(self.exp[self.i + 1] in self.condition[self.i])
                    try:
                        # if self.exp[self.i + 1] in self.condition[self.i]:\
                        if self.check_integer(index):
                            if self.check_int_condition(self.exp, self.i):
                                if self.check_integer(self.exp[self.i+1]) or self.decimal_stop(self.exp[self.i+1]):
                                    output.append(self.get_int_or_decimal_value(self.exp,self.i,str(self.exp[self.i])))
                                # else it is just one character
                                else:
                                    output.append(index)
                            else:
                                print("Invalid Input after integer")
                                return
                        else:
                            if self.check_condition(self.exp,self.i):
                                # print(index)
                                # print("someth")
                                if index == "(":
                                    self.i += 1
                                    output.append(self.recursive_function())
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
                                    elif (self.check_integer(self.exp[self.i+1]) or self.decimal_stop(self.exp[self.i+1])) and (self.exp[self.i-1] in ["(","*","/"]):
                                        output.append(self.get_int_or_decimal_value(self.exp,self.i,"-"))
                                    else:
                                        output.append(index)
                                elif index == "*":
                                    if self.exp[self.i+1] == "*":
                                        if (self.check_integer(self.exp[self.i+2]) or self.decimal_stop(self.exp[self.i+2]) or self.exp[self.i+2] == "-"):
                                            output.append("**")
                                            self.i +=1
                                        else:
                                            print("Invalid input after exponential")
                                            return
                                    else:
                                        output.append(index)
                                elif index == ".":
                                    output.append(self.get_int_or_decimal_value(self.exp,self.i,"0."))
                                
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
                                print(index)
                                print(i)
                                print("Invalid Input after character")
                                # print("Error at Character: " + str(exp[i:i+2]))
                                return
                    # Last index
                    except:
                    #     if index == "(":
                    #         self.open_brackets += 1
                    #         output.append(index)
                    # # If equals to close bracket increment
                    #     elif index == ")":
                    #         self.close_brackets += 1
                    #         output.append(index)
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
                                return
                else:
                    print("Invalid Character used")
                    return
            self.i += 1
        return output


    
# expClass = expressionValidator("( -3 / 3 ** 5 + (5**2) -- (4**-2.5))")
expClass = ExpressionValidator("((1())")
output = expClass.recursive_function()
if output == None:
    print("\nInput again")
else:
    print("\nThank you for your Input")

print(output)

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
print(flatten(recursive_mul(recursive_exponential(output))))

# print(expClass.check_integer("3"))
