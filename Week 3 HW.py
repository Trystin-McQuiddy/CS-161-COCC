#As per assignment instructions, I will have the user enter their name.
name = input("What is your name?: ")

#Then we say hi.
print('Hello ' + name + '.')

#Now we ask their age.
age = input("What is your age?: ")

#Now to add 5 years to their age.
#print(age + 5) doesn't work, as it is registering the age as a string.
#To fix that, I specify that age is an integer.
#print(int(age) + 5) will fix that issue.

#Here we print out their age in 5 years.
print('In 5 years, you will be ' + str(int(age) + 5) + ' years old.')

#Now I need to calculate hourly pay for a week, and use some floating point values.
hours = input('How many hours do you work in a week?: ')

#Now to convert to float.
hours = float(hours)

#Then we do the same process to ask their wage.
wage = input('What is your hourly wage?: ')

wage = float(wage)

#The below are just me checking to make sure they printed right.
#print(hours)
#print(wage)

#Next I need to calculate their weekly paycheck and print a message in one statement.
print('Your gross pay this week is $' + str(hours * wage) + '.')

#Then we estimate their gross annual using 52 weeks for the year.
print('Your estimated annual gross pay will be $' + str(hours * wage * 52) + '.')