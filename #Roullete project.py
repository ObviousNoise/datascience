#Roullete project
from contextlib import redirect_stderr
import random
#roullete
number = int(input("What number 1 through 10? "))
gnumber = int(random.randrange(10))
color = input("Pick a color black, or red?")
grandc = int(random.randrange(2))
if grandc == 1: 
    gcolor = ("red")
else:
    gcolor = ("black")
print(f"the number is {gnumber}")
print(f"the color is {gcolor}")



if gnumber == number:
    print("You win!")
else:
    print("You lose :(") 

