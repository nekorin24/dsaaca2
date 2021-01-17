import os
from expressionValidator import expressionValidator
from stack import Stack
from binaryTree import BinaryTree
# choice = int(input("Please select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: "))
# class.runfunction(choice-1)
def mergeSort(l):
    if len(l) > 1:
        mid = int (len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        leftIndex,rightIndex,mergeIndex = 0,0,0
        mergeList = l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if eval(leftHalf[leftIndex]) == eval(rightHalf[rightIndex]):
                if len(leftHalf[leftIndex]) < len(rightHalf[rightIndex]):
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
            else:
                if eval(leftHalf[leftIndex]) < eval(rightHalf[rightIndex]):
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
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
        if len(array)== 1:
            print("\n>>>Evaluation and sorting started:")
            print("\n*** Expressions with value=> " + str(eval(array[-1])))
            output_file.write("*** Expressions with value=> " + str(eval(array[-1])))
            print(str(array[-1]) + "==>" + str(eval(array[-1])))
            output_file.write("\n")
            output_file.write(str(array[-1]) + "==>" + str(eval(array[-1])))
            return

        recursive(array[:-1],length,output_file_edit)
    
        if eval(array[-2]) != eval(array[-1]):
            print("\n*** Expressions with value=> " + str(eval(array[-1])))
            output_file.write("\n")
            output_file.write("\n*** Expressions with value=> " + str(eval(array[-1])))
    
        print(str(array[-1]) + "==>" + str(eval(array[-1])))
        output_file.write("\n")
        output_file.write(str(array[-1]) + "==>" + str(eval(array[-1])))

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
            self.validateExpression()
        else:
            return output
    def evaluateExpression(self):
        exp = self.validateExpression()
        # print("sds")
        # print(exp)
        # expression = input("Please enter the expression you want to evaluate:\n")
        # expClass = expressionValidator("(((1+2)/3)*5)")
        # if expClass.runEntirePrograme() == None:
        #     print("Invalid output file")
        # print("evaluateExpression")
        # expression 
        # exp = expression
        tree = buildParseTree(exp)
        tree.printPreorder(0)
        print (f'The expression: {exp} evaluates to: {evaluate(tree)}')

    
    def sortExpression(self,input_file,output_file):
        array = []
        try:
            with open(str(input_file),'r') as input_file:
                for line in input_file:
                    array.append(line.replace("\n",""))
            try:
                mergeSort(array)
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
        self.sortExpression(self.getInput_file(), self.getOutput_file())
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
            print("Input is not a valid")
            return self.getChoice()
            # return
    
    def getChoice(self):
        chosen_choice = input("\nPlease select your choice ('1','2','3'):\n1. Evaluate expressions\n2. Sort expression\n3. Exit\nEnter choice: ")
        # print(self.checkChoice(chosen_choice))
        return self.checkChoice(chosen_choice)
        # return chosen_choice
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
        admission = [1839045,1234567,1234567]
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
            if currentTree.getKey() == '?':
                currentTree.setKey(t)
                currentTree.insertRight("?")
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
            else:
                currentTree.insertRight(t)
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
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