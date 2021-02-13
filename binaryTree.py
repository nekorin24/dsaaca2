# aoyang
# Binary Tree class
class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
    # Set key of tree
    def set_key(self, key):
        self.key = key
    # Get Key
    def get_key(self):
        return self.key
    # Retrieve left tree
    def get_left_tree(self):
        return self.leftTree
    # Retrieve right tree
    def get_right_tree(self):
        return self.rightTree
    # Insert into left tree
    def insert_left(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
    # Insert into right tree
    def insert_right(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.leftTree = t, self.rightTree
            t.rightTree = BinaryTree('?')
    # Print in preorder
    def print_preorder(self, level):
        print( str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.print_preorder(level+1)
        if self.rightTree != None:
            self.rightTree.print_preorder(level+1) 

    def print_postorder(self, level):
        #left >right >root
        if self.leftTree != None:
            self.leftTree.print_postorder(level+1)
        if self.rightTree != None:
            self.rightTree.print_postorder(level+1)
        print( str(level*'-') + str(self.key))
