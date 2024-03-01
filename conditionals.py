#Objective = make a calculator application made using variable and if statements

#1.get input from the user
#2.do calculation based on userinput
#2.1 check what string did user typed
#2.2 if user string ==* then
#3.Give output to the user


print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')
