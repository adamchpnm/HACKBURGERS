import sys
from colorama import Fore, Back, Style

global WINDOW_WIDTH

WINDOW_WIDTH = 75


def conversation(messages, contact, time, battery):
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))
    statusBar(time, battery)
    print(str(('─' * WINDOW_WIDTH) + f"{Style.RESET_ALL}"))
    print(Style.RESET_ALL)
    you = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.GREEN}You:")
    friend = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.BLUE}{contact}:")
    left = True
    while messages:
        if left:
            print(you)
            message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}" + messages[0])
            print(message)
            # stdout(message)
        else:
            rightPrint(friend)
            message = str(f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + messages[0])
            rightPrint(message)
        messages.pop(0)
        left = not left

    print(f"{Style.RESET_ALL}")


def stdout(message):
    sys.stdout.write(message)
    sys.stdout.write('\b' * len(message))  # \b: non-deleting backspace


def rightPrint(message):
    stdout(message.rjust(WINDOW_WIDTH))
    sys.stdout.flush()
    print()


def statusBar(time, battery):
    if battery < 10:
        batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}{battery}%"
    elif battery < 20:
        batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}{battery}%"
    else:
        batteryText = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{battery}%"
    stdout(batteryText.rjust(WINDOW_WIDTH))
    print(f"{Style.RESET_ALL}{Style.BRIGHT}{time}")
    sys.stdout.flush()


messages = ["message1", "message2", "message3", "message4", "message5", "message2", "message3", "message4", "message5", "message2", "message3", "message4", "message5"]
contact = "Jordan"
time = "18:49"
battery = 21
conversation(messages, contact, time, battery)
# Print colored text
#
# print(f"{Fore.RED}This is red")
# print(f"{Back.GREEN}This has a green background")
# print(f"{Fore.YELLOW}{Back.BLUE}This has yellow foreground and blue background")
#
# # Reset colors
# print(f"{Style.RESET_ALL}This is the default text color")
#
# # Style text
# print(f"{Style.BRIGHT}This is bright text")
# print(f"{Style.DIM}This is dim text")
# print(f"{Style.NORMAL}This is normal text")
# print(f"{Style.RESET_ALL}This is the default text style")
#
# # Combine colors and styles
# print(f"{Fore.CYAN}{Back.MAGENTA}{Style.BRIGHT}This text has a cyan foreground, magenta background, and is bright")
#
