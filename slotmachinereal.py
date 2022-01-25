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

time.sleep(1)

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
    list1 = ['1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','8','9','1','2','3','4','5','6','1','2','3','4','1','2'];
    
    #slotnumber1 = (1)
    #slotnumber2 = (1)
    #slotnumber3 = (1)
    slotnumber1 = random.choice(list1)
    slotnumber2 = random.choice(list1)
    slotnumber3 = random.choice(list1)
    slotnumber4 = random.choice(list1)
    slotnumber5 = random.choice(list1)
    slotnumber6 = random.choice(list1)
    slotnumber7 = random.choice(list1)
    slotnumber8 = random.choice(list1)
    slotnumber9 = random.choice(list1)

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
       

    UI = input("do you want to play again Y or N? ")

    #Spencer said to do the lists like this bc it makes the code look bigger
    #this just does the various ways some one could say yes or no
    if UI == ("N"):
        gameon = ("false")
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("n"):
        gameon = ("false")
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("no"):
        gameon = ("false")
        print("You italian sausage")
        time.sleep(3)
        exit
    if UI == ("No"):
        gameon = ("false")
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
#code for mass simulations and asks the user how many times they want to simulate
    if UI == ("sim"):
        onecount = (0)
        twocount = (0)
        threecount = (0)
        fourcount = (0)
        fivecount = (0)
        sixcount = (0)
        sevencount = (0)
        eightcount = (0)
        ninecount = (0)
        wincount = (0)
        loosecount = (0)
        print("super sim mode enabled")
        playnum = int(input("how many times do you want to simulate?"))
        for counter in range(playnum):
#code to actually run the game
            print("-")
            slotnumber1 = int(random.choice(list1))
            slotnumber2 = int(random.choice(list1))
            slotnumber3 = int(random.choice(list1))
            slotnumber4 = int(random.choice(list1))
            slotnumber5 = int(random.choice(list1))                
            slotnumber6 = int(random.choice(list1))
            slotnumber7 = int(random.choice(list1))
            slotnumber8 = int(random.choice(list1))
            slotnumber9 = int(random.choice(list1))
            print (f"    |{slotnumber4}|-----|{slotnumber5}|-----|{slotnumber6}|")
            print (f"--->|{slotnumber1}|-----|{slotnumber2}|-----|{slotnumber3}|<--- ")
            print (f"    |{slotnumber7}|-----|{slotnumber8}|-----|{slotnumber9}|")
            #modified versions of the if staetemnts to run the sims and count totals
            if slotnumber3 == slotnumber2 == slotnumber1:
               print("Win")
               wincount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (1):
                onecount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (2):
                twocount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (3):
                threecount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (4):
                fourcount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (5):
                fivecount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (6):
                sixcount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (7):
                sevencount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (8):
                eightcount += 1
            if slotnumber3 == slotnumber2 == slotnumber1 == (9):
                ninecount += 1
                
                   
            else:
                print("Lose")
                loosecount += 1
#printstatements for the stats                
        print ("Total Wins")
        print (wincount)
        time.sleep(0.5)
        print()
        print ("Total loses")
        print (loosecount)
        print()
        print ("number of Ones")
        print (onecount)
        print()
        print ("Number of Twos")
        print (twocount)
        print()
        print ("Number of Threes")
        print (threecount)
        print()
        print ("Number of Fours")
        print (fourcount)
        print()
        print ("Number of Fives")
        print (fivecount)
        print()
        print ("Number of Sixes")
        print (sixcount)
        print()
        print ("Number of Sevens")
        print (sevencount)
        print()
        print ("Number of Eights")
        print (eightcount)
        print()
        print ("Numer of Nines")
        print (ninecount)
        