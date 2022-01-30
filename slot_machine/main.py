import random
import datetime
import extended_slot_features as esf


def main():
    random.seed(datetime.datetime.now())
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chances = [10, 10, 10, 10, 10, 10, 5, 10, 10]

    esf.get_user_input("Are you of legal gambling age (y/n): ")

    esf.animated_title()
    esf.clear_console()
    print("Generating numbers...")
    esf.line_animation(5, 0.2)

    rand_nums = esf.pick_numbers(numbers, chances)
    rand_nums = esf.create_board(rand_nums, numbers)

    esf.clear_console()
    input("PRESS ENTER TO SPIN!!")
    esf.animate_slots(rand_nums, 0.1)

    if rand_nums[0] == rand_nums[1] == rand_nums[2]:
        print("YOU WIN!!")
    else:
        print("You lose :(")

    esf.get_user_input("Run simulation (y/n): ")
    iterations = 0
    try:
        iterations = int(input("How many iterations: "))
        if iterations <= 0:
            raise ValueError("Not a valid input!")
    except ValueError as err:
        print(err)
        exit(1)

    win_counter = 0
    lose_counter = 0

    for iteration in range(iterations):
        rand_nums = esf.pick_numbers(numbers, chances)
        rand_nums = esf.create_board(rand_nums, numbers)
        if rand_nums[0] == rand_nums[1] == rand_nums[2]:
            print("YOU WIN!!", end=" ")
            print(rand_nums[0:3])
            win_counter += 1
        else:
            print("You lose :(", end=" ")
            print(rand_nums[0:3])
            lose_counter += 1

    print(f'WINS:\t{win_counter}\nLOSES:\t{lose_counter}')


if __name__ == '__main__':
    main()
