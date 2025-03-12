# list of stored input numbers
stored_input_number = []

# loop to ask for input number
while True:
    try:

        input_number = int(input("Enter a number: "))

        # store input number to list
        stored_input_number.append(input_number)

    # stops program if not numerical value
    except ValueError:
        print("The input must be numerical")
        break
    
# exits loop and sorts the input numbers stored in list
    # print the result
# if no numbers were entered
    # print none