# list of stored input numbers
store_input_number = []

# loop to ask input numbers
while True:
    try:

        input_number = int(input("\nEnter a number: "))

        # store input numbers
        store_input_number.append(input_number)

    # stop the program if not numerical
    except ValueError:
        print("\nThe input must be numerical")
        break

# exit loop and sort the list to highest to lowest
if store_input_number:
    store_input_number.sort(reverse=True)
    # print the result
    print("\nThe entered numbers from highest to lowest is:")
    for input_number in store_input_number:
        print(input_number)
# if no numbers were entered
else:
    # print none
    print("\nNo numbers were added")