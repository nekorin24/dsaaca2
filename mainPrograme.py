import os
from refinedexpressionValidator import ExpressionValidator
from stack import Stack
from binaryTree import BinaryTree

# merge_sort function
def merge_sort(l, output_choice):
    op_choice = int(output_choice)
    if len(l) > 1:
        mid = int (len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]
        merge_sort(leftHalf,op_choice)
        merge_sort(rightHalf,op_choice)
        leftIndex,rightIndex,mergeIndex = 0,0,0
        mergeList = l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            # lefttree = build_parse_tree(leftHalf[leftIndex])
            # righttree = build_parse_tree(rightHalf[rightIndex])
            expClassLeft = ExpressionValidator(leftHalf[leftIndex])
            expClassRight = ExpressionValidator(rightHalf[rightIndex])
            outputLeft = expClassLeft.run_entire_program()
            outputRight = expClassRight.run_entire_program()
            if outputLeft == None or outputRight == None:
                print("Invalid Expression")
                return
            # print(eval(rightTree))
            lefttree = build_parse_tree(outputLeft)
            righttree = build_parse_tree(outputRight)
            # If value of expression of left tree equals to expression of right tree
            if evaluate(lefttree) == evaluate(righttree):
                if op_choice == 1:
                    # If length of left half is lower than right half
                    if len(leftHalf[leftIndex]) < len(rightHalf[rightIndex]):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    # Else length of right half should be higher or equal
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
                elif op_choice == 2:
                    # If length of left half is higher than right half
                    if len(leftHalf[leftIndex]) > len(rightHalf[rightIndex]):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    # Else length of right half should be lower or equal
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
                # Inquire for choice of ascending or descending again
                else:
                    return get_output_choice()
            # If value of both expression is not equal
            else:
                #Ascending
                if op_choice == 1:
                    print("Sorting Ascending...")
                    # If value of left tree is lower than right tree
                    if evaluate(lefttree) < evaluate(righttree):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    #Else value of right tree is lower or equals to left tree
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
                #Descending
                elif op_choice == 2:
                    print("Sorting Descending...")
                    # If value of left tree is higher than right tree
                    if evaluate(lefttree) > evaluate(righttree):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    # Else value of right tree is higher or equals to left tree
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
                # Inquire for choice
                else:
                    return get_output_choice()
                # if chosen_choice == 2:
                #     sortDescending()
            mergeIndex+=1
        # Handle those items still left in the left Half
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex+=1
            mergeIndex+=1
        # Handle those items still left in the right Half
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex+=1
            mergeIndex+=1
        # print('merge', l)


# recursive function to print the sorting of expression
def recursive(array,length,output_file_edit):
    # open output file to append
    with open(str(output_file_edit),"a") as output_file:
        # Tokenize expression in file
        expClass = ExpressionValidator(array[-1])
        output = expClass.run_entire_program()
        # If tokenized expression equals to none
        if output == None:
            print("Invalid Expression")
            return
        # print(eval(rightTree))
        # lefttree build_parse_tree(outputLeft)
        # If length of the array equals to 1 print Evaluation started
        if len(array)== 1:
            print("\n>>>Evaluation and sorting started:")
            print("\n*** Expressions with value=> " + str(evaluate(build_parse_tree(output))))
            output_file.write("*** Expressions with value=> " + str(evaluate(build_parse_tree(output))))
            print(str(array[-1]) + "==>" + str(evaluate(build_parse_tree(output))))
            output_file.write("\n")
            output_file.write(str(array[-1]) + "==>" + str(evaluate(build_parse_tree(output))))
            return

        recursive(array[:-1],length,output_file_edit)

        expClass = ExpressionValidator(array[-2])
        outputminus = expClass.run_entire_program()
        if output == None:
            print("Invalid Expression")
            return

        if evaluate(build_parse_tree(outputminus)) != evaluate(build_parse_tree(output)):
            print("\n*** Expressions with value=> " + str(evaluate(build_parse_tree(output))))
            output_file.write("\n")
            output_file.write("\n*** Expressions with value=> " + str(evaluate(build_parse_tree(output))))
    
        print(str(array[-1]) + "==>" + str(evaluate(build_parse_tree(output))))
        output_file.write("\n")
        output_file.write(str(array[-1]) + "==>" + str(evaluate(build_parse_tree(output))))

        if len(array) == length:
            print("\n>>>Evaluation and sorting completed!\n")
# MainProgram Class
class MainProgram:
    def __init__(self,choice=None):
        self.choice = choice
    # Validate expression
    def validate_expression(self):
        # Enter expression
        expression = input("\nPlease enter the expression you want to evaluate:\n")
        expClass = ExpressionValidator(expression)
        output = expClass.run_entire_program()
        # If output is None, inquire to do again
        if output == None:
            print("Invalid Expression")
            return self.validate_expression()
        else:
            return [output,expression]
    # Evaluate expression
    def evaluate_expression(self):
        exp = self.validate_expression()
        tree = build_parse_tree(exp[0])
        tree.print_preorder(0)
        # if isinstance(evaluate(tree),float) == False:
        try:
            print (f'The expression: {exp[1]} evaluates to: {evaluate(tree)}')
        except ZeroDivisionError:
            print (f'The expression: {exp[1]} cannot be evaluated! Zero Division Error.\n\nNumber cannot be divided by/with zero, result is infinite.')
            return tree.get_key()
        os.system('pause')

    # sort_expression function to sort expression
    def sort_expression(self,output_choice,input_file,output_file):
        array = []
        try:
            # Try opening input file if not give error as invalid input file
            with open(str(input_file),'r') as input_file:
                for line in input_file:
                    array.append(line.replace("\n",""))
                try:
                    # print(array)
                    array = [x.replace(" ","") for x in array]
                    merge_sort(array,output_choice)
                    try:
                        # Overwrite output file with empty values and close
                        open(str(output_file),"w").close()
                        # Use recursive function to append empty file
                        recursive(array,len(array),str(output_file))
                    except:
                        print("Invalid expression in input file!")
                        # print("Please try again.\n")
                        # self.run_sort_and_evaluate()
                        return
                except:
                    print("Invalid expression in input file!")
                    return
        except:
            print("Invalid input file!")
            return
            # print("Please try again.\n")
            # self.run_sort_and_evaluate()
        os.system('pause')
    # Run sort and evaluation function
    def run_sort_and_evaluate(self):
        self.sort_expression(self.get_output_choice(), self.get_input_file(), self.get_output_file())
    # Print exit message
    def exit(self):
        print("Bye, thanks for using ST107 DSAA: Expression Evaluator & Sorter")
    # Validation of the 3 choices
    def check_choice(self,chosen_choice):
        try:
            validate_choice = int(chosen_choice)
            if 1 <= validate_choice <= 3:
                return validate_choice
            else:
                print("Input is not part of the above options")
                return self.get_choice()
        except ValueError:
            print("Input is invalid")
            return self.get_choice()
            # return
    # Check output choice of the ascending and descending option
    def check_output_choice(self,output_choice):
        try:
            validate_outputchoice = int(output_choice)
            if 0 < validate_outputchoice < 3:
                return validate_outputchoice
            else:
                print("Input is not part of the above options")
                return self.get_output_choice()
        except ValueError:
            print("Input is not invalid")
            return self.get_output_choice()
            # return
    # Get input of the 3 choices
    def get_choice(self):
        chosen_choice = input("\nPlease select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: ")
        # print(self.check_choice(chosen_choice))
        return self.check_choice(chosen_choice)
        # return chosen_choice
    # Get the choice of ascending and descending option
    def get_output_choice(self):
        output_choice = input("\n(1) Ascending\n(2) Descending\nSelect choice:")
        return self.check_output_choice(output_choice)
    # Get input file
    def get_input_file(self):
        input_file = input("\nPlease enter input file:")
        return input_file
    # Get output file 
    def get_output_file(self):
        output_file = input("Please enter output file:")
        return output_file
    # Run the function of the appropriate choice given
    def run_choice(self,choice):
        programeArray = [self.evaluate_expression, self.run_sort_and_evaluate, self.exit]
        programeArray[choice-1]()
        # If choice equals to exit option, end program
        if choice == 3:
            return
        self.run_choice(self.get_choice())
    # Print Introduction
    def print_introduction(self):
        title = "ST107 DSAA: Expression Evaluator & Sorter"
        grpMember = ["Teh Hock Jian", "Tan Bao Quan", "Ao Yang"]
        admission = [1839045,1935347,1935602]
        ditclass = "DIT/2B/11"
        length = 100
        nameText = ""
        for i in range(len(grpMember)):
            nameText += grpMember[i]
            nameText += "(" + str(admission[i]) + ")"
            if i < len(grpMember) - 1:
                nameText += " & "
        spacing = "\n*"
        output = "*" * length
        output += spacing + " " + title + (" " * (length-len(spacing)- len(title)-1)) + "*"
        output += spacing + ("-" * (length-2)) + "*"
        output += spacing  + (" " * (length-2)) + "*"
        output += spacing + " - Done by: " + nameText + (" " * (length - len(spacing)- len(" - Done by: ") - len(nameText))) + "*"
        output += spacing + " - Class " + ditclass + (" " * (length - len(spacing) - len(" - Class ") - len(ditclass))) + "*"
        output += "\n" + ("*" * length)
        
        print(output)
# build_parse_tree function
def build_parse_tree(exp):
    tokens = exp
    # print(tokens)
    stack = Stack()
    tree = BinaryTree('?')
    stack.push(tree)
    currentTree = tree
    for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
        if t == '(':
            currentTree.insert_left('?')
            stack.push(currentTree)
            currentTree = currentTree.get_left_tree() 
        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '/', '**']:
            currentTree.set_key(t)
            currentTree.insert_right('?')
            stack.push(currentTree)
            currentTree = currentTree.get_right_tree()
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '/', '**', ')'] :
            currentTree.set_key(float(t))
            parent = stack.pop()
            currentTree = parent
        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

main_programme = MainProgram()
# Evaluate the tree to get value of the expression
def evaluate(tree):
    leftTree = tree.get_left_tree()
    rightTree = tree.get_right_tree()
    op = tree.get_key()
    if leftTree != None and rightTree != None:
        if op == '+':
            return evaluate(leftTree) + evaluate(rightTree)
        elif op == '-':
            return evaluate(leftTree) - evaluate(rightTree)
        elif op == '*':
            return evaluate(leftTree) * evaluate(rightTree)
        elif op == '/':
            return evaluate(leftTree) / evaluate(rightTree)
        elif op == '**':
            return evaluate(leftTree) ** evaluate(rightTree)
    else:
        return tree.get_key()