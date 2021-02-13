# Stack class
class Stack:

    def __init__(self):
        self.__list= []
    # Check class if it is empty
    def isEmpty(self):
        return self.__list == []
    # Check size of list
    def size(self):
        return len(self.__list)
    # Clear list
    def clear(self):
        self.__list.clear()
    # Push or add item to list
    def push(self, item):
        self.__list.append(item)
        
    # Pop tail o list
    def pop(self): # popTail
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    # Get the last element of list
    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    # Get entire list
    def getList(self):
        return self.__list
    # Print output of item
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
