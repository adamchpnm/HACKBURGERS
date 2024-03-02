class Script:

    # Each event has a dictionary of scripts, which are different ways that the event can go

    # Script can transition to another script (through Event.scriptTransition)
    # or to another event (through StateMachine.eventTransition)
    def __init__(self, script_id, energy_criterion=0, battery_criterion=0):

        # battery and energy are the only criteria which matter
        self.script_id = script_id
        self.energy_criterion = energy_criterion
        self.battery_criterion = battery_criterion

    def criteria(self, energy=0, battery=0):
        if self.energy_criterion <= energy and self.battery_criterion <= battery:
            return True
        else:
            return False


class Event:

    # Event takes in a dictionary of scripts which are the ways that a specific event can go
    # It will facilitate transitions between scripts and also transition into an initial script depending
    # on if the players stats
    # if the player is statful enough to do everything, they get a choice
    # the script object will handle all transitions to other scripts, but event starts with a starter script which will
    # set in motion a series of scripts

    def __init__(self, scripts: dict[Script: dict[int: Script]], player_stats):
        self.scripts = scripts
        self.player_states = player_stats

    #you apply check scripts to check if a script can be moved to
    def checkScripts(self, player_stats, scripts: dict[Script: dict[int: Script]]):
        unavailable_scripts = []
        for script in range(len(scripts)):
            if scripts[script].criteria(player_stats["energy"], player_stats["battery"]):
                unavailable_scripts.append(script)
        return unavailable_scripts

    # this function is basically just a nice way to display this
    def transitionToScript(self, next_script: int):
        return next_script

    # this is what we give to block out the choices you CANT TAKE
    def giveChoices(self, player_stats, scripts: dict[Script: dict[int : Script]]):
        unavailable_scripts = self.checkScripts(player_stats, scripts)


class StateMachine:
    player_stats = {"energy": 30, "battery": 30, "money": 0}
    test_script1 = Script(1)
    test_script2 = Script(2)
    test_script3 = Script(3)

    # scripts will be stored in a triple nested dictionary!!!! basically the intuition is:
    # each integer index will relate to one script in our entire program, which is the only key of the inner dictionary
    # the inner dictionary contains one value: the dictionary mapped to the script
    scripts = {test_script1: {1: test_script2, 2: test_script3}, test_script2: {1: test_script2, 2:test_script3}}

    start = Event(scripts, player_stats)
    middle = Event(scripts, player_stats)
    end = Event(scripts, player_stats)

    events = {1: start, 2: middle, 3: end}
    # transition function is more of a filter
    current_state = events[1]

    def setEvent(self, state: int):
        self.current_state = state

    def transitionToEvent(self, current_event: int, next_event: int, player_stats):
        if current_event.criteria(player_stats["energy"], player_stats["battery"]):
            self.setEvent(next_event)
    # not sure what to do here yet reworking earlier parts
