# ! check if user can vote
# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
# ?if else statement
# ?if above 18, print "You can vote" 
# ?if below 18, print "You canot vote"

age = int(input("Enter your Age: "))

if age >= 18:
    print('You van Vote')

elif age < 18:
    print("You cannot Vote")