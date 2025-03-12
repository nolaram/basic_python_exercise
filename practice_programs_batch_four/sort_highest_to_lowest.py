# list of stored input numbers
store_input_number = []

# loop to ask input numbers
while True:
    try:

        input_number = int(input("Enter a number: "))

        # store input numbers
        store_input_number.append(input_number)

    # stop the program if not numerical
    except ValueError:
        print("The input must be numerical")
        break

# exit loop and sort the list to highest to lowest
    # print the result
# if no numbers were entered
    # print none