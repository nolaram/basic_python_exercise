# input two numbers
number_one = int(input('\nEnter your first number: '))
number_two = int(input('Enter your second number: '))

# check what is the bigger number
# if number one is bigger
if number_one > number_two:
    # print "The bigger number is number one"
    print(f"\nThe bigger number is: {number_one}")
# if number two is bigger
elif number_two > number_one:
    # print "The bigger number is number two"
    print(f"\nThe bigger number is: {number_two}")
# if the two numbers are the same
    # print "The two numbers are equal"