#Leap Year Explorer 
            #not a fan, lol 


year = int(input("enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #still dont understand this 
    print(" year " ,  year , "is a leap year.")
else:
    print( year , " is not a leap year.") 

    #had to revisit old math 
