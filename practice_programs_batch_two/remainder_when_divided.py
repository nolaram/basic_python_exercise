try:
    # input two numbers
    number_one = int(input("\nEnter your first number: "))
    number_two = int(input("Enter your second number: "))

    # divide the two numbers
    remainder = number_one % number_two

    # print the remainder
    print(f"\nThe remainder of the two numbers is: {remainder}")

# added so that the user cannot devide by zero
except ZeroDivisionError:
     print("\nYou cannot devide by zero!")