#!/usr/bin/env python3

condition = True
while condition:

    #Save user's input to variable char_name and capitalizes entry
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)").capitalize()

    #Save user's input to variable char_stat and lower case's it
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)").lower()

    marvelchars= {
    "Starlord":
     {"real name": "peter quill",
     "powers": "dance moves",
     "archenemy": "Thanos"},

    "Mystique":
     {"real name": "raven darkholme",
     "powers": "shape shifter",
     "archenemy": "Professor X"},

    "Hulk":
     {"real name": "bruce banner",
     "powers": "super strength",
     "archenemy": "adrenaline"}
             }

    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}")

    check = input("Do you want to keep looking for more information? (y/n)").lower()
    if check == "y":
        condition = True
    else:
        condition = False
