# list of stored input numbers
stored_input_number = []

# loop to ask for input number
while True:
    try:

        input_number = int(input("\nEnter a number: "))

        # store input number to list
        stored_input_number.append(input_number)

    # stops program if not numerical value
    except ValueError:
        print("\nThe input must be numerical")
        break

# exits loop and sorts the input numbers stored in list
if stored_input_number:
    stored_input_number.sort()
    # print the result
    print("\nThe entered numbers from lowest to highest is:")
    for input_number in stored_input_number:
        print(input_number)
# if no numbers were entered
else:
    # print none
    print("\nThere were no numbers entered")