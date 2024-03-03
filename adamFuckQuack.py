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


def statusBar(phone,battery,timer):
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
            statusBar(True,self.battery,self.timer)
        you = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.GREEN}You:")
        friend = str(f"{Style.RESET_ALL}{Style.NORMAL}{Fore.BLUE}{contactValue}:")
        count = 0
        for owner in self.yourText:
            if not self.read_bool[count]:
                sleep(0.8)
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
        if self.bar:
            statusBar(False,None,None)
        print("")
        for line in self.lines:
            split = textwrap.fill(line, int(TEXT_WINDOW * 0.83))
            # the .83 just gives the text a bit of a chance on the screen lol
            delay_print(split)
            print("\n")
            sleep(0.8)

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
        print(" ")
        choice = self.getInput(indexes, keys)
        print(" ")
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
                    print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}You can't")
                    return self.getInput(indexes, keys)
            print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}This isn't something you feel you can do (INVALID OPTION)")
            return self.getInput(indexes, keys)
        except:
            print(f"\n{Style.RESET_ALL}{Style.DIM}{Fore.WHITE}This isn't something you feel you can do (INVALID OPTION)")
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

#start
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

#wake_1
if True:
    narration = Narrate(
        [
            "It is 8:32am. Your eyes are heavy and you can hear the sound of your alarm - your favourite song - sounding out from your desk across the room.",
            "You are tired."
        ],
        True
    )

    options = Option({"get_up_1": "[Get up and turn it off]",
               "song_play_out": "[Let it finish, the song is nearly over anyway]"}, None)
    wake_1 = Script(
        "wake_1",
        ["get_up_1","song_play_out"],
        [os.system, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

#get_up_1
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
        ["check_phone","go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#song_play_out
if True:
    narration = Narrate(
        [
            "The alarm eventually stops.",
            "Your bed is comfortable, you do not want to move."
        ],
        True
    )
    options = Option({"BLOCKED1": "[Get up and get ready for your day]", "motivate": "[Motivate yourself to get ready]", "think_1":"[Think about today]", "go_sleep_1": "Go back to sleep"}, ["BLOCKED1"])
    song_play_out = Script(
        "song_play_out",
        ["motivate","think_1","go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#go_bed_1
if True:
    narration = Narrate(
        [
            "You are lying in your bed, the blanket’s weight is comforting.",
            "It is tempting to go back to sleep."
        ],
        True
    )
    options = Option({"go_sleep_1": "[Go back to sleep]", "take_rest_1": "[Take a second to rest]", "motivate":"[Think about today]"}, [])
    go_bed_1 = Script(
        "go_bed_1",
        ["motivate","think_1","go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#reply_1
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
    options = Option({"reply_yeah": "Yeah I think so", "sorry_workshop": "Sorry, I've got a workshop I need to go to.","finish_text":"[Leave him on read]"}, None)
    reply_1 = Script(
        "reply_1",
        ["reply_yeah","sorry_workshop","finish_text"],
        [os.system,texting.conversation, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'),None, None, None]
    )

#finish_text
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

#read_message
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

#sorry_workshop
if True:
    texting = Text(
        ["hey, you still good to meet later?",
         "Sorry, I've got a workshop I need to go to.",
         "ah shit man, that sucks",
         "maybe we can do next monday? I think I have some free time after 2?"],
        "Jordan",
        [False,True,False,False],
        True,
        1,
        27,
        "10:33")
    options = Option({"put_phone_down": "[Leave him on read]", "BLOCKED1": "[Commit to meeting him on Monday]","put_phone_down":"[Give a non-commital response]"}, ["BLOCKED1"])
    sorry_workshop = Script(
        "sorry_workshop",
        ["put_phone_down"],
        [os.system, texting.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None]
    )

#reply_yeah
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
    options = Option({"put_phone_down": "[Leave him on read]", "BLOCKED1": "[Let him know you will be there]"}, ["BLOCKED1"])
    reply_yeah = Script(
        "reply_yeah",
        ["put_phone_down"],
        [os.system, texting1.conversation, texting2.conversation, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, None, None]
    )

#check_phone
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
            ["read_message","go_bed_1"],
            [narration.narrate, options.listOpt],
            [None, None]
        )

#eat_in_kitchen
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
    options = Option({"BLOCKED1": "[Throw the spoiled cereal in the bin]", "eat_spoiled": "[Slowly eat the spoiled cereal and wait for them to leave]"}, ["BLOCKED1"])
    eat_in_kitchen = Script(
            "eat_in_kitchen",
            ["eat_spoiled"],
            [narration.narrate, options.listOpt],
            [None, None]
        )

#get_food
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
        ["make_cereal","run_for_lect"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#go_kitchen
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
        [os.system,narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'),None, None]
    )

#eat_in_room
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
        ["leave_cereal","try_eat"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#leave_cereal
if True:
    narration = Narrate(
        [
            "You leave the spoiled cereal bowl on your desk.",
            "You pick up your phone.","It is 10:50am.",
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

#make_cereal
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

#motivate
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
        {"go_lect_early": "[Go to your lecture]","go_tesco": "[Go to the supermarket]", "go_kitchen": "[Go to the flat kitchen]"},
        [])
    motivate = Script(
        "motivate",
        ["go_kitchen"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#put_phone_down
if True:
    narration = Narrate(
        [
            "You are lying in your bed, the blanket’s weight is comforting.",
            "It is tempting to go back to sleep."
        ],
        True
    )
    options = Option({"go_sleep_1": "[Go back to sleep]", "take_rest_1": "[Take a second to rest]", "motivate":"[Think about today]"}, [])
    put_phone_down = Script(
        "put_phone_down",
        ["go_sleep_1","take_rest_1","motivate"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#put_plate_room
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

#run_for_lect
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

#eat_spoiled
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

#think_today
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
        {"go_bed_1": "[Go back to bed]","motivate":"[Motivate yourself to get ready]"},
        [])
    think_today = Script(
        "think_today",
        ["go_bed_1","motivate"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#throw_out
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
        {"BLOCKED1": "[Wash your tableware]","put_plate_room":"[Put your dirty tableware in your room]"},
        ["BLOCKED1"])
    throw_out = Script(
        "throw_out",
        ["put_plate_room"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#try_eat
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

#go_sleep_1
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

#wake_up_bad
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
        {"call_mum_bad": "[Run for your lecture]"},
        [])
    wake_up_bad = Script(
        "wake_up_bad",
        ["call_mum_bad"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# evasive
if True:
    narration = Narrate(
        [
            'You avoid answering her questions directly.',
            'The call ends quickly, with little but small talk.',
            'You think she\'s worried about you.'
        ],
        True
    )
    options = Option(
        {"order_dinner": "[Order dinner]","make_dinner": "[Make dinner]"},
        [])
    evasive = Script(
        "evasive",
        ["order_dinner","make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )


# evasive
if True:
    narration = Narrate(
        [
            'You lie. You claim to have had a productive day.',
            'She seems pleased to hear about what you did.',
            'You feel guilt.'
        ],
        True
    )
    options = Option(
        {"order_dinner": "[Order dinner]","make_dinner": "[Make dinner]"},
        [])
    evasive = Script(
        "evasive",
        ["order_dinner","make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# prepare_for_call

# call_bad

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
        {"order_dinner": "[Order dinner]","make_dinner": "[Make dinner]"},
        [])
    evasive = Script(
        "evasive",
        ["order_dinner","make_dinner"],
        [narration.narrate, options.listOpt],
        [None, None]
    )


allScript = {"start" : start,"wake" : wake_1,"get_up_1" : get_up_1,"song_play_out" : song_play_out,"go_bed_1" : go_bed_1,"read_message" : read_message,"finish_text" : finish_text,"reply_1" : reply_1,"sorry_workshop" : sorry_workshop,"reply_yeah" : reply_yeah,"check_phone" : check_phone,"eat_in_kitchen" : eat_in_kitchen,"go_kitchen" : go_kitchen,"get_food" : get_food,"eat_in_room" : eat_in_room,"leave_cereal" : leave_cereal,"make_cereal" : make_cereal,"motivate" : motivate,"put_phone_down" : put_phone_down,"put_plate_room" : put_plate_room,"run_for_lect" : run_for_lect,"eat_spoiled" : eat_spoiled,"think_today" : think_today,"throw_out" : throw_out,"try_eat" : try_eat,"sit_with_jordan" : sit_with_jordan,"go_lect_early" : go_lect_early,"go_lect_ontime" : go_lect_ontime,"leave_without_jordan" : leave_without_jordan,"sit_alone" : sit_alone,"talk_to_jordan" : talk_to_jordan,"wait_for_jordan" : wait_for_jordan,"watch_alone" : watch_alone,"watch_with_jordan" : watch_with_jordan,"buy pasta sauce" : buy pasta sauce,"go_tesco" : go_tesco,"eat_quietly" : eat_quietly,"finish_lunch" : finish_lunch,"go_to_lunch" : go_to_lunch,"make an excuse" : make an excuse,"reluctant_agree" : reluctant_agree,"start_eating_lunch" : start_eating_lunch,"tell_jordan_mistake" : tell_jordan_mistake,"buy_ready_meal" : buy_ready_meal,"go_home" : go_home,"go_home_no_shop" : go_home_no_shop,"go_home_shop" : go_home_shop,"go_straight_home" : go_straight_home,"go_to_shop" : go_to_shop,"leave_shop" : leave_shop,"study_afternoon" : study_afternoon,"watch_show" : watch_show,"evasive" : evasive,"prepare_for_call" : prepare_for_call,"prepare_to_talk_about_day" : prepare_to_talk_about_day,"wake_up_late" : wake_up_late,"accept_drink" : accept_drink,"find_jordan_in_queue" : find_jordan_in_queue,"prep_for_bed" : prep_for_bed,"prep_for_bed_number" : prep_for_bed_number,"leave_club" : leave_club,"leave_club_early" : leave_club_early,"leave_club_early_number" : leave_club_early_number,"enter_club" : enter_club,"sleep_for_night" : sleep_for_night,"ignore_jordan_message" : ignore_jordan_message,"keep_going_to_club" : keep_going_to_club,"go_to_club" : go_to_club,"look_for_jordan" : look_for_jordan,"push_through" : push_through,"respond" : respond,"smile_and_nod" : smile_and_nod,"tell_jordan_leaving" : tell_jordan_leaving,"try_conversation" : try_conversation,"turn_around_and_leave" : turn_around_and_leave,"wait_for_jordan_club" : wait_for_jordan_club}

def main(allScript):
    done = False
    toRun = start.runScript()
    while not done:
        if toRun == "QUIT":
            delay_print("QUITTING PROGRAM...")
            sys.exit()
        scriptRun = allScript.get(toRun)
        toRun = scriptRun.runScript()

main(allScript)
