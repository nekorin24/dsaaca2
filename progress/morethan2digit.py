class Stack:

    def __init__(self):
        self.__list= []
    def isEmpty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)

    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)

    def pop(self): # popTail
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    
    def getList(self):
        return self.__list
    
    def __str__(self):
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1 :
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output



class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
    def setKey(self, key):
        self.key = key
    def getKey(self):
        return self.key
    def getLeftTree(self):
        return self.leftTree
    def getRightTree(self):
        return self.rightTree
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.leftTree = t, self.rightTree
            t.rightTree = BinaryTree('?')
            
    def printPreorder(self, level):
        print( str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 



import re
def buildParseTree(exp):
    tokens = exp.split()
#     exp = exp.replace(" ","")
#     number_or_symbol = re.compile('(-?\d+\.\d+|\w+|[()\-+*/^])')
#     number_or_symbol = re.compile('([-+]?\d+\.\d+|[-]?[0-9]+|[**]+|[()\-+*/^])')
#     tokens = re.findall(number_or_symbol, exp)
    print(tokens)
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
