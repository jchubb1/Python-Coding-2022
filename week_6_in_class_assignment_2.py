# This is a program for my week 6 in class assignment written by Jamal Chubb Write a program with a loop that repeatedly
# asks the user to enter a word. The user should enter nothing (press Enter without typing anything) to signal the end
#  of the loop. Once the loop ends, the program should display the average length of the words entered, rounded to the
#  nearest whole number.


# Do inputting here...



# Do processing here...
from termios import TIOCPKT_FLUSHREAD


total_word_lengths = 0 
total_num_words = 0 

word = ' ' # (literally anything but '')
while word != '':
    word = input("Please enter a word:")
    if word == '':
        break
    
    total_word_lengths += len(word)
    total_num_words += 1
    

avg = total_word_lengths / total_num_words


    
    #Done.



# Do outputting here...

print("The average length of the words entered is:", int(avg))

print("End of program")