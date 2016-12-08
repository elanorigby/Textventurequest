import time
import re
from random import uniform


def slowth(string):
    counter = 0
    for letter in string:
        if re.findall(r'[,\.\s]', letter) and counter >= 100:
            print(letter)
            counter = 0
        elif re.findall(r'[,\.]', letter):
            print(letter, end='', flush=True)
            time.sleep(uniform(0.4, 0.6))
            counter += 1
        else:
            print(letter, end='', flush=True)
            time.sleep(uniform(0, 0.1))
            counter += 1

    return '\n'








# ye olde slowthe

# def slowth(string):
#     counter = 0
#     for letter in string:
#         if counter >= 90:
#             print(letter)
#             counter = 0
#         else:
#             print(letter, end='', flush=True)
#             time.sleep(uniform(0, 0.1))
#             counter += 1
#
#     return ' \n'

