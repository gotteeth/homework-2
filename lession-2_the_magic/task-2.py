#The Greatest Showdown 

#task 1 

#tough, need more practice 
            #but fairly comfortable 

number1 = int(input("enter you first number: " ))
number2 = int(input("enter your second number: "))
number3 = int(input("enter you third number here: "))

largest_number = smallest = number1 

if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3 

    print("the largest number is:" , largest_number )
    print ("this is the lowest number " , smallest)
    print ("the largest number is" , + largest_number , "and the smallest is" , + smallest)