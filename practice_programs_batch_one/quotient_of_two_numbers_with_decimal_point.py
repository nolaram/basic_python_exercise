try:
    # input two numbers
    number_one = int(input("\nEnter your first number: "))
    number_two = int(input("Enter your second number: "))

    # divide the two numbers with the decimal point on
    quotient = number_one / number_two

    # print the quotient
    print(f"\nThe quotient of the two numbers is: {quotient}")

# added so that the user cannot devide by zero
except ZeroDivisionError:
    print("\nYou cannot devide by zero!")