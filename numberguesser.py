# Importing
import random
import time
from colored import Fore, Back, Style
import os

# Colors
white = Fore.rgb(255, 255, 255)
red = Fore.rgb(255, 0, 0)
orange = Fore.rgb(255, 140, 0)
yellow = Fore.rgb(255, 255, 0)
green = Fore.rgb(0, 180, 0)
light_green = Fore.rgb(0, 220, 0)
blue = Fore.rgb(0, 0, 255)
purple = Fore.rgb(138, 43, 226)


def clearscreen():
    print(f'{orange}[+] Clearing')
    time.sleep(1)
    os.system('cls')
    print(f'{light_green}[+] Cleared')


def numberguesser():
    mode = input(f'''{orange}What mode would you like to play?
    {green}1. Classic
    2. Custom
    {orange}Your Choice ''')

    if mode == "1":
        wrong = True
        print(f'{orange}Selected')
        time.sleep(1)
        print(f'Close PyGames To Go Back')
        time.sleep(2)
        clearscreen()
        number = random.randint(1, 100)
        while wrong:
            guess = int(input('''
Guess a number between 1 and 100.
Answer: '''))
            if guess == number:
                print(f'{light_green}You got it')
                time.sleep(1)
                clearscreen()
                wrong = False
                print(f'{yellow}Thank you for playing! If you would like to play again, reopen this window.')
                time.sleep(5)
                exit(0)
            elif guess > number:
                print(f'{orange}Hint: Go lower')
                time.sleep(1)
            elif guess < number:
                print(f'{orange}Hint: Go higher')
                time.sleep(1)
            else:
                print(f'{red}Invalid Guess')
                time.sleep(1)

    elif mode == "2":
        wrong = True
        number1 = int(input(f'''
{orange}Choose your minimum number.
Answer: '''))

        number2 = int(input(f'''
{orange}Choose your maximum number.
Answer: '''))
        number = random.randint(number1, number2)

        while wrong:
            guess = int(input(f'''
{orange}Guess a number between {number1} and {number2}.
Answer: '''))

            if guess == number:
                print(f'{light_green}You got it')
                time.sleep(1)
                clearscreen()
                wrong = False
                print(f'{yellow}Thank you for playing! If you would like to play again, reopen this window.')
                time.sleep(5)
                exit(0)
            elif guess > number:
                print(f'{orange}Hint: Go lower')
                time.sleep(1)
            elif guess < number:
                print(f'{orange}Hint: Go higher')
                time.sleep(1)
            else:
                print(f'{red}Invalid Guess')
    else:
        print(f'{red}Invalid Option')
