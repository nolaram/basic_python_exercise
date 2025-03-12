# input two numbers
number_one = int(input('\nEnter your first number: '))
number_two = int(input('Enter your second number: '))

# check what is the smaller number
# if number one is the smaller number
if number_one < number_two:
    # print "The smaller number is number one"
    print(f"\nThe smaller number is: {number_one}")
# if number two is the smaller number 
elif number_two < number_one:
    # print "The smaller number is number two"
    print(f"\nThe smaller number is: {number_two}")
# if the numbers are the same
else:
    # print "The numbers are equal"
    print("\nThe two numbers are equal")