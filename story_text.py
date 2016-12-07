import time
import re
from random import uniform

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



intro = "The gates of the city loom up out of the early morning mist rising from the river. You step off the boat and " \
          "walk down the wharf through the great stone archway and into the city. The people here do not look like you, " \
          "and you pull your hood up over your head, keenly aware of your difference. As you do so, a voice suddenly calls out - "

journey_to_door = "You turn to look back towards the city gates, and when you turn again to face your advisor, she is gone. " \
                  "\"Of course she's gone,\" you think. \"And it'll bite me in the ass later that I didn't thank her.\" But " \
                  "you head back to the gates all the same. It seemed like you'd gone only a few strides into the city, " \
                  "but somehow getting back to the gates takes a long time. " \
                  "Sure enough, completely ignored or unnoticed by the throngs of sellers, buyers, traders, and hawkers " \
                  "streaming in and out of the gates, is a small wooden door. It is set into the wall a mere 10 feet from the left gate. " \
                  "On it is an inscription:"
