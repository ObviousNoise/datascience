from time import sleep
from os import system, name
import random


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pick_numbers(nums, weights):
    return random.choices(nums, weights, k=3)


def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def animated_title():
    sleep(.5)
    for x in range(9):
        print("\r--Get ready to spin!!--", end='')
        sleep(0.3)
        print("\r//Get ready to spin!!//", end='')
        sleep(0.3)
    print('\n')


def animate_slots(nums, time_to_sleep):
    for x in range(10):
        sleep(time_to_sleep)
        clear_console()
        print(f"\t-- [{random.randint(0, 9)}] || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --\n"
              f"\t-- [{random.randint(0, 9)}] || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --\n"
              f"\t-- [{random.randint(0, 9)}] || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --")
    for x in range(10):
        sleep(time_to_sleep)
        clear_console()
        print(f"\t-- {Colors.OKGREEN}[{nums[3]}]{Colors.ENDC} || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --\n"
              f"\t-- {Colors.OKGREEN}[{nums[0]}]{Colors.ENDC} || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --\n"
              f"\t-- {Colors.OKGREEN}[{nums[6]}]{Colors.ENDC} || [{random.randint(0, 9)}] || [{random.randint(0, 9)}] --")
    for x in range(10):
        sleep(time_to_sleep)
        clear_console()
        print(f"\t-- {Colors.OKGREEN}[{nums[3]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[4]}]{Colors.ENDC} || [{random.randint(0, 9)}] --\n"
              f"\t-- {Colors.OKGREEN}[{nums[0]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[1]}]{Colors.ENDC} || [{random.randint(0, 9)}] --\n"
              f"\t-- {Colors.OKGREEN}[{nums[6]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[7]}]{Colors.ENDC} || [{random.randint(0, 9)}] --")

    sleep(time_to_sleep)
    clear_console()
    print(f"\t-- {Colors.OKGREEN}[{nums[3]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[4]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[5]}]{Colors.ENDC} --\n"
          f"\t-- {Colors.OKGREEN}[{nums[0]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[1]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[2]}]{Colors.ENDC} --\n"
          f"\t-- {Colors.OKGREEN}[{nums[6]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[7]}]{Colors.ENDC} || {Colors.OKGREEN}[{nums[8]}]{Colors.ENDC} --")


def line_animation(repeat, wait):
    for x in range(repeat):
        print("\r"+"|"*20, end='')
        sleep(wait)
        print("\r"+"-" * 20, end='')
        sleep(wait)


def create_board(rand_nums, numbers):
    for num in range(len(rand_nums)):
        if (rand_nums[num] + 1) > 9:
            rand_nums.insert(num + 3, numbers[0])
        else:
            rand_nums.insert(num + 3, rand_nums[num] + 1)

        if (rand_nums[num] - 1) < 1:
            rand_nums.insert(num + 6, numbers[-1])
        else:
            rand_nums.insert(num + 6, rand_nums[num] - 1)
    return rand_nums


def get_user_input(prompt):
    try:
        user_input = str(input(prompt)).capitalize()
        if user_input != 'Y' and user_input != 'N' and user_input != 'Yes' and user_input != "No":
            raise ValueError("Not a valid input!")
        if user_input == 'N':
            exit(0)
    except ValueError as err:
        print(err)
        exit(1)
