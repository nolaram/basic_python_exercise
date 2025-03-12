store_input_number = []

# input ten numbers 
for number in range(10):
    input_number = int(input(f"\nEnter a number {number + 1}: "))
    # store the input number to the variable
    store_input_number.append(number)

unique_numbers = []

# check if input number is unique
for input_number in store_input_number:
    count = 0
    # check if input number is not unique
    for check in store_input_number:
        if input_number == check:
            count += 1
    # store in unique numbers if not repeated
    if count == 1:
        unique_numbers.append(input_number)

# print the result
print("\nThe numbers that are unique are: ")
# check if unique number has a stored unique number
if len(unique_numbers) > 0:
    for unique in unique_numbers:
        print(unique)
# if none, print "There are none input number"
else:
    print("There are none unique number")