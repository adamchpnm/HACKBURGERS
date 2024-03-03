import sys

import inquirer
import keyboard
questions = [
    inquirer.List(
        "size",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
]

answers = inquirer.prompt(questions)
print(answers)