import sys

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

cprint(figlet_format('START', font='starwars'),
       'yellow', attrs=['bold'])

current = "1"
roomTextTest = {"1": "test1", "2": "tests2", "3": "test3", "q": "quit"}
end = False
while not end:
    currentText = "Current room: "+current
    cprint(figlet_format(currentText, font='digital'), 'white', attrs=['bold'])
    choice = str(input("Choose 1,2,3,q: "))
    if choice == current:
        print("Already there")
    if not choice:
        print("No input")
    elif choice == "q":
        end = True
    else:
        text = roomTextTest.get(choice)
        cprint(figlet_format(choice, font='digital'), 'white', attrs=['bold'])
        current = choice

cprint(figlet_format('END', font='starwars'),'yellow', attrs=['bold'])