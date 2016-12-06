import sys
import story_text
from quotize import quotize
from word_scramble import word_scramble


def dec_quotize(f):
    def wrapper():
        return '"' + f() + '"'
    return wrapper


def get_name():
    name = input("What is your name, wanderer?").strip().capitalize()
    return name


def greet(name):
    return input(quotize("Well met, {}. We rarely see strangers here. Where are you from?".format(name))).strip().capitalize()


def offer_quest(name, homeland):
    answer = input(quotize("{homeland} is far off, indeed. Few travel such distances unless they seek a great prize. \n" \
                     "There is a prize here that many have sought and none have won. Tell me, {name} of {homeland}, \n"
                     "has the Dragon's Treasure not called you hither?  Y/n ".format(homeland=homeland, name=name)))

    if answer.lower() != 'n':
        print(quotize("I fear that you will not attain your goal, but nevertheless I will tell you what I know. \n" \
              "The great doors of the city through which you entered stand always open. There is another door, small and\n" \
              "unused, beside them. If you can break the enchantment sealing the door, it will lead you to a maze infested \n" \
              "with nightmares. If you gain the exit before your sanity is wrested from you by the horror of the place, \n" \
              "you will find yourself in the dragon's keep. What perils await you there, I do not know. \nGood luck, {}. "
              "May it be that we meat again.".format(name)))
    else:
        print("\nExcuse me, I mistook you for someone interesting. Good day.")
        sys.exit()



if __name__ == "__main__":
    print(story_text.intro)
    name = get_name()
    homeland = greet(name)
    offer_quest(name, homeland)

    print(story_text.journey_to_door)
    word_scramble()



