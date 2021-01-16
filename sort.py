# input_file = input("Please enter input file: ")
# output_file = input("Please enter output file: ")


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
        print('merge', l)



array = []
with open("input.txt",'r') as input_file:
    for line in input_file:
        array.append(line.replace("\n",""))
# print(array)
mergeSort(array)
# print(array)
recursive(array,len(array))

def recursive(array,length):
    with open("output.txt","a") as output_file:
        if len(array)== 1:
            print("\n>>>Evaluation and sorting started:")
            print("\n*** Expressions with value=> " + str(eval(array[-1])))
            output_file.write("*** Expressions with value=> " + str(eval(array[-1])))
            print(str(array[-1]) + "==>" + str(eval(array[-1])))
            output_file.write("\n")
            output_file.write(str(array[-1]) + "==>" + str(eval(array[-1])))
            return

        recursive(array[:-1],length)
    
        if eval(array[-2]) != eval(array[-1]):
            print("\n*** Expressions with value=> " + str(eval(array[-1])))
            output_file.write("\n")
            output_file.write("\n*** Expressions with value=> " + str(eval(array[-1])))
    
        print(str(array[-1]) + "==>" + str(eval(array[-1])))
        output_file.write("\n")
        output_file.write(str(array[-1]) + "==>" + str(eval(array[-1])))

        if len(array) == length:
            print("\n>>>Evaluation and sorting completed!")


############################### Reversed Incomplete #####################################
# def recursive(array, length):
#     if len(array == 0):
#         return
#     if length == len(array):
#         print(">>>Evaluation and sorting started:")
#         print("\n*** Expressions with value= " + str(eval(array[0])))
#     elif eval(array[0]) != eval(array[1]):
#         print("\n*** Expressions with value= " + str(eval(array[i])))
#     print(str(array[0]) + "==>" + str(eval(array[0])))
#     recursive(array[1:])

############################### ORIGINAL #####################################

# def recursive(array):
#     if len(array)== 1:
#         print("\n>>>Evaluation and sorting started:")
#         print("\n*** Expressions with value= " + str(eval(array[-1])))
#         return
#     if eval(array[-2]) != eval(array[-1]):
#         recursive(array[:-1])
#         print("\n*** Expressions with value= " + str(eval(array[-1])))
#         print(str(array[-1]) + "==>" + str(eval(array[-1])))
#     else:
#         recursive(array[:-1])
#         print(str(array[-1]) + "==>" + str(eval(array[-1])))


