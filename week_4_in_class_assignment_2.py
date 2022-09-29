# This is a program for my week 4 in class assignment #2. 
# Create a Python program that asks the user for a month as a number
#  between 1 and 12. The program should display a message indicating
#  whether the month is in the first quarter, the second quarter, 
# the third quarter, or the fourth quarter of the year


# Do inputting here...
# month = 1 # For testing purposes only
month = int(input("Please enter a number between 1-12."))

# Do processing here...
if month == 1 or month == 2 or month == 3:
    print ("First Quarter")
elif 4 <= month <= 6:
    print ("Second Quarter")
elif 7 <= month <= 9:
    print ("Third Quarter")
elif 10 <= month <= 12:
    print ("Fourth Quarter")
else:
    print("Invalid month")
# Do outputting here...