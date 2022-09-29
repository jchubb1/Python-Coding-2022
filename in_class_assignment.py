# Create a program that prompts the user for 3 bowling scores
# The program should then display the 3 scores and the average.
# Finally, prompt the user for the number of minutes to bowl 3 the games and
# display result in the format of hours : minutes

# Do inputting here...


score_1 = input("Please enter the first bowling score:")
score_2 = input("Please enter the second bowling score:")
score_3 = input("Please enter the third bowling score:")

score_1_int = int(score_1)
score_2_int = int(score_2)
score_3_int = int(score_3)
# Do processing here...
sum = score_1_int + score_2_int + score_3_int
avg = sum / 3



# Do outputting here...
print(" You first score was:",score_1)
print(" You second score was:",score_2)
print(" You third score was:",score_3)
print(" You average score was:%.2f" % avg)
#print('%.2f' % sugar2) # From "stackoverflow"

###############################################
#Finally prompt the user for the number number of minutes to bowl the 3 games and
# display the result in the format of hours : mins

#Inputting for time goes here...
mins= int(input('Enter minutes bowled'))


# Processing for time goes here... 
hrs_int = mins // 60
mins_int = mins % 60

# Outputting for time goes here..
print ("Your time bowled was(HH:MM):",hrs_int,":",mins_int)
print('This is the end of the program')

