class Script:

    #Each event has a dictionary of scripts, which are different ways that the event can go
    def __init__(self, nrgCrit = 0, batCrit = 0, failMessage=None):

        # battery and energy are the only criteria which matter
        self.nrgCrit = nrgCrit
        # self.monCrit = monCrit
        self.batCrit = batCrit

    def criteria(self, nrg = 0, bat = 0):
        if self.nrgCrit <= nrg and self.batCrit <= bat:
            return True
        else:
            return False

class Event:

    #Event takes in a dictionary of scripts which are the ways that a specific event can go
    def __init__(self, scripts: dict[int:Script]):
        self.scripts = scripts



class StateMachine:
    playerStats = {"energy": 30, "battery": 30, "money": 0}

    start = Event(0, 0)
    middle = Event(0, 0)
    end = Event(0, 0)

    events = {0: start, 1: middle, 2: end}
    # transition function is more of a filter
    currentState = events[0]

    def setEvent(self, state: int):
        self.currentState = state

    def transition_to(self, currentEvent: int, nextEvent: int, playerStats):
        if currentEvent.criteria(playerStats["energy"], playerStats["battery"]):
            self.setEvent(nextEvent)
    #not sure what to do here yet reworking earlier parts
