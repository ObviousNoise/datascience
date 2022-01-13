import math
number = int( input ("pick a number between one and ten "))
if number > 10:
    print("you idiot, the number is supposed to be between one and ten")
    exit
if number < 1:
    print("you idiot, the number is supposed to be between one and ten")
else:
    print("good job you can follow directions")
    print("I will now print your number 10 times")
    for i in range(10):
        print(number)
