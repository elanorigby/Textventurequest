import random
from slowth import slowth

def scramble_it(word):
    """
    Takes a word and returns a scrambled version of it as a list.
    :param word:
    :return:
    """
    return random.sample(word, len(word))


def guess(word):
    """
    Takes guesses as to what a scrambled word is and checks against the answer.
    Must get it right to pass.
    :param word:
    :return:
    """
    answer = input("> ")

    if answer.lower().strip() != word.lower():
        print("The way is shut. \n")
        guess(word)
    else:
        print(slowth("\nWith a small click, the door unlocks itself."))


def word_scramble():
    word_list = ["yoghurt", "yogurt", "donut", "doughnut"]
    word = random.choice(word_list)
    print("~Solve the riddle of the ancients and speak the password.~\n")
    print(scramble_it(word))
    guess(word)


if __name__ == '__main__':
    word_scramble()
