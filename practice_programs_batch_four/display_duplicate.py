# list of stored input numbers
store_input_number = []

# input ten numbers
for number in range(10):
    input_number = int(input(f"Enter number {number + 1}: "))
    # store input numbers to list
    store_input_number.append(input_number)

# list of duplicate numbers 
duplicate_number = []

# check if duplicate and put to list
for input_number in store_input_number:
    if store_input_number.count(input_number) > 1 and input_number not in duplicate_number:
        duplicate_number.append(input_number)

# print the result
print("The numbers that are duplicated are:")
if duplicate_number:
    for input_number in duplicate_number:
        print(input_number)
# if no numbers duplicated
else:
    # print none
    print("There are no numbers duplicated")