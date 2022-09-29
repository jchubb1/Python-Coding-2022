# This is a program for the week 5 in class assignment. We are expected to 
# develop a Python program that prompts the user to enter the number of baseballs
# purchased. In addition the program should ask the user if they want giftwrapping
#  and if so add another $2.00 to the order. The program should then display the 
# amount of the discount (if any) and the total amount of the purchase after the 
# discount and including the giftwrapping if needed.

# Do inputting here...
quantity_baseballs = int(input("Enter amount of baseballs for purchase."))
baseballs= 1.99 
gross_total_cost= baseballs * quantity_baseballs
discount_1 = gross_total_cost * .05
discount_2= gross_total_cost * .1
gross_total_cost_1 = gross_total_cost - discount_1
gross_total_cost_2 = gross_total_cost - discount_2
question = input("Would you like to add a gift set with your purchase?")
yes = 2.00
no = 0.00

# Do processing and outputting here...
if 0< quantity_baseballs<10:
    print ("There is no discount offered when purchasing under 10 balls.")
    print("Your total is", gross_total_cost)



if 10< quantity_baseballs< 50:
    print( "You have saved", discount_1)
    print("Your total is ", gross_total_cost - discount_1)



if quantity_baseballs> 51:
    print("With the 10 percent discount, you have saved", discount_2)
    print("Your total is", gross_total_cost - discount_2)


if question== ("yes") and 0< quantity_baseballs< 10:
    print(" Perfect! your adjusted total is", gross_total_cost + yes )
elif question== ("yes") and 10< quantity_baseballs<= 50:
    print("Perfect! your adjusted total is", gross_total_cost_1 + yes)
elif question== ("yes") and quantity_baseballs>51:
    print("Perfect! your adjusted total cost is", gross_total_cost_2 + yes)
else:
    if question==('no') and 0< quantity_baseballs< 10:
        print(" No worries, your total will remain", gross_total_cost)
    elif question== ('no') and  10< quantity_baseballs<= 50:
        print ("No worries, your total will remain", gross_total_cost_1)
    elif question== ('no') and quantity_baseballs>51:
        print ("No worries, your total will remain", gross_total_cost_2)






