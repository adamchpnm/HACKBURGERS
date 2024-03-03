#be_honest
if True:
    narration = Narrate(
        [
            "You tell Jordan you have a workshop soon.",
            "They smile but you can't help but feel you've made a mistake."
            "You apologise and decide to go to your workshop."
        ],
        True
    )
    options = Option(
        {"go_workshop": "[Go to your workshop]"}, []
    )
    be_honest = Script(
        "be_honest",
        ["go_workshop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#go_workshop
if True:
    narration = Narrate(
        ["You leave Jordan and decide to go to your workshop.",
         "Your workshop is a group project.",
         "You're terrified of getting the wrong answer.",
         "Your chest seizes, you can't go."],
        True
    )
    options = Option(
        {"home_no_shop": "[Go home]"}, []
    )
    go_workshop = Script(
        "go_workshop",
        ["home_no_shop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#go_lect_ontime
if True:
    narration = Narrate(
        ["The walk to university is short, and you get to the entrance of your lecture hall just as class is about to start.",
         "You notice Jordan is sitting in an empty row near the front of the lecture theatre.",
         "They haven't noticed you come in.",
         "You think if you try to sit with them you might still be standing when the lecturer starts talking."],
        True
    )
    options = Option(
        {"BLOCKED1" : "[Go and sit with Jordan]", "BLOCKED2": "[Sit with others]", "sit_alone": "[Sit alone at the back of the theatre]"}, ["BLOCKED1", "BLOCKED2"]
    )
    go_lect_ontime = Script(
        "go-lect-ontime",
        ["sit_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#go_lect_early
if True:
    narration = Narrate(
        ["You leave your flat, managing not to run into any of your flatmates on your way out.",
         "The walk to university is short, and you get to the entrance of your lecture hall with a handful of minutes to spare.",
         "You notice Jordan is sitting in an empty row near the front of the lecture theatre.",
         "He hasn't noticed you come in."],
        True
    )
    options = Option(
        {"sit_jordan": "[Go and sit with Jordan]", "BLOCKED1": "[Sit with others]", "sit_alone": "[Sit alone at the back of the theatre]"},
        ["BLOCKED1"]
    )
    go_lect_early = Script(
        "go_lect_early",
        ["sit_jordan", "sit_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#leave_before_jordan
if True:
    narration = Narrate(
        ["You exit the lecture hall shortly after the lecturer dismisses you.",
         "You leave the building and go somewhere you know Jordan will not see you."], True
    )
    options = Option(
        {"go_workshop": "[Go to your workshop"}, []
    )
    leave_before_jordan = Script(
        "leave_before_jordan",
        ["go_workshop"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#leave_with_jordan
if True:
    narration = Narrate(
        ["You wait at the back of the room for Jordan to notice you.",
         "When they do, they come over and ask you why you didn't come down to sit with them",
         "You can't bring yourself to tell them.",
         "You feel like you've let Jordan down."], True
    )
    options = Option(
        {"talk_jordan": "[Talk to Jordan]"}, []
    )
    leave_with_jordan = Script(
        "leave_with_jordan",
        ["talk_honest"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#sit_alone
if True:
    narration = Narrate(
        ["You decide to sit alone to watch the lecture.",
         "You can see Jordan at the front of the theatre."], True
    )
    options = Option(
        {"watch_alone": "[Watch the lecture alone]"}, []
    )
    sit_alone = Script(
        "sit_alone",
        ["watch_alone"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#sit_jordan
if True:
    narration = Narrate(
        ["You sit down next to Jordan.",
         "They give you a warm smile and greet you as they clear "],
        True
    )
    options = Option(
        {"watch_jordan": "[Sit and watch the lecture with Jordan]"}, []
    )
    sit_jordan = Script(
        "sit_jordan",
        ["watch_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#talk_jordan
if True:
    narration = Narrate(
        ["Jordan begins talking about how boring your lecturer is.",
         "You agree passively with what they say unless they seem to want your input.",
         "They seem like they're ready to go to lunch.",
         "It is 12:02pm, your workshop will be starting soon."], True
    )
    options = Option(
        {"be_honest": "[Be honest with Jordan about the workshop","go_to_lunch" : "[Go to lunch]"}, []
    )
    talk_jordan = Script(
        "talk_jordan",
        ["be_honest", "go_to_lunch"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#watch_alone
if True:
    narration = Narrate(
        ["The lecture passes slowly.",
         "You find the material dry and uninteresting.",
         "You finish taking notes slightly before the lecture ends, and pack your things away in your bag.",
         "You feel tired."], True
    )
    options = Option(
        {"leave_before_jordan": "[Leave before Jordan sees you]", "leave_with_jordan": "[Wait to leave with Jordan]"}, []
    )
    watch_alone = Script(
        "watch_alone",
        ["leave_before_jordan", "leave_with_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

#watch_with_jordan
if True:
    narration = Narrate(
        ["The lecture passes slowly.",
         "You find the material dry and uninteresting.",
         "Jordan seems not to be paying much attention.",
         "They keep showing you posts on their phone."], True
    )
    options = Option(
        {"talk_jordan": "[Talk to Jordan]"}, []
    )
    watch_with_jordan = Script(
        "watch_with_jordan",
        ["talk_jordan"],
        [narration.narrate, options.listOpt],
        [None, None]
    )

# be_honest
# sit_jordan
# go_workshop
# go_lect_ontime
# go_lect_early
# leave_before_jordan
# sit_alone
# talk_jordan
# leave_with_jordan
# watch_alone
# watch_with_jordan