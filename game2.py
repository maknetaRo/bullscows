from random import randrange, randint, choice, sample

def random_elements():
    number = randint(3, 9)
    kind = randint(0,1)
    if kind == 0:
        random_elements = [randint(1, 10) for num in range(3,10)]
    else:
        alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
        random_elements = [choice(alphabet) for elem in range(0, number)]
    return random_elements

def count_bulls(elements, elements_input):
    bulls = 0
    for i in range(len(elements_input)):
        if elements_input[i] == elements[i]:
            bulls += 1
    return bulls

def count_cows(elements, elements_input):
    cows = 0
    for i in range(len(elements_input)):
        if (elements_input[i] != elements[i]) and (elements_input[i] in elements):
            cows += 1
    return cows


def get_input(random_elements):
    secret_guesses = []
    if all(isinstance(n, int) for n in random_elements):
        print("Enter {} numbers from 1 to 9 (one digit per input)".format(len(random_elements)))
        for elem in range(len(random_elements)):
            elem = int(input(">"))
            secret_guesses.append(elem)
    else:
        print("Enter {} letters (one letter per input)".format(len(random_elements)))
        for elem in range(len(random_elements)):
            elem = input(">").lower()
            secret_guesses.append(elem)
    return secret_guesses

def play_game(secret_guesses):

    for elem in range(7):
        get_input(secret_guesses)
        cows = count_cows(random_elements, secret_guesses)
        bulls = count_bulls(random_elements, secret_guesses)
        print("Your elements are: {}".format(secret_guesses))
        print("Bulls: {}, cows: {}.".format(bulls, cows))
