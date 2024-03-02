import sys
import os
import textwrap
from colorama import Fore, Back, Style
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from time import *

global WINDOW_WIDTH

WINDOW_WIDTH = os.get_terminal_size().columns
TEXT_WINDOW = WINDOW_WIDTH + len(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}")


def statusBar(phone):
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))
    if phone:
        batteryText = "{0}% [{1:<5}]".format(battery, "|" * int(battery / 10))
        if battery < 10:
            batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}{batteryText}%"
        elif battery < 20:
            batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}{batteryText}%"
        else:
            batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{batteryText}%"
        leftPrint(batteryText.rjust(TEXT_WINDOW))
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{time}")
        sys.stdout.flush()
    else:
        print("")
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))


def leftPrint(message):
    sys.stdout.write(message)
    # self.delay_print(message)
    sys.stdout.write('\b' * len(message))  # \b: non-deleting backspace


def rightPrint(message):
    leftPrint(message.rjust(TEXT_WINDOW))
    sys.stdout.flush()
    print()


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.01)


class Text:

    messages : [str]
    contact : str
    yourText : [bool]
    bar : bool
    def __init__(self, messages, contact, yourText, bar):
        self.messages = messages
        self.contact = contact
        self.yourText = yourText
        self.bar = bar

    @staticmethod
    def ellipse():
        for x in range(0, 4):
            b = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}." * x
            print(b, end="\r")
            sleep(0.3)
        sleep(0.3)

        #
        # for i in ["..."]:
        #     sys.stdout.write(i)
        #     sys.stdout.flush()
        #     sleep(0.25)

    # def delay_print(self,s):
    #     for c in s:
    #         sys.stdout.write(c)
    #         sys.stdout.flush()
    #         sleep(0.25)
    def conversation(self):
        contactValue = self.contact
        messagesValue = self.messages
        if self.bar:
            statusBar(True)
        you = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.GREEN}You:")
        friend = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.BLUE}{contactValue}:")
        for owner in self.yourText:
            sleep(0.8)
            if not owner:
                message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messagesValue[0])
                print(friend)
                self.ellipse()
                print("", end="\r")
                print(textwrap.fill(message, int(TEXT_WINDOW * 0.83)))
                # the .83 just gives the text a bit of a chance on the screen lol
            else:
                rightPrint(you)
                sleep(1.2)
                message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                lines = self.wrapped(message)
                for line in lines:
                    rightPrint(line)
            messagesValue.pop(0)
            print("\n")

        print(f"{Style.RESET_ALL}")

    @staticmethod
    def wrapped(message):
        if len(message) <= int(TEXT_WINDOW / 2):
            return [message]

        else:
            wrappedMessage = textwrap.fill(message, int(TEXT_WINDOW / 2)).splitlines()
            for i in range(1, len(wrappedMessage)):
                wrappedMessage[i] = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + wrappedMessage[i])

            return wrappedMessage


class Narrate:

    lines : [str]
    bar : bool
    def __init__(self, lines, bar):
        self.lines = lines
        self.bar = bar

    def narrate(self):
        if self.bar:
            statusBar(False)
        print("")
        for line in self.lines:
            split = textwrap.fill(line, int(TEXT_WINDOW * 0.83))
            # the .83 just gives the text a bit of a chance on the screen lol
            delay_print(split)
            print("\n")
            sleep(1)


class Option:
    options: dict
    blocks: [int]
    def __init__(self, options: dict, blocks: [int]):
        self.options = options
        self.blocks = blocks

    def listOpt(self):
        sleep(0.3)
        print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}" + str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))

        indexes = list(options.keys())
        for key, value in options.items():
            sleep(1)
            delay_print(f"\n{key} : {value}\n")
        choice = self.getInput(indexes)
        print(" ")
        return choice

    def getInput(self, indexes):
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}")
        choice = int(input("Choice: "))
        if choice:
            if choice in indexes:
                if self.blocks is None:
                    return choice
                elif choice not in self.blocks:
                    return choice
        print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}NUH UH")
        return self.getInput(indexes)


class Title:

    title : str
    colour : str
    def __init__(self, title, colour):
        self.title = title
        self.colour = colour

    def print(self):
        cprint(figlet_format(self.title, font='starwars'), self.colour, attrs=['bold'])



global time
time = "08:32"
global battery
battery = 21


"""messages = ["you awake?",
            "no",
            "we seeing you at the lecture today?", "idk ive got a lot on",
            "you should try to go",
            "im heading there for about half 10", "maybe see you there"]
yourText = [False, True, False, True, False, False, False]
text1 = Text(messages, contact, yourText)
text1.conversation()
lines = ["You should really go to your lecture", "This is just here to fill in some space and see how it looks"]
narrate2 = Narrate(lines)
narrate2.narrate()"""

os.system('cls' if os.name == 'nt' else 'clear')
title1 = Title("Descent", "yellow")
title1.print()
sleep(3)
lines = ["You are a first year student living in university halls.","You are extremely socially anxious and suffering from what you think is depression.","Today is a day like any other."]
narrate0 = Narrate(lines,True)
narrate0.narrate()
sleep(2)
options = {1: "[Wake up]"}
options0 = Option(options, None)
choice0 = options0.listOpt()

os.system('cls' if os.name == 'nt' else 'clear')

lines = ["It is 8:32am. Your eyes are heavy and you can hear the sound of your alarm - your favourite song - sounding out from your desk across the room.","You are tired."]
narrate1 = Narrate(lines,True)
narrate1.narrate()
options = {1: "[Get up and turn it off]", 2: "[Let it finish, the song is nearly over anyway]"}
options1 = Option(options, None)
choice1 = options1.listOpt()
lines = ["You drag yourself to your feet. Your head spins a little as you adjust to being upright.","You turn off the alarm."]
narrate2 = Narrate(lines,True)
narrate2.narrate()

options = {1: "[Check phone]", 2: "[Go back to bed]", 3: "OPTION INVALID"}
options2 = Option(options, [3])
choice2 = options2.listOpt()

lines = ["It is Friday.","Your phone battery is at about 30%.","You have a message from Jordan."]
narrate3 = Narrate(lines,True)
narrate3.narrate()

options = {1: "[Read the message]", 2: "[Go back to bed]"}
options3 = Option(options, None)
choice3 = options3.listOpt()

os.system('cls' if os.name == 'nt' else 'clear')

contact = "Jordan"
messages = ["hey, you still good to meet later?"]
yourText = [False]
text1 = Text(messages, contact, yourText, True)
text1.conversation()

options = {1: "[Reply to Jordan]", 2: "[Go back to bed]"}
options4 = Option(options, None)
choice4 = options4.listOpt()

lines = ["You recall that Jordan invited you to meet for lunch today at 1pm.","You have an important workshop from 12pm until 2pm."]
narrate4 = Narrate(lines,False)
narrate4.narrate()

options = {1: '"Yeah I think so."', 2: '"Sorry, Ive got a workshop I need to go to."', 3:"[Come up with a lie]",4:"[Leave him on read]"}
options5 = Option(options, None)
choice5 = options5.listOpt()

contact = "Jordan"
messages = [options.get(choice5),"WAZZZAAAAAAA","I really want to kill myself","Jordan","DOUBLE WAZZAAAAAA"]
yourText = [True,False,True,True,False]
text1 = Text(messages, contact, yourText, False)
text1.conversation()