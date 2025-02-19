#This is my week 5 homework assignment for CS161.

#I am going to need a couple imports for later in the assignment, so I will place them
#here.

import requests
import psutil


#Part one of the assignment wants me to use an if statement to check for if a user
#given number is divisible by 5.

input_number = int(input('Please select a number: '))

def div_by_five():
    """This function is used to check and see if a number given by the user is divisible
    by 5 or not."""
    if input_number % 5 == 0:
        print(input_number, 'is divisible by 5')
    else:
        print(input_number, 'is not divisible by 5')

div_by_five()

#The next part of the assignment wants us to use if and elifs to print the name
#of a few state capitals when given the name of the state.

def state_capital():
    """This function will take the input of a user to get the name of a state and,
    assuming the chosen state is one that has been included, return the capital of
    that state."""
    pick_state = (input('Please select a state: '))
    lowercase_input = pick_state.lower()
    if lowercase_input == 'utah':
        print('The capital of Utah is Salt Lake City')
    elif lowercase_input == 'oregon':
        print('The capital of Oregon is Salem')
    elif lowercase_input == 'colorado':
        print('The capital of Colorado is Denver')
    elif lowercase_input == 'massachusetts':
        print('The capital of Massachusetts is Boston')
    elif lowercase_input == 'texas':
        print('The capital of Texas is Austin')
    elif lowercase_input == 'new york':
        print('The capital of New York is Albany')
    else:
        print('I do not know that one, sorry!')

state_capital()

#Now I need to do the same thing but using dictionaries instead.
#Setting up the dictionary comes first.

states_dic = {"Utah": "Salt Lake City",
         "Oregon": "Salem",
         "Colorado": "Denver",
         "Massachusetts": "Boston",
         "Texas": "Austin",
         "New York": "Albany"}

#Now to print off the things I listed within the dictionary I made.

for state, capital in states_dic.items():
    print(f"The capital of {state} is {capital}!")

#Next it wants me to use "match case" to do the same thing.

input_state = input('Once again, please select a state: ')

lower_input_state = input_state.lower()

match lower_input_state:
    case 'utah':
        print('The capital of Utah is Salt Lake City')
    case 'oregon':
        print('The capital of Oregon is Salem')
    case 'colorado':
        print('The capital of Colorado is Denver')
    case 'massachusetts':
        print('The capital of Massachusetts is Boston')
    case 'texas':
        print('The capital of Texas is Austin')
    case 'new york':
        print('The capital of New York is Albany')
    case _:
        print('I do not know that one, sorry!')

#I think I got this right, but if it's not what was intended for the assignment
#then please do let me know, so I can fix it.

#The next portion of the assignment wants me to use elif in a function definition
#given some information from the instructions page, so I'll do that here.

def pool_admission(age):
    """This function will take the age of a person and return the price of admission
    for that person based on the age given.

    Parameter:
    age: input an integer.

    Returns:
    Price in dollars, should be an integer."""
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    elif age >59:
        return 4


#The next part of the assignment wants me to determine how many times the string "160"
#is in the HTML code for coccbobcat.com.
url = "http://coccbobcat.com"

r = requests.get(url)

#print(r.text) I was doing some troubleshooting here.

try:
    substring = "160"
    amount = r.text.count(substring)
    print(f'The substring "{substring}" is present inside of the HTML code of {url} {amount} times!')
except:
    print("Something went wrong, try again!")

#Finally, I need to determine the number of processes running on my system.

print("The number of processes running on my system right now is ", len(psutil.pids()))