import os
from colored import Fore, Back, Style
import time
from Games.numberguesser import numberguesser
from Games.numberguesser import clearscreen

# Colors
white = Fore.rgb(255, 255, 255)
red = Fore.rgb(255, 0, 0)
orange = Fore.rgb(255, 140, 0)
yellow = Fore.rgb(255, 255, 0)
green = Fore.rgb(0, 180, 0)
light_green = Fore.rgb(0, 220, 0)
blue = Fore.rgb(0, 0, 255)
purple = Fore.rgb(138, 43, 226)


def start():
    global game
    game = input(f'''
{orange}Welcome to Py-Games!
=======Games=======
{light_green}1. Number Guesser
2. New Game...
{red}3. Coming soon
4. Coming soon
5. Coming soon
{orange}Your Choice: ''')

    if game == "1":
        clearscreen()
        numberguesser()
    else:
        print(f"{red}That game is not out yet or it is not an option. ")
        time.sleep(2)
        clearscreen()
        start()


start()
