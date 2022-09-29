# This is some examples for week 6 on looping
# Written by Jamal Chubb

print('Beginning of program...')

# Simple 'while' loop to print something a bunch of times.
# stop = False
# while stop != True:
#     print("Executing code in loop...")
#     prompt = input('Please enter the letter "a" or "b":')
#     if prompt == "a" or prompt == "b":
#         stop = True
#     else:
#         print("I told you to enter an 'a' or 'b'.")

# num = 0
# while num < 10:
#     print(num)
#     num = num + 1


# Here is "for" loop to print some peoples names...
# for name in ["Jamal", "Joe", "James"]:
#     print(name)

#or

# names = ["Jamal", "Joe", "James"]
# for name in names:
#     print(name)

# A "for" loop with numbers
# for num in [1,2,3,4,5,6,7,8,9]:
#     print(num)

# A "for" with 'range()' loop to print the numbers 0 thru 9.
# for num in range(10):
#     print(num)

# A "for" with 'range()' loop to print the numbers 2 thru 9.
# for num in range(2,10):
#     print(num)

 # A "for" with 'range()' loop to print the "even" numbers in range 0 thru 9.
# for num in range(0,10,2):
#     print(num)


 # A "for" with 'range()' loop to print the "odd" numbers in range 0 thru 9.
# for num in range(1,10,2):
#     print(num)

# A more dynamic example using "range()" in a "for" loop
# stop = int(input("Please enter the number of numbers to print:"))
# for num in range(stop):
#     print(num+1)




# Print the first 5 letters of the alphabet 10 times.
num = 0
while num< 10:
    print()
    print(num)
    for letter in ['a','b','c','d','e']: # Print the first 5 letters...
        print(letter)
    num= num +1

print('End of program.')