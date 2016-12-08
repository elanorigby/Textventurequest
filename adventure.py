import sys
import story_text
from slowth import slowth
from word_scramble import word_scramble
from maze import run_maze


def get_name():
    nombre = input(slowth('"What is your name, wanderer?"')).strip().capitalize()
    return nombre


def greet(nombre):
    greeting = input(slowth('"Well met, {name}. We rarely see strangers here. Where are you from?"'.format(name=nombre))).strip().capitalize()
    return greeting


def offer_quest(nombre, homeland):
    answer = input(slowth('"{homeland} is far off, indeed. Few travel such distances unless they seek a great prize. ' \
                     'There is a prize here that many have sought and none have won. Tell me, {name} of {homeland}, '
                     'has the Dragon\'s Treasure not called you hither?  Y/n "'.format(homeland=homeland, name=nombre)))

    if answer.lower() != 'n':
        print(slowth('"I fear that you will not attain your goal, but nevertheless I will tell you what I know. ' \
              'The great doors of the city through which you entered stand always open. There is another door, small and ' \
              'unused, beside them. If you can break the enchantment sealing the door, it will lead you to a maze infested ' \
              'with nightmares. If you gain the exit before your sanity is wrested from you by the horror of the place, ' \
              'you will find yourself in the dragon\'s keep. What perils await you there, I do not know. Good luck, {}. '
              'May it be that we meat again."'.format(nombre)))
    else:
        print(slowth("Excuse me, I mistook you for someone interesting. Good day."))
        sys.exit()



if __name__ == "__main__":
    # print(slowth(story_text.arrival))
    # name = get_name()
    # homeland = greet(name)
    # offer_quest(name, homeland)
    # print(slowth(story_text.journey_to_door))
    # word_scramble()
    print(slowth(story_text.through_the_door))
    run_maze()
    print(slowth(story_text.temp_ending))
