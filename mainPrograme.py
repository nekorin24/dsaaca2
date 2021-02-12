import os
from refinedexpressionValidator import ExpressionValidator
from stack import Stack
from binaryTree import BinaryTree
# choice = int(input("Please select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: "))
# class.runfunction(choice-1)

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
            if evaluate(lefttree) == evaluate(righttree):
                if len(leftHalf[leftIndex]) < len(rightHalf[rightIndex]):
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
            else:
                #Ascending
                if op_choice == 1:
                    print("Sorting Ascending...")
                    if evaluate(lefttree) < evaluate(righttree):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
                #Descending
                elif op_choice == 2:
                    print("Sorting Descending...")
                    if evaluate(lefttree) > evaluate(righttree):
                        mergeList[mergeIndex] = leftHalf[leftIndex]
                        leftIndex+=1
                    else:
                        mergeList[mergeIndex] = rightHalf[rightIndex]
                        rightIndex+=1
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



def recursive(array,length,output_file_edit):
    with open(str(output_file_edit),"a") as output_file:
        # print("*****************************************************************************")
        expClass = ExpressionValidator(array[-1])
        output = expClass.run_entire_program()
        if output == None:
            print("Invalid Expression")
            return
        # print(eval(rightTree))
        # lefttree build_parse_tree(outputLeft)
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
        
class MainProgram:
    def __init__(self,choice=None):
        self.choice = choice

    def validate_expression(self):
        expression = input("Please enter the expression you want to evaluate:\n")
        expClass = ExpressionValidator(expression)
        output = expClass.run_entire_program()
        if output == None:
            print("Invalid Expression")
            return self.validate_expression()
        else:
            return [output,expression]

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

    
    def sort_expression(self,output_choice,input_file,output_file):
        array = []
        try:
            with open(str(input_file),'r') as input_file:
                for line in input_file:
                    array.append(line.replace("\n",""))
                try:
                    # print(array)
                    merge_sort(array,output_choice)
                    try:
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

    def run_sort_and_evaluate(self):
        self.sort_expression(self.get_output_choice(), self.get_input_file(), self.get_output_file())
    def exit(self):
        print("Bye, thanks for using ST107 DSAA: Expression Evaluator & Sorter")
    
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
    
    def get_choice(self):
        chosen_choice = input("\nPlease select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: ")
        # print(self.check_choice(chosen_choice))
        return self.check_choice(chosen_choice)
        # return chosen_choice

    def get_output_choice(self):
        output_choice = input("\n(1) Ascending\n(2) Descending\nSelect choice:")
        return self.check_output_choice(output_choice)

    def get_input_file(self):
        input_file = input("\nPlease enter input file:")
        return input_file

    def get_output_file(self):
        output_file = input("Please enter output file:")
        return output_file

    def run_choice(self,choice):
        programeArray = [self.evaluate_expression, self.run_sort_and_evaluate, self.exit]
        programeArray[choice-1]()
        if choice == 3:
            return
        self.run_choice(self.get_choice())
    
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

def build_parse_tree(exp):
    tokens = exp
#     exp = exp.replace(" ","")
#     number_or_symbol = re.compile('(-?\d+\.\d+|\w+|[()\-+*/^])')
#     number_or_symbol = re.compile('([-+]?\d+\.\d+|[-]?[0-9]+|[**]+|[()\-+*/^])')
#     tokens = re.findall(number_or_symbol, exp)
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
# main = MainProgram()
# main.print_introduction()
# chosen_choice = main.get_choice()
# main.run_choice(chosen_choice)










# main = MainProgram()
# main.print_introduction()
# chosen_choice = main.get_choice()
# main.run_choice(chosen_choice)

# class BinaryTree:
#     def __init__(self,key, leftTree = None, rightTree = None):
#         self.key = key
#         self.leftTree = leftTree
#         self.rightTree = rightTree
#     def set_key(self, key):
#         self.key = key
#     def get_key(self):
#         return self.key
#     def get_left_tree(self):
#         return self.leftTree
#     def get_right_tree(self):
#         return self.rightTree
#     def insert_left(self, key):
#         if self.leftTree == None:
#             self.leftTree = BinaryTree(key)
#         else:
#             t =BinaryTree(key)
#             self.leftTree , t.leftTree = t, self.leftTree
#     def insert_right(self, key):
#         if self.rightTree == None:
#             self.rightTree = BinaryTree(key)
#         else:
#             t =BinaryTree(key)
#             self.rightTree , t.rightTree = t, self.rightTree
            
#     def print_preorder(self, level):
#         print( str(level*'-') + str(self.key))
#         if self.leftTree != None:
#             self.leftTree.print_preorder(level+1)
#         if self.rightTree != None:
#             self.rightTree.print_preorder(level+1) 


# class Stack:

#     def __init__(self):
#         self.__list= []
#     def isEmpty(self):
#         return self.__list == []
#     def size(self):
#         return len(self.__list)

#     def clear(self):
#         self.__list.clear()

#     def push(self, item):
#         self.__list.append(item)

#     def pop(self): # popTail
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop()

#     def get(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[-1]
    
#     def getList(self):
#         return self.__list
    
#     def __str__(self):
#         output = '<'
#         for i in range( len(self.__list) ):
#             item = self.__list[i]
#             if i < len(self.__list)-1 :
#                 output += f'{str(item)}, '
#             else:
#                 output += f'{str(item)}'
#         output += '>'
#         return output



# def build_parse_tree(exp):
#     tokens = exp.split()
#     stack = Stack()
#     tree = BinaryTree('?')
#     stack.push(tree)
#     currentTree = tree
#     for t in tokens:
#         # RULE 1: If token is '(' add a new node as left child
#         # and descend into that node
#         if t == '(':
#             currentTree.insert_left('?')
#             stack.push(currentTree)
#             currentTree = currentTree.get_left_tree() 
#         # RULE 2: If token is operator set key of current node
#         # to that operator and add a new node as right child
#         # and descend into that node
#         elif t in ['+', '-', '*', '/']:
#             currentTree.set_key(t)
#             currentTree.insert_right('?')
#             stack.push(currentTree)
#             currentTree = currentTree.get_right_tree()
#         # RULE 3: If token is number, set key of the current node
#         # to that number and return to parent
#         elif t not in ['+', '-', '*', '/', ')'] :
#             currentTree.set_key(int(t))
#             parent = stack.pop()
#             currentTree = parent
#         # RULE 4: If token is ')' go to parent of current node
#         elif t == ')':
#             currentTree = stack.pop()
#         else:
#             raise ValueError
#     return tree
# def evaluate(tree):
#     leftTree = tree.get_left_tree()
#     rightTree = tree.get_right_tree()
#     op = tree.get_key()
#     if leftTree != None and rightTree != None:
#         if op == '+':
#             return evaluate(leftTree) + evaluate(rightTree)
#         elif op == '-':
#             return evaluate(leftTree) - evaluate(rightTree)
#         elif op == '*':
#             return evaluate(leftTree) * evaluate(rightTree)
#         elif op == '/':
#             return evaluate(leftTree) / evaluate(rightTree)
#     else:
#         return tree.get_key()