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
    accept_drink = Script(
        "find_jordan_in_queue",
        ["tell_jordan_leaving", "enter_club"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# prep_for_bed


# prep_for_bed_number


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
        {"sleep_for_night_invited": "[Go to sleep for the night]"},
        [])
    leave_club = Script(
        "leave_club",
        ["sleep_for_night_invited"],
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
    leave_club_early = Script(
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
        {"sleep_for_night_invited": "[Go to sleep for the night]"},
        [])
    ignore_jordan_message = Script(
        "ignore_jordan_message",
        ["sleep_for_night_invited"],
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

# go_to_club


# look_for_jordan

# push_through

# respond

# smile_and_nod

# tell_jordan_leaving

# try_conversation

# turn_around_and_leave

# wait_for_jordan_club