# This is my week 04 in-class assignment by Jamal Chubb.

# Create a Python program that prompts the user to enter an integer. 
# The program should display “Positive” if the number is greater than 0, 
# “Negative” if the number is less than 0, and “Zero” if the number is 
# equal to 0. The program should then display “Even” if the number is even, 
# and “Odd” if the number is odd.

# Do inputting here

# user_number = 6 # For testing purposes only.

user_number = int(input("Please enter a number."))

# Do processing here...
# THe code to figure positive/negative/zero
if user_number > 0:
    print("Positive")
elif user_number < 0:
    print("Negative")
elif user_number == 0:
    print("Zero")
else: 
    print("This code will never reach this point.")

# The code to figure even/odd.
remainder = user_number % 2
if remainder == 0:
    print("Even")
else:
    print("Odd")

# Do outputting here...

