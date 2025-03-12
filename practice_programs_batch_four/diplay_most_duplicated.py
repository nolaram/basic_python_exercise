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
for number in store_input_number:
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1

# find the most frequent number input
most_frequent_number = None
highest_count = 1

for number, count in number_count.items():
    if count > highest_count:
        highest_count = count
        most_frequent_number = number

# print the result
if most_frequent_number is not None:
    print(f"The most frequent number that showed up is: {most_frequent_number}, appearing {highest_count} times")
else:
    print("No number was duplicated")
