#searching
#sorting

# !problem 1
#input

user_input = [1,2,3,4,5,6,7,8,9,11]

# ?Q: Check to see if a certain number exist in the user input array

n = 11

#linear search

result = False 
for e in user_input:
    if e == n:
        result = True
if result == True:
    print('Found')
else:
    print('Not Found')


#for e in user_input:
    #if e == n:
        #print('found')
   # else:
      #  print('Not found')

#if else, for loops, print, calculations (+, -)
    
# Time: o(n)
input = [1,2,3,4,5,6,7,8,9,10]
for i in input:
    print('hi')
    if i == 1: #o(1)
        
