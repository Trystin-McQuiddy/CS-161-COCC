#This is the Week 4 Homework assignment, working with functions and docstrings.

#First up is a function to return the average of 3 numbers.

def average(num1, num2, num3):
    """This is a simple function to take the average of three given numbers.

    num1, num2, and num3 should all be input as numbers."""

    return (num1 + num2 + num3) / 3

print(average(7, 5, 9))
print(average(6, 6, 7))

#Part 2 asked us to move the definition after the print statements.
#This won't work, as the print statements don't see the instructions after them.

#For part 3, we are asked to print a value of a parameter outside a function definition.
#print (num1)
#This doesn't work because, until we define it like in the print above, it is undefined.

#For part 4, we convert a dog's age to human years in another function.

def dog_human_age(dog_age):
    """This is a function to make a dogs age convert to human years.

    dog_age should be entered as a number"""

    human_years = 24 + (int(dog_age) - 2) * 4
    print(str(dog_age) + ' dog years is equal to ' + str(human_years) + ' human years.')

dog_human_age(5)
dog_human_age(11)
dog_human_age(7)

#Part 5 wants us to define a function that will calculate the value of a car.

def car_value():
    """This function is going to calculate the value of a user's car."""

    car_type = (input('Is your car german, japanese, or italian? '))
    car_buy_price = (input('How much did your car cost? '))
    car_age = (input('How many years have you had your car? '))
    if car_type == 'german':
        print('The value of your car is $' + str(int(car_buy_price) - (int(car_buy_price) * (.05 * int(car_age))) ) + '.')
    elif car_type == 'japanese':
        print('The value of your car is $' + str(int(car_buy_price) - (int(car_buy_price) * (.07 * int(car_age))) ) + '.')
    elif car_type == 'italian':
        print('The value of your car is $' + str(int(car_buy_price) + (int(car_buy_price) * (.05 * int(car_age))) ) + '.')

car_value()

#I believe I did what you asked of us for part 5, please correct me if I am wrong.

#Part 6 wants us to do something similar to part 4, though it looks like with inputs.

def dog_human_input():
    """This function is going to take inputs to do the same dog year calculation
    from earlier, though this time with some user inputs, and print results."""

    print('We are going to look at how old your dog is in people years!')
    dog_name = input('What is the name of your dog? ')
    dog_input_age = input('How old is your dog? ')
    print('Your ' + dog_name + ' is ' + str(24 + (int(dog_input_age) - 2) * 4) + ' people years old!')

dog_human_input()

#I believe I have done the assignment right. Please let me know if I have not.