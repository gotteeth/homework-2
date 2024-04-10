#Quick Decisions: The Event Planner 




attendees = int(input ("enter number of attendees: "))
venue1 = "large hall" 
venue2 = "conference room"

if attendees > 100:
    print("Welcome to the Santana Inn, your party will be in the," ,venue1 , "enjoy your night!")
else: 
    print ("Welcome to the Santana Inn, you party will be in the, " ,venue2 , "enjoy you night!" )



#task- 2 



caterers1 = ("vegetarian delight caterers") 
caterers2 = ("gourmet meals caterers")


they_want = input ("do you want vegetarian or gourmet food? ")


if they_want == ("vegetarian"):
    action = print("we recommend " , caterers1 , "!")
else : 
    print("how about " , caterers2 , "!")


