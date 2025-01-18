#This is my homework assignment for Week 2
#For the first segment of the assignment, I have to set a variable first.

x = 31

#Now I need to print the variable in decimal, binary, and hex.

print(x, bin(x), hex(x))

#For the second part of the assignment, I need to change the value of x.

#x = 1.825 turning this into a comment, as after running to get an error I need to change
# the number to 18 by the instructions.

x = 18

print(x, bin(x), hex(x))

#The error it is giving me is that the float object cannot be interpreted as an integer.
#This error is showing up because only and integer would be accepted, not floating point.

#For the third portion, I need to assign binary and hex values to a variable

y = 0b1011
z = 0xA3

print(y, z)

#The forth part wants to show us that we can add variables in any representation.

w = x + y + z

print('the sum is ' , w)

#Now we move on to the compression section of the assignment.
#I am not entirely certain I understand this portion of the assignment.
#I start off by choosing variable names that make sense.
#I then need to actually assign values to the variable.

o_size = 400
d_size = 30
ct_size = 167

poc = (1 - ((ct_size + d_size) / o_size)) * 100

#Now we print it all.

print('Compressed text size: ', str(ct_size),'characters.')
print('Dictionary size: ', str(d_size),'characters.')
print('Total: ', str(ct_size + d_size), 'characters')
print('Compression: ', str(poc), '%')

#I believe I have done the assignment properly, please tell me if I was wrong.