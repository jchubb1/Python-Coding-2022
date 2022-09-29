# This is the demo file for week 04

degrees = 50 # Takes the place of the input function.

is_cold = degrees < 50 # This condition that will be evaluated.


if is_cold:
    print("Wear a coat.")
else:
    print("No need to wear a coat.")
    
    
    is_very_cold = degrees < 0


    if is_very_cold:
        # Start of block of code 2...
        print("Wear a big coat 1")
        print("Wear a big coat 2")
        # End of block of code 2...
    # End of block of code...

    # Calculate grades

    grade = 95


    if grade >= 90:
        print("Your grade is an A")

    elif grade >= 80:
        print("Your grade is an B")

    elif grade >= 70:
        print("Your grade is an C")

    elif grade >= 60:
        print("Your grade is an D")

    elif grade >= 59:
        print("Your grade is an F")

    c1 = not degrees < 50 
    condition = c1 < 50 and grade > 75 



print(" End of program")

