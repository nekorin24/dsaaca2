def expressionFunc(exp):
    # remove spaces
    exp = exp.replace(" ","")
    condition = {
    "(": ["0","1","2","3","4","5","6","7","8","9",".", "-"],
    ")": ["+","-","/","*",")"],
    "+": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "-": ["0","1","2","3","4","5","6","7","8","9",".","(","-","+"],
    "*": ["0","1","2","3","4","5","6","7","8","9",".","(","*","-"],
    "/": ["0","1","2","3","4","5","6","7","8","9",".","(",'-'],
    "int": ["0","1","2","3","4","5","6","7","8","9",".","-","+","*","/",")"],
    ".":["0","1","2","3","4","5","6","7","8","9"]
    }
    array = []
    open_brackets = 0
    close_brackets = 0
    i = 0
    print("\nExpression Inputted==> " + exp + "\n")
    while i < len(exp):
        index = exp[i]
        if index != " ":
            if index in ["0","1","2","3","4","5","6","7","8","9",".","-","+","*","/",")","("]:
                try:
                    int(exp[i])
                    if exp[i+1] in ["0","1","2","3","4","5","6","7","8","9","."]:
                        output = str(exp[i])
                        no_comma = True
                        x = i
                        if exp[x] == ".":
                            no_comma = False
                        while x < len(exp):
                            if exp[x+1] in ["0","1","2","3","4","5","6","7","8","9"]:
                                output += str(exp[x+1])
                            elif exp[x+1] == ".":
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
                        array.append(output)
                        i = x
                    else:
                        array.append(index)
                # if it is not integer
                except:
                    # print(index)
                    try:
                        if exp[i+1] in condition[exp[i]]:
                            print("some")
                            if index == "+":
                                # For plus, it only matters at the end
                                if exp[i+1] == "-" or exp[i+1] == "+":
                                    pass
                                else:
                                    array.append(index)
                            elif index == "-":
                                # If another negative
                                if exp[i+1] == "-":
                                    # Switch to plus at the string
                                    exp = exp[:(i+1)] + "+" + exp[(i+2):]
                                    # exp[i+1] = "+"
                                    # array.append("+")
                                elif exp[i+1] == "+":
                                    exp = exp[:(i+1)] + "-" + exp[(i+2):]
                                # If its an integer after negative
                                elif exp[i+1] in ["0","1","2","3","4","5","6","7","8","9","."] and (exp[i-1] == "(" or exp[i-1] == "*" or exp[i-1] == "/"):
                                    #Number or decimal
                                    output = "-"
                                    no_comma = True
                                    # Index now at number or decimal
                                    x = (i)
                                    if exp[x] == ".":
                                        no_comma = False
                                    while x < len(exp):
                                        # If equals to number output add number
                                        if exp[x+1] in ["0","1","2","3","4","5","6","7","8","9"]:
                                            output += str(exp[x+1])
                                        # if equals to comma
                                        elif exp[x+1] == ".":
                                            # If comma first time add comma
                                            if no_comma == True:
                                                output += "."
                                                no_comma = False
                                            # If not first time , error
                                            else:
                                                print("Double full stop detected")
                                                return
                                                # break
                                        else:
                                            # If the previous entry equals to comma, error
                                            if exp[x] == ".":
                                                print("Invalid input after full stop")
                                                return
                                            # Break when its neither comma or integer break
                                            break
                                        # Continue loop
                                        x += 1
                                    # Append decimal to array
                                    array.append(output)
                                    # Update index of while loop
                                    i = x
                                else:
                                    # Append bracket
                                    array.append(index)
                            # Equals to multiplication
                            elif index =="*":
                                # Equals to exponential in next entry
                                if exp[i+1] == "*":
                                    # if its an integer or decimal infront of exponential
                                    if exp[i+2] in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
                                        # Append exponential
                                        array.append("**")
                                        # Update index to the next character
                                        i += 1
                                    # If its not an integer or decimal infront of exponential give error
                                    else:
                                        print("Invalid input after exponential")
                                        return
                                else:
                                    array.append(index)
                            # If decimal 
                            elif index ==".":
                                output = "0."
                                no_comma = False
                                x = i
                                while x < len(exp):
                                    # If equals to number output add number
                                    if exp[x+1] in ["0","1","2","3","4","5","6","7","8","9"]:
                                        output += str(exp[x+1])
                                    # if equals to comma
                                    elif exp[x+1] == ".":
                                        # If comma first time add comma
                                        if no_comma == True:
                                            output += "."
                                            no_comma = False
                                        # If not first time , error
                                        else:
                                            print("Double full stop detected")
                                            return
                                            # break
                                    else:
                                        # If the previous entry equals to comma, error
                                        if exp[x] == ".":
                                            print("Invalid input after full stop")
                                            return
                                        # Break when its neither comma or integer break
                                        break
                                    # Continue loop
                                    x += 1
                                # Append decimal to array
                                array.append(output)
                                # Update index of while loop
                                i = x
                            # # If equals to open bracket increment
                            elif index == "(":
                                open_brackets += 1
                                array.append(index)
                            # If equals to close bracket increment
                            elif index == ")":
                                close_brackets += 1
                                array.append(index)
                            else:
                                # print(i)
                                # print(index)
                                array.append(index)

                        else:

                            print("Invalid Input after character")
                            print("Error at Character: " + str(exp[i:i+2]))
                            return
                            # pass
                    except:

                    # else:
                        if index == "(":
                            open_brackets += 1
                            array.append(index)
                        # If equals to close bracket increment
                        elif index == ")":
                            close_brackets += 1
                            array.append(index)
            else:
                print("Invalid Character used")
                return
        i +=1
            

    if open_brackets != close_brackets:
        print("Missing Close or Open Bracket")
        return

    return array

realexp = "( -3.6 / 3 ** 5 + (5**2) -+- (4**-2.5))"
exp = realexp
output = expressionFunc(exp)
if output == None:
    print("\nInput again")
else:
    print("\nThank you for your Input")
print(output)

# array = []
# for i in range(len(exp)):
#     # Check for operants
#     if i in ['+', '-', '*', '/', ')', '(']:
#         if exp[i] == "*" and exp[i+1] == "*":
#             array.append("**")
#         else:
#             array.append(exp[i])
    # Check wether character is integer
# print(exp.replace(" ",""))
