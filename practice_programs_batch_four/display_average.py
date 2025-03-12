# list stored input numbers
store_input_number = []

# loop to ask for input numbers
while True:
    try:
        input_number = int(input("\nEnter a number: "))
        # store input number to list
        store_input_number.append(input_number)
    # stop program if not numerical
    except ValueError:
        print("\nThe input must be numerical")
        break

# exit loop and check the average of the numbers in the list
if store_input_number:
    average = sum(store_input_number) / len(store_input_number)
    # print the result
    print(f"\nThe average of all numbers is: {average}")
# if no numbers were entered
else:
    # print none
    print("\nThere were no numbers entered")