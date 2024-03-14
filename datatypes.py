# crearyion of array
array1 = [1,2,3,"thimphu",2.5]

#retrieving
element1 = array1[0]
element2 = array1[4]
lastElement = array1[-1]
print(lastElement)

print(array1)
#modifying element
array1[0] = 10
print(array1)

#getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)

#slicing
elements = array1[0:3]
print(elements)

arr1 = [1,2]
arr2 = ['thimphu','wangdue']
arr3 = arr1 + arr2
print(arr3)

#adding
arr = [1,2,3]
arr.append(4)
print(arr)

#insert at a specific index
arr.insert(1,10) # [1,10,2,3,4]
print(arr)

#adding to stack
stackVar = []
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1)
print(' After appending', stackVar)
element = stackVar.pop()
print("after appending", stackVar)
print("removed element", element)