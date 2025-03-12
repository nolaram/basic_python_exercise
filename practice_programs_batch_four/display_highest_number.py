# list of input numbers
store_input_numbers = []

# loop to ask input
while True:
    try:
        input_number = int(input("Enter a number: "))
        # store input number
        store_input_numbers.append(input_number)

    # stop program if input is not numerical
    except ValueError:
        print("The input must be numerical")
        break

# exit loop and find the highest number in list
if store_input_numbers:
    # print the result
    print("The highest number recorded was:", max(store_input_numbers))   
# if no numbers were entered
    # print none