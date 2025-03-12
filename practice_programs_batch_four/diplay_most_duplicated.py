# list of input numbers
store_input_number = []

# loop to ask input
while True:
    try:
        input_number = int(input("Enter a number: "))
        # store input numbers to list
        store_input_number.append(input_number)
    # stop program if input is not numerical
    except ValueError:
        print("The input must be numerical")
        break

# dictionary of every number input
number_count = {}

# count the frequency of number input
# find the most frequent number input
# print the result
