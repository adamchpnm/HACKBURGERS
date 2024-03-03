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


def statusBar(phone,battery,time):
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
            statusBar(True,self.battery,time)
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

class Title:
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
        True
    )
    options = Option({"wake": "[Wake up]"}, None)
    start = Script(
        "start",
        ["wake_1"],
        [os.system, title1.print, sleep, narration.narrate, sleep, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'), None, 1, None, 1, None]
    )

#wake
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
    options = Option({"check_phone_1": "[Check phone]", "go_bed_1": "[Go back to bed]", "TEST_BLOCK": "OPTION INVALID"}, [3])
    get_up_1 = Script(
        "get_up_1",
        ["check_phone_1","go_bed_1"],
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
    options = Option({"BLOCKED1": "[Get up and get ready for your day]", "motivate": "[Motivate yourself to get ready]", "think_1":"[Think about today]", "go_sleep_1": "Go back to sleep"}, [1])
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
    song_play_out = Script(
        "song_play_out",
        ["motivate","think_1","go_bed_1"],
        [narration.narrate, options.listOpt],
        [None, None]
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
    narration = Narrate(
        [
            "You recall that Jordan invited you to meet for lunch today at 1pm.",
            "You have an important workshop from 12pm until 2pm."
        ],
        True
    )
    options = Option({"reply_yeah": "Yeah I think so", "sorry_workshop": "Sorry, I've got a workshop I need to go to.","finish_text":"[Leave him on read]"}, None)
    read_message = Script(
        "read_message",
        ["reply_yeah","sorry_workshop","finish_text"],
        [os.system,texting.conversation, narration.narrate, options.listOpt],
        [('cls' if os.name == 'nt' else 'clear'),None, None, None]
    )

#finish_text
if True:
    options = Option({"put_phone_down": "[Put down your phone]"}, None)
    put_phone_down = Script(
            "put_phone_down",
            ["put_phone_down"],
            [options.listOpt],
            [None]
        )

#reply_1
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
    options = Option({"finish_texting": "[Leave him on read]", "BLOCKED1": "[Commit to meeting him on Monday]","finish_texting":"[Give a non-commital response]"}, [2])
    sorry_workshop = Script(
        "sorry_workshop",
        ["finish_texting"],
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
        [False, True, False],
        True,
        0,
        26,
        "10:41")
    options = Option({"finish_texting": "[Leave him on read]", "BLOCKED1": "[Let him know you will be there]"}, [2])
    reply_yeah = Script(
        "reply_yeah",
        ["finish_texting"],
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
    options = Option({"BLOCKED1": "[Throw the spoiled cereal in the bin]", "eat_spoiled": "[Slowly eat the spoiled cereal and wait for them to leave]"}, [1])
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
        [1,2])
    motivate = Script(
        "motivate",
        ["go_kitchen"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#put_phone_down
if True:
####NOTHING BEING CALLED HERE, END NODE
    print("END NODE")

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
        [])
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
        [])
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
            'YYou continue eating the spoiled cereal.',
            'You get halfway through the bowl.',
            'It is 10:52am.',
            'If you ran you might make it to your lecture.',
            'You feel ill.'
        ],
        True
    )
    options = Option(
        {"BLOCKED1": "[Run for your lecture]", "go_sleep_1": "[Go back to sleep]"},
        [])
    try_eat = Script(
        "try_eat",
        ["go_sleep_1"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

allScript = {"start":start}
# def main(allScript):
#     done = False
#     toRun = start.runScript()
#     while not done:
#         scriptRun = allScript.get(toRun)
#         toRun = scriptRun.runScript()
#
# main()
