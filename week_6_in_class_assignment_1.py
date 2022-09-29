# This is a program for my week 6 in class assignment written by Jamal Chubb Write a program that asks the user
#  for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should then use a loop
#  to display the distance the vehicle has traveled for each hour of that time period.


# As an example, for the following input:
# What is the speed of the vehicle in mph? 40
# How many hours has it traveled? 3 


# Here is an example of the desired output:
# Hour: 1, distance traveled:  40
# Hour: 2, distance traveled:  80
# Hour: 3, distance traveled:  120
# Do inputting here...

mph = int(input(" What is the speed of the vehicle in mph?:"))
hrs = int(input("How many hours has it traveled?:"))

# Do processing here...
for hr in range(1,hrs+1,1):
    # print(hr)
    distance = mph * hr
    # print(distance)
    print("hr:", hr, "distance traveled:",  distance)

# Now with a "while" loop...
# hr = 1
# while hr <hrs +1:
#     distance = mph * hr
#     print("hr:", hr, "distance traveled:",  distance)
#     hr = hr +1




print("End of program")

# Do outputting here...