#Slot Machine For Underaged Gambling
import math
import random
import os
import time
import random
#cleans up the terminal
os.system('cls' if os.name == 'nt' else 'clear')
#Actual code starts here
underage = input("are you of the legal gambling age in your state? ")
if underage == ("no"):
    print ("Perfect, Starting young.")
if underage == ("yes"):
    print("Aight Bet")

time.sleep(3)

print("_____________________________________")
print("""\
 ________________________________   
| we're going to have some fun...|
\ _______________________________/
       
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||      |
                    """  )
print("_____________________________________")

#this waits before clearing the loading screen no matter the OS
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
#Now for the game
gameon = ("true")
while gameon == ("true"):
    input("Press enter to pull the lever")


    timerend = time.time() + 3
    while time.time() < timerend:
        print('-----------------------------------------')
        time.sleep(0.07)
        print("=========================================")
        time.sleep(0.07)
        print("_________________________________________")
        time.sleep(0.07)

    os.system('cls' if os.name == 'nt' else 'clear')

    #now we reveal the numbers
    #slotnumber1 = (1)
    #slotnumber2 = (1)
    #slotnumber3 = (1)
    slotnumber1 = random.randrange(10)
    slotnumber2 = random.randrange(10)
    slotnumber3 = random.randrange(10)
    slotnumber4 = random.randrange(10)
    slotnumber5 = random.randrange(10)
    slotnumber6 = random.randrange(10)
    slotnumber7 = random.randrange(10)
    slotnumber8 = random.randrange(10)
    slotnumber9 = random.randrange(10)

    print("-")
    print("-")
    print (f"    |{slotnumber4}|-----|{slotnumber5}|-----|{slotnumber6}|")
    time.sleep(0.15)
    print (f"--->|{slotnumber1}|-----|{slotnumber2}|-----|{slotnumber3}|<--- ")
    time.sleep(0.15)
    print (f"    |{slotnumber7}|-----|{slotnumber8}|-----|{slotnumber9}|")
    time.sleep(0.50)
    if slotnumber3 == slotnumber2 == slotnumber1:
        print("You Must Do this a lot. You should probrobly stop")
    else:
        print("You lost because you suck, and thats ok ")
        time.sleep(0.5)
       

    UI = input("do you want to play again Y or N ")

    #Spencer said to do the lists like this bc it makes the code look bigger

    if UI == ("N"):
        gameon = ("false")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("n"):
        gameon = ("false")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("no"):
        gameon = ("false")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("No"):
        gameon = ("false")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("y"):
        randpopup = random.randrange(10)
        if randpopup == (10):
            print("someone knows what a good time is")
            time.sleep(1.5)
            gameon = ("true")
        else: 
            gameon = ("true")
    if UI == ("Y"):
        randpopup = random.randrange(10)
        if randpopup ==(10):
            print("someone knows what a good time is")
            time.sleep(1.5)
            gameon = ("true")
        else:
            gameon = ("true")













