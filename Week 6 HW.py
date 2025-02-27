#This is my week 6 homework assignment for CS161.

#the first part of the assignment wants me to use a while loop to count down from a
#user input integer and print a blastoff.

input_int = int(input('Please enter a number greater than 0: '))

#print(input_int) Here I was making sure it printed right, as I don't force integers much

while input_int > 0:
    print(input_int)
    input_int = input_int - 1
print('Blastoff!')

#Now I need to modify that previous loop so it includes if a number is even or odd.

input_int = int(input('Please enter a number greater than 0 once again: '))

while input_int > 0:
    if input_int % 2 == 0:
        print(f"{input_int} is an even number.")
    elif input_int % 2 != 0:
        print(f"{input_int} is an odd number.")
    input_int = input_int - 1
print('Blastoff!')

#Now to once again alter the loop to have it count down by an input number.

input_int = int(input('Please yet again enter a number greater than 0: '))
input_decrease = int(input('Please enter a number to count down by: '))

while input_int > 0:
    if input_int % 2 == 0:
        print(f"{input_int} is an even number.")
    elif input_int % 2 != 0:
        print(f"{input_int} is an odd number.")
    input_int = input_int - input_decrease
print('Blastoff!')

#Now to create a loop to print words until the word has a length of <5 letters.

user_word = "default"

while len(user_word) > 4:
    user_word = input("Please enter a word: ")
    if len(user_word) > 4:
        print(f"{user_word} has {len(user_word)} letters!")
    elif len(user_word) < 5:
        print(f"You did it!")
        break

#This time I'll use the same loop as last step, but have it terminate if the user exceeds
#an allotment of attempts.

user_word = "default"
tries_left = 5

while len(user_word) > 4:
    user_word = input("Please enter a word again: ")
    if tries_left == 0:
        print('loser')
        break
    elif len(user_word) > 4:
        print(f"{user_word} has {len(user_word)} letters!")
    elif len(user_word) < 5:
        print(f"You did it!")
        break
    tries_left = tries_left - 1

#This time I need to write a while loop that counts form 0 to 100 and prints in decimal,
#binary, and hex.

count_number = int(10)

while count_number <= 100:
    print(count_number , bin(count_number) , hex(count_number))
    count_number = count_number + 1

#Now I need to write two functions that print a number of *s equal to the input parameter
#and decrement that by one * until none remain. Once using iteration and once using
#recursion.

#First I'll use iteration.

stars_input = int(input("Please enter another number greater than 0: "))

while stars_input > 0:
    stars_string = ""
    stars_adjust = stars_input
    while stars_adjust > 0:
        stars_string = f"{stars_string}" + "*"
        stars_adjust = stars_adjust - 1
    print(stars_string)
    stars_input = stars_input - 1

#Now I need to do the same thing but using recursion.


def stars(num):
    """This function is meant to take a user's input and print out a number of *s
    based on the integer that was given by the user.

    text = the string that will be output at the end. Should be left as empty quotations
    num = an integer greater than 0 that the user will input"""

    if num == 0:
        return
    else:
        print("*" * num)
        num = num - 1
        stars(num)


num = int(input("Please select one last number greater than 0: "))
stars(num)