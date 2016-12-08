import random
from slowth import slowth

def scramble_it(word):
    '''
    Takes a word and returns a scrambled version of it as a list.
    :param word:
    :return:
    '''
    letter_list = list(word)
    # print(letter_list)
    len_list = list(range(0, len(letter_list)))
    # print(len_list)

    scramble_list = []
    initial_len = len(len_list)

    for i in range(0, initial_len):
        idx = random.choice(len_list)
        len_list.remove(idx)
        scramble_list.append(letter_list[int(idx)])

    return scramble_list


def guess(word):
    '''
    Takes guesses as to what a scrambled word is and checks against the answer.
    Must get it right to pass.
    :param word:
    :return:
    '''
    answer = input("~Solve the riddle of the ancients and speak the password.~\n")
    if answer.lower().strip() != word.lower():
        print("The way is shut.")
        guess(word)
    else:
        print(slowth("\nWith a small click, the door unlocks itself."))


def word_scramble():
    word_list = ["yoghurt", "yogurt", "donut", "doughnut"]
    word = random.choice(word_list)
    # print(word)
    scramble = scramble_it(word)
    print("~*~")
    print(scramble)
    guess(word)
