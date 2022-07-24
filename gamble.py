import random
answer = random.randint(1, 2)
red = "red"
black = "black"
Red = "red"
Black = "black"
RED = 'red'
BLACK = "black"
if(answer == 1):
    gamble = "red"
if(answer == 2):
    gamble = "black"
#print(answer)
human = input("Will Red or Black win?\n")
if(human.lower() == gamble):
    print("You win, the answer WAS "+gamble+"!")
if(human.lower() != gamble):
    print("You lose, the answer was "+gamble+"!")
    