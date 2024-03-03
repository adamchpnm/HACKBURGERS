import os
import sys
import textwrap
from time import *
# import inquirer

from colorama import Fore, Style
from pyfiglet import figlet_format
from termcolor import cprint

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


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.01)


class Text:
    messages: [str]
    contact: str
    yourText: [bool]
    bar: bool
    read: int
    read_bool: [bool]
    TEXT_WINDOW: int

    def __init__(self, messages, contact, yourText, bar, read):
        self.messages = messages.copy()
        self.contact = contact
        self.yourText = yourText
        self.bar = bar
        self.read_bool = [False] * len(yourText)
        for i in range(0, read):
            self.read_bool[i] = True
        self.TEXT_WINDOW = WINDOW_WIDTH + len(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}")

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
        you = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.GREEN}You:")
        friend = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.BLUE}{contactValue}:")
        count = 0
        for owner in self.yourText:
            if not self.read_bool[count]:
                sleep(0.8)
                if not owner:
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messagesValue[0])
                    print(f"{friend} - {time}")
                    self.ellipse()
                    print("", end="\r")
                    print(textwrap.fill(message, int(TEXT_WINDOW * 0.83)))
                    # print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}{time}")
                    # the .83 just gives the text a bit of a chance on the screen lol
                else:
                    self.rightPrint(f"{Fore.GREEN}{time} - {you}",len(f"-{Fore.GREEN}"))
                    sleep(1.2)
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                    lines = self.wrapped(message)
                    for line in lines:
                        self.rightPrint(line,0)
                messagesValue.pop(0)
                print("\n")
            else:
                if not owner:
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messagesValue[0])
                    print(f"{friend} - {time}")
                    print("", end="\r")
                    print(textwrap.fill(message, int(TEXT_WINDOW * 0.83)))
                    # the .83 just gives the text a bit of a chance on the screen lol
                else:
                    self.rightPrint(f"{Fore.GREEN}{time} - {you}",len(self.contact))
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                    lines = self.wrapped(message)
                    for line in lines:
                        self.rightPrint(line,0)
                messagesValue.pop(0)
                print("\n")
            count += 1
        print(f"{Style.RESET_ALL}")

    def rightPrint(self, message, adjust):
        # print(adjust)
        message = message + " "
        leftPrint(message.rjust(self.TEXT_WINDOW+adjust))
        sys.stdout.flush()
        print()

    def wrapped(self, message):
        if len(message) <= int(self.TEXT_WINDOW / 2):
            return [message]

        else:
            wrappedMessage = textwrap.fill(message, int(self.TEXT_WINDOW / 2)).splitlines()
            for i in range(1, len(wrappedMessage)):
                wrappedMessage[i] = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + wrappedMessage[i])

            return wrappedMessage


class Narrate:
    lines: [str]
    bar: bool

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
            sleep(0.8)


class Option:
    options: dict
    blocks: [int]

    def __init__(self, options: dict, blocked: [int]):
        self.options = options
        self.blocked = blocked

    def listOpt(self):
        sleep(0.3)
        print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}" + str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))

        choices = []
        indexes = list(self.options.keys())
        for key, value in self.options.items():
            sleep(0.8)
            if self.blocked:
                if key in self.blocked:
                    delay_print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}\n{key} : {value}")
                else:
                    delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{key} : {value}")
            else:
                delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{key} : {value}")
            choices.append(value)
        """
        # print(" ")
        # questions = [
        #     inquirer.List(
        #         "choice", message = ">",
        #         choices=choices, carousel=True
        #     ),
        # ]
        # answers = inquirer.prompt(questions)
        # print(answers)
        # return answers
        """
        choice = self.getInput(indexes)
        print(" ")
        return choice

    def getInput(self, indexes):
        print(f"\n{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}")
        choice = int(input("> "))
        if choice:
            if choice in indexes:
                if self.blocked is None:
                    return choice
                elif choice not in self.blocked:
                    return choice
        print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}NUH UH")
        return self.getInput(indexes)


class Title:
    title: str
    colour: str

    def __init__(self, title, colour):
        self.title = title
        self.colour = colour

    def print(self):
        # cprint(self.title, self.colour, attrs=['bold'])
        cprint(figlet_format(self.title, font='cybermedium'), self.colour, attrs=['bold'])


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


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    title1 = Title("a\n day\n   like\n    any\n     other", "yellow")
    title1.print()
    sleep(1)
    """
    lines = ["You are a first year student living in university halls.","You are extremely socially anxious and suffering from what you think is depression.","Today is A Day Like Any Other."]
    narrate0 = Narrate(lines,True)
    narrate0.narrate()
    sleep(1)
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

    lines = ["It is Friday.", "Your phone battery is at about 30%.", "You have a message from Jordan."]
    narrate3 = Narrate(lines, True)
    narrate3.narrate()

    options = {1: "[Read the message]", 2: "[Go back to bed]"}
    options3 = Option(options, None)
    choice3 = options3.listOpt()
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    contact = "Jordan"
    messages = ["hey, you still good to meet later?"]
    yourText = [False]
    text1 = Text(messages, contact, yourText, True, 0)
    text1.conversation()

    # options = {1: "[Reply to Jordan]", 2: "[Go back to bed]"}
    # options4 = Option(options, None)
    # choice4 = options4.listOpt()
    #
    # lines = ["You recall that Jordan invited you to meet for lunch today at 1pm.",
    #          "You have an important workshop from 12pm until 2pm."]
    # narrate4 = Narrate(lines, False)
    # narrate4.narrate()
    #
    options = {1: "Yeah I think so.", 2: "Sorry, I've got a workshop I need to go to.", 3: "[Come up with a lie]",
               4: "[Leave him on read]"}
    options5 = Option(options, None)
    choice5 = options5.listOpt()

    os.system('cls' if os.name == 'nt' else 'clear')

    messages.extend(
        [options.get(choice5), "WAZZZAAAAAAA", "I really want to kill myself", "Jordan", "DOUBLE WAZZAAAAAA"])
    yourText.extend([True, False, True, True, False])
    text1 = Text(messages, contact, yourText, True, 1)
    text1.conversation()


main()
