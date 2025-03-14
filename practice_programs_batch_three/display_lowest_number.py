# list of stored input numbers
stored_input_number = []

# loop to ask for input number
while True:
    try:
        
        input_number = int(input("\nEnter a number: "))

        # store input number
        stored_input_number.append(input_number)

    # stop program if the input is not numerical
    except:
        print("\nThe input must be numerical")
        break

# exit the loop and print the lowest number stored in the list
if stored_input_number:
    print("\nThe lowest number is:", min(stored_input_number))
# if no numbers were entered, print none 
else:
    print("\nNo numbers were entered")