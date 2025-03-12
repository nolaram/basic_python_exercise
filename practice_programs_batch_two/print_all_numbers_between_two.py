# input two numbers
number_one = int(input("\nEnter your first number: "))
number_two = int(input("Enter your second number: "))

# if number two is bigger, flip the input
if number_one > number_two:
    number_one, number_two = number_two, number_one

# print the numbers
for number in range (number_one + 1, number_two):
    print(number)