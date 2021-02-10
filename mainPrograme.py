import os
from refinedexpressionValidator import expressionValidator
from stack import Stack
from binaryTree import BinaryTree
# choice = int(input("Please select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: "))
# class.runfunction(choice-1)

def mergeSort(l, output_choice):
    op_choice = int(output_choice)
    if len(l) > 1:
        mid = int (len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]
        mergeSort(leftHalf,op_choice)
        mergeSort(rightHalf,op_choice)
        leftIndex,rightIndex,mergeIndex = 0,0,0
        mergeList = l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            # lefttree = buildParseTree(leftHalf[leftIndex])
            # righttree = buildParseTree(rightHalf[rightIndex])
            expClassLeft = expressionValidator(leftHalf[leftIndex])
            expClassRight = expressionValidator(rightHalf[rightIndex])
            outputLeft = expClassLeft.runEntirePrograme()
            outputRight = expClassRight.runEntirePrograme()
            if outputLeft == None or outputRight == None:
                print("Invalid Expression")
                return
            # print(eval(rightTree))
            lefttree = buildParseTree(outputLeft)
            righttree = buildParseTree(outputRight)
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
                    return getOutput_Choice()
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
        expClass = expressionValidator(array[-1])
        output = expClass.runEntirePrograme()
        if output == None:
            print("Invalid Expression")
            return
        # print(eval(rightTree))
        # lefttree buildParseTree(outputLeft)
        if len(array)== 1:
            print("\n>>>Evaluation and sorting started:")
            print("\n*** Expressions with value=> " + str(evaluate(buildParseTree(output))))
            output_file.write("*** Expressions with value=> " + str(evaluate(buildParseTree(output))))
            print(str(array[-1]) + "==>" + str(evaluate(buildParseTree(output))))
            output_file.write("\n")
            output_file.write(str(array[-1]) + "==>" + str(evaluate(buildParseTree(output))))
            return

        recursive(array[:-1],length,output_file_edit)

        expClass = expressionValidator(array[-2])
        outputminus = expClass.runEntirePrograme()
        if output == None:
            print("Invalid Expression")
            return

        if evaluate(buildParseTree(outputminus)) != evaluate(buildParseTree(output)):
            print("\n*** Expressions with value=> " + str(evaluate(buildParseTree(output))))
            output_file.write("\n")
            output_file.write("\n*** Expressions with value=> " + str(evaluate(buildParseTree(output))))
    
        print(str(array[-1]) + "==>" + str(evaluate(buildParseTree(output))))
        output_file.write("\n")
        output_file.write(str(array[-1]) + "==>" + str(evaluate(buildParseTree(output))))

        if len(array) == length:
            print("\n>>>Evaluation and sorting completed!\n")
        
class mainPrograme:
    def __init__(self,choice=None):
        self.choice = choice
    def validateExpression(self):
        expression = input("Please enter the expression you want to evaluate:\n")
        expClass = expressionValidator(expression)
        output = expClass.runEntirePrograme()
        if output == None:
            print("Invalid Expression")
            return self.validateExpression()
        else:
            return [output,expression]
    def evaluateExpression(self):
        exp = self.validateExpression()
        tree = buildParseTree(exp[0])
        tree.printPreorder(0)
        # if isinstance(evaluate(tree),float) == False:
        try:
            print (f'The expression: {exp[1]} evaluates to: {evaluate(tree)}')
        except ZeroDivisionError:
            print (f'The expression: {exp[1]} cannot be evaluated! Zero Division Error.\n\nNumber cannot be divided by/with zero, result is infinite.')
            return tree.getKey()
        os.system('pause')

    
    def sortExpression(self,output_choice,input_file,output_file):
        array = []
        try:
            with open(str(input_file),'r') as input_file:
                for line in input_file:
                    array.append(line.replace("\n",""))
                try:
                    # print(array)
                    mergeSort(array,output_choice)
                    try:
                        recursive(array,len(array),str(output_file))
                    except:
                        print("Invalid output file")
                        print("Please try again.\n")
                        self.runSortandEvaluate()
                except:
                    print("Invalid expression in input file!")
                    return
        except:
            print("Invalid input file!")
            print("Please try again.\n")
            self.runSortandEvaluate()
        os.system('pause')

    def runSortandEvaluate(self):
        self.sortExpression(self.getOutput_Choice(), self.getInput_file(), self.getOutput_file())
    def exit(self):
        print("Bye, thanks for using ST107 DSAA: Expression Evaluator & Sorter")
    
    def checkChoice(self,chosen_choice):
        try:
            validate_choice = int(chosen_choice)
            if 1 <= validate_choice <= 3:
                return validate_choice
            else:
                print("Input is not part of the above options")
                return self.getChoice()
        except ValueError:
            print("Input is invalid")
            return self.getChoice()
            # return

    def check_outputChoice(self,output_choice):
        try:
            validate_outputchoice = int(output_choice)
            if 0 < validate_outputchoice < 3:
                return validate_outputchoice
            else:
                print("Input is not part of the above options")
                return self.getOutput_Choice()
        except ValueError:
            print("Input is not invalid")
            return self.getOutput_Choice()
            # return
    
    def getChoice(self):
        chosen_choice = input("\nPlease select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: ")
        # print(self.checkChoice(chosen_choice))
        return self.checkChoice(chosen_choice)
        # return chosen_choice
    def getOutput_Choice(self):
        output_choice = input("\n(1) Ascending\n(2) Descending\nSelect choice:")
        return self.check_outputChoice(output_choice)
    def getInput_file(self):
        input_file = input("\nPlease enter input file:")
        return input_file
    def getOutput_file(self):
        output_file = input("Please enter output file:")
        return output_file
    def runChoice(self,choice):
        programeArray = [self.evaluateExpression, self.runSortandEvaluate, self.exit]
        programeArray[choice-1]()
        if choice == 3:
            return
        self.runChoice(self.getChoice())
    
    def printIntroduction(self):
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

def buildParseTree(exp):
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
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree() 
        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '/', '**']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '/', '**', ')'] :
            currentTree.setKey(float(t))
            parent = stack.pop()
            currentTree = parent
        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

main_programme = mainPrograme()

def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()
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
        return tree.getKey()
# main = mainPrograme()
# main.printIntroduction()
# chosen_choice = main.getChoice()
# main.runChoice(chosen_choice)










# main = mainPrograme()
# main.printIntroduction()
# chosen_choice = main.getChoice()
# main.runChoice(chosen_choice)

# class BinaryTree:
#     def __init__(self,key, leftTree = None, rightTree = None):
#         self.key = key
#         self.leftTree = leftTree
#         self.rightTree = rightTree
#     def setKey(self, key):
#         self.key = key
#     def getKey(self):
#         return self.key
#     def getLeftTree(self):
#         return self.leftTree
#     def getRightTree(self):
#         return self.rightTree
#     def insertLeft(self, key):
#         if self.leftTree == None:
#             self.leftTree = BinaryTree(key)
#         else:
#             t =BinaryTree(key)
#             self.leftTree , t.leftTree = t, self.leftTree
#     def insertRight(self, key):
#         if self.rightTree == None:
#             self.rightTree = BinaryTree(key)
#         else:
#             t =BinaryTree(key)
#             self.rightTree , t.rightTree = t, self.rightTree
            
#     def printPreorder(self, level):
#         print( str(level*'-') + str(self.key))
#         if self.leftTree != None:
#             self.leftTree.printPreorder(level+1)
#         if self.rightTree != None:
#             self.rightTree.printPreorder(level+1) 


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



# def buildParseTree(exp):
#     tokens = exp.split()
#     stack = Stack()
#     tree = BinaryTree('?')
#     stack.push(tree)
#     currentTree = tree
#     for t in tokens:
#         # RULE 1: If token is '(' add a new node as left child
#         # and descend into that node
#         if t == '(':
#             currentTree.insertLeft('?')
#             stack.push(currentTree)
#             currentTree = currentTree.getLeftTree() 
#         # RULE 2: If token is operator set key of current node
#         # to that operator and add a new node as right child
#         # and descend into that node
#         elif t in ['+', '-', '*', '/']:
#             currentTree.setKey(t)
#             currentTree.insertRight('?')
#             stack.push(currentTree)
#             currentTree = currentTree.getRightTree()
#         # RULE 3: If token is number, set key of the current node
#         # to that number and return to parent
#         elif t not in ['+', '-', '*', '/', ')'] :
#             currentTree.setKey(int(t))
#             parent = stack.pop()
#             currentTree = parent
#         # RULE 4: If token is ')' go to parent of current node
#         elif t == ')':
#             currentTree = stack.pop()
#         else:
#             raise ValueError
#     return tree
# def evaluate(tree):
#     leftTree = tree.getLeftTree()
#     rightTree = tree.getRightTree()
#     op = tree.getKey()
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
#         return tree.getKey()