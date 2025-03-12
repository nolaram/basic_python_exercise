store_input_numbers = [] # list for input numbers
check_seen_numbers = set() # set to track numbers

# input ten numbers
for number in range(10):
    input_number = int(input(f"\nEnter a number {number + 1}: "))
    # store the input number to the list
    store_input_numbers.append(input_number)

# check if the number is duplicated for the first occurance
print("\nThe number results are:")
for input_number in store_input_numbers:
    if input_number not in check_seen_numbers:
        # print the result
        print(input_number)
# ignore all numbers that are all ready seen by the set
        check_seen_numbers.add(input_number)

