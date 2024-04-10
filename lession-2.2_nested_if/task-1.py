# task 1 code correct

 
#Nested Decisions: The Adventure Game


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


    #task 2 setting the scene 


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
if place == "cave":
    action = input(" would you like to light a torch or proceed in the dark?")
    if action == ("light a torch"):
        print ("you found hidden treasure!")
else:
    print ("you found a hidden oasis!")
    pass 