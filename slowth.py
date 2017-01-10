import time
import re
from random import uniform


def slowth(string, debug=False):
    '''
    Takes a string and outputs it to console in a manner that somewhat mimics typing / the rhythm of speech.
    :param string:
    :return:
    '''

    if debug:
        return string + '\n'


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
            time.sleep(uniform(0, 0.08))
            counter += 1

    return '\n'
