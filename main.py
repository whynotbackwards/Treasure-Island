from assets import chest

print(chest)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nYou are a battle-weary warrior who has been in search of the greatest treasure in all the land.")
print("After months of searching, scouring, and battling, you have come to the last stage in your ancient treasure "
      "map.")
print("You must press on. For you are Sir Patrick Stewart, and the treasure is your destiny.\n")

print("You come to a fork in the road.")
print("The path to the left heads toward a lake and you see some beasts feeding on fish at the water's edge.")
print("The path to the right leads to a field of daisies. Although it is quiet... Too quiet.\n")

choice_1 = input("Which way will you go? Type 'left' or 'right': ").lower().strip()

while choice_1 not in ("left", "right"):
    choice_1 = input("\nNot an option, but I like your creativity. Type 'left' or 'right': ").lower().strip()

if choice_1 == "right":
    print("\nHidden within the daisies is a small yet deep, cavernous hole. You fall in.\n\nGAME OVER.")
else:
    print(
        "\nYou head towards the water, uneasy about the beasts. You hold your sword with a tense readiness for "
        "anything.")
    print("It turns out the beasts are pescatarians and let you go on your way.")
    print(
        "You stare at the water wondering your next move. There is an island in the middle of the lake that you could "
        "swim to.")
    print("It also appears there is an empty boat on the water that could drift towards you eventually.")

    choice_2 = input("\nDo you swim or wait for the boat? Type 'swim' to swim across to the island, or 'wait' to wait "
                     "for the boat to drift to you: ").lower().strip()

    while choice_2 not in ("swim", "wait"):
        choice_2 = input("\nNo can do. Fate has given you only two options. Type 'swim' or 'wait': ").lower().strip()

    if choice_2 == "swim":
        print("\nUnfortunately the lake is filled with mutant trout who are not pescatarians. They think you taste "
              "yummy.\n\nGAME OVER.")
    else:
        print("\nAfter hanging out with the beasts for a bit discussing sushi recipes, the boat finally drifts to the "
              "shore.")
        print("You get in and paddle yourself to the island. You hear faint triumphant music as you approach, but you "
              "ignore it.")
        print("There is a single house on the island with three doors - one red, one yellow, and one blue.")
        print("You think about it for a bit, choose a door, grab the knob, and enter.")

        choice_3 = input("\nWhich door hast thou chosen for thine treasure? Type the color of your "
                         "choice: ").lower().strip()

        if choice_3 == "red":
            print("\nYou have entered a room full of fire. Not sure why you couldn't tell it was on fire before "
                  "entering, but that's not important now.\n\nGAME OVER.")
        elif choice_3 == "blue":
            print("\nA nasty dragon has been lying in wait in this room. Not sure how he got in there, but he sure is "
                  "hungry.\n\nGAME OVER.")
        elif choice_3 == "yellow":
            print("\nIn the center of the room is the greatest treasure in the world: a signed replica of Luke "
                  "Skywalker's lightsaber.")
            print("You take it and leave in peace.")
            print("\nAlthough... you're curious what's behind the other two doors...")
            print("But you decide you've spent enough time on this and go home instead.")
            print("\nYOU WIN!")
        else:
            print("\nYou chose a door that doesn't exist. A hole has opened up in the spacetime continuum and eaten "
                  "everything in existence.\nWell, except for the next two words.\n\nGAME OVER.")
