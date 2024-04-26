class Dog:
    def __init__(self,Name,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color
        self.Name = Name

    def bark(self):
        print("Woof! Woof!")

    def sleep(self):
        print("Zzzz...")

    def eat(self):
        print("Nom nom nom!")
    
    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def run(self,speed):
        print('Okay, i will run in ' + str(speed) + 'Km/hr')
#Task 1
    def introduce(self):
        print("Hi")
        print("I am a " + str(self.breed) + " dog")
        print("I am " + str(self.age) + " years old")
        print("I am " + str(self.color) + " in color")
        

dog = Dog('Domchu','Bhutanese',20,'Black')
petdog = Dog('lal','Pug',10,'White')
myfriendDog = Dog('Dell','German Shepard',10,'Brown')


class Cat:
    def __init__(self,Name,species,age,home):
        self.species = species
        self.age = age
        self.home = home
        self.Name = Name

    def hunt(self):
        print("Slashhhh")

    def sleep(self):
        print("Zzzz...")

    def eat(self):
        print("Nom nom nom!")
    
    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def introduce(self):
        print("Hi")
        print("I am a " + str(self.breed) + " ")
        print("I am " + str(self.age) + " years old")
        print("I am " + str(self.color) + " in color")