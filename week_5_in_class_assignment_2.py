# This is a python program created by Jamal Chubb for our second in class
# assignment for week 5. We are supposed to Create a Python program that 
# asks whether any members of your party are vegetarian, vegan, or
#  gluten-free, to which then displays only the restaurants to which you
#  may take the group



# Do inputting here...
from traceback import print_list


question_1 = input("Is anyone in your party a vegetarian?:")
question_2 = input("Is anyone in your party a vegan?:")
question_3 = input("Is anyone in your party gluten-free?:")



# Do processing here...
if question_1 and question_2 and question_3== ('yes'):
    print("Your restaurant choices are: Corner Cafe and The Chef's Kitchen")
elif question_1 and question_3 == ('yes')and question_2 == ('no'):
    print("Your restaurant choices are: Main Street Pizza Company, Corner Cafe, and The Chef's Kitchen ")
elif question_1== ('yes') and question_2 and question_3 == ('no') and question_3 == ('no'):
    print("Your restaurant choices are: Mama's Fine Italian, Corner Cafe, and The Chef's Kitchen")
elif question_1 and question_2 and question_3 == ("no"):
    print(" Your restaurant choices are: Joe's Gourmet Burgers, Main Street Pizza Company, Corner Café, Mama's Fine Italian, and The Chef's Kitchen  ")



# Do outputting here...
