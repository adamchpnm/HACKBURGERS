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


def statusBar(phone, battery, timer):
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
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{timer}")
        sys.stdout.flush()
    else:
        print("")
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))


def instruction(instruction):
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))
    print(instruction.center(WINDOW_WIDTH))
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


class End:
    def __init__(self):
        pass

    def ending(self):
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}")
        statusBar(False, None, None)


class Text:
    messages: [str]
    contact: str
    yourText: [bool]
    bar: bool
    read: int
    read_bool: [bool]
    TEXT_WINDOW: int
    battery: int
    timer: str

    def __init__(self, messages, contact, yourText, bar, read, battery, timer):
        self.messages = messages.copy()
        self.contact = contact
        self.yourText = yourText
        self.bar = bar
        self.read_bool = [False] * len(yourText)
        for i in range(0, read):
            self.read_bool[i] = True
        self.TEXT_WINDOW = WINDOW_WIDTH + len(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}")
        self.battery = battery
        self.timer = timer

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
            statusBar(True, self.battery, self.timer)
        you = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.GREEN}You:")
        friend = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.BLUE}{contactValue}:")
        count = 0
        for owner in self.yourText:
            if not self.read_bool[count]:
                sleep(0.6)
                if not owner:
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messagesValue[0])
                    print(f"{friend} - {self.timer}")
                    self.ellipse()
                    print("", end="\r")
                    print(textwrap.fill(message, int(TEXT_WINDOW * 0.83)))
                    # print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}{time}")
                    # the .83 just gives the text a bit of a chance on the screen lol
                else:
                    self.rightPrint(f"{Fore.GREEN}{self.timer} - {you}", len(f"-{Fore.GREEN}"))
                    sleep(0.9)
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messagesValue[0])
                    lines = self.wrapped(message)
                    for line in lines:
                        self.rightPrint(line, 0)
                messagesValue.pop(0)
                print("\n")
            else:
                if not owner:
                    message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messagesValue[0])
                    print(f"{friend} - {self.timer}")
                    print("", end="\r")
                    print(textwrap.fill(message, int(TEXT_WINDOW * 0.83)))
                    # the .83 just gives the text a bit of a chance on the screen lol
                else:
                    self.rightPrint(f"{Fore.GREEN}{self.timer} - {you}", len(self.contact))
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


class Narrate:
    lines: [str]
    bar: bool

    def __init__(self, lines, bar):
        self.lines = lines
        self.bar = bar

    def narrate(self):
        print("")
        for line in self.lines:
            split = textwrap.fill(line, int(TEXT_WINDOW * 0.83))
            # the .83 just gives the text a bit of a chance on the screen lol
            delay_print(split)
            print("\n")
            sleep(0.5)


class Option:
    options: dict
    blocks: [str]

    def __init__(self, options: dict, blocked: [str]):
        self.options = options
        self.blocked = blocked

    def listOpt(self):
        sleep(0.1)
        print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}" + str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))

        # indexes = list(self.options.keys())
        count = 0
        indexes = []
        keys = []
        values = []
        for key, value in self.options.items():
            count += 1
            indexes.extend([str(count)])
            keys.append(key)
            values.append(value)
            sleep(0.6)
            if self.blocked:
                if key in self.blocked:
                    delay_print(f"{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}\n{count} : {value}")
                else:
                    delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{count} : {value}")
            else:
                delay_print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}\n{count} : {value}")
        print(" ")
        choice = self.getInput(indexes, keys)
        choiceIdx = keys.index(choice)
        choicePrint = f"> {values[choiceIdx]} <"
        instruction(choicePrint)
        return choice

    def getInput(self, indexes, keys):
        print(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}")
        try:
            inpVal = input("> ")
            if inpVal == 'q' or inpVal == "Q":
                return "QUIT"
            choice = int(inpVal)
            if choice:
                if keys[choice - 1] in self.options:
                    if self.blocked is None:
                        return keys[choice - 1]
                    elif keys[choice - 1] not in self.blocked:
                        return keys[choice - 1]
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}> {inpVal} - You can't")
                    return self.getInput(indexes, keys)
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")

            print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}This isn't something you feel you can do (INVALID OPTION:{inpVal})")
            return self.getInput(indexes, keys)
        except:
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}This isn't something you feel you can do (INVALID OPTION:{inpVal})")
            return self.getInput(indexes, keys)


class Title:
    title: str
    colour: str

    def __init__(self, title, colour):
        self.title = title
        self.colour = colour

    def print(self):
        # cprint(self.title, self.colour, attrs=['bold'])
        cprint(figlet_format(self.title, font='cybermedium'), self.colour, attrs=['bold'])
        instruction("answer \"q\" to any option to quit game")


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
        res = None
        for script_idx in range(len(self.script_args)):
            if self.script_body[script_idx]:
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

# start
if True:
    title1 = Title("a\n day\n   like\n    any\n     other", "yellow")
    narration = Narrate(
        [
            "You are a first year student living in university halls.",
            "You are extremely socially anxious and suffering from what you think is depression.",
            "Today is a day like any other."
        ],
        False
    )
    options = Option({"wake": "[Wake up]"}, None)
    start = Script(
        "start",
        ["wake_1"],
        [os.system, title1.print, sleep, narration.narrate, sleep, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, 1, None, 1, None]
    )

# buy_ready_meal
if True:
    narration = Narrate(
        [
            'You are pleased to see the ready meal, as it\'s one of your favourites.',
            'You check out quickly.',
            'You get startled exiting the shop as the alarm begins to ring. The security guard waves you on casually.'
        ],
        True
    )
    options = Option(
        {"go_home_shop": "[Go home]"},
        [])
    buy_ready_meal = Script(
        "buy_ready_meal",
        ["go_home"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_back_home
if True:
    narration = Narrate(
        [
            'You walk home from the cafe.',
            'On your way home you pass the local supermarket.',
            'You remember that you don\'t have very much for dinner.'
        ],
        True
    )
    options = Option(
        {"go_straight_home": "[Go straight home]", "go_to_shop": "[Go to the shop]"},
        [])
    go_back_home = Script(
        "go_back_home",
        ["go_straight_home", "go_to_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_home_no_shop
if True:
    narration = Narrate(
        [
            'You get home, and have some free time.'
        ],
        True
    )
    options = Option(
        {"study_afternoon": "[Study]", "watch_show": "[Watch the new episodes of your favourite show]"},
        [])
    go_home_no_shop = Script(
        "go_home_no_shop",
        ["study_afternoon", "watch_show"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_home_shop
if True:
    narration = Narrate(
        [
            'You get in the door and put away your shopping',
            'You have some free time.'
        ],
        True
    )
    options = Option(
        {"study_afternoon": "[Study]", "watch_show": "[Watch the new episodes of your favourite show]"},
        [])
    go_home_shop = Script(
        "go_home_shop",
        ["study_afternoon", "watch_show"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_straight_home
if True:
    narration = Narrate(
        [
            'You decide against going to the shop, you are wary to spend money.'
        ],
        True
    )
    options = Option(
        {"go_home_no_shop": "[Go home]"},
        [])
    go_straight_home = Script(
        "go_straight_home",
        ["go_home_no_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_to_shop
if True:
    narration = Narrate(
        [
            'You decide to take a trip to the supermarket on the way home.',
            'You wander the aisles aimlessly, coming across the reduced section.',
            'There is a reduced ready meal that catches your attention.'
        ],
        True
    )
    options = Option(
        {"buy_ready_meal": "[Buy the ready meal]", "leave_shop": "[Leave the shop empty handed]"},
        [])
    go_to_shop = Script(
        "go_to_shop",
        ["buy_ready_meal", "leave_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_shop
if True:
    narration = Narrate(
        [
            'You decide against buying anything, as you are wary about spending money.'
        ],
        True
    )
    options = Option(
        {"go_home_no_shop": "[Go home]"},
        [])
    leave_shop = Script(
        "leave_shop",
        ["go_home_no_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# study_afternoon
if True:
    narration = Narrate(
        [
            'You spend the next few hours doing the work for your workshop.',
            'By the time you finish, it is 5:55pm.',
            'Your mum usually calls you at 6pm.'
        ],
        True
    )
    options = Option(
        {"prepare_for_call": "[Prepare for the phone call]"},
        [])
    study_afternoon = Script(
        "study_afternoon",
        ["prepare_for_call"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# wake_1
if True:
    narration = Narrate(
        [
            "It is 10:32am. Your eyes are heavy and you can hear the sound of your alarm - your favourite song - sounding out from your desk across the room.",
            "You are tired."
        ],
        True
    )

    options = Option({"get_up_1": "[Get up and turn it off]",
                      "song_play_out": "[Let it finish, the song is nearly over anyway]"}, None)
    wake_1 = Script(
        "wake_1",
        ["get_up_1", "song_play_out"],
        [os.system, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

# get_up_1
if True:
    narration = Narrate(
        [
            "You drag yourself to your feet. Your head spins a little as you adjust to being upright.",
            "You turn off the alarm."
        ],
        True
    )
    options = Option({"check_phone": "[Check phone]",
                      "go_bed_1": "[Go back to bed]",
                      "TEST_BLOCK": "OPTION INVALID"}, ["TEST_BLOCK"])
    get_up_1 = Script(
        "get_up_1",
        ["check_phone", "go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# song_play_out
if True:
    narration = Narrate(
        [
            "The alarm eventually stops.",
            "Your bed is comfortable, you do not want to move."
        ],
        True
    )
    options = Option({"BLOCKED1": "[Get up and get ready for your day]", "motivate": "[Motivate yourself to get ready]",
                      "go_sleep_1": "Go back to sleep"}, ["BLOCKED1"])
    song_play_out = Script(
        "song_play_out",
        ["motivate", "think_1", "go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_bed_1
if True:
    narration = Narrate(
        [
            "You are lying in your bed, the blanket’s weight is comforting.",
            "It is tempting to go back to sleep."
        ],
        True
    )
    options = Option({"go_sleep_1": "[Go back to sleep]", "take_rest_1": "[Take a second to rest]",
                      "motivate": "[Think about today]"}, [])
    go_bed_1 = Script(
        "go_bed_1",
        ["motivate", "think_1", "go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# reply_1
if True:
    texting = Text(
        ["hey, you still good to meet later?"],
        "Jordan",
        [False],
        True,
        1,
        28,
        "10:32")
    narration = Narrate(
        [
            "You recall that Jordan invited you to meet for lunch today at 1pm.",
            "You have an important workshop from 12pm until 2pm."
        ],
        True
    )
    options = Option({"reply_yeah": "Yeah I think so", "sorry_workshop": "Sorry, I've got a workshop I need to go to.",
                      "finish_text": "[Leave him on read]"}, None)
    reply_1 = Script(
        "reply_1",
        ["reply_yeah", "sorry_workshop", "finish_text"],
        [os.system, texting.conversation, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None]
    )

# finish_text
if True:
    narration = Narrate(
        [
            "You put your phone away.",
            "You have 3 calls."
        ],
        True
    )
    options = Option({"put_phone_down": "[Put down your phone]"}, None)
    finish_text = Script(
        "finish_text",
        ["put_phone_down"],
        [options.listOpt],
        [None]
    )

# read_message
if True:
    texting = Text(
        ["hey, you still good to meet later?"],
        "Jordan",
        [False],
        True,
        0,
        28,
        "10:32")
    options = Option({"reply_1": "[Reply to Jordan]", "go_bed_1": "[Go back to bed]"}, None)
    read_message = Script(
        "read_message",
        ["reply_1", "go_bed_1"],
        [os.system, texting.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

# sorry_workshop
if True:
    texting = Text(
        ["hey, you still good to meet later?",
         "Sorry, I've got a workshop I need to go to.",
         "ah shit man, that sucks",
         "maybe we can do next monday? I think I have some free time after 2?"],
        "Jordan",
        [False, True, False, False],
        True,
        1,
        27,
        "10:33")
    options = Option({"put_phone_down": "[Leave him on read]", "BLOCKED1": "[Commit to meeting him on Monday]"},
                     ["BLOCKED1"])
    sorry_workshop = Script(
        "sorry_workshop",
        ["put_phone_down"],
        [os.system, texting.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

# sorry_workshop
if True:
    texting = Text(
        ["hey, you still good to meet later?",
         "Sorry, I've got a workshop I need to go to.",
         "ah shit man, that sucks",
         "maybe we can do next monday? I think I have some free time after 2?"],
        "Jordan",
        [False, True, False, False],
        True,
        1,
        27,
        "10:33")
    options = Option({"put_phone_down": "[Leave him on read]", "BLOCKED1": "[Commit to meeting him on Monday]"},
                     ["BLOCKED1"])
    sorry_workshop = Script(
        "sorry_workshop",
        ["put_phone_down"],
        [os.system, texting.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

# reply_yeah
if True:
    texting1 = Text(
        ["hey, you still good to meet later?", "Yeah I think so", "cool! see you later at the cafe then :)"],
        "Jordan",
        [False, True, False],
        True,
        1,
        27,
        "10:40")
    texting2 = Text(
        ["cba with this lecture today ngl", "you going?"],
        "Jordan",
        [False, False],
        False,
        0,
        26,
        "10:41")
    options = Option({"put_phone_down": "[Leave him on read]", "BLOCKED1": "[Let him know you will be there]"},
                     ["BLOCKED1"])
    reply_yeah = Script(
        "reply_yeah",
        ["put_phone_down"],
        [os.system, texting1.conversation, texting2.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None]
    )

# check_phone
if True:
    narration = Narrate(
        [
            "It is Friday.",
            "Your phone battery is at about 30%.",
            "You have a message from Jordan."
        ],
        True
    )
    options = Option({"read_message": "[Read the message]", "go_bed_1": "[Go back to bed]"}, [])
    check_phone = Script(
        "check_phone",
        ["read_message", "go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# eat_in_kitchen
if True:
    narration = Narrate(
        [
            "You awkwardly sit down at the kitchen table.",
            "You take a bite of your cereal.",
            "The milk is off.",
            "Your flatmate has started making toast.",
            "You feel uncomfortable."
        ],
        True
    )
    options = Option({"BLOCKED1": "[Throw the spoiled cereal in the bin]",
                      "eat_spoiled": "[Slowly eat the spoiled cereal and wait for them to leave]"}, ["BLOCKED1"])
    eat_in_kitchen = Script(
        "eat_in_kitchen",
        ["eat_spoiled"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# get_food
if True:
    narration = Narrate(
        [
            "You check your cupboard. It is empty but for a half used bag of pasta and the last scraps of a box of cornflakes.",
            "You check the fridge. All that you have is a carton of milk.",
            "The kitchen clock runs slow. It says that it is 10:47am."
        ],
        True
    )
    options = Option(
        {"make_cereal": "[Make cereal]", "run_for_lect": "[Run for your lecture]"},
        [])
    get_food = Script(
        "get_food",
        ["make_cereal", "run_for_lect"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_kitchen
if True:
    narration = Narrate(
        [
            "You enter the kitchen. It is currently empty.",
            "One of your flatmates has left their dishes unwashed beside the sink."
        ],
        True
    )
    options = Option(
        {"get_food": "[Get something to eat]"},
        [])
    go_kitchen = Script(
        "go_kitchen",
        ["get_food"],
        [os.system, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

# eat_in_room
if True:
    narration = Narrate(
        [
            "You leave the kitchen and take the cereal to your room.",
            "You sit at your desk next to your phone and your dirty dishes.",
            "You begin to eat your cereal.",
            "The milk is off.",
            "You don't want to eat it.",
            "You feel hungry."
        ],
        True
    )
    options = Option(
        {"leave_cereal": "[Leave the cereal]", "try_eat": "[Try to stomach eating the cereal]"},
        [])
    eat_in_room = Script(
        "eat_in_room",
        ["leave_cereal", "try_eat"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_cereal
if True:
    narration = Narrate(
        [
            "You leave the spoiled cereal bowl on your desk.",
            "You pick up your phone.", "It is 10:50am.",
            "If you run you will just make it to your lecture."
        ],
        True
    )
    options = Option(
        {"run_for_lect": "[Run for your lecture]", "go_bed_1": "[Go back to bed]"},
        [])
    leave_cereal = Script(
        "leave_cereal",
        ["run_for_lect", "go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# make_cereal
if True:
    narration = Narrate(
        [
            'You pour the dregs of the cornflakes into a bowl, and follow it with the last of your milk.',
            'Your flatmate walks into the kitchen. They put the kettle on in silence.',
            'You don \'t think they like you.'
        ],
        True
    )
    options = Option(
        {"eat_in_room": "[Go to your room to eat]", "eat_in_kitchen": "[Eat in the kitchen]"},
        [])
    make_cereal = Script(
        "make_cereal",
        ["eat_in_room", "eat_in_kitchen"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# motivate
if True:
    narration = Narrate(
        [
            'It takes a lot of willpower but you manage to pull yourself from your bed.',
            'You get dressed and put your things in your bag.',
            'You feel quite hungry.'
        ],
        True
    )
    options = Option(
        {"go_lect_early": "[Go to your lecture]", "go_tesco": "[Go to the supermarket]",
         "go_kitchen": "[Go to the flat kitchen]"},
        [])
    motivate = Script(
        "motivate",
        ["go_kitchen"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# take_rest_1
if True:
    narration = Narrate(
        [
            "You think you could maybe close your eyes for a second..."
        ],
        True
    )
    options = Option({"go_sleep_1": "[Shut your eyes]"}, [])
    take_rest_1 = Script(
        "take_rest_1",
        ["go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# put_phone_down
if True:
    narration = Narrate(
        [
            "You are lying in your bed, the blanket’s weight is comforting.",
            "It is tempting to go back to sleep."
        ],
        True
    )
    options = Option({"go_sleep_1": "[Go back to sleep]", "take_rest_1": "[Take a second to rest]",
                      "motivate": "[Think about today]"}, [])
    put_phone_down = Script(
        "put_phone_down",
        ["go_sleep_1", "take_rest_1", "motivate"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# put_plate_room
if True:
    narration = Narrate(
        [
            'You put your used bowl and spoon on top of the pile of dishes on your desk.',
            'You have missed the start of your lecture.',
            'You feel an urge to curl up in your bed.'
        ],
        True
    )
    options = Option(
        {"BLOCKED1": "[Leave to meet Jordan]", "go_sleep_1": "[Go back to sleep]"},
        ["BLOCKED1"])
    put_plate_room = Script(
        "put_plate_room",
        ["go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# run_for_lect
if True:
    narration = Narrate(
        [
            'You realise that if you don\'t leave now you\'ll probably be late.',
            'You leave quickly, grabbing your bag from on top of the pile of clothes on your chair.',
            'On your way out you run into your flatmate going to the kitchen.'
        ],
        True
    )
    options = Option(
        {"go_lect_ontime": "[Run to your lecture]"},
        [])
    run_for_lect = Script(
        "run_for_lect",
        ["go_lect_ontime"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# eat_spoiled
if True:
    narration = Narrate(
        [
            'You sit and try to feign that nothing is wrong. ',
            'The cereal is disgusting.',
            'Your flatmate puts a teabag in a mug, and pours the now boiled water into it.',
            'Their toast pops up, and they cover it with butter and jam.',
            'They take their breakfast and leave.',
            'You feel judged.'
        ],
        True
    )
    options = Option(
        {"throw_out": "[Throw the cereal out]"},
        [])
    eat_spoiled = Script(
        "eat_spoiled",
        ["throw_out"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# think_today
if True:
    narration = Narrate(
        [
            'Today is Friday.',
            'You have a lecture at nine, and a workshop from twelve until two.',
            'Your friend Jordan wants to go for lunch at one.',
            'You think that your mum will phone you tonight at six.',
            'Your milk has expired.'
        ],
        True
    )
    options = Option(
        {"go_bed_1": "[Go back to bed]", "motivate": "[Motivate yourself to get ready]"},
        [])
    think_today = Script(
        "think_today",
        ["go_bed_1", "motivate"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# throw_out
if True:
    narration = Narrate(
        [
            'You pour the cereal into the bin, covering it over to make sure your flatmates don\'t notice.',
            'The clock says it is 10:58am.',
            'The sink basin is filled with dirty plates.',
            'You are late for your lecture.'
        ],
        True
    )
    options = Option(
        {"BLOCKED1": "[Wash your tableware]", "put_plate_room": "[Put your dirty tableware in your room]"},
        ["BLOCKED1"])
    throw_out = Script(
        "throw_out",
        ["put_plate_room"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# try_eat
if True:
    narration = Narrate(
        [
            'You continue eating the spoiled cereal.',
            'You get halfway through the bowl.',
            'It is 10:52am.',
            'If you ran you might make it to your lecture.',
            'You feel ill.'
        ],
        True
    )
    options = Option(
        {"BLOCKED1": "[Run for your lecture]", "go_sleep_1": "[Go back to sleep]"},
        ["BLOCKED1"])
    try_eat = Script(
        "try_eat",
        ["go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_sleep_1
if True:
    narration = Narrate(
        [
            'You decide to sleep for a bit longer.',
            '...'
        ],
        True
    )
    options = Option(
        {"wake_up_bad": "[Run for your lecture]"},
        [])
    go_sleep_1 = Script(
        "go_sleep_1",
        ["wake_up_bad"],
        [narration.narrate, options.listOpt],
        [None, None]
    )
# be_honest
if True:
    narration = Narrate(
        [
            "You tell Jordan you have a workshop soon.",
            "They smile but you can't help but feel you've made a mistake."
            "You apologise and decide to go to your workshop."
        ],
        True
    )
    options = Option(
        {"go_workshop": "[Go to your workshop]"}, []
    )
    be_honest = Script(
        "be_honest",
        ["go_workshop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_workshop
if True:
    narration = Narrate(
        ["You leave Jordan and decide to go to your workshop.",
         "Your workshop is a group project.",
         "You're terrified of getting the wrong answer.",
         "Your chest seizes, you can't go."],
        True
    )
    options = Option(
        {"home_no_shop": "[Go home]"}, []
    )
    go_workshop = Script(
        "go_workshop",
        ["home_no_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_lect_ontime
if True:
    narration = Narrate(
        [
            "The walk to university is short, and you get to the entrance of your lecture hall just as class is about to start.",
            "You notice Jordan is sitting in an empty row near the front of the lecture theatre.",
            "They haven't noticed you come in.",
            "You think if you try to sit with them you might still be standing when the lecturer starts talking."],
        True
    )
    options = Option(
        {"BLOCKED1": "[Go and sit with Jordan]", "BLOCKED2": "[Sit with others]",
         "sit_alone": "[Sit alone at the back of the theatre]"}, ["BLOCKED1", "BLOCKED2"]
    )
    go_lect_ontime = Script(
        "go-lect-ontime",
        ["sit_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_lect_early
if True:
    narration = Narrate(
        ["You leave your flat, managing not to run into any of your flatmates on your way out.",
         "The walk to university is short, and you get to the entrance of your lecture hall with a handful of minutes to spare.",
         "You notice Jordan is sitting in an empty row near the front of the lecture theatre.",
         "He hasn't noticed you come in."],
        True
    )
    options = Option(
        {"sit_jordan": "[Go and sit with Jordan]", "BLOCKED1": "[Sit with others]",
         "sit_alone": "[Sit alone at the back of the theatre]"},
        ["BLOCKED1"]
    )
    go_lect_early = Script(
        "go_lect_early",
        ["sit_jordan", "sit_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_before_jordan
if True:
    narration = Narrate(
        ["You exit the lecture hall shortly after the lecturer dismisses you.",
         "You leave the building and go somewhere you know Jordan will not see you."], True
    )
    options = Option(
        {"go_workshop": "[Go to your workshop"}, []
    )
    leave_before_jordan = Script(
        "leave_before_jordan",
        ["go_workshop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_with_jordan
if True:
    narration = Narrate(
        ["You wait at the back of the room for Jordan to notice you.",
         "When they do, they come over and ask you why you didn't come down to sit with them",
         "You can't bring yourself to tell them.",
         "You feel like you've let Jordan down."], True
    )
    options = Option(
        {"talk_jordan": "[Talk to Jordan]"}, []
    )
    leave_with_jordan = Script(
        "leave_with_jordan",
        ["talk_honest"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# sit_alone
if True:
    narration = Narrate(
        ["You decide to sit alone to watch the lecture.",
         "You can see Jordan at the front of the theatre."], True
    )
    options = Option(
        {"watch_alone": "[Watch the lecture alone]"}, []
    )
    sit_alone = Script(
        "sit_alone",
        ["watch_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# sit_jordan
if True:
    narration = Narrate(
        ["You sit down next to Jordan.",
         "They give you a warm smile and greet you as they clear "],
        True
    )
    options = Option(
        {"watch_jordan": "[Sit and watch the lecture with Jordan]"}, []
    )
    sit_jordan = Script(
        "sit_jordan",
        ["watch_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# talk_jordan
if True:
    narration = Narrate(
        ["Jordan begins talking about how boring your lecturer is.",
         "You agree passively with what they say unless they seem to want your input.",
         "They seem like they're ready to go to lunch.",
         "It is 12:02pm, your workshop will be starting soon."], True
    )
    options = Option(
        {"be_honest": "[Be honest with Jordan about the workshop]", "go_to_lunch": "[Go to lunch]"}, []
    )
    talk_jordan = Script(
        "talk_jordan",
        ["be_honest", "go_to_lunch"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# watch_alone
if True:
    narration = Narrate(
        ["The lecture passes slowly.",
         "You find the material dry and uninteresting.",
         "You finish taking notes slightly before the lecture ends, and pack your things away in your bag.",
         "You feel tired."], True
    )
    options = Option(
        {"leave_before_jordan": "[Leave before Jordan sees you]", "leave_with_jordan": "[Wait to leave with Jordan]"},
        []
    )
    watch_alone = Script(
        "watch_alone",
        ["leave_before_jordan", "leave_with_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# watch_with_jordan
if True:
    narration = Narrate(
        ["The lecture passes slowly.",
         "You find the material dry and uninteresting.",
         "Jordan seems not to be paying much attention.",
         "They keep showing you posts on their phone."], True
    )
    options = Option(
        {"talk_jordan": "[Talk to Jordan]"}, []
    )
    watch_with_jordan = Script(
        "watch_with_jordan",
        ["talk_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# be_honest
# sit_jordan
# go_workshop
# go_lect_ontime
# go_lect_early
# leave_before_jordan
# sit_alone
# talk_jordan
# leave_with_jordan
# watch_alone
# watch_with_jordan

# accept_drink
if True:
    narration = Narrate(
        [
            'Jordan nods, and goes to get themselves a drink.',
            'You notice a stranger looking at you. You don\'t like feeling like you stand out.',
            'You shrink against the wall, and try to spot Jordan.'
        ],
        True
    )
    options = Option(
        {"wait_for_jordan_club": "[Wait for Jordan.]", "look_for_jordan": "[Look for Jordan]"},
        [])
    accept_drink = Script(
        "accept_drink",
        ["wait_for_jordan_club"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# find_jordan_in_queue
if True:
    narration = Narrate(
        [
            'You approach the large queue, and Jordan waves to you. They are by themselves.',
            'You make your way to Jordan, and they tell you how excited they are to go in.',
            'Your breath is shaky.'
        ],
        True
    )
    options = Option(
        {"tell_jordan_leaving": "[Tell Jordan you have to leave.]", "enter_club": "[Go in]"},
        [])
    find_jordan_in_queue = Script(
        "find_jordan_in_queue",
        ["tell_jordan_leaving", "enter_club"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_club
if True:
    narration = Narrate(
        [
            'You leave Jordan behind, and walk back through the empty streets.',
            'You have to wash these clothes.',
            'You get home and change into your pyjamas.',
            'Lying in bed, you put your phone on charge and scroll for what seems like hours.'
        ],
        True
    )
    options = Option(
        {"sleep_invited": "[Go to sleep for the night]"},
        [])
    leave_club = Script(
        "leave_club",
        ["sleep_invited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_club_early
if True:
    narration = Narrate(
        [
            'You say goodbye to Jordan and they disappear into the club to meet more friends.',
            'You walk back through the cold streets and listen to music on your phone.	',
            'Your hands shiver as you try to pull your front door key out.',
            'You get to your room without being noticed.'
        ],
        True
    )
    options = Option(
        {"prep_for_bed": "[Get ready for bed]"},
        [])
    leave_club_early = Script(
        "leave_club_early",
        ["prep_for_bed"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# leave_club_early_number
if True:
    narration = Narrate(
        [
            'You say goodbye to Jordan and they disappear into the club to meet more friends, giving you a pat on the back before they go.',
            'You walk back through the cold streets and listen to music on your phone.	',
            'Your hands shiver as you try to pull your front door key out.',
            'You get to your room without being noticed.'
        ],
        True
    )
    options = Option(
        {"prep_for_bed": "[Get ready for bed]"},
        [])
    leave_club_early_number = Script(
        "leave_club_early",
        ["prep_for_bed"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# enter_club
if True:
    narration = Narrate(
        [
            'You wait in the queue with Jordan until you are both let in.',
            'It is too loud.',
            'Your chest is vibrating. and your head hurts.'
        ],
        True
    )
    options = Option(
        {"tell_jordan_leaving": "[Tell Jordan you have to leave]", "push_through": "[Push through]"},
        [])
    enter_club = Script(
        "enter_club",
        ["tell_jordan_leaving", "push_through"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# ignore_jordan_message
if True:
    narration = Narrate(
        [
            'You can\'t bring yourself to answer Jordan\s message.',
            'You worry you\'ve let them down.'
        ],
        True
    )
    options = Option(
        {"sleep_invited": "[Go to sleep for the night]"},
        [])
    ignore_jordan_message = Script(
        "ignore_jordan_message",
        ["sleep_invited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# keep_going_to_club
if True:
    narration = Narrate(
        [
            'You walk through the cold streets in the dark. The line for the club looks long.',
            'Your chest feels tight.'
        ],
        True
    )
    options = Option(
        {"turn_around_and_leave": "[Turn around and go home]", "look_for_jordan": "[Find Jordan in the queue]"},
        [])
    keep_going_to_club = Script(
        "keep_going_to_club",
        ["turn_around_and_leave", "look_for_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# 3

# buy_pasta_sauce
if True:
    narration = Narrate(
        [
            'You pick up some nice mascarpone sauce. You feel bad about spending money just on this sauce.',
            'You pack up your shopping and head home for the day.'
        ],
        True
    )
    options = Option(
        {"go_home": "[Go home]"},
        [])
    buy_pasta_sauce = Script(
        "buy_pasta_sauce",
        ["go_home"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_tesco
if True:
    narration = Narrate(
        [
            'You decide to go to the supermarket. You are out of food.',
            'You wander the aisles and see a large clock.',
            'It is 11:20am, you have missed your lecture.',
            'You have pasta in your cupboard.',
            'You could buy pasta sauce.'
        ],
        True
    )
    options = Option(
        {"go_straight_home": "[Go straight home]", "buy_pasta_sauce": "[Buy pasta sauce]"},
        [])
    go_tesco = Script(
        "go_tesco",
        ["go_straight_home", "buy_pasta_sauce"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# eat_quietly
if True:
    narration = Narrate(
        [
            'You continue to eat the sandwich without complaining.',
            'It is dry.',
            'You are disappointed.',
            'Jordan is talking about their plans with their friends tonight.',
            'They seem to have invited you out with them.'
        ],
        True
    )
    options = Option(
        {"make_an_excuse": "[Make an excuse]", "reluctant_agree": "[Reluctantly agree]"},
        [])
    eat_quietly = Script(
        "eat_quietly",
        ["make_an_excuse", "reluctant_agree"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# finish_lunch
if True:
    narration = Narrate(
        [
            'You finish eating your lunch.',
            'Jordan has another class to get to.',
            'You are on your own again.'
        ],
        True
    )
    options = Option(
        {"go_back_home": "[Go back home]"},
        []
    )
    finish_lunch = Script(
        "finish_lunch",
        ["go_back_home"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_to_lunch
if True:
    narration = Narrate(
        [
            'You go with Jordan to the cafe near the university.',
            'You quietly order your favourite sandwich, and then you both go to sit down.',
            'Jordan loudly discusses his distaste for your lecturer.',
            'Your food arrives.',
            'You are hungry.'
        ],
        True
    )
    options = Option(
        {"start_eating_lunch": "[Start eating your lunch]"},
        []
    )
    go_to_lunch = Script(
        "go_to_lunch",
        ["start_eating_lunch"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# make_an_excuse
if True:
    narration = Narrate(
        [
            'You tell Jordan you are busy tonight.',
            'They insist that there\'s no pressure to go, and that if you change your mind later you can come along late.',
            'You think you\'ve let them down.'
        ],
        True
    )
    options = Option(
        {"finish_lunch": "[Finish your lunch]"},
        []
    )
    make_an_excuse = Script(
        "make_an_excuse",
        ["finish_lunch"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# reluctant_agree
if True:
    narration = Narrate(
        [
            'You fumble your words but agree to go clubbing with Jordan and their friends.',
            'You don\'t really want to go.'
        ],
        True
    )
    options = Option(
        {"finish_lunch": "[Finish your lunch]"},
        []
    )
    reluctant_agree = Script(
        "reluctant_agree",
        ["finish_lunch"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# start_eating_lunch
if True:
    narration = Narrate(
        [
            'You take a bite from your sandwich.',
            'They seem to have messed up your order.',
            'You are hungry.'
        ],
        True
    )
    options = Option(
        {"eat_quietly": "[Eat quietly]", "tell_jordan_mistake": "[Tell Jordan about the mistake]"},
        []
    )
    start_eating_lunch = Script(
        "start_eating_lunch",
        ["eat_quietly", "tell_jordan_mistake"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# tell_jordan_mistake
if True:
    narration = Narrate(
        [
            'You watch a waiter approach.',
            'Jordan calls them over, and tells them that your food is wrong.',
            'You feel the waiter\'s judgement.',
            'You are embarassed.',
            'You get the meal you asked for eventually. It is much nicer.',
            'Jordan is talking about their plans with their friends tonight.',
            'They seem to have invited you out with them.'
        ],
        True
    )
    options = Option(
        {"make_an_excuse": "[Make an excuse]", "reluctant_agree": "[Reluctantly agree to go]"},
        []
    )
    tell_jordan_mistake = Script(
        "tell_jordan_mistake",
        ["make_an_excuse", "reluctant_agree"],
        [narration.narrate, options.listOpt],
        [None, None]
    )
# go_to_club


# look_for_jordan

# push_through

# respond

# smile_and_nod

# tell_jordan_leaving

# try_conversation

# turn_around_and_leave

# wait_for_jordan_club

# wake_up_bad
if True:
    narration = Narrate(
        [
            'You wake up.',
            'You realise it is getting dark outside.',
            'It is Friday. Your mum will probably call you soon.'
        ],
        True
    )
    options = Option(
        {"call_bad": "[Run for your lecture]"},
        [])
    wake_up_bad = Script(
        "wake_up_bad",
        ["call_bad"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# evasive_call
if True:
    narration = Narrate(
        [
            'You avoid answering her questions directly.',
            'The call ends quickly, with little but small talk.',
            'You think she\'s worried about you.'
            'You feel hungry.'
        ],
        True
    )
    options = Option(
        {"order_dinner": "[Order dinner]", "make_dinner": "[Make dinner]"},
        [])
    evasive_call = Script(
        "evasive_call",
        ["order_dinner", "make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# lie_call
if True:
    narration = Narrate(
        [
            'You lie. You claim to have had a productive day.',
            'She seems pleased to hear about what you did.',
            'The call comes to an end.',
            'You feel guilt.',
            'You feel hunger.'

        ],
        True
    )
    options = Option(
        {"make_dinner": "[Make dinner]", "order_dinner": "[Order dinner]"},
        [])
    lie_call = Script(
        "lie_call",
        ["order_dinner", "make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# prepare_for_call
if True:
    narration = Narrate(
        [
            'You sit waiting by your phone'
        ],
        True
    )
    prepare_for_call = Script(
        "prepare_for_call",
        ["call_bad", "call_good"],
        [narration.narrate],
        [None]
    )

# call_bad
if True:
    narration = Narrate(
        [
            'Today has not been good.',
            'At 6:02pm, your phone begins to ring. It\'s your mum.',
        ],
        True
    )
    options = Option(
        {"lie_call": "[Lie about your day]", "evasive_call": "[Answer ambiguously]"},
        [])
    call_bad = Script(
        "call_bad",
        ["lie_call", "evasive_call"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# call_good
if True:
    narration = Narrate(
        [
            'You spend the next few minutes trying to remember everything that happened today.',
            'At 6:02pm, your phone begins to ring. It\'s your mum.',
            'The call is pleasant, consisting of small talk, until she asks how your day was.',
            'You tell her about your day...',
            'She seems pleased to hear about what you did.',
            'The call comes to an end.',
            'You feel at ease.',
            'You feel hungry.'
        ],
        True
    )
    options = Option(
        {"order_dinner": "[Order dinner]", "make_dinner": "[Make dinner]"},
        [])
    call_good = Script(
        "call_good",
        ["order_dinner", "make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# make_dinner
if True:
    narration = Narrate(
        [
            'You prepare your dinner.',
            'You take it to your bedroom.'
        ],
        True
    )
    options = Option(
        {"watch_show": "[Watch shows]", "finish_workshop": "[Finish workshop]", "prepare_club": "[Prepare for the club",
         "sleep_invited": "[Go to sleep for the night (if invited by Jordan)]",
         "sleep_uninvited": "[Go to sleep for the night]"},
        [])
    make_dinner = Script(
        "make_dinner",
        ["watch_show", "finish_workshop", "prepare_club", "sleep_invited", "sleep_uninvited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# watch_show
if True:
    narration = Narrate(
        [
            'You decide to spend part of the night watching tv shows.',
            'You put on your favourite show and spend the next few hours enjoying it.'
        ],
        True
    )
    options = Option(
        {"watch_show_later": "[Continue to watch shows]", "read_book": "[Read a book]",
         "sleep_invited": "[Go to sleep for the night (if invited by Jordan)]",
         "sleep_uninvited": "[Go to sleep for the night]"},
        [])
    watch_show = Script(
        "watch_show",
        ["watch_show_later", "read_book", "sleep_invited", "sleep_uninvited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# watch_show_later
if True:
    narration = Narrate(
        [
            'You decide to keep watching tv shows. You feel your head starting to hurt and your eyelids getting heavy as you struggle to keep awake.',
            'You realise you should charge your phone.'
        ],
        True
    )
    options = Option(
        {"sleep_invited": "[Go to sleep for the night (if invited by Jordan)]",
         "sleep_uninvited": "[Go to sleep for the night]"},
        [])
    watch_show_later = Script(
        "watch_show",
        ["sleep_invited", "sleep_uninvited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# finish_workshop
if True:
    narration = Narrate(
        [
            'You spend the next two hours doing the workshop you missed.',
            'It is difficult, but you power through it.',
            'You feel accomplished.'
        ],
        True
    )
    options = Option(
        {"sleep_invited": "[Go to sleep for the night (if invited by Jordan)]",
         "sleep_uninvited": "[Go to sleep for the night]", "read_book": "[Read a book]"},
        [])
    finish_workshop = Script(
        "finish_workshop",
        ["sleep_invited", "sleep_uninvited", "read_book"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# sleep_uninvited
if True:
    narration1 = Narrate(
        [
            'As you put your phone on charge for the night, you receive another text from Jordan.'
        ],
        True
    )
    texting = Text(
        ["hey you doing alright? didn't see you before?"],
        "Jordan",
        [False],
        True,
        0,
        43,
        "00:09")
    narration2 = Narrate(
        [
            '........',
            'It is 10:35am. Your eyes are heavy and you don\'t hear the sound of your alarm.',
            'You are tired.'
        ],
        True
    )
    ending = End()
    sleep_uninvited = Script(
        "sleep_uninvited",
        [],
        [os.system, narration1.narrate, texting.conversation, narration2.narrate, ending.ending],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None]
    )

# sleep_invited
if True:
    narration1 = Narrate(
        [
            'As you put your phone on charge for the night, you receive another text from Jordan.'
        ],
        True
    )
    texting = Text(
        ["shame you couldnt come tonight, its a lot of fun. hope youre doing okay"],
        "Jordan",
        [False],
        True,
        0,
        43,
        "00:09")
    narration2 = Narrate(
        [
            '........',
            'It is 10:35am. Your eyes are heavy and you don\'t hear the sound of your alarm.',
            'You are tired.'
        ],
        True
    )
    ending = End()
    sleep_invited = Script(
        "sleep_invited",
        [],
        [os.system, narration1.narrate, texting.conversation, narration2.narrate, ending.ending],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None]
    )

# read_book
if True:
    narration = Narrate(
        [
            'You pick up a book you\'ve been trying to read for the past few weeks.',
            'It is difficult, but you power through it.',
            'You spend the next hour or so reading, and feel calmer.',
            'You are tired.'
        ],
        True
    )
    options = Option(
        {"sleep_invited": "[Go to sleep for the night (if invited by Jordan)]",
         "sleep_uninvited": "[Go to sleep for the night]"},
        [])
    read_book = Script(
        "read_book",
        ["sleep_invited", "sleep_uninvited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# prep_for_bed
if True:
    narration1 = Narrate(
        [
            'As you put your phone on charge for the night, you receive another text from Jordan.'
        ],
        True
    )
    texting = Text(
        ["thanks for coming out tonight, was great to see you having fun. hope youre up for it again soon"],
        "Jordan",
        [False],
        True,
        0,
        43,
        "00:09")
    narration2 = Narrate(
        [
            'You drift off to sleep.',
            'You sleep'
        ],
        True
    )
    narration3 = Narrate(
        [
            '........',
            'It is 10:35am. Your eyes are heavy and you don\'t hear the sound of your alarm.',
            'You are tired.'
        ],
        True
    )
    ending = End()
    prep_for_bed = Script(
        "prep_for_bed",
        [],
        [os.system, narration1.narrate, texting.conversation, narration2.narrate, narration3.narrate, ending.ending],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None, None]
    )

# prep_for_bed_number
if True:
    narration1 = Narrate(
        [
            'As you put your phone on charge for the night, you receive another text from Jordan.'
        ],
        True
    )
    texting = Text(
        ["bet youre glad you came out tonight eh tiger? hope we can go clubbing together soon"],
        "Jordan",
        [False],
        True,
        0,
        43,
        "00:09")
    narration2 = Narrate(
        [
            'You drift off to sleep.',
            'You sleep'
        ],
        True
    )
    narration3 = Narrate(
        [
            '........',
            'It is 10:35am. Your eyes are heavy and you don\'t hear the sound of your alarm.',
            'You are tired.'
        ],
        True
    )
    ending = End()
    prep_for_bed_number = Script(
        "prep_for_bed_number",
        [],
        [os.system, narration1.narrate, texting.conversation, narration2.narrate, narration3.narrate, ending.ending],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None, None]
    )

# golden_end
if True:
    narration1 = Narrate(
        [
            'As you put your phone on charge for the night, you receive another text from Jordan.'
        ],
        True
    )
    texting = Text(
        ["hope youre doing okay. always here if you need to talk"],
        "Jordan",
        [False],
        True,
        0,
        43,
        "00:09")
    narration2 = Narrate(
        [
            'You drift off to sleep.',
            'You sleep'
        ],
        True
    )
    narration3 = Narrate(
        [
            '........',
            'It is 8:30am. You wake to the sound of your alarm.',
            'You are tired.'
        ],
        True
    )
    ending = End()
    sleep_invited = Script(
        "sleep_invited",
        [],
        [os.system, narration1.narrate, texting.conversation, narration2.narrate, narration3.narrate, ending.ending],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None, None]
    )

# push_through
if True:
    narration = Narrate(
        [
            'You push through the cacophony, and find an empty point against the wall.',
            'You stand talking to Jordan for a while. They offer to buy you a drink.'
        ],
        True
    )
    options = Option(
        {"accept_drink": "[Accept the drink]", "BLOCKED1": "[Decline the drink]"},
        ["BLOCKED1"])
    push_through = Script(
        "push_through",
        ["accept_drink"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# respond
if True:
    texting1 = Text(
        ["Hey, sorry, I can't make it tonight."],
        "Jordan",
        [True],
        True,
        0,
        7,
        "10:31")
    texting2 = Text(
        ["ah thats okay, maybe next time"],
        "Jordan",
        [False],
        False,
        1,
        7,
        "10:55")
    options = Option(
        {"sleep_invited": "[Go to sleep invited]"},
        [])
    respond = Script(
        "respond",
        [],
        [os.system, texting1.conversation, texting2.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None, None, None]
    )

# smile_and_nod
if True:
    narration = Narrate(
        [
            'You feel as though the stranger grows colder, and within a few minutes they spot a friend and leave.',
            'Jordan returns with your drinks.', 'You have a few more and decide to go home early.'
        ],
        True
    )
    options = Option(
        {"leave_club_early_number": "[Go home]"},
        [])
    smile_and_nod = Script(
        "smile_and_nod",
        ["leave_club_early_number"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# try_conversation
if True:
    narration = Narrate(
        [
            'You say goodbye to Jordan and they disappear into the club to meet more friends, giving you a pat on the back before they go.',
            'You walk back through the cold streets and listen to music on your phone.',
            'Your hands shiver as you try to pull your front door key out.'
        ],
        True
    )
    options = Option(
        {"leave_club_early_number": "[Go home]"},
        [])
    try_conversation = Script(
        "try_conversation",
        ["leave_club_early_number"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# tell_jordan_leaving
if True:
    narration = Narrate(
        [
            'Jordan looks upset.You feel like you\'ve killed their mood.',
            'They tell you they understand, and give you a hug.',
            'You feel pitied.'
        ],
        True
    )
    options = Option(
        {"go_home": "[Go home]"},
        [])
    tell_jordan_leaving = Script(
        "tell_jordan_leaving",
        ["go_home"],
        [narration.narrate, options.listOpt],
        [None, None]
    )
# turn_around_and_leave
if True:
    narration = Narrate(
        [
            'Jordan looks upset.You feel like you\'ve killed their mood.',
            'They tell you they understand, and give you a hug.',
            'You feel pitied.'
        ],
        True
    )
    texting = Text(
        ["hey are you on your way?"],
        "Jordan",
        [False],
        True,
        0,
        8,
        "10:3")
    options = Option(
        {"respond": "[Respond]", "ignore_jordan_message": "[Ignore their message]"},
        [])
    turn_around_and_leave = Script(
        "turn_around_and_leave",
        ["respond", "ignore_jordan_message"],
        [os.system, texting.conversation, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None]
    )

# go_home
if True:
    narration = Narrate(
        ["You leave Jordan behind and walk back through the empty streets.",
         "You have to wash these clothes.",
         "You get home and change into your pyjamas.",
         "Lying in bed, you put your phone on charge and scroll for what seems like hours."]
        , True)
    options = Option(
        {"sleep_uninvited": "[Go to sleep for the night]"}, []
    )
    go_home = Script(
        "go_home",
        ["sleep_uninvited"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# look_for_jordan
if True:
    narration = Narrate(
        ["You slink away from the stranger's gaze, and move towards the bar.",
         "You see Jordan laughing and talking to another person.",
         "You think you recognise them from your lectures, but don't think they'd recognise you."], True
    )
    options = Option(
        {"wait_for_jordan_club": "[Wait for Jordan]", "BLOCKED1": "[Say hi]"}
        , ["BLOCKED1"])
    look_for_jordan = Script(
        "look_for_jordan",
        ["wait_for_jordan_club"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# go_to_club
if True:
    narration = Narrate(
        ["You prepare to meet Jordan and their friends at the club.",
         "Tonight seems like it might be another long night.",
         "You cannot remember who Jordan said would be there.",
         "You leave your flat with enough time to get to the club.",
         "You feel uneasy."], True
    )
    options = Option(
        {"turn_around_and_leave": "[Turn around and go home]", "keep_going_to_club": "[Keep going to the club]"}, []
    )
    go_to_club = Script(
        "go_to_club",
        ["turn_around_and_leave", "keep_going_to_club"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# wait_for_jordan_club
if True:
    narration = Narrate(
        ["The stranger approaches you, introducing themselves and saying they are on your course.",
         "You don't know what they want.",
         "They begin to make small talk."
         ], True
    )
    options = Option(
        {"smile_and_nod": "[Smile and nod]", "try_conversation": "[Try and make conversation]"}, []
    )
    wait_for_jordan_club = Script(
        "wait_for_jordan_club",
        ["smile_and_nod", "try_conversation"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# gold_read_book
if True:
    narration = Narrate(
        [
            'You pick up a book you\'ve been trying to read for the past few weeks.',
            'It is difficult, but you power through it.',
            'You spend the next hour or so reading, and feel calmer.',
            'You are tired.'
        ],
        True
    )
    options = Option(
        {"golden_end": "[Go to sleep]"},
        [])
    gold_read_book = Script(
        "gold_read_book",
        ["golden_end"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

superStarYay = {"start": start,
                "make_an_excuse": make_an_excuse,
                "gold_read_book": gold_read_book,
                "wake": wake_1,
                "get_up_1": get_up_1,
                "song_play_out": song_play_out,
                "go_bed_1": go_bed_1,
                "read_message": read_message,
                "finish_text": finish_text,
                "reply_1": reply_1,
                "sorry_workshop": sorry_workshop,
                "reply_yeah": reply_yeah,
                "check_phone": check_phone,
                "eat_in_kitchen": eat_in_kitchen,
                "go_kitchen": go_kitchen,
                "get_food": get_food,
                "eat_in_room": eat_in_room,
                "leave_cereal": leave_cereal,
                "make_cereal": make_cereal,
                "motivate": motivate,
                "put_phone_down": put_phone_down, "put_plate_room": put_plate_room,
                "run_for_lect": run_for_lect,
                "eat_spoiled": eat_spoiled,
                "think_today": think_today,
                "throw_out": throw_out,
                "try_eat": try_eat,
                "sit_jordan": sit_jordan,
                "go_lect_early": go_lect_early,
                "go_lect_ontime": go_lect_ontime,
                "leave_with_jordan": leave_with_jordan,
                "sit_alone": sit_alone,
                "talk_jordan": talk_jordan,
                "watch_alone": watch_alone,
                "watch_with_jordan": watch_with_jordan,
                "buy_pasta_sauce": buy_pasta_sauce,
                "go_tesco": go_tesco,
                "eat_quietly": eat_quietly,
                "finish_lunch": finish_lunch,
                "go_to_lunch": go_to_lunch,
                "make an excuse": make_an_excuse,
                "reluctant_agree": reluctant_agree,
                "start_eating_lunch": start_eating_lunch,
                "tell_jordan_mistake": tell_jordan_mistake,
                "buy_ready_meal": buy_ready_meal,
                "go_back_home": go_back_home,
                "go_home_no_shop": go_home_no_shop,
                "go_home_shop": go_home_shop,
                "go_straight_home": go_straight_home,
                "go_to_shop": go_to_shop,
                "leave_shop": leave_shop,
                "study_afternoon": study_afternoon,
                "watch_show": watch_show,
                "evasive_call": evasive_call,
                "lie_call": lie_call,
                "call_good": call_good,
                "call_bad": call_bad,
                "wake_up_bad": wake_up_bad,
                "accept_drink": accept_drink,
                "find_jordan_in_queue": find_jordan_in_queue,
                "prep_for_bed": prep_for_bed,
                "prep_for_bed_number": prep_for_bed_number,
                "leave_club": leave_club,
                "leave_club_early": leave_club_early,
                "leave_club_early_number": leave_club_early_number,
                "enter_club": enter_club,
                "ignore_jordan_message": ignore_jordan_message,
                "keep_going_to_club": keep_going_to_club,
                "go_home": go_home,
                "go_to_club": go_to_club,
                "look_for_jordan": look_for_jordan,
                "push_through": push_through,
                "respond": respond,
                "smile_and_nod": smile_and_nod,
                "tell_jordan_leaving": tell_jordan_leaving,
                "try_conversation": try_conversation,
                "turn_around_and_leave": turn_around_and_leave,
                "wait_for_jordan_club": wait_for_jordan_club,
                "prepare_for_call": prepare_for_call,
                "read_book": read_book,
                "make_an_excuse":make_an_excuse,
                "wake": wake_1,
                "get_up_1": get_up_1,
                "song_play_out": song_play_out,
             "go_bed_1": go_bed_1,
             "read_message": read_message,
             "finish_text": finish_text,
             "reply_1": reply_1,
             "sorry_workshop": sorry_workshop,
             "reply_yeah": reply_yeah,
             "check_phone": check_phone,
             "eat_in_kitchen": eat_in_kitchen,
             "go_kitchen": go_kitchen,
             "get_food": get_food,
             "eat_in_room": eat_in_room,
             "leave_cereal": leave_cereal,
             "make_cereal": make_cereal,
             "motivate": motivate,
             "put_phone_down": put_phone_down, "put_plate_room": put_plate_room,
             "run_for_lect": run_for_lect,
             "eat_spoiled": eat_spoiled,
             "think_today": think_today,
             "throw_out": throw_out,
             "try_eat": try_eat,
             "sit_jordan": sit_jordan,
             "go_lect_early": go_lect_early,
             "go_lect_ontime": go_lect_ontime,
             "leave_with_jordan": leave_with_jordan,
             "sit_alone": sit_alone,
             "talk_jordan": talk_jordan,
             "watch_alone": watch_alone,
             "watch_with_jordan": watch_with_jordan,
             "buy_pasta_sauce": buy_pasta_sauce,
             "go_tesco": go_tesco,
             "eat_quietly": eat_quietly,
             "finish_lunch": finish_lunch,
             "go_to_lunch": go_to_lunch,
             "make an excuse": make_an_excuse,
             "reluctant_agree": reluctant_agree,
             "start_eating_lunch": start_eating_lunch,
             "tell_jordan_mistake": tell_jordan_mistake,
             "buy_ready_meal": buy_ready_meal,
             "go_back_home": go_back_home,
             "go_home_no_shop": go_home_no_shop,
             "go_home_shop": go_home_shop,
             "go_straight_home": go_straight_home,
             "go_to_shop": go_to_shop,
             "leave_shop": leave_shop,
             "study_afternoon": study_afternoon,
             "watch_show": watch_show,
             "evasive_call": evasive_call,
             "lie_call": lie_call,
             "call_good": call_good,
             "call_bad": call_bad,
             "wake_up_bad": wake_up_bad,
             "accept_drink": accept_drink,
             "find_jordan_in_queue": find_jordan_in_queue,
             "prep_for_bed": prep_for_bed,
             "prep_for_bed_number": prep_for_bed_number,
             "leave_club": leave_club,
             "leave_club_early": leave_club_early,
             "leave_club_early_number": leave_club_early_number,
             "enter_club": enter_club,
             "ignore_jordan_message": ignore_jordan_message,
             "keep_going_to_club": keep_going_to_club,
             "go_home": go_home,
             "go_to_club": go_to_club,
             "look_for_jordan": look_for_jordan,
             "push_through": push_through,
             "respond": respond,
             "smile_and_nod": smile_and_nod,
             "tell_jordan_leaving": tell_jordan_leaving,
             "try_conversation": try_conversation,
             "turn_around_and_leave": turn_around_and_leave,
             "wait_for_jordan_club": wait_for_jordan_club,
             "prepare_for_call": prepare_for_call,
             "read_book": read_book,
             "go_sleep_1": go_sleep_1,
             "sleep_uninvited": sleep_uninvited}


for i in superStarYay.values():
    ret = i.runScript()
    print(i,ret)
def game(working):
    done = False
    toRun = start.runScript()
    lect = False
    lunch = False
    shop = False
    shows = False
    callGood = False
    workshop = False

    while not done:
        if toRun == "QUIT":
            delay_print("QUITTING PROGRAM...")
            sys.exit()
        if toRun == "go_lect_early" or toRun == "go_lect_ontime":
            lect = True
        if toRun == "call_good":
            callGood = True
        if toRun == "watch_shows":
            shows = True
        if toRun == "finish_workshop":
            workshop = True
        if toRun == "go_to_lunch":
            lunch = True
        if toRun == "buy_ready_meal":
            shop = True
        if toRun == "read_book" and lect and lunch and callGood and shows and workshop and shop:
            toRun = "gold_read_book"
        scriptRun = working.get(toRun)
        toRun = scriptRun.runScript()


game(superStarYay)
