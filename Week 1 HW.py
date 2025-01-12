#Have to set up variables for part one of the assignment.
pet_type = (input(f"What type of pet do you have? "))
pet_name = (input(f"What is your pet's name? "))

#Now to execute the first part of the assignment.
print(f"I have a {pet_type} and their name is {pet_name}.")

#Now to set up more variables for part two of the assignment.
fname = (input(f"What is your first name? "))
currentage = int(input(f"What is your current age in years? "))
savings = int(input(f"How much do you save in a year? "))

#Now to execute the second part of the assignment.
print(f"Hello {fname}! You are currently {currentage} years old.")
print(f"In 10 years, you will be {currentage+10} years old.")
print(f"If you save ${savings} each year, in 5 years you will have saved ${savings*5}")
print(f"Your average monthly savings is ${savings/12}")

#Now on to the third part of the assigment. I'll set a value for seconds in January.
jansec = int(60*60*24*31)

#Now to print it in f-string
print(f"There are {jansec} seconds in the month of January.")

#Finally, on to the last part of the assignment. Starting with an input variable.
egginput = int(input(f"Please select a number of eggs. "))

#We'll have the math here.
eggdozens = int(egginput // 12 )
eggleftover = int(egginput % 12)

#Now we print.

print(f"This makes {eggdozens} dozen eggs with {eggleftover} leftover eggs.")