# list stored input numbers
store_input_number = []

# loop to ask for input numbers
while True:
    try:
        input_number = int(input("Enter a number: "))
        # store input number to list
        store_input_number.append(input_number)
    # stop program if not numerical
    except ValueError:
        print("The input must be numerical")
        break

# exit loop and check the average of the numbers in the list
    # print the result
# if no numbers were entered
    # print none