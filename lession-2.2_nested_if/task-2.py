#Quick Decisions: The Event Planner 




attendees = int(input ("enter number of attendees: "))
venue = "large hall" 


if attendees > 100:
    venue = "conference room"

print("Welcome to the Santana Inn, your party will be in the," ,venue , "enjoy your stay!")




#task- 2 



caterers1 = ("vegetarian delight caterers") 
caterers2 = ("gourmet meals caterers")


they_want = input ("do you want vegetarian or gourmet food? ")


if they_want == ("vegetarian"):
    action = print("we recommend " , caterers1 , "!")
else : 
    print("how about " , caterers2 , "!")


