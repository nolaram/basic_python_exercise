store_input_numbers = [] # list for input numbers
check_seen_numbers = set() # set to track numbers

# input ten numbers
for number in range(10):
    input_number = int(input(f"Enter a number {number + 1}: "))
    # store the input number to the list
    store_input_numbers.append(input_number)

# check if the number is duplicated for the first occurance
# ignore all numbers that are all ready seen by the set
# print the result