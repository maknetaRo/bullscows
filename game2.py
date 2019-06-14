from random import randrange, randint, choice, sample

def random_numbers():
    number = randint(3, 9)
    random_numbers = sample(range(1,9), number)
    return random_numbers

def random_letters():
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    number = randint(3, 9)
    random_letters = sample(alphabet, number)
    return random_letters

def count_bulls(nums, nums_input):
    bulls = 0
    for i in range(len(nums_input)):
        if nums_input[i] == nums[i]:
            bulls += 1
    return bulls

def count_cows(nums, nums_input):
    cows = 0
    for i in range(len(nums_input)):
        if (nums_input[i] != nums[i]) and (nums_input[i] in nums):
            cows += 1
    return cows

def play_game():
    kind = randint(0,1)
    if kind == 0:
        secret = random_numbers()
    else:
        secret = random_letters()
    return secret

    # bulls = 0
    # cows =  0
    # print("Bulls: {}, cows: {}.".format(bulls, cows))
