# list to store input numbers
store_input_number = []

# a loop that asks to input a number
while True:
    try:

        input_number = int(input("\nEnter a number: ")) 

        if input_number in store_input_number: 
            # print duplicate if the number has a same number in the list
            print("\nDuplicate")
        else:
            # print unique if the number has no same number in the list
            print("\nUnique")
            
        # store the input number to the list
        store_input_number.append(input_number)

    # stops the program if not numerical value
    except ValueError:
        print("\nThe input must be numerical!")
        break