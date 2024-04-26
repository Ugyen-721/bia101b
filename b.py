def input_str(input_string):
    floor_at_end = 0
    for i in input_string:
        if i == '(':
            floor_at_end += 1
        elif i == ')':
            floor_at_end -= 1
    print('At the end, you will be at floor number:', floor_at_end)

input_str(input('Enter Brackets: '))

#Task 2
# Given a set of open and close brackets
# check to see if the input is valid
# Example 
# ((()))
# output: true
# Example ()(()) False

input_str = ")()()()()()))))()()()"
stack = []

for i in input_str:
    if i == "(":
        stack.append(i)
    if i == ")":
        stack.pop()

length = len(stack)
if length != 0:
    print('True')
else:
    print('False')