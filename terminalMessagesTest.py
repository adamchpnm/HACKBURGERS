import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore, Back, Style


def stdout(message):
    sys.stdout.write(message)
    sys.stdout.write('\b' * len(message))  # \b: non-deleting backspace


def rightPrint(message):
    stdout(message.rjust(50))
    sys.stdout.flush()
    print()


you = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.GREEN}You:{Style.RESET_ALL}")
friend = str(f"{Style.RESET_ALL}{Style.DIM}{Fore.BLUE}friend:{Style.RESET_ALL}")
left = True
messages = ["me", "to you", "to me", "i am in your walls"]
while messages:
    if left:
        cprint(you)
        message = str(f"{Style.BRIGHT}{Fore.GREEN}"+messages[0]+f"{Style.RESET_ALL}")
        print(message)
        stdout(message)
    else:
        rightPrint(friend)
        message = str(f"{Style.BRIGHT}{Fore.BLUE}"+messages[0]+f"{Style.RESET_ALL}")
        stdout(message.rjust(50))
        sys.stdout.flush()
        rightPrint(message)
    messages.pop(0)
    left = not left
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