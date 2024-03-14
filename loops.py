# loop over an array
fruits = ['a', 'b', 'c']

# loop through each evelement
# at each stage, if the element is 'c'
# print true
for e in fruits: #1.e = 'a', 2.e = 'b', 3.e = 'c'
    if e == 'c':
        print('True')
    if e == 'b':
        print('True')

# # Iterate over a string
greeting = "Hello"
for char in greeting:
    print(char)
# Exercise: check if the string contains vowel

#iterate over a range
for i in range(14):
    print(i) #output: 5,6,7,8,9,10,11,12,13
    val = i + 5
    print(val)

#while loop
count = 0
while count < 5:
    print(count)
    count = count + 1  #output: 0,1,2,3,4

    
# user input string is unknown
# print every char of the string
s = 'helloabc'
counter = 0
lenth_s = len(s)
print('coutner:', counter)
print('len s:', lenth_s)
# 0 , 1 , 2, 3, 
print('going in loop')
while counter < lenth_s:
    print('counter:', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('-----')
