from random import randint
from os import system
num , color, vars = randint(0,100), "\033[93m", "\033[0m"
def number():
    tanitim = input("Welcome to the number guess game. Please press Enter to continue. İf you want to exit now press 'E'.").upper()
    if tanitim == 'E':
        print(color + "So Long." + vars)
    system('cls')
    rights = 5
    while 'E' != tanitim and rights > -1:
        q = int(input(f"You have {rights} right to try. Enter a value\n: "))
        if q == num:
            system('cls')
            print(color + "Welldone. You win." + vars)
            break
        elif q < num:
            if (num - q) < 5:
                print(color + "So close. Enter a little bit higher numbers.\n: " + vars)
                rights -= 1
            else:
                print(color + "Enter higher numbers.\n: " + vars)
                rights -= 1
        elif q > num:
            if (q - num) < 10:
                print(color + "So close. Enter a little bit lower numbers.\n: " + vars)
                rights -= 1
            else:
                print(color + "Enter lower numbers\n: " + vars)
                rights -= 1
    if rights <0:
        system('cls')
        print(color + "There is no right to try. Sorry" + vars)
number()
