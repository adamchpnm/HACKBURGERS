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


class Operation:
    oper_name: str


class Text(Operation):
    messages: [str]
    contact: str
    yourText: [bool]
    bar: bool
    read: int
    read_bool: [bool]
    TEXT_WINDOW: int
    battery: int
    time: str

    def __init__(self, messages, contact, yourText, bar, read, battery, time):
        self.messages = messages.copy()
        self.contact = contact
        self.yourText = yourText
        self.bar = bar
        self.read_bool = [False] * len(yourText)
        for i in range(0, read):
            self.read_bool[i] = True
        self.TEXT_WINDOW = WINDOW_WIDTH + len(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}")
        self.battery = battery
        self.time = time

    def ellipse(self):
        for x in range(0, 4):
            b = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}." * x
            print(b, end="\r")
            sleep(0.3)
        sleep(0.3)

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
                    self.rightPrint(f"{Fore.GREEN}{time} - {you}", len(f"-{Fore.GREEN}"))
                    sleep(1.2)
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                    lines = self.wrapped(message)
                    for line in lines:
                        self.rightPrint(line, 0)
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
                    self.rightPrint(f"{Fore.GREEN}{time} - {you}", len(self.contact))
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                    lines = self.wrapped(message)
                    for line in lines:
                        self.rightPrint(line, 0)
                messagesValue.pop(0)
                print("\n")
            count += 1
        print(f"{Style.RESET_ALL}")

    def rightPrint(self, message, adjust):
        # print(adjust)
        message = message + " "
        leftPrint(message.rjust(self.TEXT_WINDOW + adjust))
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


class Narrate(Operation):
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


class Option(Operation):
    options: dict
    blocks: [str]

    def __init__(self, options: dict, blocked: [str]):
        self.options = options
        self.blocked = blocked

    def listOpt(self):
        sleep(0.3)
        print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}" + str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))

        # indexes = list(self.options.keys())
        count = 0
        indexes = []
        keys = []
        for key, value in self.options.items():
            count += 1
            indexes.extend([str(count)])
            keys.append(key)
            sleep(0.8)
            if self.blocked:
                if key in self.blocked:
                    delay_print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}\n{count} : {value}")
                else:
                    delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{count} : {value}")
            else:
                delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{count} : {value}")
        choice = self.getInput(indexes, keys)
        print(" ")
        return choice

    def getInput(self, indexes, keys):
        print(f"\n{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}")
        choice = int(input("> "))
        if choice:
            if keys[choice - 1] in self.options:
                if self.blocked is None:
                    return keys[choice - 1]
                elif choice not in self.blocked:
                    return keys[choice - 1]
        print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}NUH UH")
        return self.getInput(indexes, keys)


class Title(Operation):
    title: str
    colour: str

    def __init__(self, title, colour):
        self.title = title
        self.colour = colour

    def print(self):
        # cprint(self.title, self.colour, attrs=['bold'])
        cprint(figlet_format(self.title, font='cybermedium'), self.colour, attrs=['bold'])


class Script:
    script_id: str
    # energy_criterion: int
    # battery_criterion: int
    possible: [str]
    script_body: list
    script_args: list

    # Each event has a dictionary of scripts, which are different ways that the event can go

    # Script can transition to another script (through Event.scriptTransition)
    # or to another event (through StateMachine.eventTransition)
    def __init__(self, script_id, possible: [str], script_body: list,
                 script_args: list):

        # battery and energy are the only criteria which matter
        self.script_id = script_id
        # self.energy_criterion = energy_criterion
        # self.battery_criterion = battery_criterion
        self.possible = possible
        self.script_body = script_body
        self.script_args = script_args

    def getScriptId(self):
        return self.script_id

    # def criteria(self):
    #     if self.energy_criterion <= energy and self.battery_criterion <= battery:
    #         return True
    #     else:
    #         return False

    def returnBlocked(self):
        blocked = []
        for child in self.possible:
            if not (child.criteria()):
                blocked.append(child.getScriptId())
        return blocked

    def runScript(self):
        for script_idx in range(len(self.script_args)):
            if arg := self.script_args[script_idx]:  ##arg is not None
                res = self.script_body[script_idx](arg)
            else:
                res = self.script_body[script_idx]()
        return res


"""
class StateMachine:

    def __init__(self, scripts: dict[Script: dict[int: Script]], player_stats):
        self.scripts = scripts
        self.player_states = player_stats

        # you apply check scripts to check if a script can be moved to

    # change name to getBlock, clean, make it work for single states, not all states
    def checkScripts(self, player_stats, scripts: dict[Script: dict[int: Script]]):
        unavailable_scripts = []
        for script in scripts:
            if not scripts[script].criteria(player_stats["energy"], player_stats["battery"]):
                unavailable_scripts.append(script)
        return unavailable_scripts

    # this function is basically just a nice way to display this
    # we dont give the player the choice to pick an unavailable event, so we do not have to validate inputs
    def transitionToScript(self, next_script: Script):
        return next_script

    # this is what we give to block out the choices you CANT TAKE
    # could do blocking stuff in here
    def removeChoices(self, player_stats, scripts: dict[Script: dict[int: Script]]):
        unavailable_scripts = self.checkScripts(player_stats, scripts)

    def route(self, player_stats, scripts: dict[Script: dict[int: Script]], start):
        game_running = True
        current_script = scripts[start]
        while game_running:
            print("hiii")
            # this will run the game loop, befire

    player_stats = {"energy": 30, "battery": 30, "money": 0}
    # test_script1 = Script(1)
    # test_script2 = Script(2)
    # test_script3 = Script(3)

    # scripts will be stored in a double nested dictionary!!!! basically the intuition is:
    # each script
    # the inner dictionary contains one value: the dictionary mapped to the script
    # scripts = {test_script1: {1: test_script2, 2: test_script3}, test_script2: {1: test_script2, 2: test_script3}}
"""

title1 = Title("a\n day\n   like\n    any\n     other", "yellow")


narration = Narrate(
    [
        "You are a first year student living in university halls.",
        "You are extremely socially anxious and suffering from what you think is depression.",
        "Today is a day like any other."
    ],
    True
)
options = Option({"wake_1": "[Wake up]"}, None)

start = Script(
    "start",
    ["wake_1"],
    [os.system, title1.print, sleep, narration.narrate, sleep, options.listOpt],
    [('cls' if os.name == 'nt' else 'clear'), None, 1, None, 1, None]
)

# lines = [
#     "It is 8:32am. Your eyes are heavy and you can hear the sound of your alarm - your favourite song - sounding out from your desk across the room.",
#     "You are tired."]
# narrate1 = Narrate(lines, True)
# options = {"get_up_1": "[Get up and turn it off]",
#            "song_play_out": "[Let it finish, the song is nearly over anyway]"}
# options1 = Option(options, None)
#
# wake_1_body = {"FUNCTION0": os.system, "FUNCTION1": narrate1.narrate,
#                "FUNCTION2": options1.listOpt}
#
# wake_1_args = {"FUNCTION0": ('cls' if os.name == 'nt' else 'clear'), "FUNCTION1": None,
#                "FUNCTION2": None}
# wake_1 = Script("wake_1", [], wake_1_body, wake_1_args)
#
#
#
#
#
#
#
#
#
# lines = ["You drag yourself to your feet. Your head spins a little as you adjust to being upright.",
#          "You turn off the alarm."]
# narrate2 = Narrate(lines, True)
# options = {"check_phone_1": "[Check phone]", "go_bed_1": "[Go back to bed]", "TEST_BLOCK": "OPTION INVALID"}
# options2 = Option(options, [3])
#
# get_up_1_body = {"FUNCTION1": narrate2.narrate, "FUNCTION2": options2.listOpt}
# get_up_1_args = {"FUNCTION1": None, "FUNCTION2": None}
# get_up_1 = Script("get_up_1", ["TEST_BLOCK"], get_up_1_body, get_up_1_args)
#
#
#
#
#
#
#
# contact = "Jordan"
# battery = 28
# time = "10:32"
# messages = ["hey, you still good to meet later?"]
# yourText = [False]
# text1 = Text(messages, contact, yourText, True, 0, battery, time)
# options = {1: "[Reply to Jordan]", 2: "[Go back to bed]"}
# options4 = Option(options, None)
# check_phone_1_body = {"FUNCTION0": os.system, "FUNCTION1": text1.conversation, "FUNCTION2": options4.listOpt}
# check_phone_1_args = {"FUNCTION0": ('cls' if os.name == 'nt' else 'clear'), "FUNCTION1": None, "FUNCTION2": None}
#
# check_phone_1 = Script("check_phone_1", 0, 0, [], check_phone_1_body, check_phone_1_args)










# allScript = {"start": start, "wake_1": wake_1, "get_up_1": get_up_1, "check_phone_1": check_phone_1}



start.runScript()


# def main(allScript):
#     done = False
#     toRun = start.runScript()
#     while not done:
#         scriptRun = allScript.get(toRun)
#         toRun = scriptRun.runScript()
#
# main()
