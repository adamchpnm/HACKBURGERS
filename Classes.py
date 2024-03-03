class Script:

    # Each event has a dictionary of scripts, which are different ways that the event can go

    # Script can transition to another script (through Event.scriptTransition)
    # or to another event (through StateMachine.eventTransition)
    def __init__(self, script_id, energy_criterion=0, battery_criterion=0):

        # battery and energy are the only criteria which matter
        self.script_id = script_id
        self.energy_criterion = energy_criterion
        self.battery_criterion = battery_criterion
        # self.possible = []

    def criteria(self, energy=0, battery=0):
        if self.energy_criterion <= energy and self.battery_criterion <= battery:
            return True
        else:
            return False

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
    test_script1 = Script(1)
    test_script2 = Script(2)
    test_script3 = Script(3)

    # scripts will be stored in a double nested dictionary!!!! basically the intuition is:
    # each script
    # the inner dictionary contains one value: the dictionary mapped to the script
    scripts = {test_script1: {1: test_script2, 2: test_script3}, test_script2: {1: test_script2, 2: test_script3}}


