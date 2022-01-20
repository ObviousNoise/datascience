import math
number = int( input ("pick a number between one and ten "))
count = int(input("How many times would you like me to print your number? "))
if number > 10:
    print("you idiot, the number is supposed to be between one and ten")
    exit
if number < 1:
    print("you idiot, the number is supposed to be between one and ten")
else:
    print("good job you can follow directions")
    print(f"I will now print your number {count} times")
    for i in range(count):
        print(number)
