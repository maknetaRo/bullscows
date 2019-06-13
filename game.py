from random import sample, shuffle

def random_numbers():
    random_nums = sample(range(0,9), 4)
    if random_nums[0] == 0:
        shuffle(random_nums)
    return random_nums


def count_cows(nums, nums_input):
    cows = 0
    for num in nums_input:
        if num in nums:
            cows += 1
    return cows

def count_bulls(nums, nums_input):
    bulls = 0
    for i in range(len(nums_input)):
        if nums_input[i] == nums[i]:
            bulls += 1
    return bulls

def play_again():
    play_again = input("Play again: y/n")
    while play_again == 'y':
        play_game()

def play_game():
    random_nums = random_numbers()
    score = 0
    for i in range(7):
        print("Enter 4 different numbers from 0 to 9.")
        num1 = int(input("> "))
        num2 = int(input("> "))
        num3 = int(input("> "))
        num4 = int(input("> "))
        nums_input = [num1, num2, num3, num4]
        cows = count_cows(random_nums, nums_input)
        bulls = count_bulls(random_nums, nums_input)
        print(f"Your numbers are: {num1} {num2} {num3} {num4}.")
        print(" There are {cows} cows(exist) and {bulls} bulls(match).")
        if bulls == 4:
            score += 1
            print("You won.")
            break

    play_again()

play_game()
